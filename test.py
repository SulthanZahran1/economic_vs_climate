import xarray as xr
import matplotlib.pyplot as plt

# Load the NetCDF file
data = xr.open_dataset('raw_data/gistemp1200_GHCNv4_ERSSTv5.nc')
# Assuming the variable name is 'temperature' and you want the data for a specific timestamp

