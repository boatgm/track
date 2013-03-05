from django.db import models
class auth(models.Model):
    account = models.EmailField()
    pwd = models.CharField(max_length=32)
    nickname = models.CharField(max_length=24)

class phone(models.Model):
    phonenum = models.CharField(max_length=11)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=140)
    status = models.BooleanField()
    auth_id = models.IntegerField()

    def __str__(self):
        return self.name

class phone_message(models.Model):
    send = models.CharField(max_length=11)
    to = models.CharField(max_length=11)
    content = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.name

class rss(models.Model):
    name = models.CharField(max_length=16)
    url = models.URLField()
    status = models.BooleanField()
    auth_id = models.IntegerField()

    def __str__(self):
        return self.name

class rss_item(models.Model):
    rss_id = models.IntegerField()
    title  = models.CharField(max_length=35)
    description  = models.CharField(max_length=35)
    link  = models.CharField(max_length=35)
    date = models.DateTimeField()
    article_id = models.IntegerField()

    def __str__(self):
        return self.name

class weibouser(models.Model):
    userid = models.IntegerField()
    name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=12)
    platform = models.CharField(max_length=10)
    token = models.CharField(max_length=32)
    status = models.BooleanField()
    auth_id = models.IntegerField()

    def __str__(self):
        return self.name

class weibouser_topic(models.Model):
    weibouser_id = models.IntegerField()
    text = models.TextField()
    date = models.DateTimeField()
    image_id = models.IntegerField()
    article_id = models.IntegerField()
    media_id = models.IntegerField()
    video_id = models.IntegerField()
    attachment_id = models.IntegerField()

    def __str__(self):
        return self.name

class mail(models.Model):
    mail = models.EmailField()
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    status = models.BooleanField()
    auth_id = models.IntegerField()

    def __str__(self):
        return self.name

class mail_topic(models.Model):
    send = models.EmailField()
    to = models.EmailField()
    topic = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.name

class articles(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateTimeField()
    category = models.CharField(max_length=10)
    status = models.BooleanField()
    url = models.URLField()

    def __str__(self):
        return self.name

class attachments(models.Model):
    md5 = models.CharField(max_length=32)
    name = models.CharField(max_length=50)
    size = models.FloatField()
    path = models.URLField()

class images(models.Model):
    md5 = models.CharField(max_length=32)
    name = models.CharField(max_length=50)
    size = models.FloatField()
    path = models.URLField()
    width = models.IntegerField()
    high = models.IntegerField()
    ambi = models.IntegerField()

