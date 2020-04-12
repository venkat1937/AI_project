print("================================================================================================================================================================")
print()
print("                                                  |***** PROFESSIONAL BANK BANKING BOT SYSTEM *****|                                                            ")
print()
print("================================================================================================================================================================")
print("Welcome to Professional Bank please say hello or hi or start ! to Start your banking")
val = input()
val2 = "hi"
val3 = "hello"
val4="start"
if(val == val2 or val == val3 or val==val4):
    print("Hello,Professional bank is at your service :)")
    print()
    print("How can we help you?")
    print()
    print("Types of services for you :- ")
    print()
    print("1. To Add beneficiary Account")
    print("2. To Transfer Funds")
    print("3. to check balance")
    print("4. To get Mini Statement of your Account")
    print()
    print(" press 1 to  start to add beneficiary")
    print("press 2 if you  want to trasfer money")
    print("press 3 if you to check my account balance")
    print("press 4 if want to get mini-statement")
    print("Please input a task :- ")
    input1 = input()

    input2 = "1"
    input3 = "1"
    
    input4 = "2"
    input5 = "2"

    input6 = "3"
    input7 = "3"

    input8 = "4"
    input9 = "4"
    
    mobile1 ="9133921832"
    mobile2="9133726715"
    mobile3="9682694414"
    mobile4="8885395071"

    otp1="2244"
    otp2="1937"
    otp3="1180"
    otp3="1940"
    name1="nandi sivasai"
    name2="venkatappareddy"
    name3="parmesh"
    name4="surya"
    accnum1="PBN00005626262689"
    accnum2="PBN00005626261180"
    accnum3="PBN00005626251946"

    if(input1 == input2 or input1 == input3):
        print("Enter your beneficiary name:-  ")
        Name = input()
        print("Enter beneficiary account number:- ")
        Account_number = input()
        print ("")
        print("enter the phone number ")
        phone_number= int(input())
        print("Benificiary Successfuly Added.")
        print("")
        print("")
        print("please check the benificiary account detatils that u have added")
        print("name of beneficiary is ",Name)
        print("your beneficiary account number",Account_number)
        print("phone number linked to your account is ",phone_number)
        
        print("Press 1 to quit:- ")
        choice = int(input())
        if(choice == 1):
            print("Thanks For Using Our Boting Service!!")
            print("Hope You Liked Our Services.")

    if(input1 == input4 or input1 == input5):
        print("Quick Pay")
        print("Please enter the amount:- ")
        amount = int(input())
        print("")
        print("please select  below account holders name from here as reference")
        print("")
        print("nandi sivasai,venkatappareddy,surya,parmesh")
        print("")
        print("Please enter the beneficiary account holder name:- ")
        name = input()
        if(name==name1 or name ==name2 or name ==name3 or name==name4):
            print("mam you can use these account number for reference PBN00005626262689,PBN00005626261180,PBN00005626251946 ")
            print("")
            print("Please enter the beneficiary account number:- ")
            accnum1="PBN00005626262689"
            accnum2="PBN00005626261180"
            accnum3="PBN00005626251946"
            accnum =input()
            if(accnum==accnum1 or accnum==accnum2 or accnum==accnum3):
                print("")
                print("Please enter the beneficiary IFSC code:- ")
                IFSC_code = input()
                print("")
                print("mam you can use these numbers for the reference ")
                print("")
                print("9133921832,9133726715,8885395071,9682694414")
                print("")
                print("Enter linked account registered mobile number? ")
                mobile_number = input()
                
                if(mobile_number == mobile1 or mobile_number == mobile2 or mobile_number==mobile3 or mobile_number==mobile4 ):
                    print("")
                    print("mam these are the otps that the numbers will get or the examples of otp ")
                    print("")
                    print("uses these otps for reference 2244 ,1180,1940,1937")
                    print("")
                    print("enter the otp that is sent to your linked mobile ")
                    otp = input()
                    if (otp ==otp1 or otp==otp2 or otp ==otp3 or opt == otp4):
                         print("Savings No ",accnum," Debited with INR ", amount , " towards NEFT Transfer to NEFT/", name)
                         print("Press 1 to quit:- ")
                         choice = int(input())
                         if(choice == 1):
                             print("Thanks For Using Our Boting Service!!")
                             print("Hope You Liked Our Services.")
                    else:
                        print("enter correct otp")
                else:
                    print("enter correct mobile number")

    if(input1 == input6 or input1 == input7):
        
        print("mam you can use these numbers for the reference ")
        print("")
        print("9133921832,9133726715,8885395071,9682694414")
        print("")
        print("Enter your linked account mobile number:- ")
        mobile_number = input()
        if(mobile_number == mobile1 or mobile_number == mobile2 or mobile_number==mobile3 or mobile_number==mobile4 ):
            print("Please type the OTP in correct Format:- ")
            print("")
            print("mam these are the otps that the numbers will get or the examples of otp ")
            print("")
            print("uses these otps for reference 2244 ,1180,1940,1937")
            print("")
            print("enter the otp that is sent to your linked mobile ")
            otp = input()
            if (otp ==otp1 or otp==otp2 or otp ==otp3 or opt == otp4):
                 print("mam you can use these account number for reference PBN00005626262689,PBN00005626261180,PBN00005626251946 ")
            print("")
            print("Please enter the beneficiary account number:- ")
            accnum1="PBN00005626262689"
            accnum2="PBN00005626261180"
            accnum3="PBN00005626251946"
            accnum =input()
            if(accnum==accnum1):
                print("Welcome Mr.Venkatappareddy")
                print("Greeting from Professional Bank!!")
                print("Account No. PBN00005626262689")
                print("Current Balance = INR 2,78,258")
                print("Press 1 to quit:- ")
                choice = int(input())
                if(choice == 1):
                    print("Thanks For Using Our Boting Service!!")
                    print("Hope You Liked Our Services.")
            elif(accnum==accnum2):
                    print("Welcome Mr.sivasai nandi")
                    print("Greeting from Professional Bank!!")
                    print("Account No.PBN00005626261180 ")
                    print("Current Balance = INR 2,00,258")
            elif(accnum==accnum3):
                    print("Welcome Mr.sivasai nandi")
                    print("Greeting from Professional Bank!!")
                    print("Account No.  PBN00005626251946")
                    print("Current Balance = INR 12,134,535,468")
        
    else:
        print("please check the input given")

    if(input1 == input8 or input1 == input9):
        print("mam you can use these account number for reference PBN00005626262689,PBN00005626261180,PBN00005626251946 ")
        print("")
        print("enter the account number:")
        accnum =input()
        accnum1="PBN00005626262689"
        accnum2="PBN00005626261180"
        accnum3="PBN00005626251946"
       
        
        if(accnum==accnum1 or accnum==accnum2 or accnum==accnum3):
            print("mam you can use these numbers for the reference ")
            print("")
            print("9133921832,9133726715,8885395071,9682694414")
            print("")
            print("Enter your linked account mobile number:- ")
            mobile_number = input()
            if(mobile_number == mobile1 or mobile_number == mobile2 or mobile_number==mobile3 or mobile_number==mobile4 ):
                print("Please type the OTP in correct Format:- ")
                print("")
                print("mam these are the otps that the numbers will get or the examples of otp ")
                print("")
                print("uses these otps for reference 2244 ,1180,1940,1937")
                print("")
                print("enter the otp that is sent to your linked mobile ")
                otp = input()
                if (otp ==otp1 or otp==otp2 or otp ==otp3 or opt == otp4):
                    if(accnum==accnum1):
                        print("Welcome Mr.Venkat sai surya prasad")
                        print("Greeting from Professional Bank!!")
                        print("Account No. PBN00005626262689")
                        print("TRANXCUB00000000001 | CREDIT | 75000  | 2019 - 25 - 12   04 : 34 : 16")
                        print("TRANXCUB00000000002 | CREDIT | 75000  | 2020 - 25 - 01   05 : 30 : 10")
                        print("TRANXCUB00000000003 | DEBIT  | 100000 | 2020 - 28 - 01   12 : 55 : 17")
                        print("TRANXCUB00000000004 | DEBIT  | 5000   | 2020 - 25 - 02   21 : 41 : 10")
                        print("TRANXCUB00000000005 | CREDIT | 75000  | 2020 - 25 - 02   20 : 28 : 05")
                        print("TRANXCUB00000000006 | DEBIT  | 15000  | 2020 - 20 - 03   14 : 36 : 01")
                        print("TRANXCUB00000000007 | DEBIT  | 4500   | 2020 - 21 - 03   16 : 45 : 30")
                        print("TRANXCUB00000000008 | CREDIT | 4000   | 2020 - 22 - 03   18 : 39 : 59")
                        print("TRANXCUB00000000009 | CREDIT | 55000  | 2020 - 23 - 03   06 : 12 : 55")
                        print("TRANXCUB000000000010 | DEBIT | 45000  | 2020 - 24 - 03   08 : 46 : 40")
                    elif(accaccnum==accnum2):
                        print("Welcome Mr.Venkatatappareddy ")
                        print("Greeting from Professional Bank!!")
                        print("Account No. PBN00005626261180")
                        print("TRANXCUB00000000001 | CREDIT | 20000  | 2019 - 25 - 12   04 : 34 : 16")
                        print("TRANXCUB00000000002 | CREDIT | 7500   | 2020 - 25 - 01   05 : 30 : 10")
                        print("TRANXCUB00000000003 | DEBIT  | 1500   | 2020 - 28 - 01   12 : 55 : 17")
                        print("TRANXCUB00000000004 | DEBIT  | 5000   | 2020 - 25 - 02   21 : 41 : 10")
                        print("TRANXCUB00000000005 | CREDIT | 900    | 2020 - 25 - 02   20 : 28 : 05")
                        print("TRANXCUB00000000006 | DEBIT  | 15000  | 2020 - 20 - 03   14 : 36 : 01")
                        print("TRANXCUB00000000007 | DEBIT  | 4500   | 2020 - 21 - 03   16 : 45 : 30")
                        print("TRANXCUB00000000008 | CREDIT | 4000   | 2020 - 22 - 03   18 : 39 : 59")
                        print("TRANXCUB00000000009 | CREDIT | 55000  | 2020 - 23 - 03   06 : 12 : 55")
                        print("TRANXCUB000000000010 | DEBIT | 45000  | 2020 - 24 - 03   08 : 46 : 40")
                    elif(accaccnum==accnum3):
                        print("Welcome Mr.Venkatatappareddy ")
                        print("Greeting from Professional Bank!!")
                        print("Account No. PBN00005626261180")
                        print("TRANXCUB00000000001 | CREDIT | 20000  | 2019 - 25 - 12   04 : 34 : 16")
                        print("TRANXCUB00000000002 | CREDIT | 7500   | 2020 - 25 - 01   05 : 30 : 10")
                        print("TRANXCUB00000000003 | DEBIT  | 1500   | 2020 - 28 - 01   12 : 55 : 17")
                        print("TRANXCUB00000000004 | DEBIT  | 5000   | 2020 - 25 - 02   21 : 41 : 10")
                        print("TRANXCUB00000000005 | CREDIT | 900    | 2020 - 25 - 02   20 : 28 : 05")
                        print("TRANXCUB00000000006 | DEBIT  | 15000  | 2020 - 20 - 03   14 : 36 : 01")
                        print("TRANXCUB00000000007 | DEBIT  | 4500   | 2020 - 21 - 03   16 : 45 : 30")
                        print("TRANXCUB00000000008 | CREDIT | 4000   | 2020 - 22 - 03   18 : 39 : 59")
                        print("TRANXCUB00000000009 | CREDIT | 55000  | 2020 - 23 - 03   06 : 12 : 55")
                        print("TRANXCUB000000000010 | DEBIT | 45000  | 2020 - 24 - 03   08 : 46 : 40")
                    else:
                        print("sorry sir you may have entered wrong details or you may not have account in our bank")
                    print("Press 1 to quit:- ")
                    choice = int(input())
                    if(choice == 1):
                        print("Thanks For Using Our Boting Service!!")
                        print("Hope You Liked Our Services.")
                else :
                    print("please check the otp that you have entered ")
            else:
                print("please enter the correct mobile number")
        else:
            print("please enter the correct account number ")
    else:
        print("please Enter valid input")

