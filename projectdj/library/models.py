from django.db import models

# We create a model or table where the data will be stored.
class Product(models.Model):
    id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/', verbose_name='image', null=True)
    price=models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        row='Product Name: ' + self.product_name + " - " + 'Price: $' + str(self.price)
        return row

    # We use this for delete the image
    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()