from django.db import models
from django.contrib.auth.models import User


class Projects(models.Model):
    """  Проект """
    title = models.CharField(max_length=25)
    status = models.BooleanField(default=False)
    supervisor = models.ForeignKey(User, related_name='supervisor', on_delete=models.CASCADE)
    developers = models.ManyToManyField(User, related_name='developers')
    description = models.TextField('Описание', max_length=150)
    start = models.DateField('Начало проекта')
    end = models.DateField('Конец проекта')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Tasks(models.Model):
    """ Задачи проекта """
    title_task = models.CharField(max_length=50)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name="task")
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title_task

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Comments(models.Model):
    """ Комментарий """
    text_title = models.TextField("Текст", max_length=250)
    user = models.ForeignKey(User, verbose_name='user', on_delete=models.CASCADE, blank=False,
                             null=False, related_name='user')
    parent = models.ForeignKey('self', verbose_name='Родитель', on_delete=models.SET_NULL,
                               blank=True, null=True, related_name="children")
    project = models.ForeignKey(Projects, verbose_name="проект", on_delete=models.CASCADE,
                                blank=True, null=True, related_name="comments")

    def __str__(self):
        return self.text_title

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
