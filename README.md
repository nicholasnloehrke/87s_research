# Code and hardware design files

## Block diagram

### Overall system

![complete_system_block_diagram](block_diagrams/complete_system.png)

### Power supply

![power_supply_block_diagram](block_diagrams/power_supply.png)

## Boards

### Bidirectional Load Switch

#### Known issues

- v0.1.0
    - Insufficient spacing on the AC connector 'AC_in' net to 'earth' net
    - Lack of diode inline with 5 volt supply which would cause an issue if 5 volts and 3v3 (from ISP header) are supplied simultaneously 
