import csv
from pprint import pprint

# url = 'https://raw.githubusercontent.com/jimmycrequer/roth-2019/master/neo4j/data/radicals.csv'
url = "s1_radicals_raw.csv"

with open(url) as file:
    csv_reader = csv.reader(file, delimiter=",")
    data = [row for row in csv_reader][1:]

    kanji_to_radical = {}
    radical_to_meaning = {}

    for row in data:
        radical, meaning, kanji_list = row

        for kanji in kanji_list:
            if kanji in kanji_to_radical:
                kanji_to_radical[kanji].append(radical)
            else:
                kanji_to_radical[kanji] = [radical]

        radical_to_meaning[radical] = meaning

consolidated_data = []
for kanji, radicals in kanji_to_radical.items():
    row = {"kanji": kanji, "radicals": ":".join(radicals)}
    consolidated_data.append(row)


with open("s3_radicals_output.csv", mode="w") as file:
    fieldnames = ["kanji", "radicals"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(consolidated_data)
