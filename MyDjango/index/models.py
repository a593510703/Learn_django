from django.db import models

class Type(models.Model):
    id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=20)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    weight = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

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
