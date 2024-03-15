# Name: Daniel Chorev  
# unikey: dcho3009 

import sys
import math

room_sizes = [35,136,42]

# Rooms - stored in a list of lists (like a 2d array/table).
# The first index accessing the horizontal row and the second index accessing the vertical column.
# Room 1 (16 * 5)
# room_1 = [''] * 16
# room_1[0] = ['*','*','*','*','*']
# room_1[1] = ['*','C','C','C','*']
# room_1[2] = ['*','C','C','*','*']
# room_1[3] = ['*','C','C','C','*']
# room_1[4] = ['*','*','*','*','*']
# room_1[5] = ['*','A','A','A','*']
# room_1[6] = ['*','A','A','A','*']
# room_1[7] = ['*','A','A','A','*']
# room_1[8] = ['*','A','A','A','*']
# room_1[9] = ['*','*','*','*','*']
# room_1[10] = ['*','B','B','B','*']
# room_1[11] = ['*','B','B','B','*']
# room_1[12] = ['*','B','B','B','*']
# room_1[13] = ['*','*','*','*','*']
# room_1[14] = ['*','D','D','D','*']
# room_1[15] = ['*','D','D','D','*']

# Room 2 (23*11 (19 on short end))

#room_2 = ['']* 23

# room_2[0] = ['*','A','A','-','-','-','-','-','-','-','-']
# room_2[1] = ['*','A','A','A','A','A','-','-','-','-','-']
# room_2[2] = ['*','A','A','A','A','A','A','A','A','A','*']
# room_2[3] = ['*','*','*','A','A','A','A','A','A','A','*']
# room_2[4] = ['*','*','*','*','*','*','A','A','A','A','*']
# room_2[5] = ['*','B','B','*','*','*','*','A','A','A','*']
# room_2[6] = ['*','B','B','B','B','B','*','*','*','*','*']
# room_2[7] = ['*','B','B','B','B','B','*','D','D','D','*']
# room_2[8] = ['*','B','B','B','B','B','*','D','D','D','*']
# room_2[9] = ['*','B','B','B','B','B','*','D','D','D','*']
# room_2[10] = ['*','*','*','*','*','*','*','D','D','D','*']
# room_2[11] = ['*','*','*','*','*','*','*','D','D','D','*']
# room_2[12] = ['*','C','C','C','C','C','*','D','D','D','*']
# room_2[13] = ['*','C','C','C','C','C','*','D','D','D','*']
# room_2[14] = ['*','C','C','C','C','C','*','D','D','D','*']
# room_2[15] = ['*','C','C','C','C','C','*','D','D','D','*']
# room_2[16] = ['*','C','C','C','C','C','*','*','*','*','*']
# room_2[17] = ['*','C','C','*','*','*','*','E','E','E','*']
# room_2[18] = ['*','*','*','*','*','*','E','E','E','E','*']
# room_2[19] = ['*','*','*','E','E','E','E','E','E','E','*']
# room_2[20] = ['*','E','E','E','E','E','E','E','E','E','*']
# room_2[21] = ['*','E','E','E','E','E','-','-','-','-','-']
# room_2[22] = ['*','E','E','-','-','-','-','-','-','-','-']

# Room 3 (8*6)
#room_3 = ['']*8

# room_3[0] = ['A','A','A','A','A','A']
# room_3[1] = ['A','A','A','A','A','A']
# room_3[2] = ['A','A','A','A','A','A']
# room_3[3] = ['*','*','*','*','*','*']
# room_3[4] = ['B','B','B','B','B','B']
# room_3[5] = ['B','B','B','B','B','B']
# room_3[6] = ['B','B','B','B','B','B']
# room_3[7] = ['B','B','B','B','B','B']

# Movie data
# Class for session:
class session_class:
    def __init__(self, name, year, length, start_time_hours, start_time_mins, room):
        self.name = name
        self.year = year
        self.length = length
        self.start_time_hours = start_time_hours
        self.start_time_mins = start_time_mins
        self.room = room

