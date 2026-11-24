import os

TEXT = "My coil's been jammed all week, but one look at you and suddenly everything in me wants to drop."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)
