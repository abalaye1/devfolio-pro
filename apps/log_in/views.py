from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages


def log_in(request):
    if request.user.is_authenticated:
        return redirect("contact_dashboard")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, "Welcome back!")
            return redirect("contact_dashboard")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "auth/login.html")


def log_out(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("home")
