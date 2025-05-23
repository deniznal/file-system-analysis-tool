# File System Analysis Tool

This program analyzes file systems and generates visualizations to understand file size distributions and file type patterns. It's designed to work on both Windows and Unix-based systems (like macOS).

## Features

- Recursive directory analysis
- File size distribution analysis
- File type categorization
- Generation of three types of visualizations:
  - Histogram of file sizes
  - Pie chart of file type distribution
  - Cumulative Distribution Function (CDF) of file sizes

## Requirements

- Python 3.7 or higher
- Required Python packages (install using `pip install -r requirements.txt`):
  - matplotlib
  - numpy

## Installation

1. Clone or download this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the program:
   ```bash
   python file_analysis.py
   ```
2. When prompted, enter the directory path you want to analyze
3. The program will generate:
   - A text report in the console
   - Three visualization files:
     - `file_size_histogram.png`
     - `file_type_distribution.png`
     - `file_size_cdf.png`

## File Type Categories

The program categorizes files into the following types:
- Documents (.pdf, .doc, .docx, .txt, etc.)
- Images (.jpg, .png, .gif, etc.)
- Videos (.mp4, .avi, .mov, etc.)
- Audio (.mp3, .wav, .flac, etc.)
- Code (.py, .java, .cpp, etc.)
- Archives (.zip, .rar, .7z, etc.)
- Executables (.exe, .dll, .so, etc.)
- System files (.sys, .ini, .conf, etc.)
- Other (uncategorized files)

## Notes

- The program handles permission errors gracefully
- File sizes are displayed in bytes in the visualizations
- The histogram and CDF use logarithmic scales for better visualization of the wide range of file sizes 