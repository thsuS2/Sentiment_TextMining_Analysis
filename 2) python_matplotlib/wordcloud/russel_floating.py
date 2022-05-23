import random
import math

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class analysis:
    def __init__(self):
        self.positiveWordCount = 0
        self.nagativeWordCount = 0
        self.categoryCountList = {}
        self.categoryNameList = []

    # list안에 ['기쁨', '슬픔', '공포', '분노', '혐오', '놀람', '흥미', '지루함', '통증', '중성'] 입력
    def setCategoryNameList(self, categoryWord):
        for i in range(0, len(categoryWord) - 1):
            self.categoryNameList.append(categoryWord[i][0])
        # print(self.categoryNameList)

    # 감성범주 "기타"는 일단 빼자
    # {'기쁨': 0, '슬픔': 0, '공포': 0, '분노': 0, '혐오': 0, '놀람': 0, '흥미': 0, '지루함': 0, '통증': 0, '중성': 0} 이렇게 초기화
    def setCategoryCountList(self, categoryWord):
        for i in range(0, len(categoryWord) - 1):
            self.categoryCountList[categoryWord[i][0]] = 0
            # self.categoryCountList[categoryWord[i][0]].append(categoryWord[i][0])
            # self.categoryCountList[categoryWord[i][0]].append(0)
        # print(self.categoryCountList)

    # 유클리드 디스턴스 구하기
    def getDistance(self, p1, p2):
        # p1 = Point2D(x=30, y=20)  # 점1
        # p2 = Point2D(x=60, y=50)  # 점2
        # getDistance(p1, p2)
        a = p2.x - p1.x  # 선 a의 길이
        b = p2.y - p1.y  # 선 b의 길이
        c = math.sqrt((a * a) + (b * b))  # (a * a) + (b * b)의 제곱근을 구함
        return c

    # 긍정부정 개수 세기 (x좌표가 양수면 긍정, 음수면 부정으로 그 단어의 빈도수만큼 카운팅)
    def isPositiveOrNagative(self, line):
        if (float(line[1]) > 0):
            self.positiveWordCount += line[5]
        elif (float(line[1]) < 0):
            self.nagativeWordCount += line[5]

    def categoryWordCounting(self, line, categoryWord):
        for i in range(0, len(categoryWord)):
            # 기쁨의 x,y좌표, 슬픔의 x,y좌표 ........
            a = Point2D(x=float(categoryWord[i][1]), y=float(categoryWord[i][2]))
            b = Point2D(x=float(line[1]), y=float(line[2]))
            distance = self.getDistance(a, b)

            # 유클리드 거리가 0.4보다 작으면
            if distance <= 0.4:
                # 가령 "하하"가 "기쁨" 근처에 있어도 "하하"의 대표감성이 "흥미"기 때문에 "기쁨"에 카운팅 되지 않는다.
                # 가령 "하하"의 대표감성이 "흥미 공포"인 경우는 처리하지 않았다. 대표감성이 1개인 경우만 해당된다.
                categoryNameListTemp = self.categoryNameList.copy()
                self.categoryNameList.remove(categoryWord[i][0])
                # print(categoryWord[i][0], '삭제')
                # print(self.categoryNameList)

                # if line[3] not in self.categoryNameList:
                    # print(line[0], '(', line[3], ', ', line[5], ') => ', categoryWord[i][0], '매칭')
                self.categoryCountList[categoryWord[i][0]] += line[5]  # 빈도수만큼 카운팅

                self.categoryNameList = categoryNameListTemp.copy()

