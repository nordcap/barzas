from django.db import models


class Location(models.Model):
    # Месторасположение Матценности - ФИО, комната
    place = models.CharField(
        verbose_name="Расположение МЦ",
        db_index=True,
        max_length=50,
    )

    def __str__(self):
        return self.place

    class Meta:
        verbose_name = "Расположение"  # имя в админке в ед.числе
        verbose_name_plural = "Расположение"  # имя в админке в мн.числе
        ordering = ["place"]  # сортировка по возрастанию
