from django.shortcuts import HttpResponseRedirect
from functools import wraps
from .models import CustomUser
def teacher_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.role == CustomUser.Role.TEACHER:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/home/')  # Redirect to home if user is not a teacher
    return _wrapped_view