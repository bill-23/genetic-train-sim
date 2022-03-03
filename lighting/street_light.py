import logging
from gpiozero import LED

log = logging.getLogger(__name__)

street_light_relay = LED(12)


def change_streetlight_state(enabled: bool) -> None:

    log.info(f'Turning street lights {"on" if enabled else "off"}')

    if enabled:
        street_light_relay.on()
    else:
        street_light_relay.off()