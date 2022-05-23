import random
# 가장 많이 나온 단어를 차트에 그려준다.

def run():
    import russelCsvRead
    import emotionCsvRead
    import categoryCsvRead
    import coinedWordCsvRead
    import datetime
    import numpy

    # 러셀 모델에 뿌려질 단어 최대 개수
    max_words = 20
    # 폰트 최대사이즈
    max_font_size = 60
    # 폰트 최소사이즈
    min_font_size = 26

    def create_wordcount_list():
        from nltk import collections
        filename = '31 Complete.txt'
        f = open(filename, 'r')

        # \n같은거 없애고 단어로만 자르기 위해 split 그리고 그걸 counter에 넣어줌
        c = collections.Counter(f.read().split())

        # c.most_common(num) 빈도수 상위 num만큼만 다루겠다는 의미
        # word_cloud_list[0] 하면 단어, word_cloud_list[1] 하면 빈도수 출력됨
        word_cloud_list = c.most_common(max_words)
        wordlist = []
        maplist = []

        for i in word_cloud_list:
            wordlist.append(i[0])
            maplist.append(i)
            # print(i[0])

        f.close()

        return wordlist, maplist

    colorList = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'black', 'red', 'blue', 'yellow', 'Brown',
                 'Chocolate', 'blue', 'purple']

    # scatter 관련 -> https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.scatter.html

    create_wordcount_list, create_wordcount_maplist = create_wordcount_list()

    russelWord = russelCsvRead.run()
    categoryWord = categoryCsvRead.run()
    emotionWord = emotionCsvRead.run(create_wordcount_list)
    coinedWord = coinedWordCsvRead.run(create_wordcount_list)

    # 신조어감정단어도 감정단어랑 합쳐버리자
    emotion_word_sum = emotionWord + coinedWord


    print('--------------- 빈도수 상위', max_words, '개 -------------------')
    for i in create_wordcount_maplist:
        print(i)
    print('----------------------------------------------------------------')

    # 1위부터 20위까지 폰트 수 설정 (ex : 1 = 10.0, 2 = 12.10, 3 = 14.21 ........)
    font_scale_list = []
    for i in range(0, max_words):
        num = min_font_size + (max_font_size - min_font_size) / (max_words - 1) * i
        font_scale_list.append(num)

    # 1위부터 20위 까지 카운트 수 설정
    max_count = create_wordcount_maplist[0][1]
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

    for i in emotion_word_sum:
        for j in create_wordcount_maplist:
            # print(i[0], j[0])
            if (i[0] == j[0]):
                i.append(j[1])

    # 그 카운트를 폰트사이즈로 변환해서 수정해준다.
    for i in emotion_word_sum:
        for j in range(0, max_words):
            if (i[4] >= count_scale_list[j]):
                size = j

        i[4] = font_scale_list[size]
        # print(font_scale_list[size])

    def plot_with_labels(russelWord, emotionWord, filename='tsneTest.png'):
        import matplotlib
        import matplotlib.pyplot as plt # 파이 플로트, 그래프 그려주는것
        from matplotlib import font_manager

        russelFont = font_manager.FontProperties(fname='c:/Windows/Fonts/HMKMRHD.ttf', size=14)
        # emotionFont = font_manager.FontProperties(fname='c:/Windows/Fonts/NanumMyeongjo.ttf', size=28)
        emotionFont = font_manager.FontProperties(fname='c:/Windows/Fonts/HMKMRHD.ttf', size=14)
        categoryFont = font_manager.FontProperties(fname='c:/Windows/Fonts/HMKMRHD.ttf', size=14)

        fig = plt.figure(figsize=(18, 18))  # 그래프의 가로세로 크기
        ax = fig.gca()
        ax.set_xlim([-1, 1])  # x축의 한계
        ax.set_ylim([-1, 1])  # y축의 한계

        plt.annotate(s='', xy=(1, 0), xytext=(-1, 0), arrowprops=dict(arrowstyle='<->'))
        plt.annotate(s='', xy=(0, 1), xytext=(0, -1), arrowprops=dict(arrowstyle='<->'))
        plt.title('타이틀') ##
        plt.xlabel('x축 한글표시', fontproperties=font_manager.FontProperties(fname='c:/Windows/Fonts/NanumGothic.ttf')) ##
        plt.ylabel('y축 한글표시', fontproperties=font_manager.FontProperties(fname='c:/Windows/Fonts/NanumGothic.ttf')) ##

        ax.set_xticks(numpy.arange(-1.0, 1.05, 0.05))  # x축은 0부터 10까지인데 그 사이 간격을 0.5로
        ax.set_yticks(numpy.arange(-1.0, 1.05, 0.05))

        # 러셀 단어 배치
        for line in russelWord:
            word = line[0]
            x = float(line[1])
            y = float(line[2])

            plt.scatter(x, y, color='red', s=150, alpha=1, edgecolors='none')  # 마커, s=사이즈 #edgecolors = 테두리
            # 포인트에 대한 주석달기 (이름)
            plt.annotate(word, xy=(x, y),
                         xytext=(30, 4),  # 텍스트가 점이랑 떨어져있는 정도
                         textcoords='offset points', fontproperties=font_manager.FontProperties(fname='c:/Windows/Fonts/NanumGothicBold.ttf'),
                         ha='right', va='bottom', size='14',
                         color='black', weight="bold", alpha=1.0,
                         # arrowprops=dict(arrowstyle="->")
                         )

        # # 감정 단어 배치 ##
        for line in emotion_word_sum:
            if line[2] == '30':
                continue

            word = line[0]
            x = float(line[1])
            y = float(line[2])

            plt.scatter(x, y)  # 마커, s=사이즈
            # 포인트에 대한 주석달기 (이름)
            plt.annotate(word, xy=(x, y),
                         xytext=(2, 4),  # 텍스트가 점이랑 떨어져있는 정도
                         textcoords='offset points',
                         fontproperties=font_manager.FontProperties(fname='c:/Windows/Fonts/NanumGothicBold.ttf', size=line[4]),
                         ha='right', va='bottom',
                         # color=colorList[random.randrange(0, len(colorList))],
                         color='blue',
                         alpha=0.60,     # 투명도
                         weight="bold"
                         # arrowprops=dict(arrowstyle="->")
                         )

            break

        i = 0
        # 카테고리 단어 배치
        for line in categoryWord:
            if line[2] == '30':
                continue

            word = line[0]
            x = float(line[1])
            y = float(line[2])

            # 마커, s=사이즈 facecolors=none = 채우기 없음 alpha = 투명도, edgecolor='none' = 가장자리색 없음, 색 = color='red' 또는 c=숫자(0~10000)
            markSize = 250 * float(line[3])
            plt.scatter(x, y, c=colorList[i], s=markSize * markSize, alpha=0.2)
            # plt.scatter(x, y, c='yellow', s=markSize * markSize, alpha=0.2)
            # 포인트에 대한 주석달기 (이름)
            plt.annotate(word, xy=(x, y),
                         xytext=(14, 25),  # 텍스트가 점이랑 떨어져있는 정도
                         textcoords='offset points', fontproperties=categoryFont, ha='right', va='bottom',
                         color='red', alpha=0.60
                         # arrowprops=dict(arrowstyle="->")
                         )
            i += 1

        plt.grid(linestyle=':')  # 격자무늬
        plt.savefig('그래프.png', bbox_inches='tight')
        plt.show()


# plt 저장이 안되는 것 같아서 잠시 주석 처리 ##
    try:
        import matplotlib
        import matplotlib.pyplot as plt
        from matplotlib import font_manager

        plot_with_labels(russelWord, emotionWord)

    except ImportError:
        print("Please install sklearn and matplotlib to visualize embeddings.")

    print("end", datetime.datetime.now())

    plot_with_labels(russelWord, emotionWord)

run()