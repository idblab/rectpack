from rectpack import *
import pandas as pd
import timeit as ti


def do_packing(bin_algo, pack_algo, sort_algo):
    # Create the packer instance
    packer = newPacker(
        mode=PackingMode.Offline,
        bin_algo=bin_algo,
        pack_algo=pack_algo,
        sort_algo=sort_algo,
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

    return packer


bin_algos = [
    ( PackingBin.BNF, "PackingBin.BNF" ),
    ( PackingBin.BFF, "PackingBin.BFF" ),
    ( PackingBin.BBF, "PackingBin.BBF" )
]

pack_algos = [
    ( MaxRectsBl, "MaxRectsBl" ),
    ( MaxRectsBssf, "MaxRectsBssf" ),
    ( MaxRectsBaf, "MaxRectsBaf" ),
    ( MaxRectsBlsf, "MaxRectsBlsf" ),
    ( SkylineBl, "SkylineBl" ),
    ( SkylineBlWm, "SkylineBlWm" ),
    ( SkylineMwf, "SkylineMwf" ),
    ( SkylineMwfl, "SkylineMwfl" ),
    ( SkylineMwfWm, "SkylineMwfWm" ),
    ( SkylineMwflWm, "SkylineMwflWm" ),
    ( GuillotineBssfSas, "GuillotineBssfSas" ),
    ( GuillotineBssfLas, "GuillotineBssfLas" ),
    ( GuillotineBssfSlas, "GuillotineBssfSlas" ),
    ( GuillotineBssfLlas, "GuillotineBssfLlas" ),
    ( GuillotineBssfMaxas, "GuillotineBssfMaxas" ),
    ( GuillotineBssfMinas, "GuillotineBssfMinas" ),
    ( GuillotineBlsfSas, "GuillotineBlsfSas" ),
    ( GuillotineBlsfLas, "GuillotineBlsfLas" ),
    ( GuillotineBlsfSlas, "GuillotineBlsfSlas" ),
    ( GuillotineBlsfLlas, "GuillotineBlsfLlas" ),
    ( GuillotineBlsfMaxas, "GuillotineBlsfMaxas" ),
    ( GuillotineBlsfMinas, "GuillotineBlsfMinas" ),
    ( GuillotineBafSas, "GuillotineBafSas" ),
    ( GuillotineBafLas, "GuillotineBafLas" ),
    ( GuillotineBafSlas, "GuillotineBafSlas" ),
    ( GuillotineBafLlas, "GuillotineBafLlas" ),
    ( GuillotineBafMaxas, "GuillotineBafMaxas" ),
    ( GuillotineBafMinas, "GuillotineBafMinas" )
]

sort_algos = [
    ( SORT_AREA, "SORT_AREA       " ),
    ( SORT_AREA_WEIGHT, "SORT_AREA_WEIGHT" )
]

data_sets = [
    "data/easy_set_1.csv",
    "data/easy_set_2.csv",
    "data/easy_set_3.csv",
    "data/easy_set_4.csv",
    "data/easy_set_5.csv",
    "data/easy_set_6.csv",
    "data/easy_set_7.csv",
    "data/easy_set_8.csv",
    "data/easy_set_9.csv",
    "data/easy_set_10.csv",
    "data/hard_set_1.csv",
    "data/hard_set_2.csv",
    "data/hard_set_3.csv",
    "data/hard_set_4.csv",
    "data/hard_set_5.csv",
    "data/hard_set_6.csv",
    "data/hard_set_7.csv",
    "data/hard_set_8.csv",
    "data/hard_set_9.csv",
    "data/hard_set_10.csv"
]


for pack_algo in pack_algos:
    for bin_algo in bin_algos:
        for data_set in data_sets:
            # Load the data set
            df = pd.read_csv(data_set, names=["seq", "width", "height", "weight"])

            rectangles = [(r[0], r[1], r[2], r[3]) for r in df.values]
            bins = [(b, 12, 4, 20) for b in range(1, 101)]

            for sort_algo in sort_algos:
                pack = do_packing(bin_algo[0], pack_algo[0], sort_algo[0])
                print("{}\t{}\t{}\t{}\t{}".format(pack_algo[1], bin_algo[1], data_set, sort_algo[1], len(pack.bin_list())))

