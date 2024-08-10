from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
        db_table = 'category'


class Expense(models.Model):
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='expenses')
    description = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.date} - {self.category.name}: {self.amount}"

    class Meta:
        verbose_name_plural = 'Expenses'
        db_table = 'expense'
