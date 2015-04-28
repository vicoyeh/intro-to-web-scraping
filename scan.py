from bs4 import BeautifulSoup
from urllib2 import urlopen

def check_enrollment(url):
	html = urlopen(url).read()
	soup = BeautifulSoup(html)

	enrollTotalTag = soup.find(id="ctl00_BodyContentPlaceHolder_detselect_ctl02_ctl02_EnrollTotal")
	enrollTotal = int(enrollTotalTag.contents[0].string)
	print "Current Total Enrollment is:", enrollTotal

	enrollCapTag = soup.find(id="ctl00_BodyContentPlaceHolder_detselect_ctl02_ctl02_EnrollCap")
	enrollCap = int(enrollCapTag.contents[0].string)
	print "Enrollment Capacity is:", enrollCap

	result=''
	if (enrollTotal < enrollCap):
		result = "Class is open!"
	else:
		result = "Gotta wait bro!"
	print result



if __name__ == "__main__":
	URL = "http://www.registrar.ucla.edu/schedule/detselect.aspx?termsel=15S&subareasel=COM+SCI&idxcrs=0033++++"
	check_enrollment(URL)
	print "Scanning complete!"