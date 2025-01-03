from Design_pattrens.observer_dp.Subject import Subject


class WeatherStation(Subject):

    def __init__(self):
        self.temp = 0
        self.humidity = 0
        self.observer = []

    def attach(self, observer):
        self.observer.append(observer)

    def detach(self, observer):
        self.observer.remove(observer)

    def notify(self):
        for observer in self.observer:
            observer.update(self.temp, self.humidity)
    def set_weather(self, temp, humidity):
        self.temp = temp
        self.humidity = humidity
        self.notify()