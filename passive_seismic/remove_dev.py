import os
import glob

def remove_deviation(input_file, output_file=None):
    # Input files
    if output_file is None:
        base, ext = os.path.splitext(input_file)
        output_file = f"edit_{base}{ext}"

    with open(input_file, "r") as fin, open(output_file, "w") as fout:
        for line in fin:
            # Preserve header
            if line.startswith("#"):
                fout.write(line)
                continue

            # Split tab-delimited data
            parts = line.strip().split("\t")

            # Keep Average columns
            if len(parts) >= 2:
                fout.write(f"{parts[0]}\t{parts[1]}\n")

    print(f"Saved: {output_file}")


# Process all .hv files in current folder
for hvfile in glob.glob("*.hv"):
    remove_deviation(hvfile)
