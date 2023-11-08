from django.db import models
from django.utils import timezone
import uuid
from apps.user.models import Profile, UserAccount


# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, default=uuid.uuid4)
    text = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    is_active = models.BooleanField(blank=True, default=True)
    likes = models.IntegerField(default=0, blank=True)
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(blank=True, null=True)
    deleted = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f"{self.user} create a post at {self.created}"


class Comment(models.Model):
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_active = models.BooleanField(blank=True, default=True)
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(blank=True, null=True)
    deleted = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"user {self.user_id} comment {self.post_id}"


class Like_post(models.Model):
    user_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user_id', 'post_id'],  name="unique_likes")
        ]

    def __str__(self):
        return f"user {self.user_id} like {self.post_id}"
