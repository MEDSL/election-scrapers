## Election Night Scrapers 11/6/2018

### Alabama

Code last changed: 10/25 
* ELECTION RESULTS SITE NOT LIVE
* Alabama has exportable county-level results. 
* In code, currently have to manually set download path (this will be changed)
* No hardcoded URL for downloadable results. 
* Instead code uses a ASP.NET Postback request
* Need to use Selenium to get Excel file
* URL for last primary was: "http://www2.alabamavotes.gov/electionnight/countyResultsByContest.aspx?cid=04&ecode=1001000"
* The ecode value will be the only thing that changes. 
* Export button has id="hlnkExportData"

### Alaska

No known unofficial results election night. However, Alaska does post official election results at http://www.elections.alaska.gov/doc/info/ElectionResults.php. 

### Arizona
Code not yet available. (In progress)
* ELECTION RESULTS SITE NOT LIVE
* Currently working on building scraper for 8/28 primary site. 
* No way to export unofficial data without scraping
* Need to use Selenium 

### Arkansas 

Code last changed: 10/25
* Election night site live. http://results.enr.clarityelections.com/AR/92174/Web02-state.212862/#/
* Arkansas has exportable county-level results at http://results.enr.clarityelections.com/AR/92174/214496/reports/detailxls.zip
* Code uses Python urllib library to get zip file 

CHANGES TO MAKE: Write code to extract Excel file from zip file

### California

Code last changed: 06/26
* ELECTION RESULTS SITE NOT LIVE
* Notebook created to scrape 06/5/2018 primary
* CA site currently not available

CHANGES TO MAKE: change into a python file rather than notebook

### Colorado
* ELECTION RESULTS SITE NOT LIVE
* Clarity site
* Code not uploaded yet (but will be identical to other Clarity sites

##