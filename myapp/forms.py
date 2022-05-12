from django.forms import ModelForm
from django import forms
from .models import Cliente, Animal, Consulta

class DateInput(forms.DateInput):
    input_type = 'date'
    format='%m/%d/%Y'


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            "fecha_nacimiento": DateInput()
        }

class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'

class ConsultaForm(ModelForm):
    class Meta:
        model = Consulta
        fields = ['animal', 'enfermedad','observacion']
        widgets={
            "animal": forms.Select(attrs={"class": "form-control"}),
            "enfermedad": forms.Select(attrs={"class": "form-control"}),
            "observacion": forms.Textarea(attrs={
                "id": "consulta_observacion",
                "class": "form-control"
            })
        }


    


