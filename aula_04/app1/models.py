from django.db import models

class agenda(models.Model):
    nome = models.CharField(max_length=100,
                            null=False,
                            blank=False)
    telefone = models.IntegerField();
    


