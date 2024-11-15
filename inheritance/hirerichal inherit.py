class parent:
    def __init__(self):
        pass


class child1(parent):
    def __init__(self):
        super().__init__()

    def func_child1(self):
        print("func child 1")


class child2(parent):
    def __init__(self):
        super().__init__()


c = child1()
c.func_child1()


c2 = child2()
c2.func_child1() # error here