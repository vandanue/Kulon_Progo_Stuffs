#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 23:22:07 2026

@author: vandanu
"""

from obspy import read, Stream
from pathlib import Path

# Path to directory
root_dir = Path(r"/media/vandanu/HDD/00_College/Asdos/Kulon_Progo/data/passive/K5/20260418_075235_S17")
station = root_dir.name
raw = sorted(root_dir.rglob('*cont.0.seg2'))

print(f'Total files: {len(raw)}')

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
    
x_comp.stats.channel = 'EHE'; x_comp.stats.network = station
y_comp.stats.channel = 'EHN'; y_comp.stats.network = station
z_comp.stats.channel = 'EHZ'; z_comp.stats.network = station

three = Stream(traces=[x_comp,y_comp,z_comp])

# Plot
three.plot()
