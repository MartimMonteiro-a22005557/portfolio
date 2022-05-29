from datetime import datetime

from django.db import models



# Create your models here.
from django.forms import ModelForm

def resolution_path(instance, filename):
    return f'users/{instance.id}'

class Pessoa(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    pagina = models.URLField(default="", blank=True, null=True)
    linkedin = models.URLField(default="", blank=True, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Escola(models.Model):
    nome = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50 , default = "", choices = [("Primario", "Primario"), ("Basico", "Basico"), ("Secundario", "Secundario"), ("Superior", "Superior")])
    data_de_ingresso = models.IntegerField(blank=True, null=True)
    data_de_termino = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.nome


class Linguagem(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50, blank=True, null=True)
    linguagem = models.ManyToManyField(Linguagem, blank=True, related_name="linguagens")
    participantes = models.ManyToManyField(Pessoa, blank=True, related_name="pessoas")

    def __str__(self):
        return self.nome

class Cadeira(models.Model):
    nome = models.CharField(max_length=50)
    ano = models.IntegerField(choices = [(1, 1), (2, 2), (3, 3)])
    semestre = models.IntegerField(choices = [(1, 1), (2, 2)])
    ECTS = models.PositiveIntegerField(blank=True, null=True)
    anoletivo = models.PositiveIntegerField(blank=True, null=True)
    topicos = models.TextField(blank=True, null=True)
    ranking = models.IntegerField(choices = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])
    professoresPraticas = models.ManyToManyField(Pessoa, related_name= "praticas", blank=True)
    professoresTeoricas = models.ManyToManyField(Pessoa, related_name= "teoricas", blank=True)
    projetos = models.ManyToManyField(Projeto, blank=True, related_name= "projetos")
    link = models.URLField(default="", blank=True, null=True)

    def __str__(self):
        return self.nome


class Tecnologia(models.Model):
    nome = models.CharField(max_length=50)
    acronimo = models.CharField(max_length=50, blank=True)
    ano_de_criacao = models.IntegerField(default=0)
    criador = models.ManyToManyField(Pessoa, related_name="creator")
    site_oficial = models.URLField(blank=True)
    descricao = models.CharField(max_length=50, blank=True, null=True)
    tipo = models.CharField(max_length=50 , default = "", choices = [("Front-End", "Front-End"), ("Back-End", "Back-End")])

    def __str__(self):
        return self.nome

class Laboratorio(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50, blank=True, null=True)
    url = models.URLField(max_length=50, default="", blank=True, null=True)
    numero = models.IntegerField(default=0)

    def __str__(self):
        return "Lab" + str(self.numero)


class Post(models.Model):
    autor = models.CharField(max_length=50, null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True, blank=True)
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(blank=True)
    link = models.URLField(blank=True, null=True)
    imagem = models.ImageField(blank=True, upload_to=resolution_path, null=True)


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        exclude = ["data"]

class PontuacaoQuiz(models.Model):
    nome = models.CharField(max_length=50)
    pontuacao = models.PositiveIntegerField()

class Noticia(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50)
    link = models.URLField(blank=True, null=True)



class Certificado(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50)


class Habilitacao(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50)

class Aptidao(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50, default="", choices=[("Tecnica", "Tecnica"), ("Organizativa", "Organizativa"), ("Linguagem Programação", "Linguagem Programação"),
                                                                ("Social", "Social"), ("Linguistica", "Linguistica")])
    projetos = models.ManyToManyField(Projeto, related_name="projeto")
    disciplinas = models.ManyToManyField(Cadeira, related_name="cadeiras")



class Hobby(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50)