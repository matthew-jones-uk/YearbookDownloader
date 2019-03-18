# Yearbook Downloader

This is a simple Python program to download photos and the people tagged in them from www.yearbook.com and save as a ```.jpeg``` and ```.csv```. This is done by scraping the webpage to obtain the direct download links and the tagged people from the HTML.

## Requirements

* PHP session ID
* Python 3 and required modules

## How to setup and run

For this I'll be using Google Chrome/Chromium, other browsers may be similar.

* **Step 0**: Install Python dependencies.
* **Step 1**: Login to www.yearbook.com.
* **Step 2**: On the top-left, next to the address bar, click on the padlock icon.
* **Step 3**: Click cookies > yearbook.com > Cookies > PHPSESSID. Copy the content value. It should be a string that looks something like: ```ebepdn6adf6dh5c24pdhas9b59```.
* **Step 4**: In ```main.py``` replace the cookies PHPSESSID with your value. It should look similar to this:
```
cookies = {
    'PHPSESSID': 'ebepdn6adf6dh5c24pdhas9b59',
}
```
* **Step 5**: Install the Python dependencies and run ```main.py```!
