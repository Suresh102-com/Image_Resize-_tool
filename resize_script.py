import os
from PIL import Image

# ----------------------
# SETTINGS
# ----------------------
input_folder = "images_input"      # Folder with original images
output_folder = "images_output"    # Folder to save processed images
target_size = (800, 600)           # New size (width, height)
output_format = "JPEG"             # JPEG, PNG, WEBP, etc.
quality = 85                       # Compression quality (0–100)

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Allowed file types
valid_exts = (".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tiff")

# ----------------------
# MAIN PROCESS
# ----------------------
for filename in os.listdir(input_folder):
    if not filename.lower().endswith(valid_exts):
        print(f"Skipped: {filename} (unsupported file type)")
        continue

    input_path = os.path.join(input_folder, filename)

    try:
        with Image.open(input_path) as img:
            # Resize the image (will stretch if aspect ratio differs)
            img = img.resize(target_size, Image.LANCZOS)

            # Convert to RGB if saving in JPEG or WEBP
            if output_format.upper() in ["JPEG", "WEBP"]:
                img = img.convert("RGB")

            # Build output path
            new_name = os.path.splitext(filename)[0] + f".{output_format.lower()}"
            output_path = os.path.join(output_folder, new_name)

            # Save the image
            img.save(output_path, output_format, quality=quality)

            print(f"✅ Processed: {filename} → {output_path}")

    except Exception as e:
        print(f"❌ Error with {filename}: {e}")

print("\n🎯 All done! Resized images are in:", output_folder)
