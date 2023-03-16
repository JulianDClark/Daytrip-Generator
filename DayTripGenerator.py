import random
destinations_list = ['new york', 'california', 'georgia', 'texas']
restaraunt_list = ['burger king', 'arbys','dennys','canes', 'mcdonalds']
transport_list = ['train', 'taxi', 'bus', 'plane', 'ship']
entertainment_list = ['festivals', 'museums', 'fairs', 'movies', 'zoo']



def random_trip_selection(trip_list):
    selected_trip_item = random.choice(trip_list)
    return selected_trip_item

def display_trip(destination,transportation,restaurant,entertainment):
    print(f"Destination: {destination}\nTransportation: {transportation}\nRestaurant: {restaurant}\nEntertainment: {entertainment} ")


def day_trip_generator():
    day_trip_running = True
    while day_trip_running == True:
        destination = random_trip_selection(destinations_list)
        restaurant = random_trip_selection(restaraunt_list)
        transportation = random_trip_selection(transport_list)
        entertainment = random_trip_selection(entertainment_list)
        display_trip(destination,transportation,restaurant,entertainment)
        user_input = input("Do you like this trip y/n? ")
        if user_input == "y":
            print("Awesome! Here is your trip!")
            display_trip(destination,transportation,restaurant,entertainment)
        elif user_input =="n":
            print("Sorry! we will reselect!")



day_trip_generator()
