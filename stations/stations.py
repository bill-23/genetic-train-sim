# import logging
# from gpiozero import Button


# log = logging.getLogger(__name__)

# station_one = Button(5)
# station_two = Button(6)
# station_three = Button(13)
# station_four = Button(19)


# def get_current_station() -> int:

#     if station_one.is_pressed:
#         log.info("Train at station 1")
#         return 1
#     elif station_two.is_pressed:
#         log.info("Train at station 1")
#         return 2
#     elif station_three.is_pressed:
#         log.info("Train at station 2")
#         return 3
#     elif station_four.is_pressed:
#         log.info("Train at station 2")
#         return 4
#     else:
#         return 0
