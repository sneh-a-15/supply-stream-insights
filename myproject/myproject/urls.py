from django.contrib import admin
from django.urls import path
from app1 import views as view1
from inventory import views as view2


urlpatterns = [
    # path('', view2.demo, name='demo'),  # Make sure you have a demo view in inventory
    path('admin/', admin.site.urls),
    path('', view1.SignUp, name='signup'),
    path('login/', view1.LoginPage, name='login'),
    path('logout/', view1.LogoutPage, name='logout'),
    path('products/', view2.product_list, name='product_list'),  # Ensure this view exists in inventory
    path('dashboard/', view1.user_dashboard, name='user_dashboard'),
    path('preferences/', view1.select_preferences, name='select_preferences'),
    path('notifications/', view2.user_notifications, name='user_notifications'),
    path('notifications/mark-resolved/<int:notification_id>/', view2.mark_notification_resolved, name='mark_notification_resolved'),
    path('out-of-stock/', view2.out_of_stock_products, name='out_of_stock_products'),

]