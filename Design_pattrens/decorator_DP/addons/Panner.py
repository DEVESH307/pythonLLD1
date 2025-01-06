from Design_pattrens.decorator_DP.addons.pizzaAddons import PizzaAddons


class Panner(PizzaAddons):

    def get_price(self):
        return self.pizza.get_price() + 50
