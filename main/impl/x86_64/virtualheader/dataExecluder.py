_NAME = str(open(r".\name.head", "r").readlines()[0]).replace("[", "").replace("]", "")
_VOLUME = str(open(r".\volume.head", "r").readlines()[0]).replace("[", "").replace("]", "")
_CFG = open("dgproperties.cfg", "w").write(
f"""
volume = {_VOLUME}
name = {_NAME}
volumeOS = 10
"""
)