from pathlib import Path
import csv

data = []

for file in Path(".").glob("vs*.dat"):
    station = file.stem.split("_")[-1]

    for line in open(file):
        if line.startswith("Vs30"):
            vs30 = float(line.split()[1])
            data.append([station, vs30])
            break

data.sort(key=lambda x: int(x[0][1:]))

with open("vs30.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Station", "Vs30"])
    writer.writerows(data)
