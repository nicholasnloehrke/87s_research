# Charger IC's
    - BQ24707x
        - old
    - BQ24715
        - EVM avaliable
    - BQ24725A
        - EVM avaliable
    - BQ24735
        - EVM avaliable
    - BQ25792
        - EVM avaliable
        - Integrated FETs
        - Probably the easiest to design, assuming it meets the required specs

# Fuel Gauges
    - MAX17263

# BQ25792
    - Ship mode?
    - No USB D+/-?
    - V_AC?
    - Support 2-cell only?
        - If no, hardware jumpers or software configuration?
        - PROG pin sets *default* cell count, but can this be configured at runtime?
        - Seems like setting PROG to 1-cell and then configuring at runtime is possible.
          Need to consider safety concerns if MCU is setting charge voltages

## BQ25792 Power Sequencing
    - Minimum working voltage (rising)
        - VBAT
            - Min: 3.25, nominal: 3.40, max: 3.55 (ship mode)
            - Min: 2.50, nominal: 2.60, max: 2.71 (normal mode)
        - VBUS
            - 
