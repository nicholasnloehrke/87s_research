# Code and hardware design files

### Project structure

```bash
87s_research
├── boards
│   ├── bidirectional_load_switch
│   │   ├── firmware
│   │   ├── scripts
│   │   ├── kicad
│   │   ├── spice
│   │   └── freecad
│   ├── power_supply
│   │   ├── scripts
│   │   ├── kicad
│   │   ├── spice
│   │   └── freecad
│   └── controller
│       ├── scripts
│       ├── firmware
│       ├── kicad
│       ├── spice
│       └── freecad
├── scripts
├── docs
└── LICENSE
```

```bash
87s_research
├── boards
│   ├── bidirectional_load_switch
│   │   ├── firmware
│   │   ├── freecad
│   │   ├── kicad
│   │   ├── scripts
│   │   └── spice
│   ├── controller
│   │   ├── firmware
│   │   ├── freecad
│   │   ├── kicad
│   │   ├── scripts
│   │   └── spice
│   └── power_supply
│       ├── freecad
│       ├── kicad
│       ├── scripts
│       └── spice
├── docs
└── scripts
```

- hardware
    - bidirectional_load_switch
        - kicad
        - freecad
    - power_supply
        - kicad
        - freecad
    - controller
        - kicad
        - freecad
- software
    - bidirectional_load_switch
    - power_supply
    - controller
- scripts
    - media_generation.sh

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