#pyinstaller --onefile --noconsole MrAnnotate.py
#https://www.pythonguis.com/tutorials/packaging-tkinter-applications-windows-pyinstaller/

import json
from pathlib import Path
import mrannotate as anon

image_paths = list(Path.cwd().glob("*.jpg")) + list(Path.cwd().glob("*.png"))

if len(image_paths) == 0:
    print("No images found in the current directory")
    exit()

il = anon.ImageLabeller(
    image_paths,
    []
)

il.run()

out_dict = {}

for img_path, label in il.img_labels.items():
    img_name = Path(img_path).name
    if label is not None:
        out_dict[img_name] = il.labels[label]
    else:
        out_dict[img_name] = None

with Path("MrAnnotate_ImageLabeller.json").open("w", encoding = "utf-8") as out:
    json.dump(out_dict, out)