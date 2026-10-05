from django.db import models


class Skill(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=60, default='Projeto')

    def __str__(self):
        return self.title
