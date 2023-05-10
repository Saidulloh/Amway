from django.core.mail import send_mail

from core.celery import app


@app.task
def send_message(information, instance):
    try:
        send_mail('New order!', 
                f'ФИО: {information.name} \nНомер телефона: {instance.phone_number}\nПочта: {information.gmail} \nКомментарий: {instance.comment} \nНазвание продукта: {instance.title} \nЦена продукта: {instance.price}', 
                'ssavutokhunov@gmail.com',
                ['sattarzhanovdev@gmail.com'], 
                fail_silently=False)
    except Exception as ex:
        print(ex)


@app.task
def send_message_about_consultation(instance):
    try:
        send_mail('New person for consultation!', 
                f'ФИО: {instance.name} \nНомер телефона: {instance.phone_number} \nПочта: {instance.gmail}', 
                'ssavutokhunov@gmail.com',
                ['sattarzanov@gmail.com'], 
                fail_silently=False)
    except Exception as ex:
        print(ex)
