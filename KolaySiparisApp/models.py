from __future__ import unicode_literals

from django.db import models

class food(models.Model):
	name= models.CharField(max_length=255)
	fiyat=models.PositiveIntegerField()
	belongsrestaurant=models.CharField(max_length=255)
	def __unicode__(self):
      		return "name : %s , fiyat : %s , belongsrestaurant : %s" % (self.name,self.fiyat,self.belongsrestaurant)
class restaurant(models.Model):
	name= models.CharField(max_length=255)
	location=models.CharField(max_length=255)
	belongsfood=models.CharField(max_length=255)
	def __unicode__(self):
      		return "name : %s , location : %s , belongsfood : %s" % (self.name,self.fiyat,self.belongsfood)
