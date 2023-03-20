from django.test import TestCase

# Create your tests here.
from book.models import Book


class book_test(TestCase):
    def setUp(self):
        self.book = Book.objects.create(name="python",price=450,qty=45,is_published=1,is_available=0)
        
    def test_id_name(self):
        self.assertEqual(self.book.price,450)
        self.assertEqual(self.book.name,"python")
    
    
    
    
    #  name = models.CharField(max_length=150)
    # price = models.FloatField()
    # qty = models.IntegerField()
    # is_published = models.BooleanField(default = 0)
    # is_available = models.BooleanField(default=1)