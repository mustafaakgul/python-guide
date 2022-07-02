

def solve(meal_cost, tip_percent, tax_percent):
    meal_cost = meal_cost
    mealCost = (meal_cost / 100) * tip_percent + meal_cost
    mealCost = (meal_cost / 100) * tax_percent + mealCost
    print(int(round(mealCost)))
    print("Hello {}! You just delved into python.".format(mealCost))

if __name__ == '__main__':
    input = int(input().strip())
    input = int(input)
    print("Hello", input)
    solve(input, 12, 4)

    n = int(input())
    if n >= 1 and n <= 20:
        for i in range(0, n):
            print(i ** 2)


# Comment
# Block Comment
# Conditions
# Loops

class Person:
    def __init__(self, initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge < 0:
            self.age = 0
            print("Age is not valid, setting age to 0.")
        else:
            self.age = initialAge

    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.age < 13:
            print("You are young.")
        elif self.age >= 13 and self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")

    def yearPasses(self):
        # Increment the age of the person in here
        self.age += 1

t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")