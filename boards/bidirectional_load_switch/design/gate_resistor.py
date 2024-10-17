R_NMOS = 5.1
R_OH = 9.5
R_OL = 0.4

vcc = 15
vgdf = 0

rg_on = 5
rg_off = 5

rg_fet_int = 4.7

def parallel(r1, r2):
    return 1 / ((1 / r1) + (1 / r2))

I_OH = min(4.5, (vcc-vgdf) / (parallel(R_NMOS, R_OH) + rg_on + rg_fet_int))

I_OL = min(5.3, (vcc-vgdf) / (R_OL + rg_off + rg_fet_int))

print(f'{I_OH=:.2f}')
print(f'{I_OL=:.2f}')
