import bs4
import re
import time
# from fake_useragent import UserAgent
import requests
from bean_organisation import Organisation
import my_db
import traceback

def get_headers():
    headers = {
        'cookie': 'ASP.NET_SessionId=pzku3y5prulknrnk4zweypxs; ifShowHistory=false; .ASPXANONYMOUS=2MNJBXBHC1szWhq6QurL6M9IIqv_OI1Nnj2ci7ap11Ky5QJI07r8Hjt97WME2kLm02Jge09Loa0VgdazEVPE6gyhrD8NQD77o1xcNKCaWxU_gYxWNxR5tSJEdDMB0mg5ymGCb0xhjD31h65K_64yqeVZBFO_Zj1ISnOlpXY8nEJ2DWVIVZUrguALlbLYJvZH0',
        # 传入你的cookies
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }
    return headers
def get_index_page(url):
    # url = "https://training.gov.au/Search/SearchOrganisation?Name=&IncludeUnregisteredRtos=false&IncludeNotRtos=false&orgSearchByNameSubmit=Search&AdvancedSearch=&JavaScriptEnabled=true"
    # url2="https://training.gov.au/Search/AjaxGetOrganisations?implicitNrtScope=True&includeUnregisteredRtosForScopeSearch=True&includeUnregisteredRtos=True&includeNotRtos=True&orgSearchByNameSubmit=Search&JavaScriptEnabled=true"
    # page = 2
    #
    # formdata = {'size': '100',
    #             'paged': 2,
    #             'orderBy': 'LegalPersonName - asc',
    #             'groupBy': '',
    #             'filter': '',
    #             }
    headers = {  'Connection': 'close',# 传入你的cookies
               'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
               }
    r = s.get(url=url,headers=headers)
    page_source= r.content
    return page_source
def get_org_urls(page_source):
    soup = bs4.BeautifulSoup(page_source, 'lxml')
    tbody=soup.find('tbody')
    trs=tbody.find_all('tr')
    org_urls=[]
    for tr in trs:
        org_url=tr.find('td').find('a')['href']
        if my_db.is_in_table("code",int(org_url.split('/')[-1]))==False:
            org_urls.append("https://training.gov.au" + org_url)
            # print("code:" + str(org_url.split('/')[-1]) + " has already existed")
        # org_url_response=requests.get(url=org_url,headers=get_headers())
    return org_urls
def get_data(org_urls):
    orgs=[]
    for url in org_urls:
        org=Organisation()
        response=s.get(url=url,headers=get_headers())
        time.sleep(1)
        soup=bs4.BeautifulSoup(response.content,'lxml')
        chief_sum = soup.find('h2', string='Summary').parent
        try:
            org.code = int(chief_sum.find('div', string=re.compile('Code')).parent.contents[3].getText())

            org.status = chief_sum.find('div', string=re.compile('Statu')).parent.contents[3].getText().strip()
            # print(org.__dict__)
            # ----------------------
            # soup.find('div',string=re.compile('.*Contact name:.*'))
            url_2 = url + "?tabIndex=2"
            response2 = s.get(url=url_2, headers=get_headers())
            soup2 = bs4.BeautifulSoup(response2.content, 'lxml')
            try:
                chief_info = soup2.find('h2', string=re.compile('Chief Executive')).parent
            except Exception as e:
                print(traceback.print_exc())
                org.insert_into_table()
                print("Code:"+str(org.code)  +" Something Wrong:Chief Executive !")
                continue

            # soup
            org.contact_name = chief_info.find('div', string=re.compile('Contact name:')).parent.contents[
                3].getText().strip()

            try:
                org.job_title = chief_info.find('div', string=re.compile('Job title:')).parent.contents[3].getText().strip()
            except Exception as e:
                print(traceback.print_exc())
                print("Code:"+str(org.code)  +" Something Wrong: no Job Tile!")

            org.organisation_name = chief_info.find('div', string=re.compile('Organisation name:')).parent.contents[
                3].getText().strip()

            try:
                org.email = chief_info.find('div', string=re.compile('Email:')).parent.contents[3].getText().strip()
            except Exception as e:
                print(traceback.print_exc())
                print("Code:"+str(org.code)  +" Something Wrong: no Email info!")
            org.address = chief_info.find('div', string=re.compile('Address:')).parent.contents[3].getText().strip()
            org.insert_into_table()
            orgs.append(org)
        except Exception as e:
            print(traceback.print_exc())
            print("Wrong info:")
            print(org.__dict__)

    return orgs



if __name__ == '__main__':
    # &pageSizeKey=Search_SearchOrganisation_gridRtoSearchResults&pageSize=100 &gridRtoSearchResults-page=
    s = requests.session()
    s.keep_alive = False
    s.adapters.DEFAULT_RETRIES = 5
    page = 100
    for i in range(1,page):
        allorg_url="https://training.gov.au/Search/SearchOrganisation?IncludeUnregisteredRtos=true%2Cfalse&IncludeNotRtos=true%2Cfalse&orgSearchByNameSubmit=Search&JavaScriptEnabled=true&gridRtoSearchResults-page=" + str(i) + "&pageSizeKey=Search_SearchOrganisation_gridRtoSearchResults&pageSize=100&setFocus=gridRtoSearchResults"
        # o_url = "https://training.gov.au/Search/SearchOrganisation?IncludeUnregisteredRtos=false&IncludeNotRtos=false&orgSearchByNameSubmit=Search&gridRtoSearchResults-page=" + str(i) + "&setFocus=gridRtoSearchResults&pageSizeKey=Search_SearchOrganisation_gridRtoSearchResults&pageSize=100&setFocus=gridRtoSearchResults"
        source=get_index_page(allorg_url)
        # print(source)
        org_urls=get_org_urls(source)
        orgs=get_data(org_urls)



