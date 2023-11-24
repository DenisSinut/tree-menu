from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE, verbose_name='Родительская ветка')
    url = models.CharField(max_length=255, verbose_name='URL')
    named_url = models.CharField(max_length=255, null=True, blank=True, verbose_name='Имя URL')


    class Meta:
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.name
