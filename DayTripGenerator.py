# (5 points):  As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainment in their own separate Lists. 
list = ['new york', 'california', 'georgia', 'texas']
print(list)
list = ['burger king', 'arbys','dennys','canes', 'mcdonalds']
print(list)
list = ['train', 'taxi', 'bus', 'plane', 'ship']
print(list)
list = ['festivals', 'museums', 'fairs', 'movies', 'zoo']
print(list)
#(5 points): As a user, I want a destination to be randomly selected for my day trip. 
# creating a list for random days
import random
day = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
print('orginal list is :' + str (day)) 
random_day = random.choice(day)
# printing random day of the week
print("Random selected day is : " + str(day))
# didnt give me a random day based on list making change in code 
import random
# initializing list
test_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
# printing original list
print("Original list is : " + str(test_list))
# using random.choice() to
# get a random day
random_day = random.choice(test_list)
# printing random 
print("Random selected day is : " + str(random_day))
#code is fixed random day selected was monday 
# (5 points): As a user, I want a destination to be randomly selected for my day trip. 
import random
destination = ['new york', 'california', 'georgia', 'texas']
print("destination list is : " + str(destination))
random_place = random.choice(destination)
print("Random selected destination is : " + str(random_place))
# (5 points): As a user, I want a mode of restaurant to be randomly selected for my day trip. 
import random 
restaurant = ['burger king', 'arbys','dennys','canes', 'mcdonalds']
print("restaurant list is :" + str (restaurant))
random_restaurant = random.choice(restaurant)
print("Random selected restaurant is : " + str(random_restaurant))
#(5 points): As a user, I want a mode of transportation to be randomly selected for my day trip. 
import random
transport = ['train', 'taxi', 'bus', 'plane', 'ship']
print("transport list is :" +str(transport)) #fixed typo error on code 
random_transport = random.choice(transport)
print("Random selected transport is :" + str(random_transport))
#(5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.
import random
entertainment = ['festivals', 'museums', 'fairs', 'movies', 'zoo']
print("entertainment list is :" + str(entertainment))
random_entertainment = random.choice(entertainment)
print("Random selected entertainment is :" +str(random_entertainment))
