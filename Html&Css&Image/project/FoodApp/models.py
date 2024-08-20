from django.db import models

# Create your models here.
class Item(models.Model):
      def __str__(self):
            return self.item_name
      
      item_name=models.CharField(max_length=122)
      item_desc=models.CharField(max_length=122)
      item_price=models.IntegerField()
      item_image=models.CharField(max_length=5000,default='https://www.vecteezy.com/vector-art/22058960-no-image-available-icon')