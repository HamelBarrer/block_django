from django.db import models


class Comment(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    commentaries = models.TextField(max_length=250)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.last_name} {self.last_name}'
