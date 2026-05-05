#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 13:12:51 2026

@author: vandanu
"""

from obspy import read, Stream
from pathlib import Path
import warnings
warnings.filterwarnings("ignore")

# Path to directory
root_dir = Path(r'/media/vandanu/HDD/00_College/Asdos/Kulon_Progo/data/passive/Day1_K7/20260415_073911_S2')
mseed_dir = Path(r'/media/vandanu/HDD/00_College/Asdos/Kulon_Progo/passive_seismic/mseed')

# Search all the continuous SEG files
raw = sorted(root_dir.rglob('*cont.0.seg2'))

station = root_dir.name
station_name = root_dir.name.split('_', 2)[2]

# Read
st = read(raw[0], format="SEG2", unpack_headers=True)

print(f'========== READING {len(raw)} FILES ==========')
print(f'STATION NAME:\t\t {station_name}')
print(f'START TIME:\t\t {st.stats.seg2.ACQUISITION_TIME}')
#print(f'LATITUDE:\t\t {st.stats.seg2.GPS_POSITION.split(' ')[0]}')
#print(f'LONGITUDE:\t\t {st.stats.seg2.GPS_POSITION.split(' ')[1]}')


x_comp = st[0]
y_comp = st[1]
z_comp = st[2]

for f in raw[1:]:
    st = read(f, format="SEG2", unpack_headers=True, checksize=False)
    
    x_comp += st[0]
    y_comp += st[1]
    z_comp += st[2]
    
x_comp.stats.channel = 'EHE'
y_comp.stats.channel = 'EHN'
z_comp.stats.channel = 'EHZ'

three = Stream(traces=[x_comp,y_comp,z_comp])

# Write MiniSEED
output_file = f'{station_name}_3comps.mseed'
output_folder = Path(mseed_dir,output_file)

three.write(output_folder, format='MSEED')
