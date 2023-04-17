from django.db import models

# Create your models here.

class Emp(models.Model):  # Modelo creado para ejecutar migraciones
    # Definir los datos de la clase (campos de la tabla)
    # Si no se especifica lo contrario, todos los campos seran requeridos por defecto, es decir NOT NULL
    emp_name = models.TextField()
    emp_email = models.EmailField()
    emp_mobile = models.TextField()
