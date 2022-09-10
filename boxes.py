
import re
from collections import defaultdict


with open("input.txt", "r") as f:
    boxRules = f.readlines()

boxes = defaultdict(dict)

for rule in boxRules:
    color = re.match(r'(.+?) boxes contain', rule)[1]
    if(re.match(r'(.+?) contain no other boxes', rule)):
        boxes[color] = {}
    else:
        for num, innercolor in re.findall(r'(\d+) (\w+ \w+)', rule):
            boxes[color][" ".join([innercolor])] = int(num)
       
def canContainBox(searchColor, colorInBox):
    if searchColor in str(boxes[colorInBox]):
        return True
    return any([canContainBox(searchColor, b) for b in boxes[colorInBox]])

def boxesReqiredInside(color):
    return sum([boxes[color][b] * (1 + boxesReqiredInside(b)) for b in boxes[color]])


howManyBoxesCointan = sum([canContainBox("shiny gold", box) for box in boxes])
print(howManyBoxesCointan)

requiredBoxesShineyGold = boxesReqiredInside("shiny gold")
print(requiredBoxesShineyGold)