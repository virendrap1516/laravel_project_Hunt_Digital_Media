# Hunt Digital Media – Assignment Submission  🔥

## This repository contains the completed tasks for the Hunt Digital Media assignment 🌟,

 ## 📌 Task 1: Laravel Project Setup & Login Page
 
* 1. Running a Laravel project locally

* 2. Automating the Laravel login page using Python Selenium

* 3. Integrating a static HTML calendar page into Laravel via routing

   * Connected MySQL database

   * Successfully ran the project locally

   * Verified the Laravel login page
     
## 📦▶ How to Run

* Install composer
  
 ```sh
 composer install📂
   ```
* .env file setup 

```sh
cp .env.example .env 🖥️
   ```

* Generate Laravel App Key
```sh
php artisan key:generate 🗝️
   ```
* Run Migration 
  
```sh
php artisan migrate 🔒
   ```

* Start Laravel Server 

```sh
php artisan serve ▶︎
   ```
### Open Project in Browser -

 You’ll see:- http://127.0.0.1:8000 🎉


## 📌 Task 2: Python Selenium Automation

* 1. Created a Python Selenium script

* 2. Opened the Laravel login page

* 3. Filled email and password fields with random values

* 4. Closed the browser automatically
  
## 📦▶ How to Run

* Requirements
```sh
pip install selenium webdriver-manager ⚙️
   ```

* Script File

```sh
automate_login.py 🗂️
   ```
* Run Script
  
```sh
python automate_login.py 🎯
   ```
### 🖼️ Output -

Browser opens login page ✅

Random credentials are entered ✅

Browser exits successfully ✅

## 📌Task 3: HTML Calendar Page Integration into Laravel

* 1. Extracted HTML template

* 2. Used app-calendar.html

* 3. Converted it to Laravel Blade

* 4. Fixed asset paths using {{ asset() }}

* 5. Added a Laravel route /html-page

* File Location

```sh
resources/views/app-calendar.blade.php 📂
   ```

* Route Add

```sh
Route::get('/html-page', function () {
    return view('app-calendar');
});
   ```
* Check out live page -
  
```sh
http://127.0.0.1:8000/html-page ✔️
   ```

🛠 Technologies Used

* Laravel (PHP)

* MySQL

* Python

* Selenium WebDriver

* HTML / CSS / JavaScript

* Bootstrap Admin Template

### ✅ Assignment Status

✔ Laravel setup completed

✔ Selenium automation completed

✔ HTML page successfully integrated

✔ All tasks working locally

### 📎 Notes

* Laravel server must be running before executing Selenium script

* MySQL and Apache should be running (XAMPP)

* Assets are served from Laravel public/ directory
  
_Made with ❤️ by [Virendra Pawar](https://github.com/virendrap1516)_

Email: Virendrapawar47@gmail.com 📧
