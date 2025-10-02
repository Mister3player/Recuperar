# publicaciones/forms.py (Crear este archivo)

from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    # Por ahora, usamos el formulario de creación de usuario por defecto de Django.
    # Si quieres añadir más campos (ej. nombre, apellido), se modifica aquí.
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields