from director import Director
if __name__ == '__main__':

    director = Director()
    computer = director.construct_gaming(10, 20,30,40)
    print(computer)

    office = Director().construct_office(10,10,10)
    print(office)


# TODO: Build pizza system in a builder way..