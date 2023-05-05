from django.core.mail import send_mail

from core.celery import app


@app.task
def send_message(gmail, instance):
    try:
        send_mail('Bought a new product!', 
                f'User-gmail: {gmail} \nProduct title: {instance.title} \nProduct price: {instance.price}', 
                'ssavutokhunov@gmail.com',
                ['ssavutokhunov@gmail.com'], 
                fail_silently=False)
    except Exception as ex:
        print(ex)