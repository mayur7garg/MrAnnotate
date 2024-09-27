from pathlib import Path
import mrannotate as anon

print(f"Version: {anon.__version__}")

image_paths = list(Path("..", "..", "data", "image_label_ex").glob("*.jpg"))
labels = ["Abstract", "Harry Potter", "Spider man", "Space"]

il = anon.ImageLabeller(
    image_paths,
    labels
)

il.run(start_index = 2)

for p, l in il.img_labels.items():
    print(f"{p} : {l if l is None else il.labels[l]}")