# Populating movie list with each element being a session class containing session data
movie_list = [''] * 19
movie_list[0] = session_class("The Shining","1980","2h 26m",10,0,"Room 1")
movie_list[1] = session_class("Your Name","2016","1h 52m",13,0,"Room 1")
movie_list[2] = session_class("Fate/Stay Night: Heaven's Feel - III. Spring Song","2020","2h 0m",15,0,"Room 1")
movie_list[3] = session_class("The Night Is Short, Walk on Girl","2017","1h 32m",17,30,"Room 1")
movie_list[4] = session_class("The Truman Show","1998","1h 47m",19,30,"Room 1")
movie_list[5] = session_class("Genocidal Organ","2017","1hr 55m",21,45,"Room 1")
movie_list[6] = session_class("Jacob's Ladder","1990","1h 56m",10,0,"Room 2")
movie_list[7] = session_class("Parasite","2019","2h 12m",12,15,"Room 2")
movie_list[8] = session_class("The Dark Knight","2008","2h 32min",14,45,"Room 2")
movie_list[9] = session_class("Blade Runner 2049","2017","2h 44m",17,45,"Room 2")
movie_list[10] = session_class("The Mist","2007","2h 6m",21,0,"Room 2")
movie_list[11] = session_class("Demon Slayer: Mugen Train","2020","1h59min",23,20,"Room 2")
movie_list[12] = session_class("The Matrix","1999","2h 16m",10,0,"Room 3")
movie_list[13] = session_class("Inception","2010","2h 42m",11,30,"Room 3")
movie_list[14] = session_class("Shutter Island","2010","2h 19m",14,30,"Room 3")
movie_list[15] = session_class("Soul","2020","1hr 40m",17,0,"Room 3")
movie_list[16] = session_class("Mrs. Brown","1997","1h 41min",19,0,"Room 3")
movie_list[17] = session_class("Peppa Pig: Festival of Fun","2019","1h 8min",21,0,"Room 3")
movie_list[18] = session_class("Titanic","1997","3h 30min",22,15,"Room 3")

#prices
ticket_before_4pm = 13.0
ticket_after_4pm = 15.0
popcorn_prices = [['',0],['Small',3.5],['Medium',5.0],['Large',7.0]]
discount = 0
change_sizes = [100,50,20,10,5,2,1,0.5,0.2,0.1,0.05]

#____________________________________________________________________________________
def switch_error(error_type):
    # Function to print errors and exit
    # s is for switch options
    # t is for time format
    # a is for arguments missing

    if error_type == "s":
        print()
        print("Sorry. This program does not recognise the switch options. ")
        print()
        print("Bye.")
    elif error_type == "t":
        print()
        print("Sorry. This program does not recognise the time format entered. ")
        print()
        print("Bye.")
    elif error_type == "a":
        print("Usage: python3 pizzaz.py [--show <timenow> | --book | --group]")
    exit()
# ______________________________________________________________________________________

def validate_time(input_time):
    # Validate inputted time from command line arguments
    valid_time = True

    # Check length of time is correct format
    if len(input_time) != 5:
        valid_time = False 

    # Validate if characters are digits (able to be converted to integars)
    elif input_time[0].isdigit() == False or input_time[1].isdigit() == False or input_time[3].isdigit() == False or input_time[4].isdigit() == False:
        valid_time = False

    # Validate time format (##:##) where the numbers must be a possible time (00::00 - 23:59)
    elif input_time[0] != "0" and input_time[0] != "1" and input_time[0] != "2": # Check first character is valid time
        valid_time = False
        
    # Validate if the hours is less than 23 and the minutes is less than 59
    elif int(input_time[0]+input_time[1]) > 23 or int(input_time[3]+input_time[4]) > 59:
        valid_time = False

    # Validate colon format
    elif input_time[2] != ":":
        valid_time = False
    
    return(valid_time)

# ____________________________________________________________________________________

def validate_movie(input_movie_name):
    found_movie_index = -1
    for x in movie_list:
        # Check names are the same (case insensitive)
        if input_movie_name.lower() == x.name.lower():
            
            # Save index of movie for booking
            found_movie_index = movie_list.index(x)
            break
    return(found_movie_index)

