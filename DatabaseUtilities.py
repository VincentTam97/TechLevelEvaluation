from pymongo import MongoClient


def connectDatabase():
    client = MongoClient('localhost', 27017)
    database = client['config']
    collection = database['yisuo_english_paper_done']

    return collection


def findKeywordsByThisField(field_require):
    collection = connectDatabase()
    articles = collection.find({'field': field_require})
    field_keyword_list = []
    for article in articles:
        keywords = article['keywords'].split('; ')
        #print(keywords)
        field_keyword_list.extend(keywords)

    return field_keyword_list