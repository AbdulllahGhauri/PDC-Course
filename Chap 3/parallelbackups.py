import multiprocessing
import shutil
import os

# Create sample files if they don't exist
def create_test_files():
    for i in range(1, 4):
        filename = f"data{i}.txt"
        if not os.path.exists(filename):
            with open(filename, "w") as f:
                f.write(f"This is the content of {filename}\n")
    print("✅ Test files created.")

# Function to back up a file
def backup_file(filename):
    dest = "backup_" + filename
    try:
        shutil.copy(filename, dest)
        print(f"📁 {filename} backed up as {dest}")
    except FileNotFoundError:
        print(f"⚠️ {filename} not found, skipping...")

if __name__ == "__main__":
    create_test_files()  # Ensure files exist before backup

    files = [f"data{i}.txt" for i in range(1, 4)]  # List of files
    with multiprocessing.Pool() as pool:
        pool.map(backup_file, files)

    print("✅ All backup operations completed successfully.")
