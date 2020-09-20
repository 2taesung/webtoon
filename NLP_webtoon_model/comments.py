import requests
from bs4 import BeautifulSoup
import json
import csv

# url을 받아서 id를 구해준다 Ex) url 옴니버스 장르면 그 화면에 있는 모든 웹툰들의 아이디
def get_ids(url):
    try:
       
        response = requests.get(url)
        soup = BeautifulSoup(response.text ,'html.parser')
        li_list = soup.select('#content > div.list_area > ul > li')
        webtoon_id=[]
        for li in li_list:
            a_tag = li.select_one('dl > dt > a')
            id = a_tag['href'].split('=')[1]
            webtoon_id.append(id)
        return webtoon_id

    except :
        print('id 함수 문제')

# 장르의 url을 받아 완결되지 않은 웹툰의 [순위, 웹툰의 이름] 리스트와 연재 중인 웹툰들의 url을 리스트로 반환한다.
def not_finish_get_href(url,finish_id):
    response = requests.get(url)
    soup = BeautifulSoup(response.text ,'html.parser')
    li_list = soup.select('#content > div.list_area > ul > li')
    hrefs=[]
    name=[]
    img_url=[]
    id_list = []
    url_='https://comic.naver.com'
    for li in li_list:
        a_tag = li.select_one('dl > dt > a')
        a_img = li.select_one('div > a > img')
        id = a_tag['href'].split('=')[1]
        if id not in finish_id:
            hrefs.append(url_ + a_tag['href'])
            name.append(a_tag['title'])
            img_url.append(a_img['src'])
            id_list.append(id)
    total_not_finish = []
    for i in range(0, len(name)):
        total_not_finish.append([i+1,name[i]])
    return total_not_finish, hrefs, id_list
# total_not_finish = [[순위, 웹툰 이름], [ ], .... ] / hrefs = [href, href, ...]

# 웹툰 댓글 크롤러

def comment_list(href_list,id_list):
    contents_list=[]

    for href,id in zip(href_list,id_list):
        try:
            response = requests.get(href)
            soup = BeautifulSoup(response.text ,'html.parser')
            epi_num = int(soup.select('td.title')[0].select_one('a')['href'].split('&')[1][3:])
            co_list=[]
            if epi_num>5:
                for i in range(5):
                    url = href + '&no=' + str(epi_num)
                    obj_id = id + "_" + str(epi_num)
                    get_comment(url,obj_id,co_list)
                    epi_num-=1
                contents_list.append(co_list)
            else:
                a=epi_num
                for i in range(epi_num):
                    if a != 0:
                        url = href + '&no=' + str(a)
                        obj_id = id + "_" + str(a)
                        get_comment(url,obj_id,co_list)
                        a-=1
                    else:
                        break
                contents_list.append(co_list)
        except :
            print(href)

    return contents_list

# total_comments_list = get_comments()   
        

def get_comment(url,obj_id,contents_list):
    try:
        
        headers = {
            'referer': url,
        }

        params = (
            ('ticket', 'comic'),
            ('pool', 'cbox3'),
            ('lang', 'ko'),
            ('objectId', obj_id),
        )

        response = requests.get('https://apis.naver.com/commentBox/cbox/web_naver_list_jsonp.json', headers=headers, params=params)

        idx=response.text.find('(') +1
        re=response.text[idx:]
        
        result=json.loads(re[:-2])
        comment_list=result['result']['commentList']

        for list in comment_list:
            comment=list['contents']
            comment=comment.replace('\n','')
            contents_list.append([comment])
    except :
        print('댓글 긁기 문제')


finish_url = 'https://comic.naver.com/webtoon/finish.nhn'

webtoon_url = {'액션':'https://comic.naver.com/webtoon/genre.nhn?genre=action',
'순정':'https://comic.naver.com/webtoon/genre.nhn?genre=pure',
'판타지' :'https://comic.naver.com/webtoon/genre.nhn?genre=fantasy'}

# 장르 입력을 받아서 genre에 저장
genre=input('장르를 입력해주세요(액션, 순정, 판타지) :')
# 완결 웹툰의 id를 저장해놓기
finish_id=get_ids(finish_url)
# 완결웹툰 id와 입력받은 genre를 url딕셔너리에 넣어 장르에 맞는 url not_finish_get_href함수의 인풋으로 넣는다
# 그리고 output으론 각 장르의 완결이 아닌 웹툰의 url과 이름을 리스트로 반환한다.

total_not_finish, not_finish_hrefs, id_list = not_finish_get_href(webtoon_url[genre],finish_id)

print(total_not_finish)
# 각 장르 맞춰서 베댓 csv파일 저장하기
# cm_list=comment_list(not_finish_hrefs,id_list)
# title = ['댓글','긍정/부정']
# with open('fantasy.csv', 'w', encoding='utf-8',newline='') as f:
#     wr = csv.writer(f)
#     wr.writerow(title)
#     for row in cm_list:
#         wr.writerows(row)