from Design_pattrens.observer_dp.observer import Observer


class MobileApp(Observer):
    def __init__(self, subject):
        self.subject = subject
        self.subject.attach(self)

    def update(self, temp, humidity):
        print(f"Weather updated {temp}, humidity {humidity} in mobile app")

    def shutdown(self):
        self.subject.detach(self)
