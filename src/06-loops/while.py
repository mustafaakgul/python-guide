# 1-100 e kadar

# x = 1
# while x <= 100:
#     if x % 2==1:
#         print(f'sayı tek: {x}')
#     else:
#         print(f'sayı çift: {x}')
#     x += 1

# print('bitti...')


name = '' # False
while  name.isspace():    #not name.strip():
    name = input('isminizi giriniz: ')

print(f'Merhaba, {name}')

condition = True
while condition:
    pass

user_input = ''
while user_input.lower() != 'done':
    user_input = input('Enter a new value, or done when done')

# Create the variable for user input
user_input = ''
# Create the list to store the values
inputs = []
# The while loop
while user_input.lower() != 'done':
    # Check if there's a value in user_input
    if user_input:
        # Store the value in the list
        inputs.append(user_input)
    # Prompt for a new value
    user_input = input('Enter a new value, or done when done')

new_planet = ''
planets = []
while new_planet.lower() != 'done':
    if new_planet:
        planets.append(new_planet)
    new_planet = input('Enter a new planet, or done if done')
print(planets)


planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print("The first planet is ", planets[0])
print("The second planet is ", planets[1])
print("The third planet is ", planets[2])
countdown = [4, 3, 2, 1, 0]
for number in countdown:
    from time import sleep
    print(number)
    sleep(1)
print("Blast off!! 🚀")