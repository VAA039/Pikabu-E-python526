from django.urls import path


from blog.views import home_view # from .views import home_view Можно так

urlpatterns = [
    path("", home_view)
]



