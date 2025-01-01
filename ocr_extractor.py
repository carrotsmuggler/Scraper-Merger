#!/usr/bin/env python3
import pytesseract
from pdf2image import convert_from_path
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
import sys
from concurrent.futures import ProcessPoolExecutor
import textwrap

# Specify the Tesseract executable path if it's not in your PATH
pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"


def ocr_image(image):
    try:
        return pytesseract.image_to_string(image)
    except Exception as e:
        print(f"An error occurred during OCR: {e}")
        return ""


def save_pdf_content_as_text_pdf(input_path, output_path):
    print(f"!!!! Running OCR on {input_path}")
    try:
        text = ""
        images = convert_from_path(input_path)
        with ProcessPoolExecutor() as executor:
            futures = [executor.submit(ocr_image, image) for image in images]
            for future in futures:
                text += future.result()
                text += "\n"
        # Save text as PDF
        c = canvas.Canvas(output_path, pagesize=letter)
        width, height = letter
        lines = text.split("\n")
        margin = 40
        line_height = 14
        max_line_width = width - 2 * margin
        y = height - margin
        for line in lines:
            wrapped_lines = textwrap.wrap(
                line, width=int(max_line_width / 7)
            )  # Adjust the width factor as needed
            for wrapped_line in wrapped_lines:
                if y < margin:
                    c.showPage()
                    y = height - margin
                c.drawString(margin, y, wrapped_line)
                y -= line_height
        c.save()
        print(f"++++ Saved OCR result as PDF: {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


def run_ocr(paths):
    files_to_process = []
    if len(paths) == 1 and os.path.isdir(paths[0]):
        for file in os.listdir(paths[0]):
            file_path = os.path.join(paths[0], file)
            if os.path.isfile(file_path) and file.lower().endswith(".pdf"):
                files_to_process.append(file_path)
    else:
        for path in paths:
            if os.path.isfile(path) and path.lower().endswith(".pdf"):
                files_to_process.append(path)
            else:
                print(f"File {path} is not a PDF or does not exist.")

    if files_to_process:
        # Create the ocr_extracted directory inside the provided directory
        output_dir = os.path.join(os.path.dirname(files_to_process[0]), "ocr_extracted")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        for file_path in files_to_process:
            output_path = os.path.join(
                output_dir,
                os.path.splitext(os.path.basename(file_path))[0] + "_extracted.pdf",
            )
            save_pdf_content_as_text_pdf(file_path, output_path)


# Example usage
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(
            "Usage: python ocr_extractor <path_to_pdf_or_directory> [additional_paths...]"
        )
    else:
        run_ocr(sys.argv[1:])
