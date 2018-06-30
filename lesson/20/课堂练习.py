from pathlib import Path
import csv

path = 'G:/test.csv'
p = Path(path)
if not p.parent.exists():
    p.parent.mkdir(parents=True)

s = """\
1,tom,20,
2,jerry,15,
3,,,
"""

line1 = [1, "tom", 20, '']
line2 = [2, "tom", 20, '']
line3 = [line1, line2]

with open(path, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(line1)
    writer.writerow(line2)
    writer.writerows(line3)

with open(path) as f:
    reader = csv.reader(f)
    for line in reader:
        if line:
            print(line)


# with open('G:/test.csv', 'w') as f:
#     for line in s.splitlines():
#         f.write(line + '\n')
