# Kurdish-OCR

A Kurdish OCR tool for the Badini and Sorani dialects, built on Tesseract and OpenCV with a simple desktop interface.

It's still an early prototype, so expect rough edges.

## What it does

- Reads Kurdish text from images and marks each detected word.
- Scans photographed documents: it finds the page, straightens it, then reads the text.

## Setup

You'll need Windows, Python 3.9 and [Tesseract 5](https://github.com/UB-Mannheim/tesseract/wiki) installed in `C:\Program Files\Tesseract-OCR`. You'll also need the `k_badini.traineddata` language file in Tesseract's `tessdata` folder.

```bash
pip install numpy opencv-python pytesseract imutils
python Main.py
```

Pick an image or a document, and the recognized text is printed to the console. You can try it with `4.png`.

## Notes

- The image you pick needs to be in the project folder.
- On macOS or Linux, change the Tesseract path in `Wordim.py` and `scan.py`.

## Contact

Questions or ideas? Open an issue or email rayanchicho@gmail.com.
