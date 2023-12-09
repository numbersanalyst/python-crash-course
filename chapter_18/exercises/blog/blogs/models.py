from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=60)
    text = models.TextField(max_length=550)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
