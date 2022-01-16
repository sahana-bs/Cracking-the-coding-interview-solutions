#python version of this(condensed): https://gist.github.com/yaswanthrajyadiki/f9b2ec5fbbc1368a54de

class item():
    #let's say every item is define the name of the item, quantity and price per unit
    def __init__(self, name,  price,quanity=1):
        self.name = name
        self.quantity = quanity
        self.price = price   #this is the price per unit

    def get_itemName(self):
        return self.name

    def get_quantity(self):
        return self.quantity

    def get_unitPrice(self):
        return self.price


class shoppingCart():
    def __init__(self, items=[], discount=0, tax=0, AmtPayable=0, TotalAmt=0):
        self.items = items
        self.discount = discount
        self.tax = tax
        self.AmtPayable = AmtPayable
        self.TotalAmt = TotalAmt

    def addToCart(self, newItem):
        self.items.append(newItem)

    def showCart(self):
        print("Name  | Quantity  |   Price")
        for i in self.items:
            print(i)

    def removeFromCart(self, item):
        try:
            self.items.remove(item)
            return
        except ValueError:
            print("Item not in cart")

    def get_TotalAmt(self):
        self.TotalAmt = 0
        for i in self.items:
            self.TotalAmt = self.TotalAmt + (i.quantity*i.price)
        return self.TotalAmt

    def get_PayableAmt(self):
        self.AmtPayable = self.TotalAmt - self.tax
        return self.AmtPayable




#let's test this now::

#create items to add to the cart
i1 = item("Cool Earphones", 30, 2)  #I'm in the US now, so price is in dollars!
i2 = item("Cool speakers", 50)
i3 = item("Cool headphones",80)

items = []
#add these items to the cart
cart = shoppingCart(items, 10)
cart.addToCart(i1)
cart.addToCart(i2)
cart.addToCart(i3)
cart.showCart()
