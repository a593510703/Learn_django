from django.db import models
from django.utils.html import format_html

class Type(models.Model):
    id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=20)
    def __str__(self):
        return self.type_name

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    weight = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name='产品类型')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = '产品信息'
        verbose_name_plural = '产品信息'

    def colored_type(self):
        s = self.type.type_name
        tmp_dict = {
            '手机': 'red',
            '平板电脑': 'blue',
            '智能穿戴': 'green',
        }
        color_code = 'yellow' # default is yellow
        for k, v in tmp_dict.items():
            if k in s:
                color_code = v
        return format_html(
            '<span style ="color: {};">{}</span>',
            color_code,
            self.type,
        )
    
    colored_type.short_description = '带颜色的产品类型'
            

# 一对一
class Performer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    nationality = models.CharField(max_length=20)
    masterpiece = models.CharField(max_length=50)

class Performer_info(models.Model):
    id = models.IntegerField(primary_key=True)
    performer = models.OneToOneField(Performer, on_delete=models.CASCADE)
    birth = models.CharField(max_length=20)
    elapse = models.CharField(max_length=20)

# 一对多
class Performer_2(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    nationality = models.CharField(max_length=20)

class Program_2(models.Model):
    id = models.IntegerField(primary_key=True)
    performer = models.ForeignKey(Performer_2, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

# 多对多
class Performer_3(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    nationality = models.CharField(max_length=20)

class Program_3(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    performer = models.ManyToManyField(Performer_3)
