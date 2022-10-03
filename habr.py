# Задача: пропарсить сайт habr по статьям о ds, и вернуть json файл с:
    #-названием статьи
    #-количеством лайков
    #-временем публикации
    #-теги/хабры статьи
    #-ссылкой на статью

# Импортируем необходимые библиотеки 
from encodings import utf_8
from itertools import count
from os import sep
from socketserver import DatagramRequestHandler
import requests as req
from bs4 import BeautifulSoup
import json
import tqdm

#Создаем переменную, в которую положим спарсерные данные
data = {
    "data" : []
}

# Создаем цикл, который будет перебирать поисковые страницы со статьями о DS
for page in range(1, 51):
    url = f'https://habr.com/ru/search/page{page}/?q=Data%20science&target_type=posts&order=relevance'
    resp = req.get(url)

    soup = BeautifulSoup(resp.text, "lxml")
    tags = soup.find_all(attrs= {"data-test-id" : "article-snippet-title-link"})

    # создаем цикл, который будет перебирать необходимые теги внутри страницы
    for iter in tqdm.tqdm(tags):
        # переменная для страницы статьи, которую получаем путем добавления к основной страницы части необходимой страницы
        url_object = "https://habr.com" + iter.attrs["href"]
        resp_object = req.get(url_object)
        soup_object = BeautifulSoup(resp_object.text, "lxml")

        # переменная для лайков
        tags_like = soup_object.find(attrs= {"data-test-id" : "votes-meter-value"})
        # переменная для даты и времени поста
        tags_time = soup_object.find("time")

        #Цикл для перебора и записи тегов. Здесь ошибка, так как выводится только последний тег     
        for x in soup_object.find_all(class_="tm-tags-list__link"):
            tags_habr = str(x.text)
            print(tags_habr)
         
        #добавляем в пеерменную data словарь
        data["data"].append({
            "Title:" : iter.text,
            "Like:" : tags_like.text,
            "Data:" : tags_time.text, 
            "Link:" : url_object,
            "Tags:" : tags_habr
            })           
        #Записываем инфомацию в файл после каждого круга
        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=1, ensure_ascii=False)
        

        
