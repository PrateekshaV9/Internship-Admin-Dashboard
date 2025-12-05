from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.db.models import Count

from .forms import StaffRegistrationForm, StaffOrderForm
from .models import Product, Order


def login_view(request):
    """Single login page for both Admin and Staff."""
    if request.user.is_authenticated:
        # redirect based on role
        if request.user.is_staff:
            return redirect('admin_dashboard')
        return redirect('staff_dashboard')

    message = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin_dashboard')
            else:
                return redirect('staff_dashboard')
        else:
            message = 'Invalid username or password'

    return render(request, 'login.html', {'message': message})


def register_view(request):
    """Registration for new staff users."""
    if request.method == 'POST':
        form = StaffRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # staff users: normal users (not superuser, not staff)
            user.is_staff = False
            user.save()
            return redirect('login')
    else:
        form = StaffRegistrationForm()
    return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


def is_admin(user):
    return user.is_staff  # superuser / admin users


@login_required
def staff_dashboard(request):
    """Staff page – make request/order and see their own orders."""
    if request.user.is_staff:
        # if admin somehow opens this URL, redirect them
        return redirect('admin_dashboard')

    if request.method == 'POST':
        form = StaffOrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.staff = request.user
            order.save()
            return redirect('staff_dashboard')
    else:
        form = StaffOrderForm()

    my_orders = Order.objects.filter(staff=request.user).order_by('-created_at')

    context = {
        'form': form,
        'my_orders': my_orders,
    }
    return render(request, 'staff_dashboard.html', context)


@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    """Admin dashboard with cards + charts."""
    staff_count = User.objects.filter(is_staff=False).count()
    product_count = Product.objects.count()
    order_count = Order.objects.count()

    # For pie chart: orders by status
    orders_by_status = Order.objects.values('status').annotate(total=Count('id'))
    pie_labels = [item['status'] for item in orders_by_status]
    pie_data = [item['total'] for item in orders_by_status]

    # For bar chart: imported vs non-imported products
    imported_count = Product.objects.filter(imported_from_file=True).count()
    manual_count = Product.objects.filter(imported_from_file=False).count()
    bar_labels = ['Imported', 'Manual']
    bar_data = [imported_count, manual_count]

    # List of recent orders to show in a table
    recent_orders = Order.objects.select_related('staff', 'product').order_by('-created_at')[:10]

    context = {
        'staff_count': staff_count,
        'product_count': product_count,
        'order_count': order_count,
        'pie_labels': pie_labels,
        'pie_data': pie_data,
        'bar_labels': bar_labels,
        'bar_data': bar_data,
        'recent_orders': recent_orders,
    }
    return render(request, 'admin_dashboard.html', context)
