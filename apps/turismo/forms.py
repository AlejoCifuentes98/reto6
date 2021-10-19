from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from .models import Categoria, Sitio

class categoria_agregar_form(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__' 
class sitio_agregar_form(forms.ModelForm):
    class Meta:
        model = Sitio
        fields = '__all__'
        exclude = ['usuario'] 

class login_form (forms.Form):
    usuario = forms.CharField(widget=forms.TextInput())  
    clave   = forms.CharField(widget=forms.PasswordInput(render_value=False))  

class registro_form (forms.Form):
    nombres= forms.CharField(label='Ingrese sus nombres', widget= forms.TextInput(attrs={'class':'form-contol'}))
    Apellidos= forms.CharField(label='Ingrese sus apellidos', widget= forms.TextInput(attrs={'class':'form-contol'}))
    correo    = forms.EmailField(label='Ingrese su correo', widget= forms.TextInput(attrs={'class':'form-control'}))
    clave_1  = forms.CharField(label='Ingrese su contraseña', widget= forms.PasswordInput(attrs={'class':'form-control'},render_value= False))
    clave_2  = forms.CharField(label='Confirme la contraseña', widget= forms.PasswordInput(attrs={'class':'form-control'}, render_value= False))

    def clean_username(self):
        correo = self.cleaned_data['Correo']
        try:
            c = User.objects.get(username = correo)
        except User.DoesNotExist:
            return correo
        raise forms.ValidationError('El correo ingresado, ya se encuentra registrado')

    
    
    def clean_clave_2 (self):
        clave_1 = self.cleaned_data['clave_1']
        clave_2 = self.cleaned_data['clave_2']
        if clave_1 == clave_2:
            return clave_2
        else:
            raise forms.ValidationError ('las contraseñas no coinciden, por favor Intente nuevamente')
