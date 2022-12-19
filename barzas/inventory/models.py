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


class Material(models.Model):
    # Матценность
    inv_number = models.CharField(
        verbose_name="Инвентарный номер",
        max_length=12,
        db_index=True,
    )
    name = models.CharField(
        verbose_name="Наименование МЦ",
        max_length=100,
        db_index=True,
    )
    count = models.PositiveIntegerField(
        verbose_name="Количество",
        default=0,
    )

    def __str__(self):
        return f"{self.name}[{self.inv_number}]"

    class Meta:
        verbose_name = "Матценность"  # имя в админке в ед.числе
        verbose_name_plural = "Матценности"  # имя в админке в мн.числе
        ordering = ["inv_number"]  # сортировка по возрастанию
