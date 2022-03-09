import logging
from gpiozero import LED

log = logging.getLogger(__name__)

# The car light relay is on GPIO 26
car_light_relay = LED(26)


def change_car_light_state(enabled: bool) -> None:
    """
    Method to change the state of the car lights. 

    Args:
    * `enabled` (bool): True - Lights ON, False - Lights OFF
    """

    log.info(f'Turning car lights {"on" if enabled else "off"}')

    if enabled:
        car_light_relay.on()
    else:
        car_light_relay.off()