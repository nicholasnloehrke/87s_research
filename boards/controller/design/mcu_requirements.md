# MCU Requirements

> This is a living document and will be updated continuously

## Table


## Discussion
### Memory
#### RAM

Fitting two frame buffers in memory would be ideal to allow for double
buffering. Tentatively, a 320 x 480 16BPP display is to be used, requiring
~614kB for two buffers. LVGL claims 4kB + 150B/widget or '~48kB for a UI with a
few screens'. If we use a RTOS, extra RAM for thread stacks would be nice. With
these considereations in mind, ~1MB or more of system RAM is preferred. 

#### Flash

I don't have a good idea of the flash requirements yet. LVGL wants ~100kB
(depending on enabled features) and FreeRTOS wants ~64kB (this is with TCP stack
which we don't care about). More is certainly better, but we could probably get
away with some external QSPI flash if needed. I'm going to say ~200kB of onboard
flash is a hard requirement, with 1MB total being a nice to have. The tentative
display has SD card support, but that uses the same SPI bus as the display
driver, so that's not ideal for reading/writing except at initialization.
