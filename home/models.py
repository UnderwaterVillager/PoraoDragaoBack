from django.db import models

class User(models.Model):
    username = models.CharField(verbose_name="nome", max_length=50)
    password = models.CharField(verbose_name="senha", max_length=50)
    email = models.EmailField(verbose_name="email")
    phonenumber = models.CharField(verbose_name="telefone", max_length=15)
    location = models.CharField(verbose_name="local", max_length=200)

class Product(models.Model):
    name = models.CharField(verbose_name="nome", max_length=100)
    publication_date = models.DateField(verbose_name="data de publicação")
    description = models.TextField(verbose_name="descrição")
    price = models.DecimalField(verbose_name="preço", decimal_places=2, max_digits=7)
    status = models.CharField(verbose_name="status", max_length=15)
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

class Image(models.Model):
    image_name = models.CharField(verbose_name="nome da imagem", max_length=50)
    image = models.ImageField(verbose_name="imagem", upload_to="media/")
    related_product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)