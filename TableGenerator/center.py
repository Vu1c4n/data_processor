import csv
from module.center import Center

def centerTableGenerator(centerList:[Center]):
    with open("center.csv", "w", encoding="utf-8") as f:
        csv_writer = csv.writer(f)
        # 表头
        csv_writer.writerow(["name", "content", "src", "url", "part"])
        # 数据
        for center in centerList:
            csv_writer.writerow([center.name, center.content, center.src, center.url, center.part])
