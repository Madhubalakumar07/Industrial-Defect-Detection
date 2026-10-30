
import json
import os
from PIL import Image
import matplotlib.pyplot as plt

BASE_DIR = "dataset/mvtec-ad"

with open(os.path.join(BASE_DIR, "samples.json"), "r") as f:
    data = json.load(f)

samples = data["samples"]

# Select metal_nut images
metal_nut_samples = [
    sample for sample in samples
    if sample["category"]["label"] == "metal_nut"
]

# Select normal training images
normal_samples = [
    sample for sample in metal_nut_samples
    if sample["defect"]["label"] == "good"
    and sample["split"] == "train"
]

# Select defective test images
defect_samples = [
    sample for sample in metal_nut_samples
    if sample["defect"]["label"] != "good"
]

print("Normal training images:", len(normal_samples))
print("Defective testing images:", len(defect_samples))

# Display sample images
fig, axes = plt.subplots(2, 4, figsize=(12, 6))

for i in range(4):
    sample = normal_samples[i]
    image_path = os.path.join(BASE_DIR, sample["filepath"])

    image = Image.open(image_path).convert("RGB")

    axes[0, i].imshow(image)
    axes[0, i].set_title("Normal")
    axes[0, i].axis("off")

for i in range(4):
    sample = defect_samples[i]
    image_path = os.path.join(BASE_DIR, sample["filepath"])

    image = Image.open(image_path).convert("RGB")

    axes[1, i].imshow(image)
    axes[1, i].set_title(sample["defect"]["label"])
    axes[1, i].axis("off")

plt.tight_layout()
plt.show()
