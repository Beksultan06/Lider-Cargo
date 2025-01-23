from django.shortcuts import redirect

class LoginRequiredMiddleware:
    """
    Middleware для проверки авторизации.
    Если пользователь не авторизован, перенаправляем на страницу логина.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.path not in ['/login/', '/register/', '/admin/']:
            return redirect('/login/')
        return self.get_response(request)
