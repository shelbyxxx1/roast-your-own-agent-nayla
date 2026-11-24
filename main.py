import os
import sys
from pathlib import Path


ROAST = "Nayla grades her own work top 15, then the server ranks it 1,800th of 9,229 — a legend in her own terminal."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(output_dir, exist_ok=True)
        output_path = Path(output_dir) / "entry.txt"
        output_path.write_text(ROAST + "\n", encoding="utf-8")
    except Exception as error:
        print(error, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
