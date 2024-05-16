from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class UsuarioManager(BaseUserManager):
    def create_user(self, correo_electronico, nombre_usuario, contraseña=None):
        if not correo_electronico:
            raise ValueError('El correo electrónico es obligatorio')
        usuario = self.model(correo_electronico=self.normalize_email(correo_electronico), nombre_usuario=nombre_usuario)
        usuario.set_password(contraseña)
        usuario.save(using=self._db)
        return usuario

class Usuario(AbstractBaseUser):
    ID_usuario = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=255)
    correo_electronico = models.EmailField(unique=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'correo_electronico'
    REQUIRED_FIELDS = ['nombre_usuario']

    def __str__(self):
        return self.nombre_usuario 

############################################# INVENTARIO ################################################
class Alimentos(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField(default=0)
    fecha_vencimiento = models.DateField()

    def __str__(self):
        return self.nombre

class Medicinas(models.Model):
    nombre = models.CharField(max_length=100)
    principio_activo = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField(default=0)
    fecha_vencimiento = models.DateField()

    def __str__(self):
        return self.nombre
    
class Juguetes(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre

class Utensilios(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField(default=0)
    esterilizable = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre