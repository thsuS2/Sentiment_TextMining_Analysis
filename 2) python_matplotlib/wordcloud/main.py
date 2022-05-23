def morpheme_analysis(file_name):
    import csv
    from konlpy.tag import Hannanum
    t = Hannanum()
    # 감정표현가능 형태소 분류한 거 기록할 파일 오픈
    writeFile = open('31.txt', 'w')  # 67번째 줄과 같은 파일
    # 형태소마다 어떻게 들어갔는지 기록할 파일 오픈

    # 총 단어 개수
    wordCount = 0
    # 감성 표현이 가능한 품사인
    # 명사, 동사, 형용사, 감탄사에 해당하는 형태소만 추출했을 때의 단어개수
    morWordCount = 0
    i = 0
    with open(file_name, newline='') as csvfile:
        readFile = csv.reader(csvfile, delimiter=',')
        for line in readFile:
            tagKo = t.pos(line[1])
            print(line[1])

            wordCount += len(tagKo)
            for e in tagKo:
                if (e[1] == 'N') or (e[1] == 'P') or (e[1] == 'I'):
                    print(e[0], file=writeFile)
                    print(e[0] + " : " + e[1])
                    morWordCount += 1


    print('단어개수 ', wordCount)
    print('감정표현가능 형태소만 분류한 개수 ', morWordCount)

def create_dictionary():
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

    f = open('감정단어사전 647개 스테밍.csv', 'r') # emotionCsvRead.py 파일명 통일해줘야함
    rdr = csv.reader(f)

    list = []

    for line in rdr:
        list.append(line)

    f.close()
    return list

def dictionary_matching():
    # 감정단어사전 생성
    dictionaryList = create_dictionary()

    # 감정단어와 매칭된 형태소분석 완료 단어를 기록하기 위한 파일 생성
    w = open('31 Complete.txt', 'w') # 102번째 줄과 같은 이름

    # 감정단어사전과 매칭시키기 위한 형태소분석 완료 단어 데이터 파일 오픈
    file_name = '31.txt'   # 6번째 줄과 같은 파일
    readFile = open(file_name, 'rt')

    # 매칭된 단어 개수
    successCount = 0

    while True:
        # 한 줄을 읽을 때 개행문자도 같이 읽혀서 제거해줌
        line = readFile.readline().rstrip('\n')

        if not line:
            print('감정단어사전 매칭 완료')
            readFile.close()
            break

        for i in dictionaryList:
            # ['1', '2'] 이렇게 2개이상일 때만 즉, 기본형 플러스 변형어도 갖고 있을 때
            if len(i) > 1:
                print(i[0]+','+line)
                # 형태소분석한 단어가 감정표현단어의 기본형과 같거나 변형어와 같다면
                if line == i[0] or line in i[1].split('_'):
                    w.write(i[0] + '\n')
            # ['1'] 이런식으로 기본형만 있을 때 같은지 비교
            elif line == i[0]:
                w.write(i[0] + '\n')
                print('3')

def create_wordcloud(): # 워드 클라우드 돌아가는 함수
    from os import path
    from wordcloud import WordCloud

    font_path = 'c:/Windows/Fonts/HMKMRHD.ttf'
    d = path.dirname(__file__)

    # 워드클라우드 뿌릴 데이터 파일 오픈
    filename = '31 Complete.txt' # 이 데이터를 기반으로 워드클라우드 만든다. 64번째 줄과 파일명 같게
    text = open(path.join(d, filename)).read()

    import matplotlib.pyplot as plt

    # relative_scaling = 0 ~ 1 이고 0일 수록 빽빽히 차게 된다.
    wordcloud = WordCloud(max_font_size=40, font_path=font_path, background_color='white', relative_scaling=0.48).generate(text)
    plt.figure(figsize=(18, 18))
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig('wordcloud.png', bbox_inches='tight')
    plt.show()

def run(file_path=''):
    if __name__ == '__main__':
        # 분석할 텍스트파일 경로
        file_name = 'dataset/5-1.csv'
        # file_name = file_path

        print(file_name, '분석중....')

        # 형태소분석
        morpheme_analysis(file_name)

        # # 감정단어사전 매칭
        dictionary_matching()
        #
        # # 워드클라우드 생성
        create_wordcloud()

        # 러셀모델에 플로팅
        import russel_floating
        russel_floating.run()


run()