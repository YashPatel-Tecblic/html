from django.contrib import admin
from django.urls import path
from core import views
from django.conf.urls.static import static

urlpatterns= [
    path('',views.signup1),
    path('signup/',views.signup1,name="signup"),
    path('save/',views.save1,name="save"),
    path('save2/',views.save2,name="save2"),
    path('save3/',views.login_save3,name='save3'),
    path('pay1/',views.pay1,name="pay1"),
    path('success/',views.success,name="success"),
    path('signin2/',views.signin2,name="singin2"),
    path('pay2/',views.pay2,name='pay2'),
    path('pay3/',views.pay3,name="pay3")
]