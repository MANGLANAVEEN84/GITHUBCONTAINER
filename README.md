
# GITHUBCONTAINER

## Features Added in `OCRADDED` Branch

- Latest Python and Node.js installed in the container
- Python dependencies for image processing and OCR:
	- Pillow (image manipulation)
	- pytesseract (OCR)
- System dependency: tesseract-ocr (for OCR)
- Frontend tools: yarn, vite, create-react-app, @angular/cli, @vue/cli
- Automated test scripts for:
	- OCR on real-world and synthetic images
	- Output saved as pretty-printed JSON files
- All test scripts, images, and outputs organized in `test-container` folder
- Test script deletes old output files before each run for clean results


## Automated Testing Features

- The test script (`test_ocr_image.py`) automatically:
  - Deletes any previous output JSON files before each run, ensuring only fresh results are present.
  - Processes both a real-world invoice image and a synthetic test image in one run.
  - Saves OCR results for each image in separate, clearly named JSON files for easy review.
  - Outputs are pretty-printed and structured for direct use in Python or other tools.
- All test scripts, images, and outputs are kept in the `test-container` folder for clarity and reproducibility.
- The workflow is designed for easy extension—add more test images or scripts as needed.

## How to Run OCR Tests

1. Place your test images in the `test-container` folder.
2. Run the test script in the container:
	```bash
	docker run --rm -v $(pwd):/app -w /app/test-container codespec-python-ocr-auto python3 test_ocr_image.py
	```
3. Check the output JSON files (`ocr_output_real.json`, `ocr_output_test.json`) in the `test-container` folder.

## Requirements

See `requirements.txt` for all Python dependencies.

## Notes

- The container is optimized for fast rebuilds and easy future dependency installation.
- All test assets are kept in `test-container` for clarity and reproducibility.
