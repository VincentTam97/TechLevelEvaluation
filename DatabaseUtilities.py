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


def countTechNumber(field, tech):
    collection = connectDatabase()
    years = [
        '1990-01-01', '1991-01-01', '1992-01-01', '1993-01-01', '1994-01-01', '1995-01-01', '1996-01-01',
        '1997-01-01', '1998-01-01', '1999-01-01', '2000-01-01', '2001-01-01', '2002-01-01', '2003-01-01',
        '2004-01-01', '2005-01-01', '2006-01-01', '2007-01-01', '2008-01-01', '2009-01-01', '2010-01-01',
        '2011-01-01', '2012-01-01', '2013-01-01', '2014-01-01', '2015-01-01', '2016-01-01', '2017-01-01',
        '2018-01-01',
    ]
    tech_count = []
    for year in years:
        this_year_count = 0
        articles = collection.find({'field': field, 'year': year})
        for article in articles:
            keywords = article['keywords'].split('; ')
            if tech in keywords:
                this_year_count = this_year_count + 1
        tech_count.append(this_year_count)

    return tech_count
