import os

TEXT = "My coil's been jammed for days, but one look at you and everything in me wants to drop."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)
