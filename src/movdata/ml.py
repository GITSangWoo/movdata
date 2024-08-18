import requests
import os
import json
import time
from tqdm import tqdm 
import pandas as pd 

API_KEY = os.getenv('MOVIE_API_KEY')

def save_json(data, file_path):
    # 파일저장 경로 MKDIR
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data,f,indent=4, ensure_ascii=False )
 

def req(url):
    r = requests.get(url)
    j = r.json()
    return j 

def save_movies(year, per_page=10, sleep_time=1):
    file_path = f'data/movies/year={year}/data.json'
    
    # 위 경로가 있으면 API 호출을 멈추고 프로그램 종료
    if os.path.exists(file_path):
       return False
    # totCnt 가져오고 total_pages 계산 
    url_base = f"https://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key={API_KEY}&openStartDt={year}&openEndDt={year}"
    r = req(url_base + f"&curPage=1")
    tot_cnt = r['movieListResult']['totCnt']
    total_pages = (tot_cnt // per_page) + 1  

    # total_pages 만큼 Loop 돌면서 API 호출  
    all_data = []
    for page in tqdm(range(1, total_pages + 1)):
        time.sleep(sleep_time)
        r = req(url_base + f"&curPage={page}") 
        d = r['movieListResult']['movieList']
        all_data.extend(d)
    
    save_json(all_data,file_path)
    return True 
   
def save_details(year,sleep_time=1):
    file_path = f'data/movies/year={year}/data.json'
    save_path =  f'data/movies_details/year={year}/data.json'
    
    rj=pd.read_json(file_path) 
    movie_cds=rj['movieCd']
    if os.path.exists(save_path):
        return False
    
    all_data=[]
    for movie_cd in tqdm(movie_cds):
        time.sleep(sleep_time)
        url = f"https://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={API_KEY}&movieCd={movie_cd}"
        print(url)
        r = req(url)
        d = r['movieInfoResult']['movieInfo']
        all_data.extend(d)

    save_json(all_data, save_path)    
    return True 

def save_complist(year,sleep_time=1):
    file_path = f'data/movies/year={year}/data.json'
    save_path = f'data/movies_complist/year={year}/data.json'

    if os.path.exists(save_path):
        return False
    
    rj=pd.read_json(file_path)
    companylist=rj[rj['companys'].apply(lambda x : len(x)>0)]['companys'].drop_duplicates()      
    all_data=[]
    for compNms in tqdm(companylist):
        time.sleep(sleep_time)
        compNm=compNms[0]['companyNm']
        url = f"https://kobis.or.kr/kobisopenapi/webservice/rest/company/searchCompanyList.json?key={API_KEY}&companyNm={compNm}"
        print(url)
        r = req(url)  
        d = r['companyListResult']['companyList']
        all_data.extend(d)
    
    save_json(all_data, save_path)
    return True
         


def save_compdetails(year,sleep_time=1):
    file_path = f'data/movies/year={year}/data.json'
    save_path = f'data/movies_compdetails/year={year}/data.json'

    if os.path.exists(save_path):
        return False
    
    rj=pd.read_json(file_path)
    companylist=rj[rj['companys'].apply(lambda x : len(x)>0)]['companys'].drop_duplicates()
       
    all_data=[]
    for compCds in companylist:
        time.sleep(sleep_time)
        compCd=compCds[0]['companyCd']
        url = f"https://www.kobis.or.kr/kobisopenapi/webservice/rest/company/searchCompanyInfo.json?key={API_KEY}&companyCd={compCd}"
        r = req(url)  
        d = r['companyInfoResult']['companyInfo']
        all_data.extend(d)
    
    save_json(all_data, save_path)
    return True












