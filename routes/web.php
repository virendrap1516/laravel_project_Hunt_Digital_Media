<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\Caller\LoginController;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "web" middleware group. Make something great!
|
*/

// --- LOCAL DEVELOPMENT & GENERAL ROUTES ---

// Homepage and login page will show the login form
Route::get('/', [LoginController::class, 'index']);
Route::get('login', [LoginController::class, 'index'])->name('login');

// Handles the form submission when a user tries to log in
Route::post('login', [LoginController::class, 'validateUser']);

// Handles Socialite (Google/Facebook) login
Route::get('login/{driver}/start', [LoginController::class, 'redirectToProvider']);
Route::any('login/{driver}/callback', [LoginController::class, 'handleProviderCallback']);

// Handles logging out
Route::any('logout', [LoginController::class, 'Logout']);


// --- PRODUCTION-ONLY DOMAIN ROUTES ---
// This group is now empty but can be used for routes that
// should ONLY work on your live domain.
Route::domain('da.adlynk.in')->group(function () {
    // Example: Route::get('/admin-dashboard', ...);
});

Route::get('/html-page', function () {
    return view('app-calendar');
});


Route::get('/html-page', function () {
    return redirect('/html/vertical-menu-template/app-calendar.html');
});