from django.db import models

# Create your models here.

#각 장르별 테이블
class action(models.Model):
    
    platform = models.CharField(max_length=100, default="naver")
    webtoon_name = models.CharField(max_length=100, default="더 복서")

    before_ranking = models.IntegerField(default=10000)
    after_ranking = models.IntegerField(default=10000)

    def __str__(self):
        return self.webtoon_name

    def __str__(self):
        return self.platform


class romance(models.Model):
    
    platform = models.CharField(max_length=100, default="naver")
    webtoon_name = models.CharField(max_length=100, default="더 복서")
    
    before_ranking = models.IntegerField(default=10000)
    after_ranking = models.IntegerField(default=10000)

    def __str__(self):
        return self.webtoon_name

    def __str__(self):
        return self.platform

 

class fantasy(models.Model):
    
    platform = models.CharField(max_length=100, default="naver")
    webtoon_name = models.CharField(max_length=100, default="더 복서")

    before_ranking = models.IntegerField(default=10000)
    after_ranking = models.IntegerField(default=10000)

    def __str__(self):
        return self.webtoon_name

    def __str__(self):
        return self.platform
