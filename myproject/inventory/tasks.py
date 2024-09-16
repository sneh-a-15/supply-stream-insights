# inventory/tasks.py
from celery import shared_task
from app1.models import UserProduct, Notification
from django.contrib.auth.models import User
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
                # Create or update notifications
                notifications = Notification.objects.filter(product=product, resolved=False)
                if not notifications.exists():
                    users = User.objects.all()  # Or filter users based on your criteria
                    for user in users:
                        Notification.objects.create(
                            user=user,
                            product=product,
                            message=f'Stock for {product.product_name} is low. Current stock: {product.stock_level}.'
                        )
                    logger.info(f"Created in-app notification for {product.product_name}.")
            else:
                # Mark notifications as resolved if stock is sufficient
                notifications = Notification.objects.filter(product=product, resolved=False)
                if notifications.exists():
                    notifications.update(resolved=True)
                    logger.info(f"Updated notifications for {product.product_name}.")
    except Exception as e:
        logger.error(f"Error in reduce_stock task: {e}")
