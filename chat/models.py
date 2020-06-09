from django.contrib.auth import get_user_model
from django.db import models


class Chat(models.Model):
    members = models.ManyToManyField(get_user_model(), related_name='chats')

    def get_members(self):
        return ",".join([str(member) for member in self.members.all()])


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='author')
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['sent_at']

    def __str__(self):
        return self.message
