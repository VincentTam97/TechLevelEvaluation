import DatabaseUtilities as DU
import csv

def generateCSVFiles():
    fields = ['人工智能', '智能制造', '大数据', '云计算', '工业互联网', '网络安全', '集成电路', '物联网']
    list = []
    for field in fields:
        field_list = DU.findKeywordsByThisField(field)
        list.append(field_list)

    count_list = []
    for i in range(8):
        count = {}
        for item in list[i]:
            count[item] = list[i].count(item)
        keyword_count = sorted(count.items(), key=lambda it: it[1], reverse=True)
        count_list.append(keyword_count)

        filename = str(i) + '_keywords.csv'
        writer = open(filename, 'w')
        i = 0
        for item in keyword_count:
            if i < 8:
                writer.write(item[0] + ',' + str(item[1]) + '\n')
                i = i + 1

    return count_list





if __name__ == '__main__':
    fields = ['人工智能', '智能制造', '大数据', '云计算', '工业互联网', '网络安全', '集成电路', '物联网']
    keyword_count = generateCSVFiles()

    for i in range(8):
        for top in range(8):
            print(keyword_count[i][top][0])
            tech_num = DU.countTechNumber(fields[1], keyword_count[i][top][0])
            print(tech_num)
