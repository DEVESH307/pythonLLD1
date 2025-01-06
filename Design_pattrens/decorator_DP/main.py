from Design_pattrens.decorator_DP.BasePizza import BasePizza
from Design_pattrens.decorator_DP.addons.Panner import Panner
from Design_pattrens.decorator_DP.addons.cheese import Cheese

pizza = BasePizza()
panner_pizza = Panner(pizza)

chesse_panner_pizza = Cheese(panner_pizza)

print(chesse_panner_pizza.get_price())