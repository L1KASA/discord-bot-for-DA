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
            #print(allNews)
        else:
            print("parse_html_search_media")
            return None
        return allNews

def search_image(soup):
    image_element = soup.findAll('div', class_='styles_column__r2MWX styles_md_6__XDxd6 styles_lg_8__7Mdim styles_column__5dEFP')
    if image_element:
        image_element = image_element[0].find('img', class_='image')
        if image_element:
            image_url = image_element.get('src')
            return image_url
        else:
            print("Картинка не найдена")
            return None
    else:
        print("Не удалось найти элемент с картинкой")
        return None


def get_rating(soup):
    return(soup.find('div', class_='styles_valueBlock___nWKb').find('span', class_='film-rating-value') \
            .find('span').text)
    
def parse_html_media_page(name, filename="media_page.html"):
    media_page.write_to_html(name)
    with open(filename, "r", encoding="utf-8") as f:
        contents = f.read()
    
        soup = BeautifulSoup(contents, 'lxml')

        image_url = search_image(soup)
        if not image_url:
            print("Не удалось найти URL изображения")
            return None

        rating = get_rating(soup)
        genre = []
        country = []
        year = None 

        first = soup.findAll('div', class_='styles_root__2kxYy styles_topLine__xigow')[1].find('div', class_='styles_column__r2MWX styles_md_11__UdIH_ styles_lg_15__Ai53P') \
            .find('div').findAll('div')
        for data in first:
            if "Страна" in data.text and country == []:
                country_element  = data.findAll('a')#.find('div')

                for i in country_element:
                    country.append(i.text)

            if "Жанр" in data.text and genre == []:
                genre_element = data.find('div', class_='styles_root__5PEXQ').find('div').findAll('a')
                for i in genre_element:
                   genre.append(i.text)

            if "Год производства" and year == None:
                year = data.find('a').text
        if not image_url or not rating or not genre or not country or not year:
            print("Не удалось найти все необходимые данные")
            return None
        return {
            'image_url': image_url,
            'rating': rating,
            'genre': genre,
            'country': country,
            'year': year
        }

def get_img(name):
    try:
        result = parse_html_media_page(str(parse_html_search_media(str(name))))
        if result is None:
            print("Картинка не найдена")
        else:
            print(result)
            #return
            
    except Exception as e:
        print(f"Произошла ошибка при выполнении parse_html_media_page: {e}")
        return
        #result = 'https://avatars.mds.yandex.net/get-kinopoisk-image/1900788/12835c3a-225e-4791-a0fd-f60dc50080de/1920x'

print(parse_html_media_page(parse_html_search_media('Сяня')))

#get_img("Сяня")

