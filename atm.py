import time

print("please insert your card ")

time.sleep(5)

password=1234

pin=int(input("Enter your atm pin:"))

balance = 5000

if pin==password:
    print("""
        1 == balance 
        2 == withdrwa balance
        3 == deposit balance 
        4 == exit """
          )
    
    try:
        option = int(input("please enter your choice :"))
    except:
        print("please enetr valid option :")

    if option ==1:
        print(f" your current balance is {balance}")     

        print("==========================================================================")
           
        print("==========================================================================")  
        print("==========================================================================")  

    if option ==2:
        withdraw_amount=int(input("please enetr withdrwal amount"))

        print("==========================================================================")  
        print("==========================================================================")  
        print("==========================================================================")  


        balance =balance-withdraw_amount

        print(f"{withdraw_amount} is debited from your account")

        print("==========================================================================")  
        print("==========================================================================")  
        

        print(f"your updated balance is {balance}")

        print("==========================================================================")  
        print("==========================================================================")  


    if option==3:
        deposit_amount = int(input("please eneter the deposit_amount : "))

        balance=balance+deposit_amount

        print("==========================================================================")  
        print("==========================================================================")  


        print(f"{deposit_amount} is craedited to your account")

        print("==========================================================================")  
        print("==========================================================================")  


        print(f"your updated balance is {balance}")

        print("==========================================================================")  
        print("==========================================================================")  
    if option == 4:
        breakpoint

else:
    print("wrong pin please try again")