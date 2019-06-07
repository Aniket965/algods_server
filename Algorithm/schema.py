import graphene
from graphene_django.types import DjangoObjectType
from django.db.models.aggregates import Count
import random
from datetime import datetime
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
    all_categories = graphene.List(CategoryType)
    code_of_the_day = graphene.List(AlgorithmType)
    def resolve_all_languages(self, info, **kwargs):
        return Language.objects.all()

    def resolve_all_algorithms(self, info, **kwargs):
        return Algorithm.objects.all()

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()
        
    def resolve_code_of_the_day(self, info, **kwagrs):
        total_count = Algorithm.objects.aggregate(count= Count('id'))['count']
        random.seed(datetime.day.__hash__())
        random_index = random.randint(0, total_count - 1)
        return [Algorithm.objects.all()[random_index]]
        