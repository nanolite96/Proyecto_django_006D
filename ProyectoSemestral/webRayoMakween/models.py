from django.db import models

# Create your models here.
class mecanico (models.Model):
    nombre_mec = models.CharField(primary_key=True,max_length=30)
    imagen = models.ImageField(upload_to='catego',null=True)

    def __str__(self):
        return self.nombre_mec

class Trabajos (models.Model):
    codigo = models.AutoField(primary_key=True)
    diagnostico = models.CharField(max_length=50)
    nombre = models.ForeignKey(mecanico,on_delete=models.CASCADE)
    fecha = models.TextField()
    materiales = models.TextField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='atenciones', null=True)
    comentario = models.TextField()
    publicar = models.BooleanField(default=False)

    def __str__(self):
        return str(self.codigo)

class contacto(models.Model):
    nombre_cl=models.TextField()
    correo=models.TextField()
    asunto=models.TextField()
    sugerencia=models.TextField()
    
    def __str__(self):
        return self.nombre_cl