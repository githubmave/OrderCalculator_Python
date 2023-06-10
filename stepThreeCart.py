# This class is to add 2 Dove , then add 2 Axe Deos to cart
from stepOneCart import CartOne
class CartThree:
    # given empty shopping cart
    totalPrice=0
    def __init__(self, label, unitprice):
        self.cartOne=CartOne(label,unitprice)
    # add items into shopping cart and calculate the total price
    def add_to_cart_three(self,r):
        self.cartOne.add_to_cart(r)
        CartThree.totalPrice=self.cartOne.totalPrice
    def add_tax(self,rate):
        print(f'The sale tax is: {round(CartThree.totalPrice*rate,2)}')
        CartThree.totalPrice=CartThree.totalPrice+CartThree.totalPrice*rate
        CartThree.totalPrice=round(CartThree.totalPrice,2)
# add 2 Dove soaps into cart three
cartThree=CartThree('Dove',39.99)
cartThree.add_to_cart_three(2)
print(f'After adding 2 Dove soaps, the total price for cart three is: {cartThree.totalPrice}')
# continously add 2 Axe Deos into cart three 
cartThree=CartThree('Axe',99.99)
cartThree.add_to_cart_three(2)
print(f'After adding another 2 Axe Deos , the total price for cart three is: {cartThree.totalPrice}')
# add sale tax to the total price
cartThree.add_tax(0.125)
print(f'After adding sale tax , the total price is: {cartThree.totalPrice}')
# test constructor
assert cartThree.cartOne.label=='Axe'
assert cartThree.cartOne.unitprice==99.99
# test add_to_cart_three
assert cartThree.totalPrice==314.95
print(f'after add cartThrees, total is: {cartThree.totalPrice}')

