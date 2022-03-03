import logging
from gpiozero import LED


log = logging.getLogger(__name__)

car_light_relay = LED(26)


def change_carlight_state(enabled: bool) -> None:

    log.info(f'Turning car lights {"on" if enabled else "off"}')

    if enabled:
        car_light_relay.on()
    else:
        car_light_relay.off()