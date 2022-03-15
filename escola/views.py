from rest_framework import viewsets
from escola.models import Aluno, Curso, Matricula
from .serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer


class AlunoViewSet(viewsets.ModelViewSet):
    '''
    Exibindo todos os alunos e alunas.
    '''

    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class CursoViewSet(viewsets.ModelViewSet):
    '''
    Exibindo todos os cursos
    '''
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    '''
    Exibindo todas as matriculas
    '''
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer