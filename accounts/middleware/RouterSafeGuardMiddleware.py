from django.shortcuts import redirect
from accounts.middleware.whitelisted_routes import whitelisted_urls


def utilityfunc(request, rpath):
    exception_urls = whitelisted_urls(request)
    if rpath in exception_urls:
        return redirect(rpath)
    else:
        return redirect('welcome')


def utilityfunc_wl(rpath):
    return redirect(rpath)


class RouterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        exception_urls = list(whitelisted_urls(request))
        response = self.get_response(request)
        if not request.user.is_authenticated:
            if request.path not in exception_urls:
                print("Path requested => ", request.path, "params=>", request.GET)
                # return utilityfunc(request, response)
                # request.GET.get('uidb64')
                return redirect('welcome')
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # This code is executed just before the view is called
        print(view_kwargs)