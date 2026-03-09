from django.db import models
class Department(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    objects = models.Manager()
    def __str__(self):
        return self.name
class Doctor(models.Model):
    full_name = models.CharField(max_length=150)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='doctors')
    specialty = models.CharField(max_length=100)
    image = models.ImageField(upload_to='doctors/')
    objects = models.Manager()
    def __str__(self):
        return self.full_name
class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name="Servis ati")
    description = models.TextField(verbose_name="servis haqqinda magliwmat")
    icon = models.CharField(max_length=50, help_text="Bootstrap icon klassi (misali: bi-heart-pulse)")
    objects = models.Manager()
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
    def __str__(self):
        return self.title

