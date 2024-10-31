cmake_minimum_required(VERSION 3.0)
project(bidirectional_load_switch C)

set(MCU atmega328p)
set(F_CPU 16000000UL) 

set(CMAKE_SYSTEM_NAME Generic)
set(CMAKE_C_COMPILER avr-gcc)
set(CMAKE_CXX_COMPILER avr-g++)

# Add compilation flags
add_definitions(-DF_CPU=${F_CPU})
set(CMAKE_C_FLAGS "-mmcu=${MCU} -Os -Wall")

# Source files
add_executable(bidirectional_load_switch.elf src/main.c)

# Define a target to generate the .hex file
add_custom_target(bidirectional_load_switch.hex ALL
    COMMAND avr-objcopy -O ihex -R .eeprom bidirectional_load_switch.elf bidirectional_load_switch.hex
    DEPENDS bidirectional_load_switch.elf
)

# Define a target to upload the hex file (adjust port and programmer as needed)
add_custom_target(upload
    COMMAND avrdude -c usbasp -p ${MCU} -U flash:w:bidirectional_load_switch.hex:i
    DEPENDS bidirectional_load_switch.hex
)
