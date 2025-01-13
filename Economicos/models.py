from django.db import models

# Create your models here.
class PreciosPromedios(models.Model):
    producto = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    precio = models.IntegerField()
    promedio = models.IntegerField()
    minimo = models.IntegerField()
    maximo = models.IntegerField()
    
class ProductoZapatos(models.Model):
    fecha = models.DateField()
    producto = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    precio = models.IntegerField()
    promedio = models.IntegerField()
    minimo = models.IntegerField()
    maximo = models.IntegerField()
    
    class Meta:
        ordering = ('fecha',)

class Economicos(models.Model):
    fecha = models.DateField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    productos = models.CharField(db_column='Productos', max_length=12, blank=True, null=True)  # Field name made lowercase.
    pais = models.CharField(db_column='Pais', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ciudades = models.CharField(db_column='Ciudades', max_length=12, blank=True, null=True)  # Field name made lowercase.
    precios = models.FloatField(db_column='Precios', blank=True, null=True)  # Field name made lowercase.
    minimo = models.FloatField(db_column='Minimo', blank=True, null=True)  # Field name made lowercase.
    maximo = models.FloatField(db_column='Maximo', blank=True, null=True)  # Field name made lowercase.
    promedio = models.FloatField(db_column='Promedio', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'economicos'