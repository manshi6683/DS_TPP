# ---------------- DECORATOR ---------------- #

def animal_decorator(func):

    def wrapper(*args, **kwargs):

        print("\n==============================")
        print("Animal Information")
        print("==============================")

        func(*args, **kwargs)

        print("==============================\n")

    return wrapper


# ---------------- PARENT CLASS ---------------- #

class Animal:

    def __init__(self, eat, drink):

        self.eat = eat
        self.drink = drink

    @animal_decorator
    def show_details(self):

        print(f"Eating : {self.eat}")
        print(f"Drinking : {self.drink}")


# ---------------- CHILD CLASS : CAT ---------------- #

class Cat(Animal):

    def __init__(self, eat, drink, sound):

        super().__init__(eat, drink)

        self.sound = sound

    @animal_decorator
    def show_details(self):

        print("Animal Type : Cat")
        print(f"Eating : {self.eat}")
        print(f"Drinking : {self.drink}")
        print(f"Sound : {self.sound}")


# ---------------- CHILD CLASS : DOG ---------------- #

class Dog(Animal):

    def __init__(self, eat, drink, sound):

        super().__init__(eat, drink)

        self.sound = sound

    @animal_decorator
    def show_details(self):

        print("Animal Type : Dog")
        print(f"Eating : {self.eat}")
        print(f"Drinking : {self.drink}")
        print(f"Sound : {self.sound}")


# ---------------- OBJECT CREATION ---------------- #

cat = Cat("Fish", "Milk", "Meow")
dog = Dog("Bone", "Water", "Bark")

# ---------------- OUTPUT ---------------- #

cat.show_details()
dog.show_details()