#  hello/views.py
from datetime import datetime

from django.contrib.auth import authenticate, login, logout
from django.forms import Form
from django.http import HttpResponseRedirect
from django.shortcuts import render
import collections

from django.urls import reverse

from portfolio.forms import CadeiraForm, ProjetoForm, EscolaForm, TecnologiaForm, LaboratorioForm, CertificadoForm, \
	HobbyForm, HabilitacaoForm, AptidaoForm, NoticiaForm
from portfolio.models import Cadeira, Escola, Projeto, Tecnologia, Laboratorio, Pessoa, Post, PostForm, PontuacaoQuiz, \
	Linguagem, Certificado, Habilitacao, Aptidao, Hobby, Noticia
from matplotlib import pyplot as plt


def home_page_view(request):
	print(request.user.is_authenticated)
	return render(request, 'portfolio/home.html')

def sobremim_page_view(request):
	l = list()
	cadeirass = Cadeira.objects.all()
	profs = Pessoa.objects.all()



	for x in cadeirass:
		if x.ano not in l:
			l.append(x.ano)
		x.__dict__["profs_teoricas"] = list(Pessoa.objects.filter(teoricas__id=x.id))
		x.__dict__["profs_praticas"] = list(Pessoa.objects.filter(praticas__id=x.id))

	l.sort()
	cadeiras = list(cadeirass)
	cadeiras.sort(key=lambda x: x.semestre, reverse=False)

	l2 = list()
	l3 = list()
	for a in Escola.objects.all():
		if a.tipo not in l2:
			l2.append(a.tipo)

	if "Primario" in l2:
		l3.append("Primario")
	if "Basico" in l2:
		l3.append("Basico")
	if "Secundario" in l2:
		l3.append("Secundario")
	if "Superior" in l2:
		l3.append("Superior")



	return render(request, 'portfolio/sobremim.html', {"cadeiras" : cadeiras, "anos" : l, "escolas" : Escola.objects.all(), "ensino" : l3,
													   "professores" : profs})


def projetos_page_view(request):
	projs = Projeto.objects.all()
	for x in projs:
		x.__dict__["pessoas"] = list(Pessoa.objects.filter(pessoas__id=x.id))
		x.__dict__["cadeira"] = list(Cadeira.objects.filter(projetos__id=x.id))
		x.__dict__["langs"] = list(Linguagem.objects.filter(linguagens__id=x.id))
	return render(request, 'portfolio/projetos.html', {"projetos": projs})

def web_page_view(request):
	labs = list(Laboratorio.objects.all())
	labs.sort(key=lambda x: x.numero, reverse=False)
	return render(request, 'portfolio/web.html', {"tecnologias" : Tecnologia.objects.all(), "laboratorios" : labs, "noticias" : Noticia.objects.all()})

def blog_page_view(request):
	return render(request, 'portfolio/blog.html', {"posts" : Post.objects.all()})

def contacto_page_view(request):
	return render(request, 'portfolio/contacto.html')

def newpost_page_view(request):
	# if this is a POST request we need to process the form data

	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = PostForm(request.POST, request.FILES)
		# check whether it's valid:
		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/blog')

	# if a GET (or any other method) we'll create a blank form
	else:
		form = PostForm()
	return render(request, 'portfolio/newpost.html', {'form': form})



def quiz_page_view(request):
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = Form(request.POST, request.FILES)
		# check whether it's valid:
		if form.is_valid():
			score = 0
			if(collections.Counter(request.POST.getlist("front-end[]")) == collections.Counter(
					("html", "css", "javascript"))):
				score += 1
			if (collections.Counter(request.POST.getlist("back-end[]")) == collections.Counter(
					("django", "python", "java"))):
				score += 1

			a = PontuacaoQuiz()
			a.pontuacao = score
			a.nome = request.POST["nome"]
			a.save()



	# if a GET (or any other method) we'll create a blank form
	x = []
	y = []
	for a in PontuacaoQuiz.objects.all():
		x.append(a.nome)
		y.append(a.pontuacao)
	x.reverse()
	y.reverse()
	plt.barh(x, y)
	plt.savefig('portfolio\static\portfolio\images\plot.png', bbox_inches='tight')
	plt.close()

	return render(request, 'portfolio/quiz.html')



def login_page_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(
			request,
			username=username,
			password=password)

		if user is not None:
			login(request, user)
			print(user)
			return HttpResponseRedirect('/')
		else:
			return render(request, 'portfolio/login.html', {
				'message': 'Credenciais invalidas.'
			})

	return render(request, 'portfolio/login.html')

