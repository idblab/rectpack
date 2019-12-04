from rectpack import *
import pandas as pd
import timeit as ti


# Load the data set
df = pd.read_csv("data/easy_set_1.csv", names=["seq", "width", "height", "weight"])

rectangles = [(r[0], r[1], r[2], r[3]) for r in df.values]
bins = [(b, 12, 4, 20) for b in range(1, 101)]


# Create the packer instance
packer = newPacker(
    pack_algo=MaxRectsBaf,
    bin_algo=PackingBin.BBF,
    sort_algo=SORT_AREA_WEIGHT,
    rotation=1
)


# Add the rectangles to packing queue
for r in rectangles:
    packer.add_rect(r[1], r[2], r[3], rid="Cargo #" + str(r[0]))


# Add the bins where the rectangles will be placed
for b in bins:
    packer.add_bin(b[1], b[2], b[3], bid="Container #" + str(b[0]))

# Run the packing
packer.pack()


# Show the results
for abin in packer:
    print("\n" + abin.bid + "\tused_area: " + str(abin.used_area() * 100 / 48) + "\tused_weight: " + str(abin.used_weight()))
    for rect in abin:
        print(rect.rid + "\t(" + str(rect.x) + ", " + str(rect.y) + ") { " + str(rect.width) + " x " + str(rect.height) + " | " + str(rect.weight) + " tons }")

