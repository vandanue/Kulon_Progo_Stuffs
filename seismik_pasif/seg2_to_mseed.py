#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 13:12:51 2026

@author: vandanu
"""

from obspy import read, Stream
from pathlib import Path

# Path to directory
root_dir = Path('/media/vandanu/HDD/Project/Penelitian Tapanuli Selatan/01_processing/data/20260410_112710_S43')
mseed_dir = Path('/media/vandanu/HDD/Project/Penelitian Tapanuli Selatan/01_processing/mseed')
station = root_dir.name
raw = sorted(root_dir.rglob('*cont.0.seg2'))

# Read
st = read(raw[0], format="SEG2", unpack_headers=True)

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

station_name = root_dir.name.split('_', 2)[2]

three = Stream(traces=[x_comp,y_comp,z_comp])

# Write MiniSEED
output_file = f'{station_name}_3comps.mseed'
output_folder = Path(mseed_dir,output_file)

three.write(output_folder, format='MSEED')