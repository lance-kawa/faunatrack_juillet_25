Jour 3: 
matin: form compostion, templatetags, commands,  4XX template, import-export + ordering + list_editable, modèle Inline, digressions Unfold, email 
ap:  middleware, RBAC ORM , signaux, tests, permissions

<!-- 
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.example.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'your-email@example.com'
# EMAIL_HOST_PASSWORD = 'your-email-password'


from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    return field.as_widget(attrs={"class": css_class})


class SimpleLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print(f"Request path: {request.path}")

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        return response -->

Jour 4:
matin: API
ap: MEP