import requests
from bs4 import BeautifulSoup

INSPECTION_DOMAIN = 'http://info.kingcounty.gov'
INSPECTION_PATH = '/health/ehs/foodsafety/inspections/Results.aspx'
INSPECTION_PARAMS = {
    'Output': 'W',
    'Business_Name': '',
    'Business_Address': '',
    'Longitude': '',
    'Latitude': '',
    'City': '',
    'Zip_Code': '',
    'Inspection_Type': 'All',
    'Inspection_Start': '',
    'Inspection_End': '',
    'Inspection_Closed_Business': 'A',
    'Violation_Points': '',
    'Violation_Red_Points': '',
    'Violation_Descr': '',
    'Fuzzy_Search': 'N',
    'Sort': 'H'
}


def get_inspection_page(**kwargs):
    url = INSPECTION_DOMAIN + INSPECTION_PATH
    params = INSPECTION_PARAMS.copy()
    for key, val in kwargs.items():
        if key in INSPECTION_PARAMS:
            params[key] = val
    print "getting url"
    resp = requests.get(url, params=params)
    print "got it"
    resp.raise_for_status()  # <- This is a no-op if there is no HTTP error
    # remember, in requests `content` is bytes and `text` is unicode

    with open('inspection_page.html', 'w') as outfile:
        outfile.write(resp.encoding + "\n" + resp.content)

    return resp.content, resp.encoding


def parse_search(html):
    parsed = BeautifulSoup(html)
    return parsed

if __name__ == '__main__':
    get_inspection_page()
