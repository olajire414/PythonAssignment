from unittest import TestCase
from checkout_app import*

class CheckoutApp(TestCase):
    def test_that_i_have_items_the_subtotal_of_the_item_is_quantity_multiply_by_price(self):
        quantity = 2
        price = 200

        subtotal = quantity * price

        assertEqual(400,calculate_item_total(subtotal))

    
    def test_that_i_have_items_subtotal_the_discount_is_subtotal_multiply_by_discount_rate(self):

        discount_rate = 17.5/100
        subtotal = 1000

        discount_amount = subtotal * discount_rate

        assertEqual(discount_amount,get_discount(discount_amount))

    
    def test_that_i_have_items_subtotal_the_vat_amount_is_subtotal_minus_discount_multiply_by_vat_rate(self):
 
        vat_rate = 7.5/100
        discount_amount = 46
        subtotal = 1000

        vat_amount = (subtotal - discount_amount) * (vat_rate)

        assertEqual(vat_amount,calculate_vat(vat_amount))

        
        
        
        
