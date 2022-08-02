#cal

money_owed=float(input('How much money do you owe? hint: a decimal number\n'))
apr = int(input('What is the annual percentage rate? hint: annual means yearly and use an integer\n'))
payment=float(input('What will your monthly payment be? hint: in percentage\n'))
months=int(input('How many months would you like to see the results for? hint: enter an integer of months\n'))

#divide by 100 to get the percentage and divide it by 12 to see its monthly rate
monthly_rate= apr/100/12

for i in range(months):
#add the interest
    interest_paid= monthly_rate * money_owed
    money_owed=money_owed+interest_paid

    if(money_owed-payment <= 0):
        print('The last payment is', money_owed)
        print('You paid off the loan in', i+1,'months')
        break

    #update the amount you owe
    money_owed= money_owed+interest_paid

    #I don't understand this I need help but im apparently making the payment now
    money_owed = money_owed-payment 

    print('Paid', payment, 'of which', interest_paid, 'was interest.', end='')
    print('Now I owe', money_owed)