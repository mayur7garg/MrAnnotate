from pathlib import Path

from mrannotate import ImageLabeller

image_paths = list(Path("data", "image_label_ex").glob("*.jpg"))
labels = ["Abstract", "Harry Potter", "Spider man", "Space"]

il = ImageLabeller(
    image_paths,
    labels
)

il.run()

for i in range(len(image_paths)):
    print(f"{image_paths[i].stem} - {labels[il.img_labels[i]]}")