def run(create_wordcount_list):
    import sys
    import csv
    # csv 읽는 부분

    maxInt = sys.maxsize
    decrement = True

    while decrement:
        decrement = False
        try:
            csv.field_size_limit(maxInt)
        except OverflowError:
            maxInt = int(maxInt / 10)
            decrement = True

    f = open('../coinedWordData.csv', 'r')
    rdr = csv.reader(f)

    list = []
    for line in rdr:
        # 감정단어가 데이터셋에서 감전단어사전으로 걸러진 상위 빈도수단어 리스트에 없는거면 건너뛴다.
        if line[0] not in create_wordcount_list:
            continue

        line.append('임시카테고리') # 신조어 감정단어는 기본감정단어와 다르게 카테고리가 없으니까 임의로 추가해줌
        list.append(line)
        # print(line[0])

    f.close()
    return list

# if __name__ == '__main__':
#     run()
