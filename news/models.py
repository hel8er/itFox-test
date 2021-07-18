from django.db import models


class News(models.Model):
    """Модель Новости"""
    title = models.CharField(max_length=100)
    text = models.TextField()
    pub_date = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = 'news'

    def __str__(self):
        return self.title


