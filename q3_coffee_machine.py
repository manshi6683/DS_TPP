<<<<<<< HEAD
from abc import ABC, abstractmethod

# ---------------- ABSTRACT CLASS ---------------- #

class CoffeeMachine(ABC):

    def __init__(self, coffee_name):
        self.coffee_name = coffee_name

    @abstractmethod
    def make_coffee(self):
        pass

    # Method Overloading Concept
    def ingredients(self, coffee_powder=0, milk=0, water=0, sugar=0, chocolate=0):
        print("\nIngredients Used")
        print("----------------------")
        print(f"Coffee Powder : {coffee_powder} gm")
        print(f"Milk           : {milk} ml")
        print(f"Water          : {water} ml")
        print(f"Sugar          : {sugar} tsp")
        print(f"Chocolate      : {chocolate} gm")


# ---------------- INHERITANCE ---------------- #

# Espresso Base Class
class Espresso(CoffeeMachine):

    def __init__(self):
        super().__init__("Espresso")

    # Method Overriding
    def make_coffee(self):

        print("\n===== ESPRESSO COFFEE =====")

        self.ingredients(
            coffee_powder=18,
            water=30,
            sugar=1
        )

        print("\nRecipe")
        print("----------------------")
        print("1. Heat Water")
        print("2. Add Coffee Powder")
        print("3. Extract Espresso Shot")
        print("4. Serve Hot")

        print("\nOutcome : Strong Black Coffee")


# Americano inherits Espresso
class Americano(Espresso):

    # Method Overriding
    def make_coffee(self):

        print("\n===== AMERICANO COFFEE =====")

        self.ingredients(
            coffee_powder=18,
            water=100,
            sugar=1
        )

        print("\nRecipe")
        print("----------------------")
        print("1. Prepare Espresso Shot")
        print("2. Add Extra Hot Water")
        print("3. Mix Properly")
        print("4. Serve")

        print("\nOutcome : Smooth Diluted Espresso")


# Cappuccino inherits Americano
class Cappuccino(Americano):

    def make_coffee(self):

        print("\n===== CAPPUCCINO COFFEE =====")

        self.ingredients(
            coffee_powder=18,
            milk=120,
            water=30,
            sugar=2
        )

        print("\nRecipe")
        print("----------------------")
        print("1. Prepare Espresso")
        print("2. Add Steamed Milk")
        print("3. Add Milk Foam")
        print("4. Serve Hot")

        print("\nOutcome : Creamy Foam Coffee")


# Latte inherits Cappuccino
class Latte(Cappuccino):

    def make_coffee(self):

        print("\n===== LATTE COFFEE =====")

        self.ingredients(
            coffee_powder=18,
            milk=200,
            water=30,
            sugar=2
        )

        print("\nRecipe")
        print("----------------------")
        print("1. Prepare Espresso")
        print("2. Add More Steamed Milk")
        print("3. Light Foam Layer")
        print("4. Serve")

        print("\nOutcome : Milky Smooth Coffee")


# Mocha inherits Latte
class Mocha(Latte):

    def make_coffee(self):

        print("\n===== MOCHA COFFEE =====")

        self.ingredients(
            coffee_powder=18,
            milk=150,
            water=30,
            sugar=2,
            chocolate=25
        )

        print("\nRecipe")
        print("----------------------")
        print("1. Prepare Espresso")
        print("2. Add Chocolate Syrup")
        print("3. Add Steamed Milk")
        print("4. Mix and Serve")

        print("\nOutcome : Chocolate Flavored Coffee")


# Cold Coffee inherits Mocha
class ColdCoffee(Mocha):

    def make_coffee(self):

        print("\n===== COLD COFFEE =====")

        self.ingredients(
            coffee_powder=20,
            milk=250,
            water=20,
            sugar=3,
            chocolate=15
        )

        print("\nRecipe")
        print("----------------------")
        print("1. Prepare Coffee")
        print("2. Add Cold Milk")
        print("3. Add Ice Cubes")
        print("4. Blend Properly")
        print("5. Serve Chilled")

        print("\nOutcome : Refreshing Cold Coffee")


# ---------------- USER INPUT SYSTEM ---------------- #

print("\n========== COFFEE MACHINE ==========")

print("""
1. Espresso
2. Americano
3. Cappuccino
4. Latte
5. Mocha
6. Cold Coffee
""")

choice = int(input("Enter Coffee Choice : "))

# ---------------- OBJECT CREATION ---------------- #

if choice == 1:
    coffee = Espresso()

elif choice == 2:
    coffee = Americano()

elif choice == 3:
    coffee = Cappuccino()

elif choice == 4:
    coffee = Latte()

elif choice == 5:
    coffee = Mocha()

elif choice == 6:
    coffee = ColdCoffee()

else:
    print("Invalid Choice")
    exit()

# ---------------- FINAL OUTPUT ---------------- #

