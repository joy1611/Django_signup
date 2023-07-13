from django.shortcuts import render, redirect


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Implement your logic for authentication here
        # For simplicity, we assume username and password as "admin"
        if username == 'admin' and password == 'admin':
            return redirect('redirect')  # Redirect to the redirect_view
        else:
            error_message = 'Invalid username or password.'
            return render(request, 'login.html', {'error': error_message})
    else:
        return render(request, 'login.html')


def redirect_view(request):
    username = request.GET.get('username')
    return render(request, 'redirect.html', {'username': username})


def forget_password_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        # Implement your logic for handling forget password here
        # For simplicity, we assume email as "admin@example.com"
        if email == 'admin@example.com':
            return render(request, 'password_reset.html')
        else:
            error_message = 'Invalid email.'
            return render(request, 'forget_password.html', {'error': error_message})
    else:
        return render(request, 'forget_password.html')
