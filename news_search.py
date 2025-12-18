import requests
from bs4 import BeautifulSoup

def search_news():
    # 1. 사용자에게 검색어를 입력받습니다.
    keyword = input("어떤 뉴스를 찾고 싶으신가요? : ")
    print(f"\n[{keyword}] 최신 뉴스를 가져오는 중...\n")
    
    # 구글 뉴스 검색 주소
    url = f"https://www.google.com/search?q={keyword}&tbm=nws"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 뉴스 제목이 들어있는 태그 (구글 뉴스의 기본 구조)
        # 구글은 보안이 강하지 않아 h3 태그로 제목을 쉽게 가져올 수 있습니다.
        titles = soup.find_all('h3')

        if not titles:
            print("❌ 결과를 찾지 못했습니다.")
            return

        print(f"✅ '{keyword}' 관련 최신 뉴스 상위 5개:")
        print("-" * 50)
        for i, t in enumerate(titles[:5], 1):
            print(f"{i}. {t.get_text()}")
        print("-" * 50)
        
    except Exception as e:
        print(f"❌ 에러: {e}")

# 실행
search_news()
