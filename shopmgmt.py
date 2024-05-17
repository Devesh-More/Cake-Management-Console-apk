from shoppie import Shop
import os
from tabulate import tabulate


class ShopMgmt:
    # method to add cake details
    def addProduct(self,s1):
        with open("prodData.txt","a") as fp:
            data = str(s1)
            fp.write(data)
            fp.write("\n")
        print("\nRecord saved successfully")
    
    # method to display cake details
    def displayData(self):
        try:
            with open("prodData.txt","r") as fp:
                # if file is empty
                if os.path.getsize("prodData.txt") == 0:
                    print("\nNo records found, file was empty")

                # display format
                else:
                    # used tabulate library function
                    myTable = (["Cake ID","Cake Name","Available","Cost"])
                    content = []
                    for line in fp:
                        data = line.split(",")
                        if (int(data[2])>0):
                            content.append(data)
                    if (len(content) > 0):
                        print()
                        # print(content)
                        print(tabulate(content,headers=myTable,tablefmt="fancy_grid"))
                    else:
                        print("\nCakes are out of stock")
                    
        except FileNotFoundError :
            print("\nFile not exists")
        except:
                print("\nSomething went wrong")

    # method for cake buying   
    def buyProduct(self,prod_type):
            allProd = []
            allCake = []
            # allquant = []
            found = False
            try:
                # to store Cake names in allCake (list)
                with open("prodData.txt","r") as lp:
                    for info in lp:
                        note = info.split(",")
                        if (note[2] > "0"):
                            allCake.append(note[1])
                        # allquant.append(note[2])

                with open("prodData.txt","r") as fp:
                    if os.path.getsize("prodData.txt") == 0:
                        print("\nNo records found, file was empty")
                    else:
                        for line in fp:
                            data = line.split(",")

                            # code for name matching of cake
                            if(data[1] == prod_type and int(data[2])>0):

                                print(f"\nCost per cake is ₹{data[3]}")
                                price = float(data[3])
                                
                                # if quantity given more than availability
                                ans = int(input("Enter quantity to buy: "))
                                if (ans > int(data[2])):
                                    print(f"\nOnly {data[2]} cakes left")
                                    print("\nEnter choice 2 to get cake details")
                                    break

                                else:    
                                    found = True
                                    cost = ans * price
                                    data[2] = int(data[2]) - ans
                                    data[2] = str(data[2])

                            line = ",".join(data)
                            allProd.append(line)
                        
                        
                        if (found):
                            with open("prodData.txt","w") as fp: 
                                for prod in allProd:
                                    fp.write(prod)

                                print(f"\nYour bill is ₹{(cost)} only")
                                print("Thank You 😊 Visit Again") 
   
                        elif (prod_type not in allCake):
                            print(f"\n{prod_type} is not available\nAvailable cakes are")
                            self.displayData()  # to display available cakes
                            ask = input("\nWill you prefer any of them (Yes/No)?\n")
                            if (ask.lower() == "yes"):
                                prod_type = input("Enter Cake name: ").capitalize()
                                self.buyProduct(prod_type) 
                            else:
                                if(ask.lower() == "no"):
                                    print("Thank You 😊 Visit Again")

                                else:
                                    if (ask or ask == ""):
                                        print("\nInvalid input was given")
                                        print("Answer should be (Yes/No)")

                        
            except FileNotFoundError:
                print("\nFile not exists")
            except:
                print("\nSomething went wrong")
    
    # method for searching cake by Id
    def cakeID(self,id):
        try:
            with open("prodData.txt","r") as fp:
                if os.path.getsize("prodData.txt") == 0:
                   print("\nNo records found, file was empty")
                else:
                    for line in fp:
                        data = line.split(",")
                        if (data[0] == id):
                            print("\nRecord found")

                            # display format
                            print(f'''
                            \n\t\t\tCake-id    :  {data[0]}
                            \n\t\t\tCake-name  :  {data[1]}
                            \n\t\t\tAvailable  :  {data[2]}
                            \n\t\t\tCake price :  ₹{data[3]}
                            ''')
                            break
                    else:
                        print(f"\nCake-id {id} not exists")
        except FileNotFoundError:
            print("\nFile not exists")
        except:
                print("\nSomething went wrong")
    
    # method for searching cake by name
    def cakeName(self,prod_type):
        try:
            with open("prodData.txt","r") as fp:
                if os.path.getsize("prodData.txt") == 0:
                    print("\nNo records found, file was empty")
                else:
                    for line in fp:
                        data = line.split(",")
                        if (data[1] == prod_type):
                            print("\nRecord found")

                            # display format
                            print(f'''
                            \n\t\t\tCake-id    :  {data[0]}
                            \n\t\t\tCake-name  :  {data[1]}
                            \n\t\t\tAvailable  :  {data[2]}
                            \n\t\t\tCake price :  ₹{data[3]}
                            ''')
                            break
                    else:
                        print("\nNo record found")
        except FileNotFoundError:
            print("\nFile not exists")
        except:
                print("\nSomething went wrong")
    
    # method for editing cake data
    def editData_byId(self,id):
        allProd = []
        allId = []
        allCake = []
        found = False
        try:
            # to store Id's and cake names in allId and allCake (list)
            with open("prodData.txt","r") as lp:
                for info in lp:
                    note = info.split(",")
                    allId.append(note[0])
                    allCake.append(note[1])
            
            # for matching the given details
            with open("prodData.txt","r") as fp:
                for line in fp:
                    data = line.split(",")
                    if (data[0] == id):
                        found = True

                        print("\nRecord found")
                        print(f'''
                        \n\t\t\tCake-id    :  {data[0]}
                        \n\t\t\tCake-name  :  {data[1]}
                        \n\t\t\tAvailable  :  {data[2]}
                        \n\t\t\tCake price :  ₹{data[3]}
                        ''')
                        
                        # code for updating the details (What changes to make)
                        def updateId():  # function to update cake id
                            ans = input("You wanna Change cake Id(Yes/No)?\n")
                            if (ans.lower() == "yes"):
                                ca_id = input("\nEnter new cake-id: ")

                                # checked for id's if already present
                                if (ca_id in allId):
                                    print(f"\nCan't assign id {ca_id}, it already exists")
                                else:
                                    data[0] = ca_id
                            else:
                                if (ans.lower() != "no"):
                                    print("\nInvalid input was given\nAnswer should be (Yes/No)\n")
                                    updateId()
                        updateId()

                        def updateCake_name():  # function to update cake name
                            ans = input("\nYou wanna Change cake name(Yes/No)?\n")
                            if (ans.lower() == "yes"):
                                    ca_na = input("\nEnter cake name: ").capitalize()

                                    # checked for cake names if already present
                                    if (ca_na in allCake):
                                            print(f"\nRecord already present in id {allId[allCake.index(ca_na)]}")
                                    else:
                                        data[1] = ca_na
                            else:
                                if (ans.lower() != "no"):
                                    print("\nInvalid input was given\nAnswer should be (Yes/No)\n")
                                    updateCake_name()

                        updateCake_name()

                        def change_quant():  # function to update cake quantity
                            ans = input("\nYou wanna Change cake quantity(Yes/No)?\n")
                            if (ans.lower() == "yes"):
                                data[2] = input("\nEnter cake quantity: ")
                            else:
                                if (ans.lower() != "no"):
                                    print("\nInvalid input was given\nAnswer should be (Yes/No)\n")
                                    change_quant() 

                        change_quant()   

                        def change_cost():   # function to update cake cost
                            ans = input("\nYou wanna Change cake pricing(Yes/No)?\n")
                            if (ans.lower() == "yes"):
                                data[3] = float(input("\nEnter cost of cake: "))
                                data[3] = str(data[3])+"\n"
                            else:
                                if (ans.lower() != "no"):
                                    print("\nInvalid input was given\nAnswer should be (Yes/No)\n")
                                    change_cost()
                        
                        change_cost()

                        line = ",".join(data)
                    allProd.append(line)
                
                # to save updated data in the file
                if (found):
                    with open("prodData.txt","w") as fp:
                        for cake in allProd:
                            fp.write(cake)
                        print("\nRecords updated successfully")
                        print("\nEnter choice 2 to get cake details")
                else:
                    print(f"\nNo records found for Id {id}")

        except FileNotFoundError:
            print("\nFile not found")
        except:
                print("\nSomething went wrong")
    
    # method to delete the details by id
    def deltData_byId(self,id):
        allProd = []
        found = False
        try:
            with open("prodData.txt","r") as fp:
                if os.path.getsize("prodData.txt") == 0:
                    print("\nNo records found, file was empty")
                else:
                    for line in fp:
                        data = line.split(",")
                        if (data[0] == id):
                            found = True
                        else:
                            allProd.append(line)

                    if (found):
                        with open("prodData.txt","w") as fp:
                            for cake in allProd:
                                fp.write(cake)
                            print("\nCake record removed successfully")
                            print("\nEnter choice 2 to get cake details")
                    else:
                        print("\nCake Record not found")
        except FileNotFoundError:
            print("File not exists")
        except:
                print("\nSomething went wrong")
                
    # method to format the file
    def clearData(self):
        if os.path.getsize("prodData.txt") == 0:
             print("\nNo records found, file was empty")
        else:    
            try:
                fp = open("prodData.txt","w")
                fp.close()
                print("\nFile formatted successfully")
            except:
                print("\nSomething went wrong")