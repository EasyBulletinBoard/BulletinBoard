from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name="boards", blank=True)

    def __str__(self):
        return self.name

class Card(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    attachment = models.ImageField(upload_to="cards/", null=True, blank=True)
    likes = models.PositiveIntegerField(default=0)
    liked_by = models.ManyToManyField(User, related_name="liked_cards", blank=True)

    def __str__(self):
        return f"{self.title} - {self.author}"