def run(analysis = analysis()):
    import russelCsvRead
    import emotionCsvRead
    import categoryCsvRead
    import coinedWordCsvRead
    import datetime
    import numpy
    import pie_chart
    import radar_chart


    # 폰트 최대사이즈 (26~60 = word // 300~4500 = scatter)
    # max_font_size = 60
    # min_font_size = 26
    max_font_size = 4800
    min_font_size = 200
    # max_font_size = 90
    # min_font_size = 12

    # min_scatter_size = 4500
    # max_scatter_size = 300

    def create_wordcount_list():
        from nltk import collections
        filename = '31 Complete.txt' # 파일 명 쓰기
        f = open(filename, 'r')

        # \n같은거 없애고 단어로만 자르기 위해 split 그리고 그걸 counter에 넣어줌
        c = collections.Counter(f.read().split())

        # c.most_common(num) 빈도수 상위 num만큼만 다루겠다는 의미 / # word_cloud_list[0] 하면 단어, word_cloud_list[1] 하면 빈도수 출력됨
        # word_cloud_list = c.most_common(34)
        word_cloud_list = c.most_common(len(c))
        wordlist = []
        maplist = []

        for i in word_cloud_list:
            # 빈도수가 1 이하면 걸러낸다.
            # if i[1] <= 2:
            #     continue

            wordlist.append(i[0])
            maplist.append(i)
            # print(i[0])

        f.close()

        return wordlist, maplist

    colorList = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'black', 'red', 'blue', 'yellow', 'Brown',
                 'Chocolate', 'blue', 'purple']

    # scatter 관련 -> https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.scatter.html

    create_wordcount_list, create_wordcount_maplist = create_wordcount_list()

    # 러셀 모델에 뿌려질 단어 최대 개수
    if len(create_wordcount_maplist) < 20:
        max_words = len(create_wordcount_maplist)
    else:
        max_words = len(create_wordcount_maplist)
        # max_words = 20

    russelWord = russelCsvRead.run()
    categoryWord = categoryCsvRead.run()
    emotionWord = emotionCsvRead.run(create_wordcount_list)
    coinedWord = coinedWordCsvRead.run(create_wordcount_list)

    # analysis 클래스에 있는 emotionCountList 초기화
    analysis.setCategoryCountList(categoryWord)

    # analysis 클래스에 있는 emotionNameList 초기화
    analysis.setCategoryNameList(categoryWord)

    # 신조어감정단어도 감정단어랑 합쳐버리자
    emotion_word_sum = emotionWord + coinedWord

    lemCountList = []
    # print('--------------- 빈도수 상위', max_words, '개 -------------------')
    for i in create_wordcount_maplist:
        # print(i)
        lemCountList.append(i[1])
    # print('----------------------------------------------------------------')

    # 1위부터 20위까지 폰트 수치 설정 (ex : 1 = 10.0, 2 = 12.10, 3 = 14.21 ........)
    font_scale_list = []
    for i in range(0, max_words):
        num = min_font_size + (max_font_size - min_font_size) / (max_words - 1) * i
        font_scale_list.append(num)

    # 1위부터 20위 까지 카운트 수 설정
    max_count = create_wordcount_maplist[0][1]
    print('감성사전 필터링 결과\n', create_wordcount_maplist)
    min_count = create_wordcount_maplist[max_words - 1][1]

    count_scale_list = []
    for i in range(0, max_words):
        num = min_count + (max_count - min_count) / (max_words - 1) * i
        count_scale_list.append(int(num)) # 소수점 버림

    # print(emotion_word_sum)
    # print(font_scale_list)
    # print(count_scale_list)
    # emotion_word_sum 에 apeend 각각의 단어에 어떤 폰트사이즈가 들어가야하는지 설정
    # 일단 [['겁나다', '-0.46', '0.53', '공포', 29], ['고통스럽다', '-0.34', '0.33', '통증', 41] 이런식으로 카운트만 추가해서 넣어주고
    # print(emotion_word_sum)

    # ['감격하다', '0.62', '0.81', '기쁨'] => ['감격하다', '0.62', '0.81', '기쁨', 2]
    for i in emotion_word_sum:
        for j in create_wordcount_maplist:
            # print(i[0], j[0])
            if (i[0] == j[0]):
                i.append(j[1])


    size = 0
    # 그 카운트를 폰트사이즈로 변환해서 수정해준다.
    # [단어, x좌표, y좌표, 감정범주] ==> [단어, x좌표, y좌표, 감정범주, 폰트사이즈]
    for i in emotion_word_sum:
        for j in range(0, max_words):
            # print(j)
            if (i[4] >= count_scale_list[j]):
                size = j


        i[4] = font_scale_list[size]
        # print(font_scale_list[size])

    # print(emotion_word_sum)

    # 단어빈도수를 추가해준다
    # [단어, x좌표, y좌표, 감정범주, 폰트사이즈] ==> [단어, x좌표, y좌표, 감정범주, 폰트사이즈, 단어빈도수]
    # i = 0
    # for element in emotion_word_sum:
    #     element.append(lemCountList[i])
    #     i += 1
    for i in emotion_word_sum:
        for j in create_wordcount_maplist:
            # print(i[0], j[0])
            if (i[0] == j[0]):
                i.append(j[1])

    def plot_with_labels(russelWord, emotionWord, filename='tsneTest.png'):
        try:
            import matplotlib
            import matplotlib.pyplot as plt
            from matplotlib import font_manager

            russelFont = font_manager.FontProperties(fname='c:/Windows/Fonts/HMKMRHD.ttf', size=14)
            # emotionFont = font_manager.FontProperties(fname='c:/Windows/Fonts/NanumMyeongjo.ttf', size=28)
            emotionFont = font_manager.FontProperties(fname='c:/Windows/Fonts/HMKMRHD.ttf', size=14)
            categoryFont = font_manager.FontProperties(fname='c:/Windows/Fonts/HMKMRHD.ttf', size=14)

            fig = plt.figure(figsize=(18, 10))  # 그래프의 가로세로 크기
            # fig = plt.figure(figsize=(10, 6))  # 그래프의 가로세로 크기
            ax = fig.gca()
            ax.set_xlim([-1, 1])  # x축의 한계
            ax.set_ylim([-1, 1])  # y축의 한계

            plt.annotate(s='', xy=(1, 0), xytext=(-1, 0), arrowprops=dict(arrowstyle='<->'))
            plt.annotate(s='', xy=(0, 1), xytext=(0, -1), arrowprops=dict(arrowstyle='<->'))
            # plt.title('타이틀')
            # plt.xlabel('x축 한글표시', fontproperties=font_manager.FontProperties(fname='c:/Windows/Fonts/NanumGothic.ttf'))
            # plt.ylabel('y축 한글표시', fontproperties=font_manager.FontProperties(fname='c:/Windows/Fonts/NanumGothic.ttf'))

            ax.set_xticks(numpy.arange(-1.0, 1.05, 0.05))  # x축은 0부터 10까지인데 그 사이 간격을 0.5로
            ax.set_yticks(numpy.arange(-1.0, 1.05, 0.05))

            # line = [단어, x좌표, y좌표, 감정범주, 폰트사이즈, 단어빈도수]
            # # 감정 단어 배치
            for line in emotion_word_sum:
                if line[2] == '30':
                    continue

                word = line[0]
                x = float(line[1])
                y = float(line[2])

                # print(line)

                plt.scatter(x, y, color='red', edgecolors='none', alpha=0.50, s=line[4])  # 마커, s=사이즈
                # plt.scatter(x, y)  # 마커, s=사이즈
                # 포인트에 대한 주석달기 (이름)
                # plt.annotate(word, xy=(x, y),
                #              xytext=(2, 4),  # 텍스트가 점이랑 떨어져있는 정도
                #              textcoords='offset points',
                #              fontproperties=font_manager.FontProperties(fname='c:/Windows/Fonts/NanumGothicBold.ttf',
                #                                                         size=line[4]),
                #              ha='right', va='bottom',
                #              # color=colorList[random.randrange(0, len(colorList))],
                #              color='blue',
                #              alpha=0.60,  # 투명도
                #              weight="bold"
                #              # arrowprops=dict(arrowstyle="->")
                #              )

                analysis.isPositiveOrNagative(line)
                analysis.categoryWordCounting(line, categoryWord)

            # 러셀 단어 배치 (18개)
            # [단어이름, x좌표, y좌표]
            for line in russelWord:
                word = line[0]
                x = float(line[1])
                y = float(line[2])

                plt.scatter(x, y, color='black', s=150, alpha=0.50, edgecolors='none')  # 마커, s=사이즈 #edgecolors = 테두리
                # 포인트에 대한 주석달기 (이름)
                plt.annotate(word, xy=(x, y),
                             xytext=(16, 4),  # 텍스트가 점이랑 떨어져있는 정도
                             textcoords='offset points',
                             fontproperties=font_manager.FontProperties(fname='c:/Windows/Fonts/NanumGothic.ttf'),
                             ha='right', va='bottom', size='14',
                             color='black', weight="bold", alpha=0.50,
                             # arrowprops=dict(arrowstyle="->")
                             )

            i = 0
            # 대표감성범주 단어 배치 (10개)
            # [단어, x좌표, y좌표, 원의크기]
            for line in categoryWord:
                if line[2] == '30':
                    continue

                word = line[0]
                x = float(line[1])
                y = float(line[2])

                # 마커, s=사이즈 facecolors=none = 채우기 없음 alpha = 투명도, edgecolor='none' = 가장자리색 없음, 색 = color='red' 또는 c=숫자(0~10000)
                markSize = 250 * float(line[3])
                # plt.scatter(x, y, c=colorList[i], s=markSize * markSize, alpha=0.2)
                plt.scatter(x, y, c='yellow', s=markSize * markSize, alpha=0.2)
                # 포인트에 대한 주석달기 (이름)
                plt.annotate(word, xy=(x, y),
                             xytext=(14, 25),  # 텍스트가 점이랑 떨어져있는 정도
                             textcoords='offset points', fontproperties=categoryFont, ha='right', va='bottom',
                             color='black', alpha=0.60
                             # arrowprops=dict(arrowstyle="->")
                             )
                i += 1

            plt.grid(linestyle=':')  # 격자무늬
            plt.savefig('emotionmodel.png', bbox_inches='tight')
            plt.show()

            # piechart 띄우기
            print(analysis.positiveWordCount, analysis.nagativeWordCount)
            pie_chart.create(analysis.positiveWordCount, analysis.nagativeWordCount)

            # radarchart 띄우기
            print(analysis.categoryCountList)
            radar_chart.create(analysis.categoryCountList)

        except ImportError:
            print("Please install sklearn and matplotlib to visualize embeddings.")







    plot_with_labels(russelWord, emotionWord)

run()