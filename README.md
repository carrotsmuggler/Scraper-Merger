# Scraper

A Python scraper script to download websites as PDFs and then merge them into a single PDF.
Useful for downloading documentation and feeding it into a notebookLM.

## Features

-   Download a webpage as a PDF by providing a URL.
-   Process multiple URLs from a file.
-   Interactive mode to enter URLs one by one.
-   Automatically generates filenames based on the webpage title.
-   Option to merge all downloaded PDFs into a single PDF.

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/scraper.git
    cd scraper
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

## Usage

### Command Line Options

-   `-h`, `--help`: Show the help message and exit.

### Running the Script

1. **Process a Single URL**

    ```sh
    ./scraper.py <URL>
    ```

    Example:

    ```sh
    ./scraper.py http://example.com
    ```

2. **Process Multiple URLs from a File**

    ```sh
    ./scraper.py <file_with_urls>
    ```

    Example:

    ```sh
    ./scraper.py urls.txt
    ```

    The `urls.txt` file should contain one URL per line.

3. **Interactive Mode**

    If no URL or file is provided, the script will prompt you to enter URLs interactively.

    ```sh
    ./scraper.py
    ```

    Enter URLs one by one. Type `quit` to finish and prompt for merging.

### Merging PDFs

After processing the URLs, you will be prompted to merge the downloaded PDFs into a single PDF.

```sh
Merge? (Y/N):
```

## Examples

1. **Download a single webpage as a PDF**:

    ```sh
    ./scraper.py http://example.com
    ```

2. **Download multiple webpages from a file and merge them**:

    ```sh
    ./scraper.py urls.txt
    ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.
