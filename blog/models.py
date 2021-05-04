from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Resource(models.Model):
    courseName=models.CharField(max_length=200)
    image=models.ImageField(default='default.jpg')
    content=models.TextField(default='Content to be displayed')
    file = models.FileField()
    def __str__(self):
        return self.courseName

class Courses(models.Model):
    courseName=models.CharField(max_length=200)
    image=models.ImageField(default='default.jpg')
    content=models.TextField(default='Content to be displayed')
    def __str__(self):
        return self.courseName



class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
DIFF_CHOICES=(
    ('easy','easy'),
    ('medium','medium'),
    ('hard','hard'),
)
class Quiz(models.Model):
    name=models.CharField(max_length=120)
    topic=models.CharField(max_length=120)
    number_of_question=models.IntegerField()
    time=models.IntegerField(help_text="duration of the quiz in minutes")
    score_to_pass = models.IntegerField(help_text="required score in %")
    difficuly=models.CharField(max_length= 6, choices=DIFF_CHOICES)

    def __str__(self):
        return f"{self.name}-{self.pk}"

    def get_questions(self):
        pass
