
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
<<<<<<< HEAD
        #####

    def make_sandwich(self, sandwich_size, order_ingredients):
        ########
=======
        for item, amount_needed in ingredients.items():
            if self.machine_resources[item] < amount_needed:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        for item, amount in order_ingredients.items():
            self.machine_resources[item] -= amount
        print(f"Here is your {sandwich_size} sandwich. Enjoy!")
>>>>>>> b49e9305b16195f21d5596d005f2089212bdbf9b
