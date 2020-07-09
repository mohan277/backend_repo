from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 100)
    profile_pic = models.TextField()

    def __str__(self):
        return self.name

class Post(models.Model):
    content = models.CharField(max_length=1000)
    posted_at = models.DateTimeField(auto_now = True)
    posted_by = models.ForeignKey(User,on_delete = models.CASCADE)

    def __str__(self):
        return self.content

class Comment(models.Model):
    content = models.CharField(max_length = 1000)
    commented_at = models.DateTimeField(auto_now = True)
    commented_by = models.ForeignKey(User,on_delete = models.CASCADE)
    post = models.ForeignKey(Post,on_delete = models.CASCADE)
    parent_comment = models.ForeignKey(
        "self",on_delete = models.CASCADE,null = True,blank=True)

    def __str__(self):
        return self.content

class Reaction(models.Model):
    REACT_CHOICES=(
        ('WOW','WOW'),
        ('LIT','LIT'),
        ('LOVE','LOVE'),
        ('HAHA','HAHA'),
        ('THUMBS-UP','THUMBS-UP'),
        ('THUMBS-DOWN','THUMBS-DOWN'),
        ('ANGRY','ANGRY'),
        ('SAD','SAD')
        )

    post = models.ForeignKey(Post,on_delete = models.CASCADE,null = True)

    comment = models.ForeignKey(
        Comment,on_delete = models.CASCADE,null =True,blank=True)

    reaction = models.CharField(max_length=100,choices = REACT_CHOICES)

    reacted_at = models.DateTimeField(auto_now = True)

    reacted_by = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.reaction