from list_of_served import Restaurant


restaurant = Restaurant('American Burgers&Steaks', 'Fast food')

print(restaurant.name)
print(restaurant.cuisine)

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.set_number_served(45)
restaurant.increment_number_served(12)

restaurant.describe_restaurant()
