from django.core.mail import send_mail

from core.celery import app


@app.task
def send_message(information, instance):
    try:
        send_mail('New order!', 
                f'User-name: {information.name} \nUser-gmail: {information.gmail} \nProduct title: {instance.title} \nProduct price: {instance.price}', 
                'ssavutokhunov@gmail.com',
                ['sattarzhanovdev@gmail.com'], 
                fail_silently=False)
    except Exception as ex:
        print(ex)


@app.task
def send_message_about_consultation(instance):
    try:
        send_mail('New person for consultation!', 
                f'User-name: {instance.name} \nUser-gmail: {instance.gmail} \Phone number: {instance.phone_number} \nDate time: {instance.created_at}', 
                'ssavutokhunov@gmail.com',
                ['sattarzanov@gmail.com'], 
                fail_silently=False)
    except Exception as ex:
        print(ex)
