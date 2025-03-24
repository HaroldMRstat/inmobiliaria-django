from django.core.exceptions import PermissionDenied

def solo_trabajadores(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and hasattr(request.user, 'rol') and request.user.rol == 'trabajador':
            return func(request, *args, **kwargs)
        raise PermissionDenied  # Bloquea el acceso si no es trabajador
    return wrapper