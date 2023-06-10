# This class is to add 3 more dove soap to existing cart and calculate
from stepOneCart import CartOne
class CartTwo:
    # given empty shopping cart  
    totalPrice=0
    def __init__(self,label,unitprice):
        # envoke CartOne instance
        self.cartOne=CartOne(label,unitprice)
    # add  more  soaps onto empty cart and calculate the total price
    def add_to_cart_two(self,t):
        self.cartOne.add_to_cart(t)  
        CartTwo.totalPrice=self.cartOne.totalPrice   
# add 5 Dove soaps to cart two
cartTwo=CartTwo('Dove',39.99)
cartTwo.add_to_cart_two(5)
print(f'After adding 5 Dove, the total price for cart two is : {cartTwo.totalPrice}')
# continously add 3 Dove soaps to cart two
cartTwo.add_to_cart_two(3)
print(f'After adding 3 more Dove, the total price for cart two is : {cartTwo.totalPrice}')
# test class constructor
assert cartTwo.cartOne.label == 'Dove'
assert cartTwo.cartOne.unitprice == 39.99
# test add_to_cart_two()
assert cartTwo.totalPrice==319.92


