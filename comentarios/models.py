from django.db import models
from django.utils import timezone
from posts.models import Post
from django.contrib.auth.models import User

# Create your models here.
class Comentario(models.Model):
    nome_coment = models.CharField(max_length=150)
    email_coment = models.EmailField()
    comentario = models.TextField(max_length=500)
    post_coment = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_coment = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data_coment = models.DateTimeField(default=timezone.now)
    publicado_coment = models.BooleanField(default=False)

    def __str__(self):
        return self.nome_coment