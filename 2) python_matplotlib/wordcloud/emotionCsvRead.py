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

    try:
        f = open('../emotionData.csv', 'r')  # 수정 전 데이터일경우 끝에 수정전 쓸것
    except FileNotFoundError:
        print('file not found')
        return

    rdr = csv.reader(f)

    list = []
    for line in rdr:
        # 감정단어가 데이터셋에서 감전단어사전으로 걸러진 상위 빈도수단어 리스트에 없는거면 건너뛴다.
        if line[0] not in create_wordcount_list:
            continue

        list.append(line)
        # print(line[0])

    f.close()
    return list

# if __name__ == '__main__':
#     run()

