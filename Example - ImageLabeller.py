from pathlib import Path
import mrannotate as anon

print(anon.__version__)

image_paths = list(Path("data", "image_label_ex").glob("*.jpg"))
labels = ["Abstract", "Harry Potter", "Spider man", "Space"]

il = anon.ImageLabeller(
    image_paths,
    labels
)

il.run()

for i in range(len(image_paths)):
    print(f"{image_paths[i].stem} - {labels[il.img_labels[i]]}")