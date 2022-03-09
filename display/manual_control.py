import tkinter as tk
from tkinter import ttk
import logging
from train.train import Train
from lighting.street_light import change_street_light_state
from lighting.car_light import change_car_light_state
from gpiozero import Button


log = logging.getLogger(__name__)


class ManualController(tk.Tk):

    def __init__(self, train: Train):
        super().__init__()

        self.train = train

        self.title("Train Sim")
        self.geometry('800x500')
        
        self.station_one = Button(5)
        self.station_one.when_pressed = self.get_station_image
        self.station_one.when_released= self.get_station_image
        self.station_two = Button(19)
        self.station_two.when_pressed = self.get_station_image
        self.station_two.when_released = self.get_station_image
        self.station_three = Button(6)
        self.station_three.when_pressed = self.get_station_image
        self.station_three.when_released = self.get_station_image
        self.station_four = Button(13)
        self.station_four.when_pressed = self.get_station_image
        self.station_four.when_released = self.get_station_image

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

        self.image = tk.PhotoImage(file='assets/stations-all-red.png')

        self.label = ttk.Label(self.left_frame, image=self.image)
        self.label.image = self.image

        self.label.pack()

        self.right_frame = ttk.Frame(
            self.content, 
            borderwidth=5, 
            relief="ridge", 
            width=295, 
            height=300
        )

        self.speed_slider = ttk.Scale(
            self.content,
            from_=0,
            to=100,
            orient=tk.VERTICAL,
            length=250,
            command=self.speed_changed,
            variable=self.speed_value,
        )

        self.speed_slider.set(100.0)

        self.street_light_checkbox = ttk.Checkbutton(
            self.content,
            text='Street Lights',
            command=self.street_lights_changed,
            variable=self.street_lights_bool,
            onvalue=True,
            offvalue=False,
        )

        self.car_light_checkbox = ttk.Checkbutton(
            self.content,
            text='Car Lights',
            command=self.car_lights_changed,
            variable=self.car_lights_bool,
            onvalue=True,
            offvalue=False
        )

        for count, direction in enumerate(self.directions):
            self.radio_button = ttk.Radiobutton(
                self.content,
                text=direction[0],
                value=direction[1],
                command=self.direction_changed,
                variable=self.selected_direction
            )

            self.radio_button.grid(column=4, row=count, columnspan=2)

        self.content.grid(column=0, row=0)

        self.left_frame.grid(column=0, row=0, columnspan=4, rowspan=4)

        self.right_frame.grid(column=4, row=0, columnspan=4, rowspan=4)

        self.speed_slider.grid(column=6, row=0, columnspan=2, rowspan=4, pady=25)

        self.street_light_checkbox.grid(column=0, row=5, padx=5, pady=5)

        self.car_light_checkbox.grid(column=1, row=5, padx=5, pady=5)


    def get_current_value(self):
        return '{: .2f}'.format(100 - self.speed_value.get())

    def speed_changed(self, event):
        self.train.set_train_speed(float(self.get_current_value()))

    def street_lights_changed(self):
        change_street_light_state(enabled=self.street_lights_bool.get())

    def car_lights_changed(self):
        change_car_light_state(enabled=self.car_lights_bool.get())

    def direction_changed(self):
        self.train.set_train_direction(self.selected_direction.get())

    def get_station_image(self):
        if self.station_one.is_pressed:
            log.info("Train at sensor 1")
            new_photo = tk.PhotoImage(file=self.image_dict.get(1))
            self.label.config(image=new_photo)
            self.label.image = new_photo
        elif self.station_two.is_pressed:
            log.info("Train at sensor 2")
            new_photo = tk.PhotoImage(file=self.image_dict.get(2))
            self.label.config(image=new_photo)
            self.label.image = new_photo
        elif self.station_three.is_pressed:
            log.info("Train at sensor 3")
            new_photo = tk.PhotoImage(file=self.image_dict.get(3))
            self.label.config(image=new_photo)
            self.label.image = new_photo
        elif self.station_four.is_pressed:
            log.info("Train at sensor 4")
            new_photo = tk.PhotoImage(file=self.image_dict.get(4))
            self.label.config(image=new_photo)
            self.label.image = new_photo
        else:
            new_photo = tk.PhotoImage(file=self.image_dict.get(0))
            self.label.config(image=new_photo)
            self.label.image = new_photo