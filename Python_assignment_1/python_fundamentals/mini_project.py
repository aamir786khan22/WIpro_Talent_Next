'''
MINI PROJECT
1.create a python program that asks the user how far they want to travel. if they want to travel less than three miles tell them to ride Bicycle. if they want to travel more than three miles, but less than three hundred miles, tell them to ride Motor-cycle. if they want to travel three hundred miles or more tell them to driver Super-Car.
Sample Output:
How far would you like to travel in miles? 2500
I suggest Super-Car to your destination
'''

def travel_mode_suggestion():
    miles = int(input("How far would you like to travel in miles? "))

    if miles < 3:
        print("I suggest riding a Bicycle to your destination.")
    elif miles >= 3 and miles < 300:
        print("I suggest riding a Motor-cycle to your destination.")
    else:
        print("I suggest using a Super-Car to reach your destination.")

'''
MINI PROJECT
2.Let's assume you are planning to use your python skills to build an App for Mobile.
You decide to host your application on servers running in the cloud. you pick a hosting provider that charges $0.51 per hour. you will launch your services using one server and want to know how much it will cost to operate per day, per week, per month.
Write a python program that displays the answers to the following questions:
How much does it cost to operate one server per day?
How much does it cost to operate one server per week?
How much does it cost to operate one server per month?
How much days can I operate one server with $918?
'''    

def server_cost_calculator():
    hourly_rate = 0.51
    daily_cost = hourly_rate * 24
    weekly_cost = daily_cost * 7
    monthly_cost = daily_cost * 30  # assuming 30 days in a month
    budget = 918
    affordable_days = budget / daily_cost

    print(f"Cost to run one server per day: ${daily_cost:.2f}")
    print(f"Cost to run one server per week: ${weekly_cost:.2f}")
    print(f"Cost to run one server per month: ${monthly_cost:.2f}")
    print(f"With $918, you can run one server for approximately {affordable_days:.2f} days.")
