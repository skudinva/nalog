import requests
import json
c_base_url = 'https://bo.nalog.ru'
c_nbo_org_search_url = c_base_url + '/nbo/organizations/'

def run_search(name, page):
    params = {'name': name, 'page': page, 'allFieldsMatch': 'false'}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
    resp = requests.get(url=c_nbo_org_search_url, params=params, headers=headers)
    if resp.status_code == 200:
        return resp.json()
    elif resp.status_code != 200:
        print('Что-то пошло не так.')
        print(resp)

def parse_one_page(search_result):
    result = []
    if not search_result:
        return False
    if search_result.get('empty') == 'true':
        return False
    in_page = search_result.get('numberOfElements')
    for i in range(in_page):
        one = {'id': search_result.get('content', [])[i].get('id'),
               'inn': search_result.get('content', [])[i].get('inn'),
               'shortName': search_result.get('content', [])[i].get('shortName')}
        result.append(one)
    return result

def parse_result (name):
    s_page = -1
    result = []
    while True:
        s_page = s_page + 1
        js = run_search(s_name, s_page)
        page_result = parse_one_page(js)
        if not page_result:
            return result
        result.append(page_result)

s_name = input('Введите наименование: ')
print(parse_result(s_name))

