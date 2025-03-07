# MCU Requirements

> This is a living document and will be updated continuously as requirements change

## Table

| Category    | Requirement | Amount                         | Details                                                                       |
|-------------|-------------|--------------------------------|-------------------------------------------------------------------------------|
| Memory      | RAM         | 700kB (min), ~1MB+ (preferred) | Needed for frame buffers (~614kB), LVGL (~48kB), and RTOS overhead            |
|             | Flash       | 200kB (min), 1MB+ (preferred)  | LVGL (~100kB), FreeRTOS (~64kB). External QSPI flash likely needed with 200kB |
| Performance | General     | N/A                            | Any MCU meeting RAM/Flash requirements should be sufficient                   |
| Peripherals | PWM         | 1x (min), 8x (preferred)       | For load switch channels                                                      |
|             | SPI         | 1x                             | Display                                                                       |
|             | I2C         | 0x, 1x (preferred)             | Display touch controller and STUSB4500                                        |
|             | USB         | 1x                             | For firmware updates and potential data logging                               |
|             | QSPI        | 0x, 1x (preferred)             | For external flash                                                            |
|             | GPIO        | TBD                            | Needed for encoders, load switch, expansion                                   |

## Discussion

### Memory

#### RAM

Fitting two frame buffers in memory would be ideal to allow for double buffering.  Tentatively, a 320 x 480 16BPP
display is to be used, requiring ~614kB for two buffers. LVGL claims 4kB + 150B/widget or '~48kB for a UI with a few
screens'. If we use a RTOS, extra RAM for thread stacks would be nice. With these considereations in mind, 700kB is
required and ~1MB or more of system RAM is preferred. 

#### Flash

I don't have a good idea of the flash requirements yet. LVGL wants ~100kB (depending on enabled features) and FreeRTOS
wants ~64kB (this is with TCP stack which we don't care about). More is certainly better, but we could probably get away
with some external QSPI flash if needed. I'm going to say ~200kB of onboard flash is a hard requirement, with 1MB total
being a nice to have. The tentative display has SD card support, but that uses the same SPI bus as the display driver,
so that's not ideal for reading/writing except at initialization.

### Performance

Performance is important, but just about any MCU that meets the RAM/flash requirements will be sufficient.

### USB-C Power Delivery

The STM32U5* chips have an integrated USB-C PD controller, but to reduce development time/complexity, I think using a
standalone STUSB4500 PD controller makes sense. It will take up some more board area and increase BOM count + cost, but
I think it still makes sense and reduces power sequencing complexity.

# Options
- STM32U575CGU3
    - Cheapest MCU on Digikey (thats in stock) that fits requirements
- STM32U575RITx
    - Similar to above, but with more IO
