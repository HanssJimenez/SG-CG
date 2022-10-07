from django import forms
from django.contrib.auth.models import User
from principal.models import UserProfileInfo, Inventario

class UserForm(forms.ModelForm):
    password = forms.CharField(widget= forms.PasswordInput())
    vpassword = forms.CharField(widget= forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email', 'password')
    def clean(self):
        cleaned_data = super().clean()
        p = cleaned_data['password']
        vp = cleaned_data['vpassword']
        if p != vp:
            raise forms.ValidationError('La constraseña no es igual')

class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')

class AgreProdForm(forms.ModelForm):
    class Meta():
        model = Inventario
        fields = ('categoria', 'nombre_p', 'cantidad')
    def clean_categoria(self):
        categoria = self.cleaned_data.get('categoria')
        if not categoria:
            raise forms.ValidationError('Completa este campo')
        for instance in Inventario.objects.all():
            if instance.categoria == categoria:
                raise forms.ValidationError(str(categoria) + ' ya existe')
        return categoria

    def clean_nombre_p(self):
        nombre_p = self.cleaned_data.get('nombre_p')
        if not nombre_p:
            raise forms.ValidationError('Completa este campo')
        return nombre_p  


class BusquedProductoForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['categoria', 'nombre_p']