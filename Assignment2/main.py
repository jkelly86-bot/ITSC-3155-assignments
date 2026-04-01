import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
<<<<<<< HEAD
sandwich_maker_instance = #####
cashier_instance = ######
=======
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()
>>>>>>> b49e9305b16195f21d5596d005f2089212bdbf9b




def main():
    ###  write the rest of the codes ###
<<<<<<< HEAD

=======
    is_on = True

    while is_on:
        choice = input("What would you like? (small/medium/large/report/off): ").lower()

        if choice == "off":
            is_on = False

        elif choice == "report":
            print("Current Resources:")
            for item, amount in resources.items():
                print(f"{item}: {amount}")

        elif choice in recipes:
            sandwich = recipes[choice]
            ingredients = sandwich["ingredients"]
            cost = sandwich["cost"]

            if sandwich_maker_instance.check_resources(ingredients):
                payment = cashier_instance.process_coins()
                if cashier_instance.transaction_result(payment, cost):
                    sandwich_maker_instance.make_sandwich(choice, ingredients)

        else:
            print("Invalid option. Try small, medium, large, report, or off.")
>>>>>>> b49e9305b16195f21d5596d005f2089212bdbf9b
if __name__=="__main__":
    main()
