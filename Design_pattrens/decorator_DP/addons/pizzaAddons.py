from Design_pattrens.decorator_DP.pizza import Pizza


class PizzaAddons(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza
