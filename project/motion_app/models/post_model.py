from django.conf import settings
from django.db import models
from django.forms import ModelForm


class PostItem(models.Model):
    title = models.CharField(
        verbose_name='title',
        max_length=100,
    )
    content = models.TextField(
        verbose_name="content",
        blank=True,
        max_length=160,
    )
    created = models.DateTimeField(
        verbose_name="created",
        auto_now_add=True,
    )
    likes = models.IntegerField(
        verbose_name='likes',
        default=0,
    )
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        verbose_name='user',
        on_delete=models.CASCADE,
        related_name='posts',
    )

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class PostItemForm(ModelForm):
    class Meta:
        model = PostItem
        fields = ['title', 'content']
