# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 14:39:35 2020

@author: HP
"""


data = {2500: 1.8, 1000: 5, 3000: 1, 2000: 3}

#Inserting key, value as principal, time to data
for principal, time in data.items():
    try:
        principal = float(input("\nInsert principal amount: "))
        time = float(input("\nInsert time: "))
        break
    except Exception:
        print("\nWhoops, the input is incorrect")
        print("Only numbers are accepted")
   

#Function taking array as single arguement
def interestCalculator(principal, time):
    """
    Parameters
    ----------
    principal : TYPE
        DESCRIPTION.
    time : TYPE
        DESCRIPTION.

    Returns
    -------
    interestData : TYPE
        DESCRIPTION.

    """
    #conditions for eveluating the interest rate
    if (principal >= 2500) and (time > 1 and time < 3):
        rate = 3
    elif (principal >= 2500) and (time >= 3):
        rate = 4
    elif (principal < 2500) and (time <= 1):
        rate = 2
    else:
        rate = 1
    interest = (principal * rate * time)/100
    print('\nThe interest rate is: ', interest)
    #showing the raw data for each parameter
    interestData = {'principal': principal, 'time': time, 'rate': rate, 'interest': interest}
    print("\nAn array of intrest data showing principal, rate, time, interest below")
    print(interestData)
    return interestData

def main():
    while True:
        interestCalculator(principal, time)
        restart = input('\nWould you like to calculate more? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


    