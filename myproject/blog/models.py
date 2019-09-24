from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    
    STATUS = (
        ('active', 'Ativo'),
        ('draft', 'Rascunho')
    )
    
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.FileField(upload_to = '', null=True, blank= True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug= models.SlugField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    status = models.CharField(max_length=15, choices=STATUS)
    
    def __str__(self):
        return self.title
    