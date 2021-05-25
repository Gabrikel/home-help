from django.test import TestCase
from django.contrib.auth.models import User
from store.models import Category, Store, Product

class TestCategoriesModel(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name='lacost', slug='lacost')

    def test_category_model_entry(self):
        """
        Test Category model insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_entry(self):
        """
        Test Category model default name
        """
        data = self.data1
        self.assertEqual(str(data), 'lacost')

class TestStoreModel(TestCase):
    def setUp(self):
        Category.objects.create(name='django', slug='django')
        self.data1 = Store.objects.create(name = 'test name', slug = 'test-name', category_id=1, address = 'test address', city = 'test city', cep = '12345678')
    
    def test_store_model_entry(self):
        """
        Test Store model insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Store))
        self.assertEqual(str(data), 'test name')
    

class TestProductModel(TestCase):
    def setUp(self):
        Category.objects.create(name='django', slug='django')
        Store.objects.create(name = 'test name', slug = 'test-name', category_id=1, address = 'test address', city = 'test city', cep = '12345678')
        self.data1 = Product.objects.create(category_id=1, store_id=1, name = 'product test', description = 'description test', 
            slug = 'product-test', price = 0, unity = 'unity test')

    def test_product_model_entry(self):
        """
        Test Product model insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'product test')

