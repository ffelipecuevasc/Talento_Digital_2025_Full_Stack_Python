from django import forms

class AlumnoForm(forms.Form):
    # Si es del tipo TEXTO, debe ser CharField
    nombre = forms.CharField(label='Nombre', max_length=100)
    apellido = forms.CharField(label='Apellido', max_length=100)
    # Si es del tipo EMAIL, automáticamente va a validar que tenga @ y un formato final de .cl (por ejemplo)
    correo_electronico = forms.EmailField(label='Correo Electrónico')