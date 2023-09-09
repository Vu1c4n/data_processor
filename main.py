from pathlib import Path

from module.center import Center
from module.part import Part

from ListGenerator import centerListGenerator as clg
from ListGenerator import  partListGenerator as plg

import csv

from TableGenerator.part import partTableGenerator as ptg
from TableGenerator.center import centerTableGenerator as ctg


if __name__ == "__main__":
    dataPath = Path.cwd() / "data"
    partList:[Part] = plg.getPartList(dataPath)
    centerList:[Center] = clg.getCenterList(dataPath)
    ptg(partList)
    ctg(centerList)
