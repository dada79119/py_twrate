import requests
from bs4 import BeautifulSoup

def rate(currencyname):
    url ="http://rate.bot.com.tw/xrt?Lang=zh-TW"
    #print(url)
    print('Start parsing rate ...')
    rs = requests.session()
    res = rs.get(url, verify=False)
    #print(res)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    #print(soup)
    upd_time=soup.find_all("span",{"class":"time"})[0].string
    currency=soup.find_all("div",{"class":"visible-phone print_hide"})
    ratelist=['紐元','歐元','日圓','英鎊','印尼幣','南非幣','瑞士法郎','澳幣','新加坡幣','瑞典幣','美金','越南盾','韓元','泰幣','菲國比索','人民幣','馬來幣','港幣','加拿大幣']
    dic={}
    i=1
    for c in currency:
        dic[c.string.strip()[:-6]]=i
        i+=2
    #print(dic)
    content=""
    if currencyname=='匯率':
        for k in dic:
            idx=dic[k]
            srate=soup.find_all("td",{"data-table":"本行現金賣出"})[idx].string
            crate=soup.find_all("td",{"data-table":"本行即期賣出"})[idx].string
            content+= k + '\n'
            content+='現金賣出匯率' + srate + '\n'
            content+='即期賣出匯率' + crate + '\n'
            content+='-------[牌告更新時間：' + upd_time + ']------- \n'

    elif currencyname in ratelist :    
        idx=dic[currencyname]
        srate=soup.find_all("td",{"data-table":"本行現金賣出"})[idx].string
        crate=soup.find_all("td",{"data-table":"本行即期賣出"})[idx].string
        #print(crate)
        content+=currencyname + '\n'
        content+='現金賣出匯率' + srate + '\n'
        content+='即期賣出匯率' + crate + '\n'
        content+='牌告更新時間：' + upd_time
    else :
        content+='請輸入正確的幣值'
        content+='如 紐元,歐元,日圓,英鎊,印尼幣,南非幣,瑞士法郎,澳幣,新加坡幣 \n'
        content+='瑞典幣,美金,越南盾,韓元,泰幣,菲國比索,人民幣,馬來幣,港幣,加拿大幣'
 
   
    return content

print(rate('匯率'))
