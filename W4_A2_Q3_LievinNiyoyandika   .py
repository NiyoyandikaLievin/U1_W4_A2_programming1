'''Omondi car rental business'''
import sys
class car:

    def __init__(self, list_of_car):        # init function for construct the program
        self.available_cars = list_of_car
        available_cars=["Toyota","Corola","Benze","Helyx","Hama"]   # list of cars


       # all cars detail information
        car_detail = {
            'Toyota': {'model':'Camry', 'releasing': '2015', 'acquired': '2019', 'amount_made': 0, 'car_plate_number': ' RUS5001',
                       'Renting_times': 0},
            'Corola': {'model':'Cavre', 'releasing': '2016', 'acquired': '2018', 'amount_made': 0, 'car_plate_number': ' RUS5002',
                       'Renting_times': 0},
            'Benze': {'model':'Keke','releasing': '2017', 'acquired': '2017', 'amount_made': 0, 'car_plate_number': ' RUS5003',
                      'Renting_times': 0},

            'Helyx': {'model':'Varde', 'releasing': '2018', 'acquired': '2016', 'amount_made': 0, 'car_plate_number': ' RUS5004',
                      'Renting_times': 0},

            'Hama': {'model':'Drago','releasing': '2019', 'acquired': '2015', 'amount_made': 0, 'car_plate_number': ' RUS5005',
                     'Renting_times': 0}}


    def display_available_cars(self):        # to show the available cars
        print("<< the available car are : >>")
        print(35 * "=")
        for car in self.available_cars:
            print(car)

    def lend_car(self, requested_car):
        if requested_car is self.available_cars: # when the car is on the list of available_cars
            self.available_cars.remove(requested_car)  # to remove the car from the list which is rented


    #this is for removing the old cars
    def removeout_car (self,old_car):
        if old_car is self.available_cars:
            self.available_cars.remove(old_car)

            print("hello dear customers! we are happy to let you know that we have removed an old car in company, the old car was: ", old_car)

    def add_car(self):   # this defined for adding new car

       a = input()
       input("name of new added car")
       self.available_cars.append()  # to add the returned and new car on the available list
       print("thanks the available car are now increased. hope that we are providing good services")



print("each car payment will be at least $30 per day, the total payment will be under control of discount according to days number")
days= int(input("how many days do you want to rent car?"))
Name = input("what is your full name?:")             # inputer user name

# for defining cost of renting with its discount according to number of days customer rented the the car
def car_cost(days):
    if days <=7:
        return(days*35)
    elif days <= 15:
        return (days*35)-20

    else:
        return (days*35) - 35

print("total amount you have to pay are: $ ",(car_cost(days)))       # the amount user have to pay in all renting days

# this is for enabling the choice to happen for any one using the program
class users:

    def requist_car(self):
        pass

    def restore_car(self):
        pass

    def old_car(self):
        pass


def main():
    vehicles= car(["Toyota","Corola","Benze","Helyx","Hama"])

    person = users() # imply that tenant class is related to person


    done = False

    while done == False: # to make while loop to continue after any selected choice

           # this is to construct program to allow the user to chose the services they want to look for
        print()
        print( "========Omondi Car Rental service=========")
        print("1. Display all available cars")
        print("2. Rent the car")
        print("3. new added car")
        print("4. Return of car")
        print("5. Remove out old car")
        print("6. Exit")

       # choice one is for dispaying available cars
        choice = int(input(" enter your choice"))
        if choice == 1:
           vehicles.display_available_cars()

           # choice 2 renting the car
        elif choice == 2:
            vehicles.lend_car(person.requist_car())
            choice =input("enter you chosen car")
            print("your car rent is successful made, your rented car is :",choice)
            vehicles.available_cars.remove(choice)

            # all this if statment in choice 2 are for counting rent time and calculating money made form each car
            rent_time = 0
            money_made = car_cost(days)

            if choice == "Toyota":
                rent_time += 1
                money_made = money_made * rent_time
                print("Hama is rented:", rent_time, "times, and money it made are: $ ", money_made)
            elif choice == "Corola":
                rent_time += 1
                money_made = money_made * rent_time
                print("Hama is rented:", rent_time, "times, and money it made are: $ ", money_made)
            elif choice == "Benze":
                rent_time += 1
                money_made = money_made * rent_time
                print("Hama is rented:", rent_time, "times, and money it made are: $ ", money_made)
            elif choice == "Helyx":
                rent_time += 1
                money_made = money_made * rent_time
                print("Hama is rented:", rent_time, "times, and  money it made are: $ ", money_made)
            elif choice == "Hama":
                rent_time += 1
                money_made = money_made * rent_time
                print("Hama is rented:", rent_time,"times, and money it made are: $ ",money_made)

        # choice 3 is for adding new car
        elif choice == 3:
            x = input("enter added car")
            print("new car :", x , "is successful added")
            vehicles.available_cars.append(x)

          # choice 4 is for returning the car
        elif choice == 4:
            x = input("enter the returned car")
            print("the restore is successful made, the restored car is :", x)
            vehicles.available_cars.append(x)

             # choice 5 is for removing the car
        elif choice ==5:
            x =input("enter the old car")
            print("old car", x," is successful removed")
            vehicles.available_cars.remove(x)
         # is for quitting the system
        elif choice ==6:
            sys.exit()

main()    # calling the function


