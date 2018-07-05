import DatabaseUtilities as DU
import AnalysisUtilities as AU


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


def collectTechNumber(order):
    fields = ['人工智能', '智能制造', '大数据', '云计算', '工业互联网', '网络安全', '集成电路', '物联网']
    keyword_count = generateCSVFiles()
    this_field_number_collection = []
    for top in range(8):
        tech_num = DU.countTechNumber(fields[order], keyword_count[order][top][0])
        this_field_number_collection.append(tech_num)

    return this_field_number_collection


def collectPeriodResult(order):
    fields = ['人工智能', '智能制造', '大数据', '云计算', '工业互联网', '网络安全', '集成电路', '物联网']
    keyword_count = generateCSVFiles()
    this_field_period_collection = []
    for top in range(8):
        tech_num = DU.countTechNumber(fields[order], keyword_count[order][top][0])
        tech_period = AU.getAllPeriod(tech_num)
        this_field_period_collection.append(tech_period)

    return this_field_period_collection


def generateYearSeries(start_year, year_num):
    year_list = []
    for i in range(year_num):
        year_list.append(i + start_year)

    return year_list


def generateTechSeries(order):
    keyword_count = generateCSVFiles()
    tech_list = []
    for top in range(8):
        tech = keyword_count[order][top][0]
        tech_list.append(tech)

    return tech_list


def generateResultByField(order):
    result_list = []

    year_list = generateYearSeries(1990, 29)
    tech_list = generateTechSeries(order)
    tech_num_list = collectTechNumber(order)
    period_list = collectPeriodResult(order)

    result_list.append(year_list)
    result_list.append(tech_list)
    result_list.append(tech_num_list)
    result_list.append(period_list)

    print(result_list)
    return result_list


if __name__ == '__main__':
    generateTechSeries(1)
