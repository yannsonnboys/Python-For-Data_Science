# Rental Time calculator

#total_price = 0

# 1) Hour rental
def hourly_rental(n_time):
    if n_time > 0:
        total_price = n_time * 100
        print("Your total bill for renting this car is: ", total_price)




# 2) Day rental
def daily_rental(n_time):
    if n_time > 0:
        total_price = n_time * 90
        print("Your total bill for renting this car is: ", total_price)




# 3) Week rental
def week_rental(n_time):
    if n_time > 0:
        total_price = n_time * 80
        print("Your total bill for renting this car is: ", total_price)
    