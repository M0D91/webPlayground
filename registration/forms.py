from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models  import User
from .models import Profile

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Requerido, debe ser un email valido, 254 caracteres máximo')
    
    class Meta:
        model = User
        #El campo email ya es parte del modelo User y por eso funcionara.
        #Si quisieramos ampliar el formulario con nuevos campos deberemos
        #crearlos previamente en el modelo para poder extenderlos al formulario
        fields = ('username','email','password1','password2')
        ### Extendemos la config y simplemente añadimos un campo mas pero no modificaremos
        ### los widgets aqui, porque se puede hacer, pero eso anularia las validaciones 
        ### y comprobaciones de seguridad que trae por defecto la clase forms.
        ### Esos cambios deben hacerse en el views.py para no interferir con las validaciones.


    # Definimos una funcion con la termnologia clean_CampoDelFormulario para hacer 
    # validaciones. Sin la logica de 'clean_' no funcionará
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El email ya existe, prueba otro')
        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar','bio','link']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'bio' : forms.Textarea(attrs={'class':'form-control mt-3','rows':3,'placeholder':'Biografia'}),
            'link' : forms.URLInput(attrs={'class':'form-control mt-3','placeholder':'Enlace'}),
        }

class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text='Requerido, debe ser un email valido, 254 caracteres máximo')

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('El email ya existe, prueba otro')
        return email