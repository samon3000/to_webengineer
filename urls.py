import views
from ajango.urls.pattern import URLPattern

url_patterns = [
    URLPattern("/now$", views.now),
    URLPattern("/show_request$", views.show_request),
    URLPattern("/parameters$", views.parameters),
    URLPattern("/safe$", views.safe),
    URLPattern("/set_cookie$", views.set_cookie),
    URLPattern("/login$", views.login),
    URLPattern("/welcome$", views.welcome),
    URLPattern("/user/<user_id>/profile$", views.user_profile),
]