import time

class Product:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"{self.name.capitalize()} ({self.name})")

def get_choice_input(prompt, choices):
    while True:
        value = input(prompt)
        if value in choices:
            return value
        else:
            print(f"Please enter one of the following choices: {', '.join(choices)}")

def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid integer.")

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")

def get_yes_no_input(prompt):
    while True:
        value = input(prompt).strip().lower()
        if value in ['yes', 'no']:
            return value == 'yes'
        else:
            print("Please enter 'yes' or 'no'.")

def make_cream():
    print("To create face cream, we need 4 ingredients: water, glycerin, hyaluronic acid, provitamin B5.")
    mix = get_yes_no_input("Do you want to mix all the ingredients? (yes/no): ")
   
    if mix:
        print("\nLet's start making the face cream...")
        ingredients = 0
       
        while ingredients < 4:
            print("Adding ingredient...")
            time.sleep(1)
            ingredients += 1
            print(f"Added {ingredients} ingredients out of 4")
       
        print("Face cream is almost ready! Just need to add preservatives.")
        while True:
            count = get_float_input("Enter the amount of preservative you want to add (you need to add 0.7ml for a 50ml jar): ")
           
            if abs(count - 0.7) < 1e-6:
                print("You entered the correct amount of preservative, mixing the cream...")
                time.sleep(1)
                print("Congratulations, your 50ml face cream is ready!")
                break
            else:
                print("Incorrect amount of preservative. Try again.")
    else:
        print("Okay, we can try later!")

def make_shampoo():
    print("To create shampoo, we need water, coconut oil, provitamin B5, and fragrance.")
    time.sleep(1)
    print("Congratulations, your shampoo is ready!")

def make_serum():
    print("To create serum, we need hyaluronic acid, niacinamide, vitamin C, and antioxidants.")
    time.sleep(1)
    print("Congratulations, your serum is ready!")

def main():
    hello = get_yes_no_input("Hello! Today you are creating your own cosmetic product. Do you want to start? (yes/no): ")

    if hello:
        remaining_products = {
            '1': Product("face cream"),
            '2': Product("shampoo"),
            '3': Product("face serum")
        }
       
        while remaining_products:
            print("\nChoose the product you want to make:")
            for number, product in remaining_products.items():
                print(f"{number}. {product.name.capitalize()}")
           
            available_choices = remaining_products.keys()
            choice_prompt = "Your choice (" + ", ".join([f"{num} for {product.name}" for num, product in remaining_products.items()]) + "): "
            choice = get_choice_input(choice_prompt, available_choices)

            if choice in remaining_products:
                if choice == '1':
                    make_cream()
                elif choice == '2':
                    make_shampoo()
                elif choice == '3':
                    make_serum()
               
                del remaining_products[choice]
               
                if remaining_products:
                    another = get_yes_no_input("Do you want to make something else? (yes/no): ")
                    if not another:
                        print("See you next time!")
                        break
                else:
                    print("You made all the products! Great job!")
            else:
                print("Invalid choice, try again.")
    else:
        print("Okay, see you next time!")

main()