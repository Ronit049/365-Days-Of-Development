
import subprocess
from pathlib import Path

repo = Path(__file__).resolve().parent

# Each entry should correspond to a real learning or coding update.
tasks = [
    ("Day 01: Add Python basics notes", "Python/day-01.md"),
    ("Day 02: Add variables and data types", "Python/day-02.md"),
    ("Day 03: Add conditional statements", "Python/day-03.md"),
    ("Day 04: Add loops practice", "Python/day-04.md"),
    ("Day 05: Add functions notes", "Python/day-05.md"),
]

for title, filename in tasks:
    file_path = repo / filename

    if not file_path.exists():
        print(f"Skipping missing file: {filename}")
        continue

    subprocess.run(["git", "add", filename], cwd=repo, check=True)

    result = subprocess.run(
        ["git", "diff", "--cached", "--quiet"],
        cwd=repo
    )

    if result.returncode == 0:
        print(f"Skipping unchanged file: {filename}")
        continue

    subprocess.run(
        ["git", "commit", "-m", title],
        cwd=repo,
        check=True
    )

print("Finished processing commit tasks!")
