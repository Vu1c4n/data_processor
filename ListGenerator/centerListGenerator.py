from pathlib import Path

from module import *

from util import FileProcessor

def getCenterList(dataPath:Path):
    fp = FileProcessor()
    partList = fp.getPartList(dataPath)
    rtnList = []
    for part in partList:
        partPath = Path(dataPath / part.name)
        centerList = fp.getCenterList(partPath)
        for center in centerList:
            centerPath = Path(partPath / center.name)
            # content
            center.content = fp.getIntro(centerPath)
            # part
            center.part = part.name
            rtnList.append(center)
    return rtnList
            