from pathlib import Path

RAW_DIR = Path("data/raw")
IMG_EXTS = {".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff", ".webp"}

def is_image_or_symlink(p: Path) -> bool:
    return (p.is_file() or p.is_symlink()) and p.suffix.lower() in IMG_EXTS and not p.name.startswith(".")

def count_in_dir(d: Path) -> int:
    return sum(1 for p in d.rglob("*") if is_image_or_symlink(p))

def main():
    if not RAW_DIR.exists():
        print(f"ERROR: {RAW_DIR} not found. Run this from the project root.")
        return

    datasets = sorted([p for p in RAW_DIR.iterdir() if p.is_dir()], key=lambda p: p.name.lower())

    print("DATASET STATISTICS (counts of image files)")
    print(f"Root: {RAW_DIR.resolve()}\n")

    grand_total = 0

    for ds in datasets:
        print(f"=== {ds.name} ===")
        ds_total = 0

        for split in ["train", "val", "test"]:
            split_dir = ds / split
            if not split_dir.exists():
                print(f"- {split}: MISSING\n")
                continue

            classes = sorted([p for p in split_dir.iterdir() if p.is_dir()], key=lambda p: p.name.lower())

            split_total = 0
            print(f"- {split}:")

            for cls in classes:
                n = count_in_dir(cls)
                split_total += n
                print(f"  - {cls.name}: {n}")

            print(f"  split total: {split_total}\n")
            ds_total += split_total

        print(f"dataset total: {ds_total}\n")
        grand_total += ds_total

    print(f"GRAND TOTAL (all datasets): {grand_total}")

if __name__ == "__main__":
    main()