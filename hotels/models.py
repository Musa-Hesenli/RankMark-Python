from django.db import models

# Create your models here.
class CategoryModel(models.Model):
    name = models.CharField(verbose_name = 'Category name', max_length = 30)
    image = models.ImageField(verbose_name = 'Category image')

    class Meta:
        verbose_name_plural = 'Category Model'

    def __str__(self):
        return self.name

class Hotels(models.Model):
    name = models.CharField(max_length = 100, verbose_name = 'Hotels\'s name')
    main_image = models.ImageField(verbose_name = 'Main Image')
    about_short_text = models.CharField(verbose_name = 'Short text about', max_length = 100)
    place_in_map = models.CharField(max_length = 10000, verbose_name = "Map Query")
    view = models.IntegerField()
    email = models.EmailField()
    price = models.IntegerField(null = True)
    phone_number = models.CharField(max_length = 100)
    description = models.TextField()
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Restaurants'    

class Images(models.Model):
    restaurant = models.ForeignKey(Hotels, on_delete = models.CASCADE)
    image = models.ImageField()    

 
class Reviews(models.Model):
    restaurant = models.ForeignKey(Hotels, on_delete = models.CASCADE)
    writer = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.comment

class RatingOfHotel(models.Model):
    restaurant = models.ForeignKey(Hotels, on_delete = models.CASCADE)
    rate_number = models.IntegerField()    

