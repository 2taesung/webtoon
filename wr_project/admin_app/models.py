from django.db import models

# Create your models here.

class action(models.Model):
    before_ranking = models.IntegerField(default=10000)
    after_ranking = models.IntegerField(default=10000)

    # def __str__(self):
    #     return self.choice_text

class romance(models.Model):
    before_ranking = models.IntegerField(default=10000)
    after_ranking = models.IntegerField(default=10000)

class fantasy(models.Model):
    before_ranking = models.IntegerField(default=10000)
    after_ranking = models.IntegerField(default=10000)
