import os

# Get project root (one level above src/)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

raw_path = os.path.join(BASE_DIR, "data", "raw", "demo.txt")
processed_path = os.path.join(BASE_DIR, "data", "processed", "processed.txt")

os.makedirs(os.path.dirname(processed_path), exist_ok=True)

with open(raw_path, "r") as f:
    data = f.read()

processed_data = data.upper()   # simple processing

with open(processed_path, "w") as f:
    f.write(processed_data)

print("Preprocessing completed")