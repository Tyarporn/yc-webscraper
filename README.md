# yc-webscraper
Web Scraper for the Y Combinator website
______
## Instructions
1. Open the code on your favorite python interpreter (I used [pycharm](https://www.jetbrains.com/pycharm/) - it's the best <3)
2. Install requests, Selenium, and BeautifulSoup. If you don't know how to, go to your terminal and type `pip3 install -r requirements.txt`
3. Download a web driver. Selenium, which is used in the code to automate scrolling needs this to control a browser. I used [Chrome](https://chromedriver.chromium.org/downloads) but Selenium also supports [Firefox](https://developer.mozilla.org/en-US/docs/Web/WebDriver) and IE (may support others). Do note though that if you don't use Chrome, you need to change the driver object:
    * go to where the code says `driver = webdriver.Chrome(driver_path)`
    * change Chrome to whatever you're using
4. Change the driver path to wherever your driver is 
    * ie `driver_path = "/path/to/your/driver"`
5. Go to the Y-Combinator site then go to the [companies](https://www.ycombinator.com/companies/) tab. 
6. Apply all the filters you want.
7. Copy the url now. 
8. Go to the code and where it says `directory_url`, delete my url and replace it with yours. 
9. Run `yc-scraper.py` (I'll probably change that name later.)
10. The code should open a browser and you'll see a browser pop up. DO NOT CLOSE YET. 
11. When it gets to the very bottom of the page, then it is safe to close. 
12. You will see a bunch of printed "Recording X " statements. This means it is making the csv file. 
13. Once the process is done, you will see that it has made a csv file named `ycinfo.csv` 
14. Upload the csv file to Google Sheets and there ya go!
