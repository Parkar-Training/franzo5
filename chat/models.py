from django.db import models


class ChatModel(models.Model):
    CId = models.AutoField
    to_id = models.IntegerField()
    from_id = models.IntegerField()
    msg = models.CharField(max_length=500, error_messages={
        "max_length": "Chat message cannot be more than 500 characters."})
    chat_created = models.DateTimeField(auto_now_add=True)
