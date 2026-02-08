from django.db import models
from django.urls import reverse

class Item(models.Model):

    #It defines how an object should look when converted to text.
    def __str__(self):
        return self.name
    
    #only for CBV
    def get_absolute_url(self):
        return reverse('mysite:detail')
    
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.URLField(
        max_length=500, default="https://png.pngtree.com/element_our/png/20180930/food-icon-design-vector-png_120564.jpg")
    is_available = models.BooleanField(default=True)
    created_at= models.DateTimeField(auto_now_add=True)
