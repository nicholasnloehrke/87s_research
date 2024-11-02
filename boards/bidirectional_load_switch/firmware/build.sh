#!/bin/bash

SRC_DIR="src"
BUILD_DIR="build"

mkdir -p "$BUILD_DIR"

# compile
avr-gcc -mmcu=attiny85 -Os -o "$BUILD_DIR/main.elf" "$SRC_DIR/main.c"

# generate hex file
avr-objcopy -O ihex "$BUILD_DIR/main.elf" "$BUILD_DIR/main.hex"

# optionally upload
if [[ "$1" == "--upload" || "$1" == "-u" ]]; then
    avrdude -c stk500v2 -p t85 -P COM3 -U flash:w:"$BUILD_DIR/main.hex"
else
    echo "Skipping upload. Run with '--upload' or '-u' to upload to board."
fi
