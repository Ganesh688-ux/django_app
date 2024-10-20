from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly,AllowAny
from .models import Question, Choice
from .serializers import QuestionSerializer, ChoiceSerializer
from rest_framework.pagination import PageNumberPagination
class QuestionPagination(PageNumberPagination):
    page_size=5
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]
    Pagination_class = QuestionPagination

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


