from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    username = models.CharField(db_column="username",max_length=50)
    email = models.EmailField(unique=True, max_length=50)
    password = models.CharField(max_length=50)
    avatar = models.CharField(max_length=100)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    cod_emp = models.IntegerField(db_column='COD_EMP')  # Field name made lowercase.
    rut_empresa = models.IntegerField(db_column='RUT_EMPRESA')  # Field name made lowercase.

    class Meta:
        db_table = 'usuario'