import os

# Get project root (one level above src/)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

processed_path = os.path.join(BASE_DIR, "data", "processed", "processed.txt")
model_path = os.path.join(BASE_DIR, "models", "model.txt")

# Ensure models directory exists
os.makedirs(os.path.dirname(model_path), exist_ok=True)

# Read processed data
with open(processed_path, "r") as f:
    data = f.read()

# Simulate training
model_output = "Model trained on data:\n" + data

# Save model
with open(model_path, "w") as f:
    f.write(model_output)

print("Training completed")