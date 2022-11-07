from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

#Create your models here.



class Frecuencia(models.Model):
    id_frecuencia = models.AutoField(primary_key=True)
    dias = models.IntegerField()

    def nombre_frecuencia(self):
        return "{}". format(self.dias)

    def __str__(self):
        return self.dias


class Despacho(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    disponible = models.BooleanField()

    #ARREGLAR def nombre_despacho(self):
        # string st
        # mybool = self.disponible
        # if mybool : st ="no"
        # else: st ="si"
        # # return "{}". format(self.disponible)
    def __str__(mybool):
        return st


class Cantidad(models.Model):
    id_cantidad = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=(70))
    cantidad = models.IntegerField()

    def __str__(self):
        return self.tipo


class Asesoria_contable(models.Model):
    id_asesoria_contable = models.AutoField(primary_key=True)
    tiene_asesoria = models.BooleanField()
    def nombre_tiene_asesoria(self):
        return "{}". format(self.tiene_asesoria)
    def __str__(self):
        return self.nombre


class Marketing(models.Model):
    id_marketing = models.AutoField(primary_key=True)
    name = models.CharField(max_length=75)   

    def __str__(self):
        return self.nombre



class Insumo(models.Model):
    id_insumo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    id_cantidad = models.ForeignKey(Cantidad, on_delete=models.CASCADE)
    id_frecuencia = models.ForeignKey(Frecuencia, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    id_despacho = models.ForeignKey(Despacho, on_delete=models.CASCADE)
    id_insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)
        
    def __str__(self):
        return self.nombre

class Emprendimiento(models.Model):
    id_emprendimiento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=55)    
    email = models.CharField(max_length=125)    
    website = models.CharField(max_length=300)
    id_marketing = models.ForeignKey(Marketing, on_delete=models.CASCADE)
    id_asesoria_contable = models.ForeignKey(Asesoria_contable, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Industria(models.Model):
    id_industria = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=45) 
    id_emprendimiento = models.ForeignKey(Emprendimiento, on_delete=models.CASCADE) 

    def __str__(self):
        return self.nombre



class Perfil_emprendedora(models.Model):
    id_perfil_emprendedora = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=75)    
    fecha_nacimiento = models.DateField()   
    email = models.CharField(max_length=45)   
    telefono = models.IntegerField()   
    whatsapp = models.IntegerField()   
    telegram = models.CharField(max_length=30)   
    direccion = models.TextField(max_length=100)   
    id_emprendimiento = models.ForeignKey(Emprendimiento, on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre 


class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    id_emprendimiento = models.ForeignKey(Emprendimiento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Provincia(models.Model):
    id_provincia = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    id_provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre







