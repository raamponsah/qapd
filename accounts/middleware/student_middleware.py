from django.shortcuts import redirect
from django.urls import reverse

from accounts.middleware.LecturerProfileMiddleware import utilityfunc
from accounts.middleware.whitelisted_routes import whitelisted_urls
from accounts.models import Student


def router_middleware(get_response):
    def middleware(request):
        response = get_response(request)
        try:
            if request.user.id is not None and request.user.is_student is True and request.user.is_active is True:
                Student.objects.filter(user=request.user).get()
        except Student.DoesNotExist:
            while not (request.path == reverse('student_profile_create', kwargs={'pk': request.user.id})):
                return redirect(reverse('student_profile_create', kwargs={'pk': request.user.id}))
        return response

    return middleware