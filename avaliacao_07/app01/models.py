from django.db import models

class Boletins(models.Model):
    matricula = models.IntegerField()
    nome_do_aluno = models.CharField(max_length=100)
    nota1 = models.FloatField()
    nota2 = models.FloatField()
    

