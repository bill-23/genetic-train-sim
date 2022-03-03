import tkinter as tk
from tkinter import ttk
import logging
from train.train import Train
from lighting.street_light import change_streetlight_state
from lighting.car_light import change_carlight_state
from stations.stations import get_current_station


log = logging.getLogger(__name__)


class ManualController(tk.Tk):

    def __init__(self, train: Train):
        super().__init__()

        self.train = train

        self.title("Train Sim")
        self.geometry('800x500')

        self.selected_direction = tk.StringVar()
        self.selected_direction.set('F')

        self.speed_value = tk.DoubleVar()

        self.car_lights_bool = tk.BooleanVar()

        self.street_lights_bool = tk.BooleanVar()

        self.directions = (('Forward', 'F'), ('Reverse', 'R'))

        self.image_dict = {
            0: 'assets/stations-all-red.png',
            1: 'assets/stations-one-green.png',
            2: 'assets/stations-two-green.png',
            3: 'assets/stations-three-green.png',
            4: 'assets/stations-four-green.png',
            12: 'assets/stations-one-two-green.png',
            34: 'assets/stations-three-four-green.png',
        }

        self.content = ttk.Frame(self)

        self.left_frame = ttk.Frame(
            self.content, 
            borderwidth=5, 
            relief="ridge", 
            width=500, 
            height=300
        )

        self.image = tk.PhotoImage(file=self.image_dict.get(get_current_station(), 'assets/stations-all-red.png'))

        self.label = ttk.Label(self.left_frame, image=self.image).pack()

        self.right_frame = ttk.Frame(
            self.content, 
            borderwidth=5, 
            relief="ridge", 
            width=300, 
            height=300
        )

        self.speed_slider = ttk.Scale(
            self.content,
            from_=0,
            to=100,
            orient=tk.VERTICAL,
            command=self.speed_changed,
            variable=self.speed_value
        )

        self.speed_slider.set(100.0)

        self.street_light_checkbox = ttk.Checkbutton(
            self.content,
            text='Street Lights',
            command=self.street_lights_changed,
            variable=self.street_lights_bool,
            onvalue=True,
            offvalue=False
        )

        self.car_light_checkbox = ttk.Checkbutton(
            self.content,
            text='Car Lights',
            command=self.car_lights_changed,
            variable=self.car_lights_bool,
            onvalue=True,
            offvalue=False
        )

        for count, direction in enumerate(self.directions, start=2):
            self.radio_button = ttk.Radiobutton(
                self.content,
                text=direction[0],
                value=direction[1],
                command=self.direction_changed,
                variable=self.selected_direction
            )

            self.radio_button.grid(column=count, row=5)

        self.content.grid(column=0, row=0)

        self.left_frame.grid(column=0, row=0, columnspan=4, rowspan=4)

        self.right_frame.grid(column=4, row=0, columnspan=4, rowspan=4)

        self.speed_slider.grid(column=6, row=5, pady=20)

        self.street_light_checkbox.grid(column=0, row=5)

        self.car_light_checkbox.grid(column=1, row=5)

        
    def get_current_value(self):
        return '{: .2f}'.format(100 - self.speed_value.get())

    def speed_changed(self, event):
        self.train.set_train_speed(self.get_current_value())

    def street_lights_changed(self):
        change_streetlight_state(enabled=self.street_lights_bool.get())

    def car_lights_changed(self):
        change_carlight_state(enabled=self.car_lights_bool.get())

    def direction_changed(self):
        self.train.set_train_direction(self.selected_direction.get())

    