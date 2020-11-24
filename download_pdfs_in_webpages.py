import os
import requests
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup



def get_all_urls_in_one_page(url):
    res = []
    html = urlopen(url)
    bs = BeautifulSoup(html, 'html.parser') #解析网页
    hyperlink = bs.find_all('a')  #获取所有超链接
    for h in hyperlink:
        hh = h.get('href')
        res.append(hh)
    return res

if __name__ == '__main__':
    url = 'https://hub.baai.ac.cn/view/4155'
    all_urls = get_all_urls_in_one_page(url)
    pdf_urls = [u for u in all_urls if u.endswith('pdf')]
    if not os.path.exists('download_pdfs'):
        os.mkdir('download_pdfs')
    save_file = 'download_pdfs' + '/' 
    for i, suburl in enumerate(pdf_urls):
        with open(save_file+str(i)+'.pdf', 'wb') as f:
            r = urllib.request.urlopen(suburl)
            block_sz = 8192
            while True:
                buffer = r.read(block_sz)
                if not buffer:
                    break
                f.write(buffer)
