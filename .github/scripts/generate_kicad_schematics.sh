#!/bin/bash

# # schematic pdf
# kicad-cli sch export pdf -n --output kicad/bidirectional_load_switch/schematic/schematic.pdf kicad/bidirectional_load_switch/bidirectional_load_switch.kicad_sch

# # pcb pdf

# # front
# kicad-cli pcb export pdf --output kicad/bidirectional_load_switch/pcb/front.pdf -l F.Cu kicad/bidirectional_load_switch/bidirectional_load_switch.kicad_pcb
# # back
# kicad-cli pcb export pdf --output kicad/bidirectional_load_switch/pcb/back.pdf -l B.Cu kicad/bidirectional_load_switch/bidirectional_load_switch.kicad_pcb
# # both
# kicad-cli pcb export pdf --output kicad/bidirectional_load_switch/pcb/both.pdf -l B.Cu,F.Cu kicad/bidirectional_load_switch/bidirectional_load_switch.kicad_pcb

# # convert pdf to images
# pdftoppm kicad/bidirectional_load_switch/pcb/front.pdf -singlefile kicad/bidirectional_load_switch/pcb/front -png
# pdftoppm kicad/bidirectional_load_switch/pcb/back.pdf -singlefile kicad/bidirectional_load_switch/pcb/back -png
# pdftoppm kicad/bidirectional_load_switch/pcb/both.pdf -singlefile kicad/bidirectional_load_switch/pcb/both -png
# pdftoppm kicad/bidirectional_load_switch/schematic/schematic.pdf -singlefile kicad/bidirectional_load_switch/schematic/schematic -png
# pdftoppm kicad/bidirectional_load_switch/schematic/schematic.pdf -f 2 -singlefile kicad/bidirectional_load_switch/schematic/channel_schematic -png

# # merge pdfs
# pdfunite kicad/bidirectional_load_switch/schematic/schematic.pdf kicad/bidirectional_load_switch/pcb/back.pdf kicad/bidirectional_load_switch/pcb/front.pdf kicad/bidirectional_load_switch/pcb/both.pdf kicad/bidirectional_load_switch/printable.pdf

kicad-cli sch export pdf -n --output boards/bidirectional_load_switch/schematic.pdf boards/bidirectional_load_switch/pcb/bidirectional_load_switch.kicad_sch
