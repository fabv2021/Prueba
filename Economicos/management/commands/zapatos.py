import csv
from datetime import datetime
from django.utils.formats import get_format
from itertools import islice
from django.conf import settings
from django.core.management.base import BaseCommand
from Economicos.models import ProductoZapatos

class Command(BaseCommand):
    help = 'Load data'
    
    def handle(self,*args,**kwargs):
        datafiles = settings.BASE_DIR /'data'/'zapatos.csv'
        
        with open(datafiles,'r') as csvfile:
            reader = csv.DictReader(islice(csvfile,1,None))
            for row in reader:
                fecha = datetime.strptime('01-Enero-2022','%d-%B-%Y')
                fecha = datetime.strptime('01-enero-2022','%d-%B-%Y'
                    day = 1,
                    month=(row['Mes']),
                    year=int(row['Ano']),
                ))
                
                ProductoZapatos.objects.get_or_create(
                    date=fecha,
                    producto = row['Productos'],
                    pais = row['Pais'],
                    ciudad = row['Ciudades'],
                    precio = row['Precios'],
                    promedio = row['Valor Promedio'],
                    minimo = row['Valor Minimo'],
                    maximo = row['Valor Maximo'],                    
                    )