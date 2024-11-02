#define F_CPU 8000000UL

#include <avr/io.h>
#include <util/delay.h>

#define PIN_NFAULT         PB4
#define PIN_NFAULT_RESET   PB2
#define PIN_FAULT_STATUS   PB1
#define PIN_CURRENT_SENSOR PB3

int main(void)
{
    DDRB |= (1 << PIN_FAULT_STATUS);
    DDRB |= (1 << PIN_NFAULT);
    PORTB |= (1 << PIN_NFAULT);
    
    while (1)
    {
        PORTB |= (1 << PIN_FAULT_STATUS);
        _delay_ms(50);

        PORTB &= ~(1
         << PIN_FAULT_STATUS);
        _delay_ms(50);
    }
}
