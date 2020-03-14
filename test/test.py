
import bs4
import re
import time
from fake_useragent import UserAgent
import requests
# url="https://training.gov.au/Search/AjaxGetOrganisations?implicitNrtScope=True&includeUnregisteredRtosForScopeSearch=True&includeUnregisteredRtos=False&includeNotRtos=False&orgSearchByNameSubmit=Search&JavaScriptEnabled=true"
# url2="https://training.gov.au/Search/AjaxGetOrganisations?implicitNrtScope=True&includeUnregisteredRtosForScopeSearch=True&includeUnregisteredRtos=True&includeNotRtos=True&orgSearchByNameSubmit=Search&JavaScriptEnabled=true"
# url3="https://training.gov.au/Search/SearchOrganisation?IncludeUnregisteredRtos=true%2Cfalse&IncludeNotRtos=true%2Cfalse&orgSearchByNameSubmit=Search&JavaScriptEnabled=true&page=3&gridRtoSearchResults-page=1&setFocus=gridRtoSearchResults&pageSizeKey=Search_SearchOrganisation_gridRtoSearchResults&pageSize=50&setFocus=gridRtoSearchResults"
#
# url4="https://training.gov.au/Search/SearchOrganisation?IncludeUnregisteredRtos=true%2Cfalse&IncludeNotRtos=true%2Cfalse&orgSearchByNameSubmit=Search&JavaScriptEnabled=true&gridRtoSearchResults-page=1&pageSizeKey=Search_SearchOrganisation_gridRtoSearchResults&pageSize=100&setFocus=gridRtoSearchResults&gridRtoSearchResults-page=9"
#
# url5="https://training.gov.au/Search/SearchOrganisation?Name=&IncludeUnregisteredRtos=false&IncludeNotRtos=false&orgSearchByNameSubmit=Search&AdvancedSearch=&JavaScriptEnabled=true"
#
#
# headers = {
#     'cookie': 'ASP.NET_SessionId=pzku3y5prulknrnk4zweypxs; ifShowHistory=false; .ASPXANONYMOUS=2MNJBXBHC1szWhq6QurL6M9IIqv_OI1Nnj2ci7ap11Ky5QJI07r8Hjt97WME2kLm02Jge09Loa0VgdazEVPE6gyhrD8NQD77o1xcNKCaWxU_gYxWNxR5tSJEdDMB0mg5ymGCb0xhjD31h65K_64yqeVZBFO_Zj1ISnOlpXY8nEJ2DWVIVZUrguALlbLYJvZH0',
#     # 传入你的cookies
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
#     }
#
# formdata = {'size': '100',
#             'paged': '2',
#             'orderBy': 'LegalPersonName - asc',
#             'groupBy': '',
#             'filter': '',
#             }
# r = requests.post(url=url4, data=formdata, headers=headers)
# print(r.text)
soup = bs4.BeautifulSoup(open("detailcontact.html"),'lxml')
# chief_info = soup.find('h2',string='Summary').parent
chief_info = soup.find('h2',string=re.compile('Chief Executive')).parent
# soup re.compile('Chief Executive')
print(chief_info)
# cont = chief_info.find('div', string=re.compile('Contac')).parent.contents[3].getText().strip()
cont = chief_info.find('div', string=re.compile('Contact name:')).parent.contents[3].getText().strip()
print(cont)

