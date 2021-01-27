from django.db import models
#from pyts import timezone
# Create your models here.

#class Post(models.Model):
#    title = models.CharField(max_length=50)
#    pub_date = models.DateTimeField('date published')
    #user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
#    content = models.TextField()

#    def __str__(self):
#        return self.postname

class Photo(models.Model):
    #post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    content = models.TextField(null=True)
    #pub_date = models.DateTimeField(auto_now_add=True, verbose_name='putDate',default=timezone.now)

    class Meta:
        db_table = "Photos"
        verbose_name = "Photos"
        verbose_name_plural = "Photos"

    def __str__(self):
        return self.title