=======
from abc import ABC, abstractmethod

# ---------------- ABSTRACT CLASS ---------------- #

class CoffeeMachine(ABC):

    def __init__(self, coffee_name):
        self.coffee_name = coffee_name

    @abstractmethod
    def make_coffee(self):
        pass

    # Method Overloading Concept
    def ingredients(self, coffee_powder=0, milk=0, water=0, sugar=0, chocolate=0):
        print("\nIngredients Used")
        print("----------------------")
        print(f"Coffee Powder : {coffee_powder} gm")
        print(f"Milk           : {milk} ml")
        print(f"Water          : {water} ml")
        print(f"Sugar          : {sugar} tsp")
        print(f"Chocolate      : {chocolate} gm")


# ---------------- INHERITANCE ---------------- #

# Espresso Base Class
class Espresso(CoffeeMachine):

    def __init__(self):
        super().__init__("Espresso")

    # Method Overriding
    def make_coffee(self):

        print("\n===== ESPRESSO COFFEE =====")

        self.ingredients(
            coffee_powder=18,
            water=30,
            sugar=1
        )

        print("\nRecipe")
        print("----------------------")
        print("1. Heat Water")
        print("2. Add Coffee Powder")
        print("3. Extract Espresso Shot")
        print("4. Serve Hot")

        print("\nOutcome : Strong Black Coffee")


# Americano inherits Espresso
class Americano(Espresso):

    # Method Overriding
    def make_coffee(self):

        print("\n===== AMERICANO COFFEE =====")

        self.ingredients(
            coffee_powder=18,
            water=100,
            sugar=1
        )

        print("\nRecipe")
        print("----------------------")
        print("1. Prepare Espresso Shot")
        print("2. Add Extra Hot Water")
        print("3. Mix Properly")
        print("4. Serve")

        print("\nOutcome : Smooth Diluted Espresso")


# Cappuccino inherits Americano
class Cappuccino(Americano):

    def make_coffee(self):

        print("\n===== CAPPUCCINO COFFEE =====")

        self.ingredients(
            coffee_powder=18,
            milk=120,
            water=30,
            sugar=2
        )

        print("\nRecipe")
        print("----------------------")
        print("1. Prepare Espresso")
        print("2. Add Steamed Milk")
        print("3. Add Milk Foam")
        print("4. Serve Hot")

        print("\nOutcome : Creamy Foam Coffee")


# Latte inherits Cappuccino
class Latte(Cappuccino):

    def make_coffee(self):

        print("\n===== LATTE COFFEE =====")

        self.ingredients(
            coffee_powder=18,
            milk=200,
            water=30,
            sugar=2
        )

        print("\nRecipe")
        print("----------------------")
        print("1. Prepare Espresso")
        print("2. Add More Steamed Milk")
        print("3. Light Foam Layer")
        print("4. Serve")

        print("\nOutcome : Milky Smooth Coffee")


# Mocha inherits Latte
class Mocha(Latte):

    def make_coffee(self):

        print("\n===== MOCHA COFFEE =====")

        self.ingredients(
            coffee_powder=18,
            milk=150,
            water=30,
            sugar=2,
            chocolate=25
        )

        print("\nRecipe")
        print("----------------------")
        print("1. Prepare Espresso")
        print("2. Add Chocolate Syrup")
        print("3. Add Steamed Milk")
        print("4. Mix and Serve")

        print("\nOutcome : Chocolate Flavored Coffee")


# Cold Coffee inherits Mocha
class ColdCoffee(Mocha):

    def make_coffee(self):

        print("\n===== COLD COFFEE =====")

        self.ingredients(
            coffee_powder=20,
            milk=250,
            water=20,
            sugar=3,
            chocolate=15
        )

        print("\nRecipe")
        print("----------------------")
        print("1. Prepare Coffee")
        print("2. Add Cold Milk")
        print("3. Add Ice Cubes")
        print("4. Blend Properly")
        print("5. Serve Chilled")

        print("\nOutcome : Refreshing Cold Coffee")


# ---------------- USER INPUT SYSTEM ---------------- #

print("\n========== COFFEE MACHINE ==========")

print("""
1. Espresso
2. Americano
3. Cappuccino
4. Latte
5. Mocha
6. Cold Coffee
""")

choice = int(input("Enter Coffee Choice : "))

# ---------------- OBJECT CREATION ---------------- #

if choice == 1:
    coffee = Espresso()

elif choice == 2:
    coffee = Americano()

elif choice == 3:
    coffee = Cappuccino()

elif choice == 4:
    coffee = Latte()

elif choice == 5:
    coffee = Mocha()

elif choice == 6:
    coffee = ColdCoffee()

else:
    print("Invalid Choice")
    exit()

# ---------------- FINAL OUTPUT ---------------- #

>>>>>>> 0a37d2ea2e0c746b420f97eccb9689fdeea510b4
coffee.make_coffee()