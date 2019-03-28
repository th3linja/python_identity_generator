# python_identity_generator
Using existing modules to help create an identity generator - not that you actually need one.

## Getting Started
This script uses `request` and `BeautifulSoup` to scrape information off of [https://www.fakepersongenerator.com/](https//www.fakepersongenerator.com/) to provide a fake identity. There are quite a few flaws in regards with parsing the information but it works overall. The excess information that this site provides amounts to the point that it's scary. Why would anyone want this information? I don't know...but now it's available in script.

## Prerequisites
* Python
* BeautifulSoup
* Requests

## Installing
If you do not have Python installed, you can download the latest version from this [link](https://www.python.org/). When installing, make sure to enable pip in `Optional Features`. After installing, head over to Advanced System Settings -> Environment Variables and add Python into PATH.

If you do not have `requests` or `BeautifulSoup`, run `pip3 install requests` and `pip3 install BeautifulSoup` in the command prompt (cmd).

Download the script from the repository and run.

## Running the Program
When you initially run the program, the program just spits out a random generated name off of the site [https://www.fakepersongenerator.com/](https//www.fakepersongenerator.com/). If you want to see the all of the generated data, you can pass a loop through the dictionary `person_data` to print a list of all of the data scraped off of the site. Otherwise, you can create multiple print statements through the object to get specific data.

## Issues
There are quite a few issues in regards to using `request` and `BeautifulSoup` on [https://www.fakepersongenerator.com/](https//www.fakepersongenerator.com/).
1. Should the site go down, the script is invalid.
2. Should any information generated from another site go down, the script is **partially** invalid. (Most of the data is generated off other sites).
3. Should you not have internet, the script is invalid.
4. Should you encounter a captcha, the script is invalid.
5. A new person is generated every time the code is ran - even if stored as a variable.
5. The code sucks. Deal with it, it's a work in progress.

## Future Improvements
* I might consider creating an identity file with stored information so this script works offline as well. (But why...?)
* Improve information parsing.
* Make data extractable

## Authors
th3linja

## Acknowledgements
Thank you authors of `BeautifulSoup` and `requests`.

* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)

* [requests](http://docs.python-requests.org/en/master/)
