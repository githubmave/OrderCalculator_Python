# The class is to add 5 dove soaps into empty shopping cart and calculate the total price
class CartOne:
    # Given empty shopping cart
    cartItems=[]
    totalPrice=0
    def __init__(self,label,unitprice):
       # given label name and unitprice
        self.label=label
        self.unitprice=unitprice
    # add new items onto shopping cart
    def add_to_cart(self,m):
        # cartItems=[]
        subTotal=round(self.unitprice*m,2)
        print({self.label})
        print(f'{self.unitprice} x {m}')
        print(f'subTotal = {subTotal}')
        CartOne.cartItems.append({'label':self.label,'UnitPrice':self.unitprice,'Quantity':m})
        # print(f'test cartItems: {CartOne.cartItems}')

        CartOne.totalPrice=CartOne.totalPrice+subTotal
        CartOne.totalPrice=round(CartOne.totalPrice,2)
    # calculate the total price for cart items
    def count_cart_price (self):
        # print(f'The total price for cart one items is : {CartOne.totalPrice}')  
        return CartOne.totalPrice
# test class constructor(_init_)
myCart=CartOne('Dove',39.99)
assert myCart.label == 'Dove'
assert myCart.unitprice == 39.99
# test add_to_cart function
myCart.add_to_cart(5)
assert myCart.totalPrice==199.95
# test count_cart_price() function
assert myCart.count_cart_price()==199.95








