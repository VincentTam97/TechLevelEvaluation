import numpy as np
import pandas as pd
from scipy.optimize import leastsq
import pylab as pl


def predictWithPolyFunction(x, y):
    z = np.polyfit(x, y, 3)
    p = np.poly1d(z)
    fu_x = np.arange(1, 30, 1)
    fu_y = p(fu_x)
    return fu_y


def getPeriod1(y_pred):
    original_data = pd.DataFrame(y_pred)
    diff_1 = original_data.diff()
    median = original_data.median()

    candidate_indices = []
    for index, row in original_data.iterrows():
        if row[0] < median[0]:
            candidate_indices.append(index)

    possible_candidates = pd.DataFrame(columns=('og_index', 'diff1'))
    for index, row in diff_1.iterrows():
        if index in candidate_indices:
            possible_candidates.loc[possible_candidates.shape[0]] = {'og_index': index, 'diff1': row[0]}

    return int(possible_candidates.iloc[possible_candidates['diff1'].idxmin()]['og_index'])


def getPeriod2(y_pred):
    original_data = pd.DataFrame(y_pred)
    diff_1 = original_data.diff()
    maxnum = original_data.max()

    candidate_indices = []
    for index, row in original_data.iterrows():
        if row[0] < maxnum[0]:
            candidate_indices.append(index)

    possible_candidates = pd.DataFrame(columns=('og_index', 'diff1'))
    for index, row in diff_1.iterrows():
        if index in candidate_indices:
            possible_candidates.loc[possible_candidates.shape[0]] = {'og_index': index, 'diff1': row[0]}

    return int(possible_candidates.iloc[possible_candidates['diff1'].idxmax()]['og_index'])


def getPeriod3(y_pred):
    original_data = pd.DataFrame(y_pred)
    diff_1 = original_data.diff()
    median = original_data.median()

    candidate_indices = []
    for index, row in original_data.iterrows():
        if row[0] > median[0]:
            candidate_indices.append(index)

    possible_candidates = pd.DataFrame(columns=('og_index', 'diff1', 'diff1_abs'))
    for index, row in diff_1.iterrows():
        if index in candidate_indices:
            possible_candidates.loc[possible_candidates.shape[0]] = {
                'og_index': index, 'diff1': row[0], 'diff1_abs': abs(row[0])
            }

    return int(possible_candidates.iloc[possible_candidates['diff1_abs'].idxmin()]['og_index'])


def getPeriod4(y_pred):
    original_data = pd.DataFrame(y_pred)
    diff_1 = original_data.diff()
    diff_2 = diff_1.diff()
    period3 = getPeriod3(y_pred)

    candidate_indices = []
    for index, row in original_data.iterrows():
        if index > period3:
            candidate_indices.append(index)

    possible_candidates = pd.DataFrame(columns=('og_index', 'diff2'))
    for index, row in diff_2.iterrows():
        if index in candidate_indices:
            possible_candidates.loc[possible_candidates.shape[0]] = {'og_index': index, 'diff2': row[0]}

    return int(possible_candidates.iloc[possible_candidates['diff2'].idxmin()]['og_index'])


# to test
def verifyPeriod(index_1, index_2, index_3, index_4):
    if index_1 < index_2 < index_3 < index_4:
        return [1, 1, 1, 1]
    elif index_1 < index_2 < index_3:
        return [1, 1, 1, 0]
    elif index_1 < index_2 < index_4:
        return [1, 1, 0, 1]
    elif index_1 < index_3 < index_4:
        return [1, 0, 1, 1]
    elif index_2 < index_3 < index_4:
        return [0, 1, 1, 1]
    elif index_2 < index_3:
        return [0, 1, 1, 0]
    elif index_1 < index_2:
        return [1, 1, 0, 0]
    elif index_1 < index_3:
        return [1, 0, 1, 0]
    elif index_1 < index_4:
        return [1, 0, 0, 1]
    elif index_2 < index_4:
        return [0, 1, 0, 1]
    elif index_3 < index_4:
        return [0, 0, 1, 1]
    else:
        return [0, 0, 1, 0]


def getAllPeriod(num_y):
    x = np.arange(1, 30, 1)
    y = np.array(num_y)
    y_pred = predictWithPolyFunction(x, y)
    index_1 = getPeriod1(y_pred)
    index_2 = getPeriod2(y_pred)
    index_3 = getPeriod3(y_pred)
    index_4 = getPeriod4(y_pred)
    verify_list = verifyPeriod(index_1, index_2, index_3, index_4)
    index_list = [index_1, index_2, index_3, index_4]
    for i in range(4):
        if verify_list[i] == 0:
            index_list[i] = 99

    period_collection = []
    for i in range(29):
        if i == index_list[0]:
            period_collection.append("萌芽期")
        elif i == index_list[1]:
            period_collection.append("成长期")
        elif i == index_list[2]:
            period_collection.append("成熟期")
        elif i == index_list[3]:
            period_collection.append("衰退期")
        else:
            period_collection.append("")

    return period_collection


def analyseDBContent():
    fields = ['人工智能', '智能制造', '大数据', '云计算', '工业互联网', '网络安全', '集成电路', '物联网']
    for i in range(8):
        filename = str(i) + fields[i] + '_dbcontent.txt'
        reader = open(filename, 'r')
        line = reader.readline()
        result_list = eval(line)
        for j in range(8):
            pre_time = result_list[3][j]
            for item in pre_time:
                if (item != '') and (pre_time.index(item)%2 != 0):
                    if pre_time[pre_time.index(item)-1] == '':
                        pre_time[pre_time.index(item)-1] = item
                    pre_time[pre_time.index(item)+1] = ''
            result_list[3][j] = pre_time
        print(result_list)
        result_str = str(result_list)
        result_str = result_str.replace('\'', '\"')
        result_str = result_str.replace(', ', ',')
        writer = open(filename, 'w')
        writer.write(result_str)