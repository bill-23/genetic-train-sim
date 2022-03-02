import logging
from gpiozero import LED, PWMLED

log = logging.getLogger(__name__)


class Train:

    motor_speed = PWMLED(21)

    direction_one = LED(20)
    direction_two = LED(16)

    def __init__(self):
        log.info("Train instantiated")

    def set_train_direction(self, direction: str) -> None:

        log.info(f'Setting direction: {"Forward" if direction == "F" else "Reverse"}')
        
        if direction == "F":
            direction_one.on()
            direction_two.off()
        else:
            direction_one.off()
            direction_two.on()

    def set_train_speed(self, speed) -> None:
        motor_speed.value = speed
        log.info(f"Motor speed now: {speed}")

    