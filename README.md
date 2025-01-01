# Scraper

A Python scraper script to download websites as PDFs and then merge them into a single PDF.
Useful for downloading documentation and feeding it into a notebookLM.

## Features

-   Download a webpage as a PDF by providing a URL.
-   Process multiple URLs from a file.
-   Support for sections in the URL file.
-   Interactive mode to enter URLs one by one.
-   Automatically generates filenames based on the webpage title.
-   Option to merge all downloaded PDFs into a single PDF.
-   Option to run OCR.

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/carrotsmuggler/Scraper-Merger.git
    cd Scraper-Merger
    chmod +x scraper
    ```

2. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Requirements

-   Python 3.x
-   `pdfkit`
-   `requests`
-   `beautifulsoup4`
-   `PyPDF2`
-   `pytesseract`
-   `pdf2image`
-   `reportlab`
-   `pymupdf`

## Usage

### Command Line Options

-   `-h`, `--help`: Show the help message and exit.
-   `--ocr`: Run OCR on the merged PDFs.
-   `--ocr-only`: Skips the scraping and only runs the OCR extractor script.

### Running the Script

1. **Process a Single URL**

    ```sh
    ./scraper <URL>
    ```

    Example:

    ```sh
    ./scraper http://example.com
    ```

2. **Process Multiple URLs from a File**

    ```sh
    ./scraper <file_with_urls>
    ```

    Example:

    ```sh
    ./scraper urls.txt
    ```

    The `urls.txt` file can contain one URL per line or sections with URLs. If sections are used, each section should start with a line beginning with `#`, followed by the section name. URLs under each section will be processed and merged into separate PDF files.

    Example of a file with sections:

    ```
    # Section 1
    http://example.com
    http://example.org

    # Section 2
    http://example.net
    http://example.edu
    ```

    In this example, the script will create `Section_1.pdf` from the URLs in Section 1 and `Section_2.pdf` from the URLs in Section 2.

3. **Interactive Mode**

    If no URL or file is provided, the script will prompt you to enter URLs interactively.

    ```sh
    ./scraper
    ```

    Enter URLs one by one. Type `quit` to finish and prompt for merging.

### Merging PDFs

After processing the URLs, you will be prompted to merge the downloaded PDFs into a single PDF.

```sh
Merge files? (Y/N):
```

### Running OCR

Some pdfs are downloaded as images, with no searchable text. This can be an issue for LLMs and notebooks. To solve this, you can object character recognition (OCR) with tesseract to convert the pdfs to images.

To run OCR, use the `--ocr` flag. This will convert all the merged files into text and save them as pdfs. Can look meddy, but is searchable text. OCR restuls are saved in the `ocr-extracted` folder.

```sh
./scraper urls.txt --ocr
```

If you have already run the scraper and later decide to run ocr as well, no need to scrape again. Using the `ocr-only` flag lets you run just the ocr part. This converts the passed in files to ocr pdfs.

You can either pass in the list of file paths, or a directory and all the pdf files in the top level of the directory will be processed with OCR.

```sh
./scraper --ocr-only result.pdf
```

Or,

```sh
./scraper --ocr-only ./scraper-dump
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
