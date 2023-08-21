lines = open(r".\dgproperties.cfg", "r").readlines()
for line in lines:
    line.replace(r"\n", "")
    print(line)