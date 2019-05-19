from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Language(models.Model):
    lang_name = models.CharField(max_length=256)

    def __str__(self):
        return self.lang_name

    def __unicode__(self):
        return self.lang_name


class Algorithm(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500,null=True)
    langs = models.ManyToManyField(Language)
    created_at = models.DateTimeField('created_at', auto_now=True)
    updated_at = models.DateTimeField('updated_at', auto_now=True)
    category = models.ForeignKey(
        Category, models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Code(models.Model):
	algo = models.ForeignKey(Algorithm, on_delete=models.CASCADE,)
	content = models.TextField(max_length=20000, null=False)
	lang = models.ForeignKey(Language, on_delete=models.CASCADE)

