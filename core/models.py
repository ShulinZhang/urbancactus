from django.db import models
from django.urls import reverse

# Create your models here.
class Event(models.Model):
	slug = models.SlugField(primary_key=True, max_length=255)
	english_name = models.CharField(max_length=255)
	chinese_name = models.CharField(max_length=255)
	image = models.CharField(max_length=255)
	english_introduction = models.TextField()
	chinese_introduction = models.TextField()
	english_full_description = models.TextField()
	chinese_full_description = models.TextField()
	event_date = models.DateField()
	publish_date = models.DateField()

	def __str__(self):
		return str(self.event_date) + " - " + self.english_name + " (published: " + str(self.publish_date) + ")"

	def get_absolute_url(self):
		return reverse('events-single', args=[self.slug])

	class Meta:
		ordering = ['-event_date', '-publish_date']

class ProductSeries(models.Model):
	slug = models.SlugField(primary_key=True, max_length=255)
	english_name = models.CharField(max_length=255)
	chinese_name = models.CharField(max_length=255)
	#english_description = models.TextField()
	#chinese_description = models.TextField()
	english_graphic = models.CharField(max_length=255)
	chinese_graphic = models.CharField(max_length=255)
	icon = models.CharField(max_length=255)
	image = models.CharField(max_length=255)

	def __str__(self):
		return self.english_name

	def get_absolute_url(self):
		return reverse('products-single', args=[self.slug])

class Product(models.Model):
	slug = models.SlugField(primary_key=True, max_length=255)
	english_name = models.CharField(max_length=255)
	chinese_name = models.CharField(max_length=255)
	english_description = models.TextField()
	chinese_description = models.TextField()
	image = models.CharField(max_length=255)
	series = models.ForeignKey(ProductSeries, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.english_name + " (" + str(self.series) + ")"

class Partner(models.Model):
	slug = models.CharField(max_length=255)
	english_name = models.CharField(max_length=255)
	chinese_name = models.CharField(max_length=255)
	english_url = models.URLField()
	chinese_url = models.URLField()
	logo = models.CharField(max_length=255)
	english_description = models.TextField()
	chinese_description = models.TextField()
	alliance_member = models.BooleanField(default=False)
	usage_image = models.CharField(max_length=255, default="")
	product_series = models.ManyToManyField(ProductSeries)

	def __str__(self):
		return self.english_name

	def get_absolute_url(self):
		return reverse('partners-single', args=[self.slug])

class MarkerType(models.Model):
	english_name = models.CharField(max_length=255)
	chinese_name = models.CharField(max_length=255)
	icon = models.CharField(max_length=255, null=True, blank=True)
	colour = models.CharField(max_length=10, null=True, blank=True)

	def __str__(self):
		return self.english_name

class Marker(models.Model):
	english_name = models.CharField(max_length=255)
	chinese_name = models.CharField(max_length=255)
	english_description = models.TextField()
	chinese_description = models.TextField()
	latitude = models.DecimalField(max_digits=9, decimal_places=6)
	longitude = models.DecimalField(max_digits=9, decimal_places=6)
	english_url = models.URLField()
	chinese_url = models.URLField()
	marker_type = models.ForeignKey(MarkerType, on_delete=models.CASCADE)

	def __str__(self):
		return self.english_name + " (" + str(self.map_type) + " at " + str(self.latitude) + ", " + str(self.longitude) + ")"

class Map(models.Model):
	slug = models.CharField(max_length=255)
	english_name = models.CharField(max_length=255)
	chinese_name = models.CharField(max_length=255)
	marker_types = models.ManyToManyField(MarkerType)

	def __str__(self):
		return self.slug

	def get_absolute_url(self):
		return reverse('map', args=[self.slug])
