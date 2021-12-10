from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=100, blank=True, unique=True)
    author = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', null=True, blank=True,)
    body = models.TextField(blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.title