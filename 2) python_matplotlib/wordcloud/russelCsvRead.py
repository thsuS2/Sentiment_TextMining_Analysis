def run():
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

    f = open('russelData.csv', 'r')
    rdr = csv.reader(f)

    list = []
    for line in rdr:
        list.append(line)
        # print(line[1])

    f.close()
    return list

if __name__ == '__main__':
    run()
