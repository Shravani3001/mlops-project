import os
import yaml
processed_path = "data/processed/processed.txt"
model_path = "models/model.txt"
metrics_path = "metrics.txt"

os.makedirs("models", exist_ok=True)

with open(processed_path, "r") as f:
    data = f.read()

model_output = "Model trained on data:\n" + data

with open(model_path, "w") as f:
    f.write(model_output)

# Simple metric
with open(metrics_path, "w") as f:
    f.write(f"data_length: {len(data)}\n")

print("Training completed")
