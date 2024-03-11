import requests
import datetime as dt
from googletrans import Translator

class Astro():

    def text_translator(self, text: str, scr="en", dest="ru") -> str:
        try:
            translator = Translator()
            translation = translator.translate(text=text, src=scr, dest=dest)

            return translation.text
        except Exception as ex:
            return "Не найдено информации."
    def givePhoto(self, date: str) -> (str, str):
        endPoint = 'https://api.nasa.gov/planetary/apod'
        params = {'api_key': 'DEMO_KEY', 'date': date}
        res = requests.get(endPoint, params=params).json()
        if "explanation" in res:
            explanation = res['explanation']
            explanation = Astro.text_translator(explanation)
        else:
            explanation = "Не найдено информации."
        if "url" in res:
            urlPhoto = res['url']
        else:
            urlPhoto = "https://www.istockphoto.com/ru/%D0%B2%D0%B5%D0%BA%D1%82%D0%BE%D1%80%D0%BD%D0%B0%D1%8F/%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD-%D0%BE%D1%88%D0%B8%D0%B1%D0%BA%D0%B8-404-%D1%81-%D1%84%D0%BE%D0%BD%D0%BE%D0%BC-%D0%BA%D0%BE%D1%81%D0%BC%D0%BE%D1%81%D0%B0-%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0-%D0%BD%D0%B5-%D0%BD%D0%B0%D0%B9%D0%B4%D0%B5%D0%BD%D0%B0-%D1%81%D0%BE%D0%BE%D0%B1%D1%89%D0%B5%D0%BD%D0%B8%D0%B5-gm1250923288-364912259"
        return (urlPhoto, explanation)

    def checkDate(self, userData: str) -> bool:
        try:
            userData = dt.datetime.strptime(userData, "%Y-%m-%d")
        except ValueError:
            return False
        return dt.datetime.now() > userData

        #photoURL, photoExp = givePhoto(userText)
        #params = {'chat_id': chatID, 'text': 'Нужна дата в формате ГГГГ-ММ-ДД'}
