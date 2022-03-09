import logging
from gpiozero import LED, PWMLED
from exc.exceptions import TrainSimInvalidInputError

log = logging.getLogger(__name__)


class Train:

    def __init__(self):
        log.info("Train instantiated")

        # PWM control on pin 21
        self.motor_speed = PWMLED(21)

        # Direction control 1 on pin 20
        self.direction_one = LED(20)

        # Direction control 2 on pin 16
        self.direction_two = LED(16)

        self.set_train_direction(direction="F")

    def set_train_direction(self, direction: str) -> None:
        """
        Sets the desired direction of the train. The L239D motor controller uses two control pins to set the 
        direction by alternating the input values.

        Args:
        * `direction` (str): Either `F` (forward), or `R` (reverse)

        Raises:
        * `TrainSimInvalidInputError`: If direction is not `F` or `R`
        """
        if direction not in ["F", "R"]:
            msg = f"Error! Expected either F or R to call set_train_direction but received {direction}"
            raise TrainSimInvalidInputError(msg=msg)

        log.info(f'Setting direction: {"Forward" if direction == "F" else "Reverse"}')
        
        if direction == "F":
            self.direction_one.on()
            self.direction_two.off()
        else:
            self.direction_one.off()
            self.direction_two.on()

    def set_train_speed(self, speed: float) -> None:
        """
        Adjusts the desired train speed. The L239D controller uses a PWM input to set the speed. 

        Args:
        * `speed` (float): The desired PWM amount (0->100)
        """
        self.motor_speed.value = speed / 100
        log.info(f"Motor speed now: {speed}")

    