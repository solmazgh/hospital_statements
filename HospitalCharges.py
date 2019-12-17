'''Project4
Hospital Charges
BY Solmaz Gharagozloo
10/18/2018'''



print("\033[0;34m----------------------Welcome To Encino Hospital Billing Center----------------------\n")
def InPatient(a,b,c,d):
    total=float((a*b)+c+d)
    return total
def OutPatient(c,d):
    total=float(c+d)
    return total
def validateinput(x):  
        if(x<0):
          print("\033[1;31m --your input could not be less than ziro--")
      
          x=float(input("\033[1;30mPlease re-enter your number: "))
          
        return x
          

userinput=int(input("\033[1;30mChoose 1 or 2 from the list below \n1- in-patient\n2- out-patient\n:"))
if(userinput==1):
    days=validateinput(int(input("Please enter he number of days spent in the hospita: ")))
    
    rate=validateinput(float(input("please enter the daily rate: ")))
    
    serviceCharge=validateinput(float(input("please enter Charges for hospital services (lab tests, etc.)e: ")))
    
    medicationCharge=validateinput(float(input("Please enter Hospital medication charges: ")))
    print("\033[0;34m--------------------------------------------------------------------------------------")
    print("\033[1;32mYour balance is:  $",format(InPatient(days,rate,serviceCharge,medicationCharge),'.2f'))
elif(userinput==2):
    serviceCharge=validateinput(float(input("please enter Charges for hospital services (lab tests, etc.)e: ")))
    
    medicationCharge=validateinput(float(input("Please enter Hospital medication charges: ")))
   
    print("\033[0;34m--------------------------------------------------------------------------------------")
    print("\033[1;32mYour balance is:  $", format(OutPatient(serviceCharge,medicationCharge),'.2f'))
    
else:
    print("\033[1;31mWrong Choice, Try late")
    exit(0)
    

    