from bs4 import BeautifulSoup
import unittest
import re

def get_images_amount(body):
    imgs = body.find_all('img')
    fit_imgs = len(
        [x for x in imgs if x.get('width') and int(x.get('width')) >= 200]
    )
    return fit_imgs

def get_headers_amount(body):
    headers = body.find_all(re.compile('^h[1-6]$'))
    count = 0
    for header in headers:
        children = header.find_all(recursive=False)
        if children:
            children_content = [x.getText() for x in children if x.getText()]
            try:
                first_letter = children_content[0][0]
                if first_letter in 'ETC':
                    count += 1
            except IndexError:
                pass
        else:
            try:
                first_letter = header.getText()[0]
                if first_letter in 'ETC':
                    count += 1
            except IndexError:
                pass
    return count



def get_max_links_len(body):
    max_count = 0
    all_links = body.find_all('a')
    for link in all_links:
        current_count = 1
        siblings = link.find_next_siblings()
        for sibling in siblings:
            if sibling.name == 'a':
                current_count += 1
                max_count = max(current_count, max_count)
            else:
                current_count = 0
    return max_count


def get_lists_num(body):
    count = 0
    all_lists = body.find_all(['ul', 'ol'])
    for tag in all_lists:
        if not tag.find_parents(['ul', 'ol']):
            count += 1
    return count


def parse(path_to_file):    
    with open(path_to_file,'r',encoding='utf-8') as html:
        soup = BeautifulSoup(html, "lxml")    
    
    body = soup.find(id="bodyContent")
#     print(body)
    imgs = get_images_amount(body)
    headers = get_headers_amount(body)
    linkslen = get_max_links_len(body)
    lists = get_lists_num(body)
    
    return [imgs, headers, linkslen, lists]
