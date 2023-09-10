from pathlib import Path

from module.center import Center
from module.part import Part

from ListGenerator import center as clg
from ListGenerator import  part as plg

from TableGenerator.part import partTableGenerator as ptg
from TableGenerator.center import centerTableGenerator as ctg

from util import FileProcessor

picSuffixList = ['.jpg', '.jpeg', '.png']

def generateForm():
    dataPath = Path.cwd() / "data"
    partList:[Part] = plg.getPartList(dataPath)
    centerList:[Center] = clg.getCenterList(dataPath)
    ptg(partList)
    ctg(centerList)


def editPicName():
    dataPath = Path.cwd() / "data"
    fp = FileProcessor()
    partNameList:[str] = fp.getDirList(dataPath)
    for part in partNameList:
        partPath = dataPath / Path(part)
        picIndex = 1
        for path in partPath.iterdir():
            if path.is_file() & (path.suffix in picSuffixList):
                newName = part + "_" + str(picIndex) + ".jpg"
                newPath = partPath  /  Path(newName)
                picIndex += 1
                Path(path).replace(newPath)
