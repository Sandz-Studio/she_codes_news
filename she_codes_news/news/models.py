from django.db import models
from django.contrib.auth import get_user_model


class NewsStory(models.Model):
    Categories = [
        ('Animals', 'Animals'),
        ('Travel', 'Travel'),
        ('Food', 'Food'),
        ('World', 'World'),
        ('Sport', 'Sport'),
        ('Lifestyle', 'Lifestyle'),
        ('Entertainment', 'Entertainment'),
        ('Technology', 'Technology')
    ]

    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    category = models.CharField(max_length=15, blank=False, choices=Categories, default="")
    pub_date = models.DateField()
    content = models.TextField()
    image = models.URLField(null=True, blank=True)






