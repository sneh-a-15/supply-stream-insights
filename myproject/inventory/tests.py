from django.test import TestCase

# Create your tests here.
from .models import Product, Supplier, PurchaseOrder

class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            id=1,
            name='Test Product',
            description='A test product description',
            category='Test Category',
            price=99.99,
            image_url='http://example.com/image.jpg'
        )

    def test_product_str(self):
        self.assertEqual(str(self.product), 'Test Product')

class SupplierModelTest(TestCase):
    def setUp(self):
        self.supplier = Supplier.objects.create(
            id=1,
            name='Test Supplier',
            contact_info='Contact info for test supplier'
        )

    def test_supplier_str(self):
        self.assertEqual(str(self.supplier), 'Test Supplier')

class PurchaseOrderModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            id=1,
            name='Test Product',
            description='A test product description',
            category='Test Category',
            price=99.99,
            image_url='http://example.com/image.jpg'
        )
        self.supplier = Supplier.objects.create(
            id=1,
            name='Test Supplier',
            contact_info='Contact info for test supplier'
        )
        self.purchase_order = PurchaseOrder.objects.create(
            product=self.product,
            supplier=self.supplier,
            quantity=10,
            date_ordered='2024-08-01'
        )

    def test_purchase_order_str(self):
        expected_str = f"Order {self.purchase_order.id} - {self.product.name} from {self.supplier.name}"
        self.assertEqual(str(self.purchase_order), expected_str)