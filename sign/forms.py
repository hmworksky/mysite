
from django.contrib.auth.forms import UserCreationForm
from .moles import User

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
	model = User
	fields = ("username")
