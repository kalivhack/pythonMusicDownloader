# Music Downloader

This Python script retrieves URLs of music files from the "https://now.morsmusic.org" website and downloads them into a local "files" folder. The script utilizes the requests and BeautifulSoup modules to scrape the website for music file links and the urllib module to download the files to the local machine.

## Installation

To use this script, you'll need to have Python 3 and the following modules installed:

- requests
- beautifulsoup4
- json
- fake_useragent

You can install these modules by running the following command:

```bash
pip install requests beautifulsoup4

Usage

To use the script, simply run the "music_downloader.py" file and wait for the downloads to complete. The downloaded music files will be stored in a "files" folder located in the same directory as the script.

bash

python music_downloader.py
