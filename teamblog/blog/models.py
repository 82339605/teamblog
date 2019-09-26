from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=11)
    loginname = models.CharField(max_length=30)
    pwd = models.CharField(max_length=20)
    uemail = models.EmailField(max_length=30)
    url = models.URLField(max_length=200)
    isActive = models.BooleanField(default=False)
    def __str__(self):
        return self.username
    class Meta:
        db_table='user'
        verbose_name_plural = '用户'
class Message(models.Model):
    author = models.CharField(max_length=20)
    time = models.CharField(max_length=50)
    about = models.CharField(max_length=20)
    reason = models.CharField(max_length=20,default='不为啥')
    imgs = models.CharField(max_length=40,default=True)
    def __str__(self):
        return self.author
    class Meta:
        db_table = 'message'
        verbose_name_plural = '文章信息'
class Topic(models.Model):
    justOne = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    select = models.CharField(max_length=30)
    content = models.CharField(max_length=1000)
    imgs = models.ImageField(upload_to='static/upload',null=True)
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'topic'
        verbose_name_plural = '超级大肥猫发表的博客'
class aboutMy(models.Model):
    text = models.CharField(max_length=1000)
    name = models.CharField(max_length=100)
    class Meta:
        db_table = 'about'
        verbose_name_plural = '留言'