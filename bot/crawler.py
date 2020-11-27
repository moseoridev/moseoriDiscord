from os import error
import requests
from bs4 import BeautifulSoup


def makeHtml(URL):
    headers = {
        'Host': 'www.coupang.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'ko-KR,ko;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'http://click.linkprice.com/click.php?m=coupang&a=A100211316&l=9999&l_cd1=3&l_cd2=0&tu=https%3A%2F%2Fwww.coupang.com%2Fvp%2Fproducts%2F2378328151%3FitemId%3D4145966771%26vendorItemId%3D72129866907%26q%3DUN65TU8000FXZA%26itemsCount%3D4%26searchId%3D49d56f37836f476b92a499170788767e%26rank%3D0%26isAddedCart%3D&u_id=ppomppu_372713',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0',
        'TE': 'Trailers'}

    req = requests.get(URL, headers=headers)
    if req.status_code == 200:
        return req.text
    else:
        raise Exception('접속에 실패했습니다.')


def isSoldOut(url):
    html = makeHtml(url)
    soup = BeautifulSoup(html, 'html.parser')
    js = soup.select('head > script:nth-child(32)')

    return ('"soldOut":true' in str(js[0]))


# isSoldOut('https://www.coupang.com/vp/products/2378328151')
