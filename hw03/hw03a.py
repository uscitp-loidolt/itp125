def hotel_cost(nights):
    result = 140 * nights
    return result

def plane_ride_cost(city):
    if city == "Charlotte":
        cost = 183
        return cost
    elif city == "Tampa":
        cost = 220
        return cost
    elif city == "Pittsburgh":
        cost = 222
        return cost
    elif city == "Los Angeles":
        cost = 475
        return cost

def rental_car_cost(days):
    result = days * 40

    if days >= 7:
        result -= 50
    elif days >= 3 and days < 7:
        result -= 20

    return result

def trip_cost(city, days, spending_money):
    return hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + spending_money

print trip_cost("Los Angeles", 5, 600)
