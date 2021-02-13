from django.db import models

# Create your models here.


class Categorie(models.Model):
    categoryName = models.CharField(max_length=200)
    categoryId = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.categoryName


class BlogPost(models.Model):
    blogTitle = models.CharField(max_length=200)
    blogId = models.IntegerField()
    blogCategory = models.ForeignKey("Categorie" , on_delete = models.CASCADE)
    blogContent = models.TextField(max_length=1000)

    def __str__(self):
        return self.blogTitle