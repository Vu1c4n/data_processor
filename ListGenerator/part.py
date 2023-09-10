from pathlib import Path

from module.part import Part

from util import FileProcessor

def getPartList(dataPath:Path) -> [Part]:
    fp = FileProcessor()
    partList = fp.getPartList(dataPath)

    for part in partList:
        partPath = Path(dataPath / part.name)
        # centers
        part.centers = fp.getNameList(partPath)
        # content
        part.content = fp.getIntro(partPath)

    return partList