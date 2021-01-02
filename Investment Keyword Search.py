# HW6_3 股票消息面分析
# 接收輸入
company = input().split(',')
keyword = input().split(',')
news_title = []
while True:
    title = input()
    title = title.replace(" ", "")  # 去除空格
    if title == "INPUT_END":
        break
    news_title.append(title)

# 關鍵字根據長度排序的冗長寫法
keyword_length = []
for k in keyword:
    keyword_length.append([len(k), k])

keyword_length.sort(reverse=True)

for i, k in enumerate(keyword_length):
    keyword[i] = k[1]

# 關鍵字根據長度排序的簡潔寫法
# keyword.sort(key=len, reverse=True)


# 斷詞
company_ans = []
token_ans = []
print("news_title:", news_title)

for title in news_title:
    # company
    # 排序公司順序，出現次數多的放前面
    company_times = []
    times_list = []
    for i in range(len(company)):
        appear_times = title.count(company[i])
        if appear_times == 0:
            continue
        else:
            company_times.append([appear_times, company[i]])
            times_list.append(appear_times)
    # print("company_times:", company_times)
    company_times.sort(reverse=True)
    print("company_times:", company_times)
    print("company:", company)

    # 次數相同以輸入順序排序
    for i in range(len(company_times)):
        times = times_list.count(company_times[i][0])
        if times > 1:  # 代表出現次數一樣
            if i > 0:
                last_index = i - 1
                # 上一個的出現次數一樣，代表前面已經處理過，跳過
                if company_times[i][0] == company_times[last_index][0]:
                    continue

            # 概念上就是分成三個list，list1是相同出現次數以前的所有公司；
            # list2是預備裝重新根據輸入順序排序的出現次數一樣的公司；
            # list3 = 相同出現次數以後的所有公司
            # 將要排序的部分(calculate_area)重新根據輸入順序排序後裝回list2，就完成了
            after_index = i+times
            equal_num = times

            list1 = company_times[:i]
            list2 = []
            list3 = company_times[after_index:]

            # 將calculate_area重新根據輸入順序排序
            calculate_area = company_times[i:after_index]
            calculate_area_company = []
            for x in calculate_area:
                calculate_area_company.append(x[1])
            # print(calculate_area)
            # 從一開始的所有公司的列表中，依序找到相對應的公司
            # append到list2裡面，結果就會根據輸入順序排序
            for i in range(len(company)):
                if company[i] in calculate_area_company:
                    # 找到calculate_area中公司名稱一樣的
                    for k in range(len(calculate_area)):
                        if calculate_area[k][1] == company[i]:
                            list2.append(calculate_area[k])

            company_times = list1 + list2 + list3
    print("company_times:", company_times)
    company_string = ''
    for c in company_times:
        if company_string == '':
            company_string += c[1]
        else:
            company_string += ',' + c[1]

    if company_string == '':
        company_ans.append("NO_MATCH")
        token_ans.append("")
        continue
    else:
        company_ans.append(company_string)
    print("keyword:", keyword)

    # token
    token_index_list = []
    # token_list = []
    for key in keyword:
        idx = title.find(key)
        title_tmp = title
        while idx != -1:
            token_index_list.append([idx, len(key)])
            title_tmp = title_tmp.replace(key, " "*len(key), 1)
            idx = title_tmp.find(key)
    # 排序token_index_list，因為關鍵字不一定照新聞標題順序出現
    token_index_list.sort()

    # 移除重疊的關鍵字
    token_index_list_new = []
    for i in range(len(token_index_list)):
        if i == 0:
            token_index_list_new.append(token_index_list[i])
        else:
            last = token_index_list_new[-1]

            index0 = last[0]
            len0 = last[1]

            index1 = token_index_list[i][0]
            len1 = token_index_list[i][1]

            if index0 + len0 > index1 and len0 < len1:  # 不合條件就取代
                # print(token_index_list)
                # print(token_index_list[i])
                token_index_list_new[-1] = token_index_list[i]

            elif index0 + len0 > index1 and len0 >= len1:  # 符合條件就跳過
                # print(token_index_list[i])
                continue
            else:   # 沒有重複一律就加進去
                token_index_list_new.append(token_index_list[i])

    token_string = ''
    for i in range(len(token_index_list_new)):
        if i == 0:
            index0 = 0  # 非關鍵字起點index
        else:
            # 非關鍵字起點index，就是上個關鍵字的起始index+它的長度
            index0 = sum(token_index_list_new[i-1])

        # key1_pos
        # 非關鍵字終點index、關鍵字起點index
        index1 = token_index_list_new[i][0]
        # 關鍵字終點index
        index2 = token_index_list_new[i][0] + token_index_list_new[i][1]
        if i == 0:
            if title[index0:index1] == "":
                token_string += title[index1:index2]
            else:
                token_string += title[index0:index1] + '/' \
                                + title[index1:index2]
        else:
            if title[index1:index2] == "":
                token_string += '/' + title[index0:index1]
            else:
                token_string += '/' + title[index0:index1] + '/' \
                                + title[index1:index2]

    # 剩下最後一段
    # 沒有任何可以斷的關鍵字，就回傳原始標題
    if token_string == "":
        token_string = title
    elif title[index2-1] != title[-1]:
        token_string += '/' + title[index2:]

    # 移除可能的//，因為關鍵字可能相連
    token_string = token_string.replace("//", "/")
    token_ans.append(token_string)


# 合併公司名稱與斷詞，輸出結果
for i in range(len(company_ans)):
    if company_ans[i] == "NO_MATCH":
        print(company_ans[i])
    else:
        print(company_ans[i] + ';' + token_ans[i])