# ____________________________________________________________________________________
# Function to calculate and print change required.
# Takes total_price as a parameter and asks for amount paid as input
# Calculates required change and which notes and coins.
def calculate_change(final_price):
    change = -1
    amount_paid_valid = False
    while change < 0 or amount_paid_valid == False :
        amount_paid = float(input("Enter the amount paid: $"))
        # Checking that amount paid is a valid money value. (multiple of 5 cents)        
        if (amount_paid*100)% 5 == 0:
            amount_paid_valid = True
        else:
            print("The input given is not divisible by 5c. Enter a valid payment.")
            continue
        change = amount_paid - final_price
        # Not enough money paid.
        if change < 0:
            print("The user is ${:.2f} short. Ask the user to pay the correct amount.".format(change*-1))
    
    # Print change, notes and coins.
    # Adjusts the printing so that the formating is correct and in line.
    print("Change: ${:.2f}".format(change))
    for x in change_sizes:
        if change / x >= 1:
            if x >= 1:
                print(" $" + "{}:".format(x).rjust(3) + " {}".format(math.floor(change/x)))
            elif x == 0.5:
                print(" 50c:" + " {}".format(math.floor(change/x)))
            elif x == 0.2:
                print(" 20c:" + " {}".format(math.floor(change/x)))
            elif x == 0.1:
                print(" 10c:" + " {}".format(math.floor(change/x)))
            elif x == 0.05:
                print(" 5c:" + " {}".format(math.floor(change/x)))
            change = change % x

# ____________________________________________________________________________________


# Print greeting:
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~ Welcome to Pizzaz cinema ~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

# Validate command line input
if len(sys.argv) > 1:
    switch = sys.argv[1]

# Validate correct number of command line arguments
if len(sys.argv) < 2:
    switch_error("a")

# Validate correct switches in command line arguments.
elif switch != "--show" and switch != "--book" and switch != "--group":
    switch_error("s")

# Validate correct number of arguments for show switch
elif switch == "--show" and len(sys.argv) != 3:
    switch_error("s")

# Show switch
elif switch == "--show":

    # Validate inputted time from command line arguments
    input_time = sys.argv[2]

    # Call time validation function and return the validation state (True or false)
    valid_time = validate_time(input_time)
 
    if valid_time == False:
        switch_error("t")
    else:
        # Valid time established - switch option: --show

        input_hours = int(input_time[0]+ input_time[1])
        input_mins = int(input_time[3] + input_time[4])

        print()
        # Print valid movies from list
        for x in movie_list:
            if x.start_time_hours >= input_hours and x.start_time_mins >= input_mins:
                print("{}. {}. {}. {}:{:02d}. {}".format(x.name,x.year,x.length,x.start_time_hours,x.start_time_mins,x.room))
                    
        print()   
        print("Bye.")
        exit()

# Validate correct command line args when book switch is entered.
elif switch == "--book" and len(sys.argv) != 2:
    switch_error("s")

