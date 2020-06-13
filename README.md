# Mzitu_Spider

[![license](https://img.shields.io/github/license/ZYSzys/Mzitu_Spider.svg)](https://github.com/ZYSzys/Mzitu_Spider/blob/master/LICENSE)

对美女图片网站 http://www.mzitu.com 进行爬取，分类型下载美女图片，爬虫采用scrapy框架， 该站有封ip策略，可以配合proxypool 对整站进行抓取
。
#### 依赖环境
    python>=3.7

    scrapy>=2.1.0

#### 安装步骤
1. 在终端输入如下命令：
    ```bash
    git clone https://github.com/ZYSzys/Mzitu_Spider.git
    ```
2. 在当前目录下输入：
    ```bash
    cd Mzitu-Scrapy
    pip install -r requirements.txt
    scrapy crawl mzitu
    ```
3. 按照自己的电脑环境，配置爬虫参数
    ```python
    # 修改模型 /Mzitu-Scrapy/Mzitu/settings.py 文件
   
    # 图片存储路径
    IMAGES_STORE = '/home/Mzitu' 
    # 代理池的 url 地址
    PROXY_URL = 'http://192.168.50.20:5010/get/'
    ```
运行爬虫，如图所示  
![](/screenshots/1.png)  

稍等几分钟后，当前目录下生成Mzitu文件夹，首页每套图以存储在其中  
![](/screenshots/2.png)  