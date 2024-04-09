import sqlite3
import media_get

def fetch_data():
    try:
        # Устанавливаем соединение с базой данных
        db = sqlite3.connect("mediabase.db")

        # Создаем курсор
        cursor = db.cursor()

        # Выполняем SQL-запрос для извлечения данных из базы
        cursor.execute('SELECT MEDIA_NAME, IMAGE, KINOPOISK_RATING, GENRE, COUNTRY, SINCE FROM MEADIABASE')

        # Получаем результаты запроса
        data = cursor.fetchall()

        # Создаем массив для хранения результатов
        result = []

        # Перебираем записи из базы
        for record in data:
            name, image, kinopoisk_rating, genre_str, country_str, since = record
            genre = genre_str.split(',') if genre_str else []  # Преобразуем строку обратно в список
            country = country_str.split(',') if country_str else []  # Преобразуем строку обратно в список
            
            if image is None:
                # Если изображение отсутствует, используем метод p(name)
                print(name)
                # Получаем данные из media_get
                media_data = media_get.get_img(name)
                print(media_data)
                if media_data:
                    image_url = media_data.get('image_url')
                    rating = media_data.get('rating')
                    genre = media_data.get('genre', [])
                    country = media_data.get('country', [])
                    year = media_data.get('year')
                else:
                    print("Ошибка: Не удалось получить данные из media_get")
                    continue  # Пропускаем запись, если не удалось получить данные из media_get
                print(image_url, '\n', rating, '\n', genre, country, year)
                #print(f"New image URL for {name}: {image_url}")  # Добавлено для отладки
                # Обновляем базу данных с новыми данными
                update_query = '''
                    UPDATE MEADIABASE
                    SET IMAGE = ?, KINOPOISK_RATING = ?, GENRE = ?, COUNTRY = ?, SINCE = ?
                    WHERE MEDIA_NAME = ?
                '''
                print(f"SQL query: {update_query}")  # Добавлено для отладки
                cursor.execute(update_query, (image_url, rating, ','.join(genre), ','.join(country), year, name))
                db.commit()  # Сохраняем изменения
            else:
                image_url = image
            # Добавляем данные в массив результатов
            result.append({
                "name": name,
                "image": image_url,
                "kinopoisk_rating": kinopoisk_rating,
                "genre": genre,
                "country": country,
                "since": since
            })

        # Закрываем соединение с базой данных
        cursor.close()
        db.close()
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        result = None

    return result



# Пример использования функции fetch_data
def main():
    data = fetch_data()
    if data is not None:
        for item in data:
            print(item['genre'])
    else:
        print("Не удалось получить данные из базы данных")

#def main():
#    # Получаем все данные из базы данных
#    data = fetch_data()
#
#    # Проверяем, получены ли данные
#    if data:
#        # Выводим данные из базы
#        for item in data:
#            print("Name:", item["name"])
#            print("Image URL:", item["image"])
#            print("Kinopoisk Rating:", item["kinopoisk_rating"])
#            print("Genre:", item["genre"])
#            print("Country:", item["country"])
#            print("Since:", item["since"])
#            print("-----------------------")
#    else:
#        print("Ошибка: Не удалось получить данные из базы данных")

if __name__ == "__main__":
    main()
