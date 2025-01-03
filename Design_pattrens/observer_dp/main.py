import time

from Design_pattrens.observer_dp.MobileApp import MobileApp
from Design_pattrens.observer_dp.Tv import Tv
from Design_pattrens.observer_dp.weatherstation import WeatherStation

if __name__ == '__main__':

    weatherStation = WeatherStation()


    # -- OBSERVERS --
    Mobile_app= MobileApp(weatherStation)
    tv = Tv(weatherStation)

    # ATTACH to subject..
    # weatherStation.attach(Mobile_app)
    # weatherStation.attach(tv)

    # SENSOR UPDATED THE DATA..
    weatherStation.set_weather(10,20)
    weatherStation.set_weather(15,25)
    # weatherStation.detach(tv)
    tv.shutdown()

    weatherStation.set_weather(10,20)
    time.sleep(5)
    weatherStation.set_weather(50, 50)





