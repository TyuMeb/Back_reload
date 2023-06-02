from django.db import models

from main_page.models import UserAccount


# class Room(models.Model):
#     name = models.CharField(max_length=128)
#     online = models.ManyToManyField(to=UserAccount, blank=True)
#
#     def get_online_count(self):
#         return self.online.count()
#
#     def join(self, user):
#         self.online.add(user)
#         self.save()
#
#     def leave(self, user):
#         self.online.remove(user)
#         self.save()
#
#     def __str__(self):
#         return f'{self.name} ({self.get_online_count()})'


class Conversation(models.Model):
    initiator = models.ForeignKey(to=UserAccount, on_delete=models.SET_NULL, null=True, related_name='initiator')
    receiver = models.ForeignKey(to=UserAccount, on_delete=models.SET_NULL, null=True, related_name='receiver')
    start_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.initiator} - {self.receiver}'


class Message(models.Model):
    sender = models.ForeignKey(to=UserAccount, on_delete=models.CASCADE)
    conversation_id = models.ForeignKey(to=Conversation, on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    content = models.FileField(upload_to='files/', blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return f'{self.sender.surname} {self.sender.name}: {self.text}[:50] ({self.timestamp})'
