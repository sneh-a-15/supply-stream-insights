from celery import shared_task
from app1.models import UserProduct
from django.core.mail import send_mail
import logging

logger = logging.getLogger(__name__)

@shared_task
def reduce_stock():
    try:
        logger.info("Starting reduce_stock task.")
        products = UserProduct.objects.all()
        for product in products:
            if product.stock_level > 0:
                product.stock_level -= 1
                product.save()
                logger.info(f"Reduced stock for {product.product_name}. New stock level: {product.stock_level}")

            if product.stock_level <= 300:
                notify_supplier(product)
    except Exception as e:
        logger.error(f"Error in reduce_stock task: {e}")

def notify_supplier(product):
    try:
        send_mail(
            'Stock Alert',
            f'Stock for {product.product_name} is low. Current stock: {product.stock_level}.',
            'nairsneha1508@gmail.com',
            ['extsnehaa@gmail.com'],
            fail_silently=False,
        )
        logger.info("Mail sent!")
    except Exception as e:
        logger.error(f"Error sending email: {e}")
