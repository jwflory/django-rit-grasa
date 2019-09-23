from django.db import models

class User(models.Model):
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    role = models.CharField(max_length=40)
    image_reference = models.CharField(max_length=40)

    def __str__(self):
        return self.email


class Category(models.Model):
    description = models.CharField(max_length=40)

    def __str__(self):
        return self.description


class Program(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=250)
    status = models.CharField(max_length=10)
    address = models.CharField(max_length=40)
    website = models.CharField(max_length=40)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
