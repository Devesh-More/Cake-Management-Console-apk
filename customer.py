from shopmgmt import ShopMgmt
import random
import getpass

if (__name__ == "__main__"):
    cgmt = ShopMgmt()
    bh = 0 
    print("\nCustomer's login\n")
    us = input("User-Id: ")
    password = getpass.getpass(prompt="Enter password: ")

    if (us == "C77BTES" and password == "password@22"):
        captcha = random.randint(1111,9999)
        print(f"Captcha Generated: {captcha}")
        cap = int(input("\nEnter numeric captcha: "))

        if (cap == captcha):
            print("\n\t\t---- Welcome to Birthday Bites \"Fall in love with every bite\" ----\n")
            print("Enter choice 2 to get cake details")
        else:
            print("Invalid Captcha, Try Again")
            exit()
    else:
        print("Invalid user-id or password, Try Again")
        exit()

    while (bh != "logout"):
        print("\n\t1. Buy cake")
        print("\t2. Display Cake Details")
        print("\t3. Search by Cake-ID")
        print("\t4. Search by Cake-name")
        print("\t5. Service Feedback...\n")

        bh = (input("Enter your choice: "))
    
        if (bh == "1"):
            product = input("Enter cake name to buy: ").capitalize()
            cgmt.buyProduct(product)
        
        elif (bh == "2"):
            cgmt.displayData()

        elif (bh == "3"):
            cid = input("Enter cake-id: ")
            cgmt.cakeID(cid)
        
        elif (bh == "4"):
            product = input("Enter cake name: ").capitalize()
            cgmt.cakeName(product)

        elif (bh == "5"):
            print("\nChoose your feedback option")
            def feed_back():
                print("\n1. Poor     2. Good     3. Very Good     4. Excellent")
                feedback = input("\nSelect your feedback option here: ")
                if(feedback == "1"):
                    print("\nOhh no sorry for the inconvinience 😔... we will try to improve our services")
                elif(feedback == "2"):
                    print("\nThat's what we like to hear")
                elif(feedback == "3"):
                    print("\nThat's great you just made our day!!")
                elif (feedback == "4"):
                    print("\nYou have putted a big smile 🤗 on our face!!!")
                else:
                    print("\n\"Please select options in (1/2/3/4)\"")
                    feed_back()

            feed_back()
            print("Thank You 😊 Visit Again")
        
        elif (bh == "logout"):
            print("You have been logged out successfully")
        
        # elif (bh):
        #     print("Invalid choice was entered")

        # elif (bh == ""):
        #     print("Choice can't be blank")
        
        else:
            print("Invalid choice was entered")
