from django.shortcuts import redirect
from django.urls import reverse


class SearchMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == "POST" and 'searchInput' in request.POST:
            search_str = request.POST.get('searchInput')
            return redirect('search prod', search_str=search_str)

        response = self.get_response(request)
        return response


class AdminRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith(reverse('admin:index')) and not request.user.is_authenticated:
            return redirect('index')
        response = self.get_response(request)
        return response
