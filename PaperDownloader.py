#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'swl'
__mtime__ = '9/13/18'
"""
import os
import re
import traceback

import requests
from bs4 import BeautifulSoup

prefix = "http://openaccess.thecvf.com/"
suffix = "CVPR2017"

save_dir = suffix


def get_pdf(data):
    """
    打开pdf并存储
    """
    href, title = data
    name = re.sub(r'[\\/:*?"<>|]', ' ', title)  # 将论文名字中的转移字符用空格替代
    if os.path.isfile(save_dir + "/%s" % name):
        print("File already exsists,skip %s " % name)
        return
    try:
        content = requests.get(prefix + href).content
        with open(save_dir + "/%s.pdf" % name, 'wb') as f:
            f.write(content)
        print("Finish downloading %s" % title)
    except:
        print("Error when downloading %s" % title)
        print(traceback.format_exc())


def main():
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    html = requests.get(prefix + "%s.py" % suffix).content
    soup = BeautifulSoup(html, 'lxml')
    a_list = soup.find_all('a')  # 获取存储论文pdf的a标签
    title_list = soup.find_all("dt", {"class": "ptitle"})  # 获取存储title的dt标签
    title_list = [_.text for _ in title_list]
    pdf_list = []
    for a in a_list:
        if a.text.strip() == "pdf":
            href = a.get("href").strip()
            pdf_list.append(href)
    assert len(pdf_list) == len(title_list), "numbers of title and pdf not equal"
    print("Find %d papers" % len(pdf_list))
    for href, title in zip(pdf_list, title_list):
        get_pdf((href, title))


if __name__ == '__main__':
    main()
