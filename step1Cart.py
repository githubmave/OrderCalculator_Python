
class CartOne:
    # Given empty shopping cart
     cartItems=[]
   
 
     def __init__(self,label,unitprice):
       # given label name and unitprice
        self.label=label
        self.unitprice=unitprice
     # add 5 Dove soap into shopping cart
     def countCartPrice (self,n):
        i=0
        while i < n:
          CartOne.cartItems.append({'label':self.label,'UnitPrice':self.unitprice})
          i+=1
        # calculate total price
   
        print(f'The total price for cart items is : {round(self.unitprice*n*100/100,2)}')  
        return  round(self.unitprice*n*100/100,2)
# myInstance = CartOne('Dove Soap', 39.99)
# test class constructor(_init_)
myCart=CartOne('Dove',39.99)
assert myCart.label == 'Dove'
assert myCart.unitprice == 39.99
# test countCartPrice function
myCart=CartOne('Dove',39.99)

assert myCart.countCartPrice(5) ==199.95



