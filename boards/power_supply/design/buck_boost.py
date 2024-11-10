# TPS552872

#########################################
#              Minimum Vin              #
#########################################

V_UVLO = 1.23

R2 = 100e3
R1 = 100e3

Vin_min = V_UVLO * (1 + (R1 / R2))

print(f'Minimum Vin (V): {Vin_min:.2f}')


#########################################
#          Switching Frequency          #
#########################################

R_FSW = 9.31e3

f_sw = (1000 / (0.05 * R_FSW + 35)) * 1e6

print(f'Switching Frequency (Mhz): {f_sw * 1e-6:.2f}')


#########################################
#             Output Voltage            #
#########################################

R_FBBT = 56.2e3
V_REF = 1.2
R_FBUP = 100e3

V_OUT = V_REF * (1 + (R_FBUP / R_FBBT))

print(f'Output Voltage (V): {V_OUT:.2f}')