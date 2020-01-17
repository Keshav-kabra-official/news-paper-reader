import requests as rq
import json

def read(string_to_read):
    from win32com.client import Dispatch
    speak= Dispatch("SAPI.spvoice")
    speak.Speak(string_to_read)


def get_category():
    print("Please select category of news\n1- General\n2- Business\n"
          "3- Entertainment\n4- Health\n5- Science\n6- Sports\n7- Technology\n")
    category=int(input("Your Input"))
    if category<1 or category>7:
        read("Please select a valid Category from List")
        print("Please select a valid Category from List")
        get_category()
    return category


def get_news(category):
    print(category)
    if category == 1:
        category = "general"
    if category == 2:
        category = "business"
    elif category == 3:
        category = "entertainment"
    elif category == 4:
        category = "health"
    elif category == 5:
        category = "science"
    elif category == 6:
        category = "sport"
    elif category == 7:
        category = "Technology"

    API_KEY="6dc31be9789842ba952258f46370a90c"
    api_url= f"https://newsapi.org/v2/top-headlines?country=in&category={category}&apiKey={API_KEY}"
    print(f"Please wait i am loading breaking newses from {category} Category for you")
    read(f"Please wait i am loading breaking newses from {category} Category for you")
    top_news= rq.get(api_url).text
    news_json= json.loads(top_news)
    print()
    for x in news_json["articles"]:
        print(f"{x['title']}")
        read(f"{x['title']}")


if __name__ == '__main__':
    print("Hi user! Welcome to news reader")
    read("Hi user! Welcome to news reader. Please Select a category from the list")
    category=get_category()
    get_news(category)
