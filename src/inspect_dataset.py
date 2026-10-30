
import json
from collections import Counter, defaultdict

# Load dataset metadata
with open("dataset/mvtec-ad/samples.json", "r") as f:
    data = json.load(f)

samples = data["samples"]

# Count images by category
category_counts = Counter()

# Count images by defect type
defect_counts = Counter()

# Count images by split
split_counts = Counter()

# Detailed category distribution
details = defaultdict(Counter)

for sample in samples:
    category = sample["category"]["label"]
    defect = sample["defect"]["label"]
    split = sample["split"]

    category_counts[category] += 1
    defect_counts[defect] += 1
    split_counts[split] += 1

    details[category][f"{split}_{defect}"] += 1

print("\nTOTAL IMAGES:", len(samples))

print("\nCATEGORY DISTRIBUTION:")
for category, count in sorted(category_counts.items()):
    print(f"{category:15} : {count}")

print("\nDEFECT DISTRIBUTION:")
for defect, count in sorted(defect_counts.items()):
    print(f"{defect:20} : {count}")

print("\nSPLIT DISTRIBUTION:")
for split, count in split_counts.items():
    print(f"{split:15} : {count}")

print("\nDETAILED CATEGORY DISTRIBUTION:")
for category, counts in sorted(details.items()):
    print(f"\n{category}")
    for label, count in sorted(counts.items()):
        print(f"  {label:25} : {count}")
