from django.urls import path

from . import views

app_name = "base"
urlpatterns = [
    path("", views.home_view, name="home"),
    path("privacy", views.PrivacyPolicyView.as_view(), name="privacy-policy"),
    path("error-handling-test", views.error_handling_test_view, name="error-handling"),
]