# Book switch:
elif switch == "--book":
    # Get movie input and validate by searching through movies list.
    found_movie_index = -1
    print()
    while found_movie_index == -1:
        
        input_movie_name = input("What is the name of the movie you want to watch? ")
        
        # call validate_movie function to check movie entered is in the list
        found_movie_index = validate_movie(input_movie_name)

        # If movie isn't found ask to retry and validate answer is 'y' or 'n' or 'Y' or 'N'        
        if found_movie_index == -1:
            retry = 'a'
            while retry.lower() != 'y' and retry.lower() != 'n':
                retry = input("Sorry, we could not find that movie. Enter Y to try again or N to quit. ")
                if retry.lower() == 'n':
                    print()
                    print("Bye.")
                    exit()

    # Ask if user wants popcorn and validate input. Retry until valid input.
    popcorn_yn = " "
    print()
    while popcorn_yn.lower() != 'y' and popcorn_yn.lower() != 'n' :
        popcorn_yn = input("Would you like to order popcorn? Y/N ")
    popcorn_size = ''
    # If the user wants popcorn, ask for size. Retry until there is valid input
    if popcorn_yn.lower() == 'y':
        popcorn_size = " "
        while popcorn_size.lower() != 's' and popcorn_size.lower() != 'm' and popcorn_size.lower() != 'l':
            popcorn_size = input("You want popcorn. What size Small, Medium or Large? (S/M/L) ")
    

    # Find index for popcorn prices list based on size choice to find price
    if popcorn_size.lower() == "s":
        popcorn_size_price = 1
    elif popcorn_size.lower() == "m":
        popcorn_size_price = 2
    elif popcorn_size.lower() == "l":
        popcorn_size_price = 3
    else:
        popcorn_size_price = 0

    print()
    print("The seat number for person 1 is #17")
    print()

    # Decide ticket price based on time of the movie.
    if movie_list[found_movie_index].start_time_hours >= 16:

        # Movie after 4pm.
        # Total cost is ticket price plus popcorn price from list using calculated index.
        total_cost = ticket_after_4pm + popcorn_prices[popcorn_size_price][1]

        print("For 1 person, the initial cost is ${:.2f}".format(total_cost))

        # Print out cost information using ljust and rjust to align prices in a column.
        print(" Person 1: Ticket from 16:00".ljust(34) + "$" + "{:.2f}".format(ticket_after_4pm).rjust(5))
        
        # Only print popcorn price if there was popcorn requested.
        if popcorn_size_price > 0:
            print(" Person 1: {} popcorn".format(popcorn_prices[popcorn_size_price][0]).ljust(34) + "$" + "{:.2f}".format(popcorn_prices[popcorn_size_price][1]).rjust(5))
            print()
        print(" No discounts applied".ljust(34) + "$" + "{:.2f}".format(discount).rjust(5))
        print()
        print("The final price is".ljust(34) + "$" + "{:.2f}".format(total_cost-discount).rjust(5))

    else:
        # Movie before 4pm.
        total_cost = ticket_before_4pm + popcorn_prices[popcorn_size_price][1]
        print("For 1 person, the initial cost is ${:.2f}".format(total_cost))
        print(" Person 1: Ticket before 16:00".ljust(34) + "$" + "{:.2f}".format(ticket_before_4pm).rjust(5))
        if popcorn_size_price > 0:
            print(" Person 1: {} popcorn".format(popcorn_prices[popcorn_size_price][0]).ljust(34) + "$" + "{:.2f}".format(popcorn_prices[popcorn_size_price][1]).rjust(5))
            print()
            print(" No discounts applied".ljust(34) + "$" + "{:.2f}".format(discount).rjust(5))
            print()
            print("The final price is".ljust(34) + "$" + "{:.2f}".format(total_cost-discount).rjust(5))

    final_price = total_cost - discount
    
    print()
    calculate_change(final_price)
    
    print()
    print("Bye.")


# Validate correct command line args when group switch is entered.
elif switch == "--group" and len(sys.argv) != 2:
    switch_error("s")
