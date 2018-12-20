# 论文下载爬虫

## 可下载会议(期刊)论文

+ CVPR
+ ECCV
+ ICCV

下载地址为[CVF](http://openaccess.thecvf.com/CVPR2017.py)

## 环境

```
Python>=3.5
requests
BeautifulSoup
```

## 使用

根据下载论文的会议和时间修改suffix,如

```Python
suffix = "CVPR2018"

python PaperDownloader.py
```