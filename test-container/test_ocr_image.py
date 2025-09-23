
import os
import glob
from PIL import Image
import pytesseract
import json

# Delete old output files before running tests
for f in glob.glob("ocr_output_*.json"):
    try:
        os.remove(f)
        print(f"[INFO] Deleted old output file: {f}")
    except Exception as e:
        print(f"[WARN] Could not delete {f}: {e}")

# Test 1: Real-world image
real_image_path = 'Invoice Bill2.jpg'
if not os.path.exists(real_image_path):
    print(f"[FAIL] Test image '{real_image_path}' not found.")
    exit(1)
img = Image.open(real_image_path)
extracted = pytesseract.image_to_string(img)
print(f"[TEST] OCR extracted from real image:\n{extracted.strip()}")
output = {
    "image_file": real_image_path,
    "ocr_text": extracted.strip().splitlines()
}
with open("ocr_output_real.json", "w") as f:
    json.dump(output, f, indent=2, ensure_ascii=False)
print("[INFO] OCR result saved to ocr_output_real.json (pretty-printed lines).")

# Test 2: Synthetic test image
test_image_path = 'test_ocr_image.png'
if not os.path.exists(test_image_path):
    print(f"[FAIL] Test image '{test_image_path}' not found.")
    exit(1)
img2 = Image.open(test_image_path)
extracted2 = pytesseract.image_to_string(img2)
print(f"[TEST] OCR extracted from test image:\n{extracted2.strip()}")
output2 = {
    "image_file": test_image_path,
    "ocr_text": extracted2.strip().splitlines()
}
with open("ocr_output_test.json", "w") as f:
    json.dump(output2, f, indent=2, ensure_ascii=False)
print("[INFO] OCR result saved to ocr_output_test.json (pretty-printed lines).")

print("[INFO] OCR test completed on both images.")
exit(0)

# Use pytesseract to extract text from the image
