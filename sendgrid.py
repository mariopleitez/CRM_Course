from django.core.mail import send_mail
send_mail('Subject here', 'Here is the message.', 'mariopleitez@gmail.com', ['mariopleitez@gmail.com'], fail_silently=False)