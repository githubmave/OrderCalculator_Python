
class CartOne:
    # Given empty shopping cart
     cartItems=[]
    # Given product label and unit prices
     label='Dove Soap'
     UnitPrice=39.99
     def __init__(self):
        # add 5 Dove soap into shopping cart
        i=0
        while i < 5:
          CartOne.cartItems.append({'label':CartOne.label,'UnitPrice':CartOne.UnitPrice})
          i+=1
        # calculate total price
        self.totalPrice=CartOne.UnitPrice*5
        print(f'The total price for cart items is : {self.totalPrice}')       
myInstance = CartOne()