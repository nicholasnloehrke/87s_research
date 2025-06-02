MCU = attiny85
SRC_DIR = src
BUILD_DIR = build
SRC = $(SRC_DIR)/main.c
ELF = $(BUILD_DIR)/main.elf
HEX = $(BUILD_DIR)/main.hex
PROGRAMMER = stk500v2

all: $(HEX)

$(ELF): $(SRC)
	mkdir -p $(BUILD_DIR)
	avr-gcc -mmcu=$(MCU) -Os -o $(ELF) $(SRC)

$(HEX): $(ELF)
	avr-objcopy -O ihex $(ELF) $(HEX)

upload: $(HEX)
ifndef PORT
	$(error PORT is not set. Usage: make upload PORT=COM3)
endif
	avrdude -c $(PROGRAMMER) -p t85 -P $(PORT) -U flash:w:$(HEX)

clean:
	rm -rf $(BUILD_DIR)

.PHONY: all upload clean
