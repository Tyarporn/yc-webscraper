# yc-webscraper
Web Scraper for the Y Combinator website.
- Finds title (Company), location, founder, description, linkedin, and website
______
## Instructions
1. Clone the repository onto your computer. If you don't know how to do this, follow this [link](https://www.instructables.com/Downloading-Code-From-GitHub/)
2. Open the code on your favorite python interpreter (I used [pycharm](https://www.jetbrains.com/pycharm/) - it's the best <3)
3. Install requests, Selenium, and BeautifulSoup. If you don't know how to, go to your terminal and type `pip3 install -r requirements.txt`
4. Download a web driver. Selenium, which is used in the code to automate scrolling needs this to control a browser. I used [Chrome](https://chromedriver.chromium.org/downloads) but Selenium also supports [Firefox](https://developer.mozilla.org/en-US/docs/Web/WebDriver) and IE (may support others). Do note though that if you don't use Chrome, you need to change the driver object:
    * go to where the code says `driver = webdriver.Chrome(driver_path)`
    * change Chrome to whatever you're using
5. Change the driver path to wherever your driver is 
    * ie `driver_path = "/path/to/your/driver"`
6. Go to the Y-Combinator site then go to the [companies](https://www.ycombinator.com/companies/) tab. 
7. Apply all the filters you want.
8. Copy the url now. 
9. Go to the code and where it says `directory_url`, delete my url and replace it with yours. 
10. Run `yc-scraper.py` (I'll probably change that name later.)
11. The code should open a browser and you'll see a browser pop up. DO NOT CLOSE YET. 
12. When it gets to the very bottom of the page, then it is safe to close. 
13. You will see a bunch of printed "Recording X " statements. This means it is making the csv file. 
14. Once the process is done, you will see that it has made a csv file named `ycinfo.csv` 
15. Upload the csv file to Google Sheets and there ya go!
