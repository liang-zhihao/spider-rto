import gevent
from gevent import monkey
monkey.patch_all()
import bs4
import re
import time
# from fake_useragent import UserAgent
import requests
from bean_organisation import Organisation
import my_db
import traceback
import run_monkey
import my_requests

if __name__ == '__main__':
    # allorg_url = "https://training.gov.au/Search/SearchOrganisation?IncludeUnregisteredRtos=true%2Cfalse&IncludeNotRtos=true%2Cfalse&orgSearchByNameSubmit=Search&JavaScriptEnabled=true&gridRtoSearchResults-page=" +"" + "&pageSizeKey=Search_SearchOrganisation_gridRtoSearchResults&pageSize=100&setFocus=gridRtoSearchResults"
    start_page=1
    end_page = 121
    process_num=8
    if end_page-start_page>8:
        process_num=8
    else:
        process_num=end_page-start_page
    process_num=8
    gs=[]
    url_sp=["https://training.gov.au/Search/SearchOrganisation?IncludeUnregisteredRtos=true%2Cfalse&IncludeNotRtos=true%2Cfalse&orgSearchByNameSubmit=Search&JavaScriptEnabled=true&gridRtoSearchResults-page=","&pageSizeKey=Search_SearchOrganisation_gridRtoSearchResults&pageSize=100&setFocus=gridRtoSearchResults"]
    for id in range(process_num):
        my_range=list(range(start_page+id,end_page,process_num))
        gs.append(gevent.spawn(run_monkey.run_gevent,id,my_range,url_sp))
    gevent.joinall(gs)
    print("is over?")




