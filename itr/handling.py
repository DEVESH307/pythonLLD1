from decimal import DivisionByZero


def credit():
    print("money credited")


def debit():
    raise Exception


def account():
    try:
        debit()
    except Exception as e:
        print(e)
    credit()
    print("done")


account()


def db():
    raise Exception


def create_user():
    print("creating user")
    try:
        db()
    except Exception as e:
        print(e)
    print("created user")


create_user()


class NegativeException(Exception):
    pass


def calculator(num1, num2):
    try:
        if num1 < 0:
            raise NegativeException("neg num..")

        ans = (num1 / num2)
        ans += 1

    except ZeroDivisionError:
        print("division by zero try another number")

    except NegativeException as ne:
        print("We can't take negative number" + str(ne))
    finally:
        print("e")  #close connections...


calculator(-1, 10)

print("lkdaflkd")
