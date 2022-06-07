from django.urls import path
from .views import CreateAccountView
from .views import ViewAccount
app_name = 'users'

urlpatterns = [
  path('create-account/', CreateAccountView.as_view(),
  name = 'createAccount'),
  path('account/', ViewAccount.as_view(),
  name = 'account')
]