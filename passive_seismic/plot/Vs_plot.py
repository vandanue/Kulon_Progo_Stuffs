# Generated from: Vs_plot.ipynb
# Converted at: 2026-04-16T22:37:11.707Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# #### Vs Plot
# Author: Annora Vandanu Erlangga


import numpy as np
import matplotlib.pyplot as plt
import os

filename = r"/media/vandanu/HDD/00_College/Asdos/Kulon_Progo/passive_seismic/inverse/vs_S6.dat"
stat = os.path.splitext(os.path.basename(filename))[0].split('_')[1]

with open(filename, "r") as file:
    for line in file:
        line = line.strip()  
        if "value=" in line:
            value = line.split("value=")[-1].strip()
            print(f"Misfit value: {value}")

# Read .dat file from dinver
def read_vs_data(filename): 
    vs, depth = [], []

    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            max_depth = 30  # hard coded to input depth here
            if len(parts) == 2:
                try:
                    v = float(parts[0])
                    d = float(parts[1]) if parts[1].lower() != 'inf' else max_depth
                    vs.append(v)
                    depth.append(d)
                except ValueError:
                    continue

    return np.array(vs), np.array(depth)

# Read file and then plot
vs, depth = read_vs_data(filename)

plt.figure(figsize=(4, 12))
plt.plot(vs, depth, 'r-', linewidth=3)
plt.gca().invert_yaxis()
#plt.xlim(0,2300)
plt.xlabel("Shear wave velocity (m/s)")
plt.ylabel("Depth (m)")
plt.title(f"{stat} $V_s$ Profile", fontsize=20)
plt.grid()
plt.savefig(f"{stat}_vs.png")
plt.show()
