#-------------------------------------------------------------------------------
# Name:        zenpencils downloader linux
# Purpose:
#
# Author:      Aditya Sapate
#
#-------------------------------------------------------------------------------

from bs4 import BeautifulSoup
import urllib2
import os
import sys

dir = os.path.dirname(os.path.abspath(__file__))
zendir = dir +"/ZenComics"


if not os.path.exists(zendir):
        os.makedirs(zendir)

for url_range in range(1,161):

    main_url = "http://zenpencils.com/comic/" + str(url_range)
    headers = {'User-agent': 'Mozilla/5.0'}

    main_url_opener = urllib2.Request(main_url, None, headers)
    main_url_response = urllib2.urlopen(main_url_opener).read()
    #~ print main_url_response
    main_url_soup = BeautifulSoup(main_url_response)

    for comiclink in main_url_soup.find_all('img'):
        all_links = comiclink.get('src')
        
        if all_links.split('/')[3] == 'wp-content':
			
            filename = all_links.split('/')[5]
            fname = zendir+"/"+filename
            if (not( os.path.isfile(fname))):
				
				res = urllib2.Request(all_links,None,headers)
				img= urllib2.urlopen(res).read()

				with open(zendir+"/"+filename,"wb")as image:
						image.write(img)
				print "Completed Download of  :"+filename
				
			

