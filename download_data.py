import kagglehub
import shutil
import os

# Download latest version of the dataset
path = kagglehub.dataset_download("ekkykharismadhany/csecicids2018-cleaned")

print("Dataset downloaded to:", path)

# Move files into ./data/ folder
target_dir = "data"
os.makedirs(target_dir, exist_ok=True)

for file_name in os.listdir(path):
    full_path = os.path.join(path, file_name)
    if os.path.isfile(full_path):
        shutil.copy(full_path, os.path.join(target_dir, file_name))
        print(f"Copied {file_name} -> {target_dir}/")
