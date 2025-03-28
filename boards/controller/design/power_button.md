# Power Button

The controller will implement a soft latching power circuit, as described
[here](https://circuitcellar.com/resources/quickbits/soft-latching-power-circuits/).
While it's possible to put the MCU and other peripherals into a sleep state,
removing power completely will result in the longest battery life in an off
state. Additionally, the LCD used was not designed with low power in mind, so
even in a sleep state there will be considerable power draw.
