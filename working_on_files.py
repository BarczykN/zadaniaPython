import os
from PIL import Image
import math
import numpy as np
import random


def tree(root):
    for root, files, dirs in os.walk(root):
        for name in files:
            print(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))
def main():


# ========================================PLIKI=============================================================
    files = os.listdir('dev')
    print(len(files))

    tree(".")

    for i in range(1, 3):
        im = Image.open('dev/foto' + str(i) + '.jpg')
        im.save('dev/foto' + str(i) + '.png')


# -------------------------------------------Working on text---------------------------------------
    dictionary ={
    " i ": " oraz ",
    "oraz": "ii",
    " nigdy ": " prawie nigdy ",
    " dlaczego ": " czemu "
    }

    with open('textStream.txt', encoding="utf8") as file:
        lines = file.read()
        print(str(lines).replace("oraz", dictionary["oraz"]).replace(" i ", dictionary[" i "])
        .replace(" nigdy ", dictionary[" nigdy "])
        .replace(" dlaczego ", dictionary[" dlaczego "])
        .replace(" ii ", " i "))



if __name__ == '__main__':
    main()