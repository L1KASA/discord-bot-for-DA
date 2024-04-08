import search_media
import media_page
from bs4 import BeautifulSoup

def parse_html_search_media(name, filename="search_media.html"):
    search_media.write_to_html(name)
    with open(filename, "r", encoding="utf-8") as f:
        contents = f.read()
    
        soup = BeautifulSoup(contents, 'lxml')
    
        allNews = soup.find('div', class_='right').find('a', class_="js-serp-metrika")

        if allNews:
            allNews = allNews.get('data-id')
            print(allNews)
        else:
            print("parse_html_search_media")
            return None
        return allNews

def parse_html_media_page(name, filename="media_page.html"):
    media_page.write_to_html(name)
    with open(filename, "r", encoding="utf-8") as f:
        contents = f.read()
    
        soup = BeautifulSoup(contents, 'lxml')

# картинки
        allNews = soup.findAll('div', class_='styles_column__r2MWX styles_md_6__XDxd6 styles_lg_8__7Mdim styles_column__5dEFP')[0] \
            .find('img', class_='image')#.get('src') #\
        if allNews:
            allNews = allNews.get('src')
            
        else:
            print("Картинка не найдена")
            return None

# рейтинг
        #allNews = soup.find('div', class_='styles_root__4VfvJ styles_basicInfoSection__EiD2J') \
        #    .findAll('div', class_='styles_root__2kxYy styles_topLine__xigow')[0] #\
        #
        #a = allNews.find('div', class_='styles_column__r2MWX styles_md_6__XDxd6 styles_lg_6__eGSDb') \
        #        .find('span', class_='styles_ratingNeutral__meu3w')
        #print(a.text)
        
# ищем год и прочую инфу
        #allNews = soup.find('div', class_='styles_root__4VfvJ styles_basicInfoSection__EiD2J') \
        #    .findAll('div', class_='styles_root__2kxYy styles_topLine__xigow')[1] #\
            #.find('div', class_='styles_rowDark__ucbcz styles_row__da_RK')#.get('data-id')
        #print(allNews)

        #filteredNews = []


        #a = allNews.find('div', class_='styles_column__r2MWX styles_md_11__UdIH_ styles_lg_15__Ai53P') \
        #        .findAll('div', class_='styles_valueDark__BCk93 styles_value__g6yP4')
        #
        #for data in a:
        #    if data.find('a'):
        #    #a = data.find('div', class_='styles_column__r2MWX styles_md_11__UdIH_ styles_lg_15__Ai53P') \
        #    #    .findAll('div', class_='styles_titleDark___tfMR styles_title__b1HVo')
        #        #filteredNews.append(data.text)
        #        print(data.text)


        #    print()
        #print(filteredNews)
        #for data in filteredNews:
        #    if data.find('ul', class_='links'):
        #        #filteredNews.append(data.text)
        #        print(data.text)
        #print(filteredNews)
        #for data in allNews:
        #    if data.find('ul', class_='links') is not None:
        #        filteredNews.append(data.text)
        #soup = BeautifulSoup('search_media.html', 'html.parser')
        #return allNews
        return allNews if allNews else None

#media_page.write_to_html(str(5212441))
#parse_html_media_page()
#parse_html_media_page(str(parse_html_search_media('Ривердейл')))

#def get_img(name):
#    №parse_html_media_page(str(parse_html_search_media(str(name))))
def get_img(name):
    try:
        result = parse_html_media_page(str(parse_html_search_media(str(name))))
        print(result)
        if result is None:
            print("Картинка не найдена")
        else:
            print(result)
            return result
            
    except Exception as e:
        print(f"Произошла ошибка при выполнении parse_html_media_page: {e}")
        #result = 'https://avatars.mds.yandex.net/get-kinopoisk-image/1900788/12835c3a-225e-4791-a0fd-f60dc50080de/1920x'


#get_img("Шоу")
#parse_html_media_page(parse_html_search_media('Во все тяжкие'))


get_img("Фишер")

