# Internship-Admin-Dashboard

A role-based **Admin & Staff Management System** built using **Django**, demonstrating user authentication, product management, request handling, and analytics visualizations.  

This project is a simplified version of the admin dashboard I built during my internship, recreated to demonstrate my Django skills clearly for interviews.

---

## 🚀 Features

### 🔐 Authentication & Roles
- Single login page for both **Admin** and **Staff**
- Role-based redirection
  - Admin → Admin Dashboard
  - Staff → Staff Dashboard
- Staff registration page

---

## 🧑‍💼 Admin Features (Superuser)
- Can log in through Django Admin (`/admin/`)
- Can **add, edit, delete products**
- Can view and manage all staff orders
- Admin Dashboard includes:
  - ✔ Total Staff Count  
  - ✔ Total Products  
  - ✔ Total Orders  
  - ✔ Pie Chart (Orders by Status)  
  - ✔ Bar Chart (Imported vs Manual Products)  
  - ✔ Recent Orders Table  
- Full database management through Django Admin Panel

---

## 👨‍🔧 Staff Features (Normal User)
- Can log in through main login page
- Can submit a **request/order** for a product
- Can choose:
  - Product  
  - Quantity  
- Can view **their own request history**, including:
  - Product name  
  - Quantity  
  - Status (Pending / Approved / Rejected / Completed)
  - Timestamp

---

## 📦 Product Categories Used
The following product categories (example from Titan Company context) are pre-loaded:

- Octane Series  
- Edge Series  
- Neo Series  
- Raga Collection (Women)  
- Automatic Series  

Admins add these in Django Admin.

---

## 🗄️ Database Models

### **Product**
- name  
- sku  
- quantity  
- price  
- imported_from_file (for bar chart analytics)  

### **Order**
- staff (User)  
- product  
- quantity  
- status  
- timestamp  

---

## 📊 Technologies Used
- **Python 3**
- **Django**
- **SQLite**
- **Bootstrap 5**
- **Chart.js** (Pie & Bar Charts)
- **Django Admin Panel**

---

## 🏗️ Project Structure

django_dashboard/
│
├── dashboard/
│ ├── models.py
│ ├── forms.py
│ ├── views.py
│ ├── urls.py
│ ├── templates/
│ │ ├── login.html
│ │ ├── register.html
│ │ ├── staff_dashboard.html
│ │ └── admin_dashboard.html
│ └── admin.py
│
├── inventory_dashboard/
│ ├── settings.py
│ ├── urls.py
│
├── manage.py
└── README.md
