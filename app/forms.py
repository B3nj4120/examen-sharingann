from django import forms
from .models import contacto, tienda
from django.contrib.auth.forms import UserCreationForm



class ContactoForm(forms.ModelForm):

    class Meta:
       model = contacto
       #fiels = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
       fields= '__all__'

class TiendaForm(forms.ModelForm):
    class Meta:
        model = tienda
        fields = '__all__'

        widgets ={ 
            "fecha_fabricacion": forms.SelectDateWidget()
        }

class CustomUserCteationForm(UserCreationForm):
    pass