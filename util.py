from pathlib import Path
from module.center import Center
from module.part import Part


class FileProcessor:
    # APIs
    def getPartList(self, partPath:Path) ->[Part]:
        partList = []
        partNameList = self.__getSectionList(partPath)
        for partName in partNameList:
            part = Part(name = partName)
            partList.append(part)
        return partList
    
    def getCenterList(self, centerPath:Path) ->[Center]:
        centerList = []
        centerNameList = self.__getSectionList(centerPath)
        for centerName in centerNameList:
            center = Center(name = centerName)
            centerList.append(center)
        return centerList

    def getNameList(self, sectionPath:Path) -> [str]:
        return self.__getSectionList(sectionPath)

    def getIntro(self, sectionPath: Path) ->str:
        intro = str()
        for path in sectionPath.iterdir():
            if path.suffix == ".txt":
                intro = self.__readTxt(path)
                break
        return intro

    # Helper Methods
    def __readTxt(self, txtPath: Path) -> str:
        with open(txtPath, "r", encoding="utf-8") as file:
            content = file.read()
        return content
    
    def __getSectionList(self, sectionPath: Path) -> [str]:
        sectionList = []
        for path in sectionPath.iterdir():
            if path.is_file():
                continue
            sectionList.append(path.name)
        return sectionList