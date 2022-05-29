from django.contrib import admin

# Register your models here.
from portfolio.models import Pessoa, Cadeira, Escola, Linguagem, Projeto, Tecnologia, Laboratorio, PontuacaoQuiz, \
    Noticias, Certificado, Habilitacao, Aptidao, Hobby


class PessoaAdmin(admin.ModelAdmin):
    fields = (("first_name", "last_name"), "pagina", "linkedin")


class CadeiraAdmin(admin.ModelAdmin):
    fields = ("nome", ("ano", "semestre"), "ECTS", "anoletivo", "topicos", "ranking", ("professoresPraticas", "professoresTeoricas"), "projetos", "link")


class EscolaAdmin(admin.ModelAdmin):
    fields = ("nome", "tipo", "data_de_ingresso", "data_de_termino")


class LinguagemAdmin(admin.ModelAdmin):
    fields = ("nome",)


class ProjetoAdmin(admin.ModelAdmin):
    fields = ("nome", "descricao", "linguagem", "participantes")


class TecnologiaAdmin(admin.ModelAdmin):
    fields = ("nome", "acronimo", "descricao", "tipo", "ano_de_criacao", "criador", "site_oficial")

class LaboratorioAdmin(admin.ModelAdmin):
    fields = ("nome", "descricao", "url", "numero")


class PontuacaoQuizAdmin(admin.ModelAdmin):
    fields = ("nome", "pontuacao")

class NoticiasAdmin(admin.ModelAdmin):
    fields = ("nome", "descricao", "link")


class CertificadoAdmin(admin.ModelAdmin):
    class Meta:
        fields = "__all__"


class HabilitacaoAdmin(admin.ModelAdmin):
    class Meta:
        fields = "__all__"


class AptidaoAdmin(admin.ModelAdmin):
    class Meta:
        fields = "__all__"


class HobbyAdmin(admin.ModelAdmin):
    class Meta:
        fields = "__all__"


admin.site.register(Pessoa, PessoaAdmin)

admin.site.register(Cadeira, CadeiraAdmin)

admin.site.register(Escola, EscolaAdmin)

admin.site.register(Linguagem, LinguagemAdmin)

admin.site.register(Projeto, ProjetoAdmin)

admin.site.register(Tecnologia, TecnologiaAdmin)

admin.site.register(Laboratorio, LaboratorioAdmin)

admin.site.register(PontuacaoQuiz, PontuacaoQuizAdmin)

admin.site.register(Noticias, NoticiasAdmin)

admin.site.register(Certificado, CertificadoAdmin)

admin.site.register(Habilitacao, HabilitacaoAdmin)

admin.site.register(Aptidao, AptidaoAdmin)

admin.site.register(Hobby, HobbyAdmin)