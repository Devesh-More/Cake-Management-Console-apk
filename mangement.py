from shopmgmt import ShopMgmt
from shoppie import Shop
import random
import os
import getpass

if (__name__ == "__main__"):
    mgmt = ShopMgmt()
    ch = 0 
    print("\nOwner's login\n")
    us = input("User-Id: ")
    password = getpass.getpass(prompt="Enter password: ")

    if (us == "K21WSHR" and password == "password@22"):
        captcha = random.randint(1111,9999)
        print(f"Captcha Generated: {captcha}")
        cap = int(input("\nEnter numeric captcha: "))

        if (cap == captcha):
            print("\n\t\t---- Welcome to Birthday Bites \"Fall in love with every bite\" ----\n")
            print("\n\t\t\t\t   ---- Admin's Portal ----\n")
            print("Enter choice 2 to get cake details")
        else:
            print("Invalid Captcha, Try Again")
            exit()
    else:
        print("Invalid userID or password, Try Again")
        exit()

    while (ch != "8"):
        print("\n\t1. Add new Cake Details")
        print("\t2. Display Cake Details")
        print("\t3. Search by Cake-ID")
        print("\t4. Search by Cake-name")
        print("\t5. Edit by Cake-Id")
        print("\t6. Delete records by Cake-Id") 
        print("\t7. Clear file records")
        print("\t8. Log out....\n")
    
        ch = (input("Enter your choice: "))
        if (ch == "1"):
            try:
                with open("prodData.txt","r") as fp:
                    cid = input("Enter CakeID: ")
                    product = input("Enter product name: ").capitalize()
                    for line in fp:
                        inf = line.split(",")
                        # print(inf)
                        if (inf[0] == cid):
                            print(f"\nID {inf[0]} already exists, Try again")
                            print("\nEnter choice 2 to get cake details")
                            break
                        elif (inf[1] == product):
                            print(f"\nRecord already present in id {inf[0]}")
                            print("\nEnter choice 2 to get cake details")
                            break

                    else:
                        try:
                            prod_quant = input("Enter product quantity: ")
                            prod_price = float(input("Enter product price: "))
                        except Exception as e:
                            print("Error :",e)
                                
                        s1 = Shop(cid,product,prod_quant,prod_price)
                        mgmt.addProduct(s1)
                        print("\nEnter choice 2 to get cake details")

            except FileNotFoundError:
                print("No file found to save data")
        
        elif (ch == "2"):
            mgmt.displayData()
            
        elif (ch == "3"):
            cid = input("Enter cake-id to be searched: ")
            mgmt.cakeID(cid)
        
        elif (ch == "4"):
            product = input("Enter cake name to be searched: ").capitalize()
            mgmt.cakeName(product)
        
        elif (ch == "5"):
            with open("prodData.txt","r") as fp:
                if os.path.getsize("prodData.txt") == 0:
                    print("No records found, file was empty")
                else:
                    cid = input("Enter cake-id to be updated: ")
                    mgmt.editData_byId(cid)

        elif (ch == "6"):
            cid = input("Enter cake-id to be deleted: ")
            mgmt.deltData_byId(cid)

        elif (ch == "7"):
            mgmt.clearData()
        
        elif (ch == "8"):
            print("You have been logged out successfully")

        # elif (ch):
        #     print("Invalid choice was entered")

        # elif (ch == ""):
        #     print("Choice can't be blank")

        else:
            print("Invalid choice was entered")


                




                    
            



