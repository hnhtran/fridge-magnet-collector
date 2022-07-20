from django.db import models
from django.urls import reverse

# Create your models here.
WHERE = (
        ('FR', 'Fridge'),
        ('DR', 'Door'),
        ('BR', 'Wall Board'),
        ('OT', 'Other'),
)

class Magnet(models.Model):
    name = models.CharField(max_length=50)
    kind = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    year = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'magnet_id': self.id})

class Surface(models.Model):
    date = models.DateField('Displayed date')
    where = models.CharField(
        'Surface location',
        max_length=2,
        choices=WHERE,
        default=WHERE[0][0]
        # default='FR'
    )
    
    magnet = models.ForeignKey(Magnet, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_where_display()} on {self.date}'