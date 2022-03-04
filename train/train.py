import logging
from gpiozero import LED, PWMLED

log = logging.getLogger(__name__)


class Train:

    def __init__(self):
        log.info("Train instantiated")

        self.motor_speed = PWMLED(21)
        self.direction_one = LED(20)
        self.direction_two = LED(16)
        self.set_train_direction(direction="F")

    def set_train_direction(self, direction: str) -> None:

        log.info(f'Setting direction: {"Forward" if direction == "F" else "Reverse"}')
        
        if direction == "F":
            self.direction_one.on()
            self.direction_two.off()
        else:
            self.direction_one.off()
            self.direction_two.on()

    def set_train_speed(self, speed) -> None:
        self.motor_speed.value = float(speed) / 100
        log.info(f"Motor speed now: {speed}")

    