# yc-webscraper
Web Scraper for the Y Combinator website

## Instructions
1. Open the code on your favorite python interpreter (I used pycharm - it's the best <3)
2. Install requests, Selenium, and BeautifulSoup. If you don't know how to, go to your terminal and type "pip3 install -r requirements.txt"
3. Download a web driver. Selenium, which is used in the code to automate scrolling needs this to control a browser. I used Chrome but Selenium also supports  Firefox and IE (may support others) 
4. Go to the Y-Combinator site then go to the companies tab. 
5. Apply all the filters you want.
6. Copy the url now. 
7. Go to the code and where it says "directory_url", delete my url and replace it with yours. 
8. Run main.py (I'll probably change that name later.)
9. The code should open a browser and you'll see a browser pop up. DO NOT CLOSE YET. 
10. When it gets to the very bottom of the page, then it is safe to close. 
11. You will see a bunch of printed "Recording X " statements. This means it is making the csv file. 
12. Once the process is done, you will see that it has made a csv file named "ycinfo.csv" 
13. Upload the csv file to Google Sheets and there ya go!
