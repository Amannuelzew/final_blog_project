from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.caption}"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    image = models.FileField(upload_to="images",default="")
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag)

class Comment(models.Model):
    username=models.CharField(max_length=100,default="")
    email=models.EmailField(default="")
    comment = models.TextField(max_length=300)
    date=models.DateField(auto_now=True)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.comment}"
