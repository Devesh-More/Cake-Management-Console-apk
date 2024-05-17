class Shop:
    def __init__(self,id,prod_type,quantity,price):
        self.cid = id
        self.product = prod_type
        self.prod_quant = quantity
        self.prod_price = price

    def __str__(self):
        data = self.cid+","+self.product+","+self.prod_quant+","+str(self.prod_price)
        return data

if (__name__ == "__main__"):
    s1 = Shop(str(101),"Black Forest",str(8),str(400))
    with open("prodData.txt","r") as fp:
        for line in fp:
            inf = line.split("+")
            print(inf)
