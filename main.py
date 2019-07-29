'''
 @author : Keshav Kabra
'''

# ------------------------------------ PROGRAM ----------------------------------- #

import requests
import json
import datetime

# --------------------- Function to speak the news --------------------- #
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Rate = -1
    speak.Speak(str)

if __name__ == '__main__':

    # -------------------------- Today's Date --------------------------- #
    dt = datetime.date.today()
    print(f"Date : {dt}\n")
    speak(f"Welcome; Today is {dt}. I am here to read today's news headlines : ")

    # --------------- News-headlines or Description also ---------------- #

    speak("If you want the description of news as well, press d , Press any other key to hear"
          " headlines only.")
    print("If you want the description of news as well, press d")
    x = input()
    print("\n  -- Copy the URL and Paste it in your browser to Read full article --\n")

    # ------------------- Getting news from internet -------------------- #
    url = ('https://newsapi.org/v2/top-headlines?'
           # 'sources=news_paper_name'
           'country=your_country'
           'apiKey=your_api_key')
    response = requests.get(url)
    text = response.text
    j = json.loads(text)

    if x=='d' or x=='D':
        speak("OK, so today's news with description are : ")
    else :
        speak("OK, so today's news headlines are : ")

    # --------------- Speaking and Printing top 10 news ---------------- #

    art = j['articles']
    i = 0
    for articles in art:
        print(articles['title'])
        # news as well as description
        if x=='d' or x=='D':
            print("   ", articles['description'])
            speak(f" News {i+1} : ")
            speak(articles['title'])
            speak("Description : ")
            speak(articles['description'])
        # news headlines only
        else:
            speak(f" News {i+1} : ")
            speak(articles['title'])
        print("    For more : ", articles['url'])
        i += 1

        print()

    speak("Thank you very much !")
    print("\nThank you very much !!!")
    print("\n ***** Designed by : KESHAV KABRA *****")
    speak("Press any key to exit ")
    x = input()
