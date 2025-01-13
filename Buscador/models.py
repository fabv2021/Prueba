from django.db import models
from django.core import validators

# Create your models here.



class Empresas(models.Model):
   
    empresa = models.CharField(db_column='Empresa', max_length=500,blank=True,null=True)  # Field name made lowercase.
    rubro = models.CharField(db_column='Rubro', max_length=500,blank=True,null=True)  # Field name made lowercase.
    actividad = models.CharField(db_column='Actividad', max_length=500,blank=True,null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=3000,blank=True,null=True)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=100,blank=True,null=True)  # Field name made lowercase.
    comuna = models.CharField(db_column='Comuna', max_length=100,blank=True,null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=100,blank=True,null=True)  # Field name made lowercase.
    ciudad = models.CharField(db_column='Ciudad', max_length=1000,blank=True,null=True)  # Field name made lowercase.
    pais = models.CharField(db_column='Pais', max_length=100,blank=True,null=True)  # Field name made lowercase.
    contacto = models.CharField(db_column='Contacto', max_length=500,blank=True,null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100,blank=True,null=True)  # Field name made lowercase.
    validacion = models.CharField(db_column='Validacion', max_length=100,blank=True,null=True)  # Field name made lowercase.
    calificacion = models.CharField(db_column='Calificacion', max_length=5000,blank=True,null=True)  # Field name made lowercase.
    
    fields ='__all__'

    class Meta:
        
        db_table = 'empresas'


