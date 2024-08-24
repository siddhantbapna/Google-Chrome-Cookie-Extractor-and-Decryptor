# Google-Chrome-Cookie-Extractor-and-Decryptor
This repo contains the code for extracting the locally stored google chrome cookies and decrypt them to get the actual value of the cookies.


# Chrome Cookies Extractor and Decryptor

Welcome to the **Chrome Cookies Extractor and Decryptor** project! This repository contains a powerful toolset to fetch, decrypt, and store cookies from Google Chrome. Whether you're a developer, security researcher, or tech enthusiast, these scripts provide an efficient way to manage your browser's cookies.

## Overview

### `batty.bat` - Fetch Chrome Cookies
The `batty.bat` script is designed to extract all cookie files from Google Chrome and store them in a designated folder named `new`. This process is automated, allowing you to retrieve cookies with just a double-click.

### `decrypt.py` - Decrypt Chrome Cookies
Once the cookies are fetched, the `decrypt.py` script decrypts these cookies and saves the output in a `manky.csv` file. This CSV file contains all the decrypted cookie data in an easily accessible format for further analysis or use.

## Usage Instructions

### Prerequisites

Before you start, ensure you have the following:

- **Python 3.x** installed on your system.
- **Google Chrome** installed (as the cookies are extracted from Chrome).

### Step 1: Extract Cookies with `batty.bat`

1. Double-click the `batty.bat` file.
2. The script will automatically fetch all cookies from Chrome and store them in the `new` folder.

### Step 2: Decrypt Cookies with `decrypt.py`

1. Ensure the `new` folder contains the cookies fetched by `batty.bat`.
2. Run the `decrypt.py` script:
   ```bash
   python decrypt.py
