class CoffeeMachine:
    def __init__(self, water, milk, coffee, cups, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money

    def status(self):
        print(f'\nThe coffee machine has: \n{self.water} of water'
              f'\n{self.milk} of milk\n{self.coffee} of coffe beans'
              f'\n{self.cups} of disposable cups\n{self.money} of money')

    def take_c(self):
        print(f'I gave you {self.money}\n')
        self.money -= self.money

    def fill_c(self):
        self.water += int(input('Write how many ml of water you want to add:'))
        self.milk += int(input('Write how many ml of milk  you want to add:'))
        self.coffee += int(input('Write how many grams of coffe beans  you want to add:'))
        self.cups += int(input('Write how many disposable cups you want to add:'))

    def buy_c(self):
        buy = input(f'\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        if buy == '1':
            if self.water < 250 or self.coffee < 16 or self.cups < 1:
                print(f'Sorry, not enough resources!')
            else:
                print('I have enough resources, making you a coffee!')
                self.water -= 250
                self.coffee -= 16
                self.cups -= 1
                self.money += 4
        elif buy == '2':
            if self.water < 350 or self.coffee < 20 or self.cups < 1:
                print(f'Sorry, not enough resources!')
            else:
                print('I have enough resources, making you a coffee!')
                self.water -= 350
                self.milk -= 75
                self.coffee -= 20
                self.cups -= 1
                self.money += 7
        elif buy == '3':
            if self.water < 200 or self.milk < 100 or self.coffee < 12 or self.cups < 1:
                print(f'Sorry, not enough resources!')
            else:
                print('I have enough resources, making you a coffee!')
            self.water -= 200
            self. milk -= 100
            self.coffee -= 12
            self.cups -= 1
            self.money += 6
        else:
            pass

    @staticmethod
    def order_c():
        while True:
            order = input('Write action (buy, fill, take, remaining, exit):')
            if order == 'buy':
                coffee_machine.buy_c()
                print(f'')
            elif order == 'fill':
                coffee_machine.fill_c()
                print(f'')
            elif order == 'take':
                coffee_machine.take_c()
            elif order == 'remaining':
                coffee_machine.status()
                print(f'')
            else:
                exit()


if __name__ == '__main__':
    coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
    coffee_machine.order_c()