# Group switch:
elif switch == "--group":
    group_fits_room = False
    while group_fits_room == False:
        # Get movie input and validate by searching through movies list.
        found_movie = False
        found_movie_index = -1
        print()
        while found_movie_index == -1:
            input_movie_name = input("What is the name of the movie you want to watch? ")

            # Check movie entered is in list
            found_movie_index = validate_movie(input_movie_name)
                  
            # If movie isn't found ask to retry and validate answer is 'y' or 'n' or 'Y' or 'N'        
            if found_movie_index == -1:
                retry = 'a'
                while retry.lower() != 'y' and retry.lower() != 'n':
                    retry = input("Sorry, we could not find that movie. Enter Y to try again or N to quit. ")
                    if retry.lower() == 'n':
                        print()
                        print("Bye.")
                        exit()
        print()
        # Ask for how many people and retry (or quit) until a valid result.
        num_persons = 0
        while num_persons <= 1:
            num_persons = int(input("How many persons will you like to book for? "))
            if num_persons <= 1:
                retry = 'a'
                while retry.lower() != 'y' and retry.lower() != 'n':
                    retry = input("Sorry, you must have at least two customers for a group booking. Enter Y to try again or N to quit. ")
                    if retry.lower() == 'n':
                        print()
                        print("Bye.")
                        exit()      


        if int(movie_list[found_movie_index].room[-1]) % 2 == 0:
            room_capacity = int(room_sizes[int(movie_list[found_movie_index].room[-1])-1]/2)
        else:
            room_capacity = int(room_sizes[int(movie_list[found_movie_index].room[-1])-1]/2 + 1)

        if num_persons > room_capacity:
                retry = 'a'
                while retry.lower() != 'y' and retry.lower() != 'n':
                    retry = input("Sorry, we do not have enough space to hold {} people in the theater room of {} seats. Enter Y to try a different movie name or N to quit.".format(num_persons,room_capacity))
                    if retry.lower() == 'n':
                        print()
                        print("Bye.")
                        exit() 

        else:
            group_fits_room = True
    seat_num = 1
    print()
    persons_with_popcorn = [0]
    for x in range(1,num_persons+1):
        # Ask if user wants popcorn and validate input. Retry until valid input.
        popcorn_yn = " "
        
        while popcorn_yn.lower() != 'y' and popcorn_yn.lower() != 'n' :
            popcorn_yn = input("For person {}, would you like to order popcorn? Y/N ".format(x))
        
        popcorn_size = ''

        # If the user wants popcorn, ask for size. Retry until there is valid input
        if popcorn_yn.lower() == 'y':
            popcorn_size = " "
            while popcorn_size.lower() != 's' and popcorn_size.lower() != 'm' and popcorn_size.lower() != 'l':
                popcorn_size = input("Person {} wants popcorn. What size Small, Medium or Large? (S/M/L) ".format(x))

        # Find index for popcorn prices list based on size choice to find price and add the size to the list of people ordering popcorn.
        if popcorn_size.lower() == "s":
            persons_with_popcorn.insert(x,1)
        elif popcorn_size.lower() == "m":
            persons_with_popcorn.insert(x,2)
        elif popcorn_size.lower() == "l":
            persons_with_popcorn.insert(x,3)
        else:
            persons_with_popcorn.insert(x,0)

    print()
    # Print seat numbers, skipping a seat between people.
    for x in range(1,num_persons+1):
        print("The seat number for person {} is #{}".format(x,(2*x)-1))
        

    # Calculate popcorn costs
    total_popcorn_cost = 0
    for x in persons_with_popcorn:
            total_popcorn_cost += popcorn_prices[x][1]
    ticket_price = 0

    # Decide ticket price based on time of the movie.
    if movie_list[found_movie_index].start_time_hours >= 16:
        ticket_price = ticket_after_4pm
        ticket_time_print = "from 16:00"
    else:
        ticket_price = ticket_before_4pm
        ticket_time_print = "before 16:00"

    print()
    
    # Total cost is ticket price plus total popcorn cost calculated
    total_cost = ticket_price*num_persons + total_popcorn_cost

    print("For {} persons, the initial cost is ${:.2f}".format(num_persons,total_cost))
    
    num_popcorns = 0
    # Print out cost information using ljust and rjust to align prices in a column.
    for x in range(1,num_persons+1):
        print(" Person {}: Ticket {}".format(x,ticket_time_print).ljust(34) + "$" + "{:.2f}".format(ticket_price).rjust(5))
        
        # Only print popcorn price if there was popcorn requested.
        if persons_with_popcorn[x] != 0:
            print(" Person {}: {} popcorn".format(x, popcorn_prices[persons_with_popcorn[x]][0]).ljust(34) + "$" + "{:.2f}".format(popcorn_prices[persons_with_popcorn[x]][1]).rjust(5))
            num_popcorns += 1

    # Decide if discount should be applied
    if total_cost > 100:
        # Calculate discount
        ticket_discount = 0.1*ticket_price*num_persons
        popcorn_discount = 0.2*total_popcorn_cost
        
        # Round discounts for printing
        ticket_discount_print = round(ticket_discount,2)
        popcorn_discount_print = round(popcorn_discount,2)
        print()
        print(" Discount applied tickets x{}".format(num_persons).ljust(33) + "-$" + "{:.2f}".format(ticket_discount_print).rjust(5))
        print(" Discount applied popcorn x{}".format(num_popcorns).ljust(33) + "-$" + "{:.2f}".format(popcorn_discount_print).rjust(5))

        # Total discount calculated
        discount = ticket_discount+popcorn_discount

        # Correct rounding for discount price based on cents.
        if (discount*100) % 5 != 0:
            if str(discount*100)[-1] == "1" or str(discount*100)[-1] == "6":
                discount -= 0.01
            elif str(discount*100)[-1] == "2" or str(discount*100)[-1] == "7":
                discount -= 0.02
            elif str(discount*100)[-1] == "3" or str(discount*100)[-1] == "8":
                discount += 0.02
            elif str(discount*100)[-1] == "4" or str(discount*100)[-1] == "9":
                discount += 0.01

    # Print no discount line
    if discount == 0:
        print()
        print(" No discounts applied".ljust(34) + "$" + "{:.2f}".format(discount).rjust(5))
    
    #Calculate and print final price
    final_price = total_cost - discount
    print()
    print("The final price is".ljust(34) + "$" + "{:.2f}".format(final_price).rjust(5))
    
    print()
    calculate_change(final_price)
    
    print()
    print("Bye.")



