from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from datetime import datetime
from kivy.app import App
from kivy.clock import Clock
from pprint import pprint
import requests


class DateTimeScreen(GridLayout):
    dayOfWeek = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]

    def __init__(self, **kwargs):
        super(DateTimeScreen, self).__init__(**kwargs)


    def update(self, *args):
        self.clear_widgets()
        date = datetime.now()
        day = self.dayOfWeek[date.weekday()][:3]

        self.cols = 1
        self.add_widget(
            Label(
                text= day + " " + str(date.date().strftime("%d.%m.%Y")),
                font_size="40")
            )
        self.add_widget(
            Label(
                text=str(date.time().strftime("%H:%M:%S")),
                font_size="40", bold=True)
            )


class SmartMirror(App):

    weatherURL = "http://samples.openweathermap.org/data/2.5/forecast?id=524901&appid=b1b15e88fa797225412429c1c50c122a1"

    def build(self):
        r = requests.get(self.weatherURL)
        pprint(r.json())

        timeScreen = DateTimeScreen()
        Clock.schedule_interval(timeScreen.update, 1)
        return timeScreen


if __name__ == "__main__":
    SmartMirror().run()
