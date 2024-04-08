import sqlite3
import media_get

def fetch_data():
    try:
        # Устанавливаем соединение с базой данных
        db = sqlite3.connect("mediabase.db")

        # Создаем курсор
        cursor = db.cursor()

        # Выполняем SQL-запрос для извлечения данных из базы
        cursor.execute('SELECT MEDIA_NAME, IMAGE FROM MEADIABASE')

        # Получаем результаты запроса
        data = cursor.fetchall()

        # Создаем массив для хранения результатов
        result = []

        # Перебираем записи из базы
        for record in data:
            name, image = record
            if image is None:
                # Если изображение отсутствует, используем метод p(name)
                print(name)
                image_url = media_get.get_img(name)
                print(f"New image URL for {name}: {image_url}")  # Добавлено для отладки
                # Обновляем базу данных с новым URL изображения
                update_query = '''
                    UPDATE MEADIABASE
                    SET IMAGE = ?
                    WHERE MEDIA_NAME = ?
                '''
                print(f"SQL query: {update_query}")  # Добавлено для отладки
                cursor.execute(update_query, (image_url, name))
                db.commit()  # Сохраняем изменения
            else:
                image_url = image
            # Добавляем данные в массив результатов
            result.append({"name": name, "image": image_url})

        # Закрываем соединение с базой данных
        cursor.close()
        db.close()

        return result
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

# Пример использования функции fetch_data
def main():
    data = fetch_data()
    if data is not None:
        for item in data:
            print(f"Name: {item['name']}, Image: {item['image']}")
    else:
        print("Не удалось получить данные из базы данных")


main()