def logout_page_view(request):
	logout(request)

	return render(request, 'portfolio/home.html')


def lista_page_view(request):
	a = None
	target = request.GET["target"]
	if target == "cadeira":
		a = Cadeira.objects.all()
	elif target == "projeto":
		a = Projeto.objects.all()
	elif target == "escola":
		a = Escola.objects.all()
	elif target == "post":
		a = Post.objects.all()
	elif target == "tecnologia":
		a = Tecnologia.objects.all()
	elif target == "laboratorio":
		a = Laboratorio.objects.all()
	elif target == "noticia":
		a = Noticia.objects.all()


	return render(request, 'portfolio/lista.html', {"lista": a, "target" : target})

def editar_page_view(request):
	if request.method == 'POST':

		if "cadeira" in request.GET:
			a = Cadeira.objects.get(id=request.GET["cadeira"])
			form = CadeiraForm(request.POST, instance=a)
		elif "projeto" in request.GET:
			a = Projeto.objects.get(id=request.GET["projeto"])
			form = ProjetoForm(request.POST, instance=a)
		elif "escola" in request.GET:
			a = Escola.objects.get(id=request.GET["escola"])
			form = EscolaForm(request.POST, instance=a)
		elif "post" in request.GET:
			a = Post.objects.get(id=request.GET["post"])
			form = PostForm(request.POST, instance=a)
		elif "laboratorio" in request.GET:
			a = Laboratorio.objects.get(id=request.GET["laboratorio"])
			form = LaboratorioForm(request.POST, instance=a)
		elif "tecnologia" in request.GET:
			a = Tecnologia.objects.get(id=request.GET["tecnologia"])
			form = TecnologiaForm(request.POST, instance=a)
		elif "certificado" in request.GET:
			a = Certificado.objects.get(id=request.GET["certificado"])
			form = CertificadoForm(request.POST, instance=a)
		elif "habilitcao" in request.GET:
			a = Habilitacao.objects.get(id=request.GET["habilitcao"])
			form = HabilitacaoForm(request.POST, instance=a)
		elif "aptidao" in request.GET:
			a = Aptidao.objects.get(id=request.GET["aptidao"])
			form = AptidaoForm(request.POST, instance=a)
		elif "hobby" in request.GET:
			a = Hobby.objects.get(id=request.GET["hobby"])
			form = HobbyForm(request.POST, instance=a)
		elif "noticia" in request.GET:
			a = Noticia.objects.get(id=request.GET["noticia"])
			form = NoticiaForm(request.POST, instance=a)




		form.save()
		return HttpResponseRedirect('/')

	if request.method == 'GET':
		form = Form()
		if "cadeira" in request.GET:
			a = Cadeira.objects.get(id=request.GET["cadeira"])
			form = CadeiraForm(instance=a)
		elif "projeto" in request.GET:
			a = Projeto.objects.get(id=request.GET["projeto"])
			form = ProjetoForm(instance=a)
		elif "escola" in request.GET:
			a = Escola.objects.get(id=request.GET["escola"])
			form = EscolaForm(instance=a)
		elif "post" in request.GET:
			a = Post.objects.get(id=request.GET["post"])
			form = PostForm(instance=a)
		elif "tecnologia" in request.GET:
			a = Tecnologia.objects.get(id=request.GET["tecnologia"])
			form = TecnologiaForm(instance=a)
		elif "laboratorio" in request.GET:
			a = Laboratorio.objects.get(id=request.GET["laboratorio"])
			form = LaboratorioForm(instance=a)
		elif "certificado" in request.GET:
			a = Certificado.objects.get(id=request.GET["certificado"])
			form = CertificadoForm(instance=a)
		elif "habilitcao" in request.GET:
			a = Habilitacao.objects.get(id=request.GET["habilitcao"])
			form = HabilitacaoForm(instance=a)
		elif "aptidao" in request.GET:
			a = Aptidao.objects.get(id=request.GET["aptidao"])
			form = AptidaoForm(instance=a)
		elif "hobby" in request.GET:
			a = Hobby.objects.get(id=request.GET["hobby"])
			form = HobbyForm(instance=a)
		elif "noticia" in request.GET:
			a = Noticia.objects.get(id=request.GET["noticia"])
			form = NoticiaForm(instance=a)

		return render(request, 'portfolio/editar.html', {"form": form})


