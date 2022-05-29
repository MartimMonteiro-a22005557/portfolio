from django.forms import ModelForm

from portfolio.models import Cadeira, Projeto, Escola, Tecnologia, Laboratorio, Certificado, Habilitacao, Aptidao, Hobby


class CadeiraForm(ModelForm):
    class Meta:
        model = Cadeira
        fields = '__all__'

class ProjetoForm(ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'

class EscolaForm(ModelForm):
    class Meta:
        model = Escola
        fields = '__all__'

class TecnologiaForm(ModelForm):
    class Meta:
        model = Tecnologia
        fields = '__all__'

class LaboratorioForm(ModelForm):
    class Meta:
        model = Laboratorio
        fields = '__all__'


class CertificadoForm(ModelForm):
    class Meta:
        model = Certificado
        fields = '__all__'


class HabilitacaoForm(ModelForm):
    class Meta:
        model = Habilitacao
        fields = '__all__'


class ApitdaoForm(ModelForm):
    class Meta:
        model = Aptidao
        fields = '__all__'


class HobbyForm(ModelForm):
    class Meta:
        model = Hobby
        fields = '__all__'