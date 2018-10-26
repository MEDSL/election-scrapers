import urllib
import os 

if __name__== "__main__":

	path = "ENTER_PATH"
	urllib.urlretrieve("http://results.enr.clarityelections.com/AR/92174/214496/reports/detailxls.zip", path)