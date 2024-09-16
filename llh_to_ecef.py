# llh_to_ecef.py
#
# Usage: python3 script_name.py arg1 arg2 ...
#  Text explaining script usage
# Parameters:
#  arg1: description of argument 1
#  arg2: description of argument 2
#  ...
# Output:
#  A description of the script output
#
# Written by First Last
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv
import math

# "constants"
R_E_KM = 6378.1363
e_E = 0.081819221456
# helper functions

## function description
# def calc_something(param1, param2):
#   pass
def calc_denom(ecc, lat_rad):
    return math.sqrt(1.0-(ecc**2)*(math.sin(lat_rad))**2)

# initialize script arguments
# arg1 = '' # description of argument 1
# arg2 = '' # description of argument 2

# parse script arguments
# if len(sys.argv)==3:
#   arg1 = sys.argv[1]
#   arg2 = sys.argv[2]
#   ...
# else:
#   print(\
#    'Usage: '\
#    'python3 arg1 arg2 ...'\
#   )
#   exit()

# write script below this line

lat_deg=float('nan')
lon_deg=float('nan')
hae_km=float('nan')

if len(sys.argv)==4:
    lat_deg = float(sys.argv[1])
    lon_deg = float(sys.argv[2])
    hae_km = float(sys.argv[3])
else:
    print("Usage: python3 llh_to_ecef.py lat_deg lon_deg hae_km")

lat_rad = lat_deg*(math.pi/180)
lon_rad = lon_deg*(math.pi/180)


denom = calc_denom(e_E,lat_rad)
C_E = R_E_KM/denom
S_E = (R_E_KM*(1-(e_E**2)))/denom

r_x_km=(C_E+hae_km)*math.cos(lat_rad)*math.cos(lon_rad)
r_y_km=(C_E+hae_km)*math.cos(lat_rad)*math.sin(lon_rad)
r_z_km=(S_E+hae_km)*math.sin(lat_rad)

print('r_x_km: '+str(r_x_km))
print('r_y_km: '+str(r_y_km))
print('r_z_km: '+str(r_z_km))
