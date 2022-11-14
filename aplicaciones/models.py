from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

#Create your models here.



class Frecuencia(models.Model):
    id_frecuencia = models.AutoField(primary_key=True)
    dias = models.IntegerField()

    def nombre_frecuencia(self):
        result = "{}". format(self.dias)
        return result +' días'

    def __str__(self):
        return self.nombre_frecuencia()

class Despacho(models.Model):
    id_despacho = models.AutoField(primary_key=True)
    disponible = models.BooleanField()

    def esta_disponible(self):
        result = "{}". format(self.disponible)
        if result == "True":
            return "Si"
        if result == "False":
            return "No"
        else:
            return "Quizas"

    def __str__(self):
        return self.esta_disponible()


class Cantidad(models.Model):
    OPCIONES =(
            ('Kilos','Kilos'),
            ('Gramos','Gramos'),
            ('Litros','Litros'),
            ('Metros','Metros'),
            ('Metros²','Metros²'),
            ('Metros³','Metros³'),
            ('Centimetros','Centimetros'),
            ('Unidad(es)','Unidad(es)')
        )

    id_cantidad = models.AutoField(primary_key=True)
    tipo = models.CharField(choices=OPCIONES,max_length=(70))
    cantidad = models.IntegerField()

    def valor_compuesto(self):
        result1 = "{}". format(self.tipo)
        result2 = "{}". format(self.cantidad)
        return  result2 +' '+ result1 

    def __str__(self):
        return self.valor_compuesto()


class Asesoria_contable(models.Model):
    id_asesoria_contable = models.AutoField(primary_key=True)
    tiene_asesoria = models.BooleanField()
    def nombre_tiene_asesoria(self):
        result = "{}". format(self.tiene_asesoria)
        if result == "True":
            return "Si"
        if result == "False":
            return "No"
        else:
            return "Quizas"
        
    def __str__(self):
        return self.nombre_tiene_asesoria()


class Marketing(models.Model):
    id_marketing = models.AutoField(primary_key=True)
    name = models.CharField(max_length=75)   

    def __str__(self):
        return self.name


class Industria(models.Model):
    id_industria = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=45) 
    
    def __str__(self):
        return self.name

class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre

class Provincia(models.Model):
    id_region = models.ForeignKey(Region, on_delete=models.CASCADE)
    id_provincia = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    
    def __str__(self):
        return self.nombre


class Comuna(models.Model):
    id_provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    id_comuna = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    
    def __str__(self):
        return self.nombre


class Perfil_emprendedora(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_perfil_emprendedora = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=75)    
    fecha_nacimiento = models.DateField()   
    email = models.CharField(max_length=45)   
    telefono = models.IntegerField()   
    whatsapp = models.IntegerField()   
    telegram = models.CharField(max_length=30)   
    direccion = models.TextField(max_length=100)   
    
    def __str__(self):
        return self.nombre 

class Emprendimiento(models.Model):
    id_perfil_emprendedora = models.ForeignKey(Perfil_emprendedora, on_delete=models.CASCADE)
    id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    id_industria = models.ForeignKey(Industria, on_delete=models.CASCADE)
    id_emprendimiento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=55)    
    email = models.CharField(max_length=125)    
    website = models.CharField(max_length=300)
    id_marketing = models.ForeignKey(Marketing, on_delete=models.SET_NULL, blank=True, null=True)
    id_asesoria_contable = models.ForeignKey(Asesoria_contable, on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.nombre



class Producto(models.Model):
    id_emprendimiento = models.ForeignKey(Emprendimiento, on_delete=models.CASCADE)
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    id_despacho = models.ForeignKey(Despacho, on_delete=models.SET_NULL, blank=True, null=True)
            
    def __str__(self):
        return self.nombre

class Insumo(models.Model):
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    id_insumo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    id_cantidad = models.ForeignKey(Cantidad, on_delete=models.SET_NULL, blank=True, null=True )
    id_frecuencia = models.ForeignKey(Frecuencia, on_delete=models.SET_NULL, blank=True, null=True )
    
    def __str__(self):
        return self.nombre
























