# python_identity_generator
Using existing modules to help create an identity generator - not that you actually need one.

## Getting Started
This script uses `request` and `BeautifulSoup` to scrape information off of [https://www.fakepersongenerator.com/](https//www.fakepersongenerator.com/) to provide a fake identity. There are quite a few flaws in regards with parsing the information but it works overall. The excess information that this site provides amounts to the point that it's scary. Why would anyone want this information? I don't know...but now it's available in script.

## Issues
There are quite a few issues in regards to using `request` and `BeautifulSoup` on [https://www.fakepersongenerator.com/](https//www.fakepersongenerator.com/).
1. Should the site go down, the script is invalid.
2. Should any information generated from another site go down, the script is invalid.
3. Should you not have internet, the script is invalid.
4. The code sucks. Deal with it, it's a work in progress.

## Future Improvements
* I might consider creating an identity file with stored information so this script works offline as well. (But why...?)
* Improve information parsing.
* Make data extractable
