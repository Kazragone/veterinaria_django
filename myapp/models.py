from django.db import models

ESPECIES_DE_ANIMALES = (
        (0, "Mamiferos"),
        (1, "Aves"),
        (2, "Reptiles"),
        (3, "Ranas y sapos")
)

TIPOS_DOCUMENTO = (
    ("dni", "DNI"),
    ("cd", "Cedula")
)

# Create your models here.

class Cliente(models.Model):
    tipo_documento = models.CharField("Tipo de documento", choices=TIPOS_DOCUMENTO, default="dni", max_length=10)
    documento = models.CharField(max_length=50, unique=True)
    fecha_nacimiento = models.DateField()
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    activo = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True) 

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return '{}, {}'.format(self.apellido, self.nombre)

class Animal(models.Model):
    especie = models.IntegerField(choices=ESPECIES_DE_ANIMALES, default=0)
    tipo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField(blank=True, null=True)
    duenio = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return self.nombre

class Enfermedad(models.Model):
    nombre = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Consulta(models.Model):
    fecha_de_consulta = models.DateTimeField(auto_now_add=True)
    animal = models.ForeignKey(Animal, on_delete=models.PROTECT)
    enfermedad = models.ForeignKey(Enfermedad, on_delete=models.PROTECT)
    observacion = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ['-fecha_de_consulta']

    def __str__(self):
        return 'Consulta con fecha {}'.format(self.fecha_de_consulta.strftime('%d/%m/%Y %H:%M:%S'))