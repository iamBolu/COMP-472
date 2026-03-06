from pathlib import Path
import hashlib

ROOT = Path("data/raw/miracle9to9")
IMG_EXTS = {".jpg",".jpeg",".png",".bmp",".tif",".tiff",".webp"}

def sha1(path: Path, chunk=1024*1024) -> str:
    h = hashlib.sha1()
    with path.open("rb") as f:
        while True:
            b = f.read(chunk)
            if not b:
                break
            h.update(b)
    return h.hexdigest()

def get_hashes(split: str):
    base = ROOT / split
    files = [f for f in base.rglob("*") if f.is_file() and f.suffix.lower() in IMG_EXTS]
    hashes = set()
    print(f"{split}: found {len(files)} image files")
    for i, f in enumerate(files, 1):
        hashes.add(sha1(f))
        if i % 2000 == 0:
            print(f"{split}: hashed {i}/{len(files)}")
    print(f"{split}: unique hashes {len(hashes)}")
    return hashes

def main():
    print("Starting miracle9to9 REAL leakage check (content hashes)...")
    if not ROOT.exists():
        print("ERROR: folder not found:", ROOT.resolve())
        return

    tr = get_hashes("train")
    va = get_hashes("val")
    te = get_hashes("test")

    print("\nINTERSECTIONS (REAL duplicates by content)")
    print("train ∩ val :", len(tr & va))
    print("train ∩ test:", len(tr & te))
    print("val ∩ test  :", len(va & te))
    print("\nDone.")

if __name__ == "__main__":
    main()
