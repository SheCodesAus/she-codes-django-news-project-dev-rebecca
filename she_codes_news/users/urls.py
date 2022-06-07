from django.urls import path
from .views import CreateAccountView
from .views import ViewAccount
app_name = 'users'

urlpatterns = [
<<<<<<< Updated upstream
  path('create-account/', CreateAccountView.as_view(),
  name = 'createAccount'),
  path('account/', ViewAccount.as_view(),
  name = 'account')
=======
  path('create-account/', CreateAccountView.as_view(), name = 'createAccount'),
>>>>>>> Stashed changes
]