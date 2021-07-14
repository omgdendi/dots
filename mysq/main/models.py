from django.db import models


class Dots(models.Model):
    x_value = models.FloatField('X', max_length=15)
    y_value = models.FloatField('Y', max_length=15)
    r_value = models.IntegerField('R')
    result = models.BooleanField('Result')

    def __str__(self):
        return 'Точка - ' + str(self.id)

    class Meta:
        verbose_name = 'Точка'
        verbose_name_plural = 'Точки'
