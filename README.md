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

### Arkansas 

Code last changed: 10/25
* Election night site live. http://results.enr.clarityelections.com/AR/92174/Web02-state.212862/#/
* Arkansas has exportable county-level results at http://results.enr.clarityelections.com/AR/92174/214496/reports/detailxls.zip
* Code uses Python requests library to get zip file 

CHANGES TO MAKE: Write code to have extract Excel file from zip file
