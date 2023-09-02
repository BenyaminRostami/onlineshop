from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth import get_user_model
class CustomUserCreationForm(UserCreationForm):
    class meta:
        model=get_user_model()
        fields= ('username' , 'email' , )


class CustomUserChangeForm(UserChangeForm):
    class meta:
        model=get_user_model
        fields = ('username' , 'email' , )