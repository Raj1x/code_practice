from pathlib import Path

class DiskInspector:
  def __init__(self, lol):
    self.lol = Path(lol)
  def FileShit(self, extension):
    box = []
    for thing in self.lol.iterdir():
      if thing.is_file():
        if thing.suffix == extension:
          box.append(thing)
    return box
#You can select path in the inspector down below
Inspector = DiskInspector(".")
#Here u can change the type of shi that the script will look for in the path you chosed
result = Inspector.FileShit(".py")
print(result)

          
