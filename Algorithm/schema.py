import graphene
from graphene_django.types import DjangoObjectType

from .models import Algorithm,Language,Code,Category

class LanguageType(DjangoObjectType):
    class Meta:
        model = Language

class AlgorithmType(DjangoObjectType):
    class Meta:
        model = Algorithm
class CodeType(DjangoObjectType):
    class Meta:
        model = Code

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class Query(object):
    all_languages = graphene.List(LanguageType)
    all_algorithms = graphene.List(AlgorithmType)
    all_code = graphene.List(CodeType)
    def resolve_all_languages(self, info, **kwargs):
        return Language.objects.all()

    def resolve_all_algorithms(self, info, **kwargs):
        return Algorithm.objects.all()
        