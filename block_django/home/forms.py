from django import forms

from .models import Comment

from users.models import User


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'first_name', 'last_name', 'commentaries'
        ]
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'commentaries': 'Comentario',
        }


class RegisterForm(forms.Form):
    username = forms.CharField(
        required=True,
        min_length=6,
        max_length=25,
        widget=forms.TextInput(
            attrs={
                'class': 'form-input',
                'id': 'username',
            }
        )
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-input',
                'id': 'email',
            }
        )
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-input',
            }
        )
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-input',
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El nombre de usuario ya esta en uso')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El correo de usuario ya esta en uso')
        return email

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2', 'Las contraseñas no coinceden')

    def save(self):
        return User.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password'),
        )
