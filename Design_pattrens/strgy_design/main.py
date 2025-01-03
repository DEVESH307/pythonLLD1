from Design_pattrens.strgy_design.PaymentFactory import PaymentFactory

if __name__ == '__main__':
    user_choice = input('Enter your choice: credit_card/debit_card').strip().lower()

    try:
        mode = PaymentFactory.get_strgy(user_choice)
        mode.pay(100)

    except ValueError as e:
        print(e)
