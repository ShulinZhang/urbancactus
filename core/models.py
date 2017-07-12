from django.db import models
from django.urls import reverse

# Create your models here.
class Event(models.Model):
	slug = models.SlugField(primary_key=True, max_length=255)
	title = models.CharField(max_length=255)
	image = models.CharField(max_length=255)
	introduction = models.TextField()
	full_content = models.TextField()
	event_date = models.DateField()
	publish_date = models.DateField()

	def __str__(self):
		return str(self.event_date) + " - " + self.title + " (published: " + str(self.publish_date) + ")"

	def get_absolute_url(self):
		return reverse('events-single', args=[self.slug])

	class Meta:
		ordering = ['-event_date', '-publish_date']

class ProductSeries(models.Model):
	slug = models.SlugField(primary_key=True, max_length=255)
	title = models.CharField(max_length=255)
	image = models.CharField(max_length=255)

	def __str__(self):
		return self.title

class Product(models.Model):
	slug = models.SlugField(primary_key=True, max_length=255)
	title = models.CharField(max_length=255)
	image = models.CharField(max_length=255)
	description = models.TextField()
	series = models.ForeignKey(ProductSeries, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.title + " (" + str(self.series) + ")"

class Partner(models.Model):
	name = models.CharField(max_length=255)
	url = models.URLField()
	logo = models.CharField(max_length=255)
	story = models.TextField()
	products = models.ManyToManyField(Product)

	def __str__(self):
		return self.name

class MapType(models.Model):
	name = models.CharField(max_length=255)
	icon = models.CharField(max_length=255, null=True, blank=True)
	colour = models.CharField(max_length=10, null=True, blank=True)

	def __str__(self):
		return self.name

class MapMarker(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	latitude = models.DecimalField(max_digits=9, decimal_places=6)
	longitude = models.DecimalField(max_digits=9, decimal_places=6)
	link = models.URLField()
	map_type = models.ForeignKey(MapType, on_delete=models.CASCADE)

	def __str__(self):
		return self.name + " (" + str(self.map_type) + " at " + str(self.latitude) + ", " + str(self.longitude) + ")"
