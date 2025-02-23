from pathlib import Path
import shutil

def main():
    for f in Path(".").glob("*.md"):
        print(f)

        new_d = f.parent / f.with_suffix("").name
        print(">>", new_d)
        new_d.mkdir(parents=True, exist_ok=True)

        shutil.move(f, new_d / "index.md")

if __name__ == "__main__":
    main()
