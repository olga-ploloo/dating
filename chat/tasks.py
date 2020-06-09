from django.conf import settings
from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from chat.models import Message, Chat
User = get_user_model()


@shared_task
def new_message(message_id):
    message = Message.objects.filter(is_read=False).filer(id=message_id).first()
    if message:
        members_ids = Chat.objects.values_list('members__id', flat=True).get(id=message.chat_id)
        message_author = message.author_id
        for member in members_ids:
            if member != message_author:
                user = User.objects.get(id=member)
                email_message = f'Hi {user.first_name}! You have new message ' \
                                f'from {message.author}:\n  {message.message}\n'
                send_mail(
                    subject='New message',
                    message=email_message,
                    from_email=settings.ADMIN_EMAIL,
                    recipient_list=[user.email]
                )



