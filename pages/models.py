from django.db import models
# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    description = models.TextField(verbose_name="Klinika haqqinda magliwmat")
    video_url = models.URLField(blank=True, null=True, verbose_name="YouTube video linki")
    image = models.ImageField(upload_to='about/', verbose_name="Tiykargi bettegi suwret")
    text1_title=models.CharField(max_length=200)
    text1_text=models.TextField(null=True, blank=True)
    text2_title = models.CharField(max_length=200)
    text2_text = models.TextField(null=True, blank=True)
    text3_title = models.CharField(max_length=200)
    text3_text = models.TextField(null=True, blank=True)
    objects = models.Manager()
    class Meta:
        verbose_name = "Klinika haqqinda"
        verbose_name_plural = "Klinika haqqinda"
    def __str__(self):
        return self.title
class FAQ(models.Model):
    question = models.CharField(max_length=255, verbose_name="soraw")
    answer = models.TextField(verbose_name="juwap")
    objects = models.Manager()
    class Meta:
        verbose_name = "Kop beriletugin soraw"
        verbose_name_plural = "Kop beriletugin sorawlar"
    def __str__(self):
        return self.question
class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/', verbose_name="Suwret")
    caption = models.CharField(max_length=100, blank=True, verbose_name="Suwret ati (optional)")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    class Meta:
        verbose_name = "Galereya"
        verbose_name_plural = "Galereya"
    def __str__(self):
        return f"suwret {self.id}"


class Testimonial(models.Model):
    name = models.CharField(max_length=150)
    job = models.CharField(max_length=100)
    comment = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)

    def __str__(self):
        return self.name
