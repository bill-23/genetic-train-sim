import logging
from gpiozero import LED

log = logging.getLogger(__name__)

# Street light relay is on GPIO 12
street_light_relay = LED(12)


def change_street_light_state(enabled: bool) -> None:
    """
    Method to change the state of the street lights. 

    Args:
    * `enabled` (bool): True - Lights ON, False - Lights OFF
    """

    log.info(f'Turning street lights {"on" if enabled else "off"}')

    if enabled:
        street_light_relay.on()
    else:
        street_light_relay.off()

        