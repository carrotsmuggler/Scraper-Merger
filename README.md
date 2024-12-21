# Scraper

A Python scraper script to download websites as PDFs and then merge them into a single PDF.
Useful for downloading documentation and feeding it into a notebookLM.

## Features

-   Download a webpage as a PDF by providing a URL.
-   Process multiple URLs from a file.
-   Interactive mode to enter URLs one by one.
-   Automatically generates filenames based on the webpage title.
-   Option to merge all downloaded PDFs into a single PDF.

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

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
