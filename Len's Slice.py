toppings = ["pepperoni", "pineaple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2] 
num_pizzas = len(toppings)
print("We sell " + str(num_pizzas) + " different kind of pizzas! ")

pizzas = list(zip(prices, toppings))
print(pizzas)

pizzas.sort()

cheapest_pizza = pizzas[0]
print(cheapest_pizza)

three_cheapest = pizzas[0:3]
print(three_cheapest)