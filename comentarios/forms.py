from django.forms import ModelForm
from .models import Comentario

class FormComentario(ModelForm):
    class Mesta:
        model = Comentario
        fields = ('nome_comentario', 'nome_comentario', 'comentario')