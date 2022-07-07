from django.db import models


# точка погрузки или выгрузки самосвалов
class Point(models.Model):
    name = models.CharField(verbose_name='Наименование',
                            db_index=True,
                            unique=True,
                            max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пункт погрузки/выгрузки"  # имя в админке в ед.числе
        verbose_name_plural = "Пункты погрузки/выгрузки"  # имя в админке в мн.числе
        ordering = ['name']  # сортировка по возрастанию


# Таблица расстояний между точками загрузки-разгрузки
class Distance(models.Model):
    point_start = models.ForeignKey(Point,
                                    verbose_name='Пункт загрузки',
                                    related_name='pointStart',
                                    on_delete=models.PROTECT)
    point_final = models.ForeignKey(Point,
                                    verbose_name='Пункт разгрузки',
                                    related_name='pointFinal',
                                    on_delete=models.PROTECT)
    distance = models.DecimalField(verbose_name='Расстояние',
                                   max_digits=2,
                                   decimal_places=1,
                                   default=0.0)

    def __str__(self):
        return f"{self.point_start}->{self.point_final}"

    class Meta:
        verbose_name = "Расстояние между складами"
        verbose_name_plural = "Расстояние между складами"
        ordering = ['point_start', 'point_final']
