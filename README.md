# EVENT_STUDY_ANALYSIS_M-A
Deals with all the acquisitions which took place in INDIA after 2012 involving S&amp;P BSE 500 Companies at present,i could analyze it 
for 463 acquisitions on the chart

The acusition data list is taken from Prowessdx and then web scraing and data collection was automated to get the stock prices for all those 
companies.The estmation window was one year and the event window was (-10,+10).

The scraping code for generating stock prices excel sheet is are two python files which are based on BeautifulSoup,Selenium and Javascript.
You will need a mozilla driver or a chrome driver to run through the entire automated web scrapper.All you need is to feed in the filename which
contains the acquiring companies and all the the acquistion date.

Also all the analysis have been done on jupyter's notebook i-python files and are available with respective names.Pandas,numpy and matplotlib has been 
used with the regression and estimation based on scikit learn linearregression module.

Any issue you can get to me.
