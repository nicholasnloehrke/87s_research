# Code and hardware design files

## Device

### Front panel

![front_panel](docs/really_professional_front_panel_mockup.png)

## Bidirectional Load Switch

### Render

![render](kicad/bidirectional_load_switch/renders/raytraced.png)

### Schematic

#### Overall

![schematic](kicad/bidirectional_load_switch/schematic/schematic.png)

#### Channel 1

![channel_schematic](kicad/bidirectional_load_switch/schematic/channel_schematic.png)

#### Front copper

![front_pcb](kicad/bidirectional_load_switch/pcb/front.png)

#### Back copper

![back_pcb](kicad/bidirectional_load_switch/pcb/back.png)

#### Combined copper

![back_pcb](kicad/bidirectional_load_switch/pcb/both.png)

### Known issues
- v0.1.0
    - Insufficient spacing on the AC connector 'AC_in' net to 'earth' net
    - Lack of diode inline with 5 volt supply which would cause an issue if 5 volts and 3v3 (from ISP header) are supplied simultaneously 
    - The overline (for negative logic) of ' $ \overline{\text{fault\_reset}} $ ' silkscreen is difficult to read