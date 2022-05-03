from django.contrib import admin
from .models import Comentario

# Register your models here.
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_coment', 'email_coment', 'post_coment', 'data_coment', 'publicado_coment')
    list_editable = ('publicado_coment',)
    list_display_links = ('id', 'nome_coment')


admin.site.register(Comentario, ComentarioAdmin)