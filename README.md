

# Multi Shop - سایت فروشگاهی لباس

**توسعه‌دهنده**: Matin Talkhabi  
**نام پروژه**: Multi Shop  
**توضیحات**: یک سایت فروشگاهی کامل برای فروش انواع پوشاک

## توضیحات پروژه (فارسی)

### معرفی
سایت **Multi Shop** یک پلتفرم آنلاین حرفه‌ای و کاربرپسند برای فروشگاه‌های لباس است. این سایت با استفاده از جدیدترین تکنولوژی‌ها و ابزارها طراحی شده و قابلیت‌های فراوانی برای کاربران و مدیران فروشگاه فراهم می‌کند.

### ویژگی‌های کلیدی
- **طراحی واکنش‌گرا با Tailwind CSS**: سایت به طور کامل برای انواع دستگاه‌ها (موبایل، تبلت و دسکتاپ) بهینه‌سازی شده است.
- **سیستم مدیریت محصولات و موجودی**: مدیران فروشگاه می‌توانند محصولات خود را به راحتی اضافه، ویرایش و مدیریت کنند.
- **فیلترهای پیشرفته جستجو**: کاربران می‌توانند به راحتی محصولاتی که به دنبال آن هستند را بر اساس دسته‌بندی، سایز، رنگ و قیمت پیدا کنند.
- **سبد خرید و پرداخت ایمن**: امکان اضافه کردن محصولات به سبد خرید، پرداخت آنلاین با درگاه‌های پرداخت امن و مشاهده وضعیت سفارشات.
- **سیستم ثبت‌نام و ورود کاربران**: کاربران می‌توانند با استفاده از سیستم‌های مختلف احراز هویت وارد سایت شوند و پروفایل کاربری خود را مدیریت کنند.
- **پنل مدیریت قوی با Django**: مدیران فروشگاه می‌توانند سفارشات، مشتریان و تنظیمات سایت را از طریق پنل مدیریتی مبتنی بر Django مدیریت کنند.

### تکنولوژی‌ها و ابزارهای استفاده شده
- **Frontend**: Tailwind CSS, HTML, JavaScript
- **Backend**: Django (پایتون)
- **Database**: PostgreSQL
- **Payment Gateway**: Stripe (درگاه پرداخت آنلاین)
- **Authentication**: JWT (JSON Web Token) برای احراز هویت امن

### نحوه راه‌اندازی (Setup)
برای راه‌اندازی پروژه، مراحل زیر را دنبال کنید:

1. ابتدا ریپازیتوری را کلون کنید:
   ```bash
   git clone https://github.com/matintalkhbi/multi_shop.git
   ```

2. به دایرکتوری پروژه بروید:
   ```bash
   cd multi_shop
   ```

3. محیط مجازی پایتون را بسازید و فعال کنید:
   ```bash
   python -m venv venv
   source venv/bin/activate  # برای سیستم‌عامل‌های مک و لینوکس
   venv\Scripts\activate  # برای ویندوز
   ```

4. وابستگی‌های پروژه را نصب کنید:
   ```bash
   pip install -r requirements.txt
   ```

5. تنظیمات پایگاه داده را پیکربندی کنید و مهاجرت‌های Django را اجرا کنید:
   ```bash
   python manage.py migrate
   ```

6. سرور محلی را اجرا کنید:
   ```bash
   python manage.py runserver
   ```

### دستورات گیت
برای اضافه کردن ریموت و آپلود پروژه به ریپازیتوری گیت‌هاب خود:

```bash
git remote add origin https://github.com/matintalkhbi/multi_shop.git
git branch -M main
git push -u origin main
```

## English Description

### Introduction
**Multi Shop** is a professional and user-friendly online platform for clothing stores. It is built using the latest technologies to provide a seamless shopping experience for users and powerful management tools for store owners.

### Key Features
- **Responsive Design with Tailwind CSS**: The website is fully optimized for mobile, tablet, and desktop devices.
- **Product and Inventory Management**: Store managers can easily add, edit, and manage their products.
- **Advanced Search Filters**: Users can find products based on categories, size, color, and price with ease.
- **Secure Shopping Cart and Payment**: Customers can add products to the cart, make secure payments online, and track their orders.
- **User Authentication**: Users can sign up and log in using secure authentication methods to manage their profiles.
- **Powerful Admin Panel with Django**: Store owners can manage orders, customers, and site settings through a robust admin interface.

### Technologies and Tools Used
- **Frontend**: Tailwind CSS, HTML, JavaScript
- **Backend**: Django (Python)
- **Database**: PostgreSQL
- **Payment Gateway**: Stripe for secure online transactions
- **Authentication**: JWT (JSON Web Token) for secure user authentication

### Setup Instructions
To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/matintalkhbi/multi_shop.git
   ```

2. Navigate to the project directory:
   ```bash
   cd multi_shop
   ```

3. Create and activate a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS and Linux
   venv\Scripts\activate  # On Windows
   ```

4. Install project dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Configure the database settings and run Django migrations:
   ```bash
   python manage.py migrate
   ```

6. Run the local development server:
   ```bash
   python manage.py runserver
   ```

### Git Commands
To set up the remote repository and push the code to GitHub:

```bash
git remote add origin https://github.com/matintalkhbi/multi_shop.git
git branch -M main
git push -u origin main
```

--- 

This README covers both Persian and English descriptions to accommodate a diverse range of developers and users. Happy coding! 😊
