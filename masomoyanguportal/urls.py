from django.contrib import admin
from django.urls import path
from django.urls.conf import include
# Registration
from masomoyangu import views as masomoyangu_views
# Login
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('masomoyangu.urls')),
    path('registration/', masomoyangu_views.registration, name='registration' ),
    path('login/', auth_views.LoginView.as_view(template_name='masomoyangu/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='masomoyangu/logout.html'), name='logout'),
    #Password Reset URLS
    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name='masomoyangu/password_reset.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name='masomoyangu/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='masomoyangu/password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='masomoyangu/password_reset_done.html'), name='password_reset_complete'),
]
