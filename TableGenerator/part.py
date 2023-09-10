import csv
from module.part import Part

def partTableGenerator(partList:[Part]):
    with open("./output/part.csv", "w", encoding="utf-8") as f:
        csv_writer = csv.writer(f)
        # 表头
        csv_writer.writerow(["name", "centers", "content", "src"])
        # 数据
        for part in partList:
            csv_writer.writerow([part.name, part.centers, part.content, part.src])