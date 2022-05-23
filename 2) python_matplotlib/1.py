import russelCsvRead
import emotionCsvRead
import categoryCsvRead
import coinedWordCsvRead
import datetime
import numpy

colorList = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'black', 'red', 'blue', 'yellow', 'Brown', 'Chocolate', 'blue', 'purple']

# scatter 관련 -> https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.scatter.html

russelWord = russelCsvRead.run()
emotionWord = emotionCsvRead.run()
categoryWord = categoryCsvRead.run()
coinedWord = coinedWordCsvRead.run()

def plot_with_labels(russelWord, emotionWord, filename='tsneTest.png'): # 파일 이름 변경
    russelFont = font_manager.FontProperties(fname='c:/Windows/Fonts/HMKMRHD.ttf', size=14)
    # emotionFont = font_manager.FontProperties(fname='c:/Windows/Fonts/NanumMyeongjo.ttf', size=28)
    categoryFont = font_manager.FontProperties(fname='c:/Windows/Fonts/HMKMRHD.ttf', size=14)

    fig = plt.figure(figsize=(18, 18)) # 그래프의 가로세로 크기
    ax = fig.gca()
    ax.set_xlim([-1, 1])    # x축의 한계
    ax.set_ylim([-1, 1])    # y축의 한계

    plt.annotate(s='', xy=(1, 0), xytext=(-1, 0), arrowprops=dict(arrowstyle='<->'))
    plt.annotate(s='', xy=(0, 1), xytext=(0, -1), arrowprops=dict(arrowstyle='<->'))
    ax.set_xticks(numpy.arange(-1.0, 1.05, 0.05))  # x축은 0부터 10까지인데 그 사이 간격을 0.5로
    ax.set_yticks(numpy.arange(-1.0, 1.05, 0.05))


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
        # 포인트에 대한 주석달기 (이름)
        plt.annotate(word, xy=(x, y),
                 xytext=(10, 0), # 텍스트가 점이랑 떨어져있는 정도
                 textcoords='offset points', fontproperties=font_manager.FontProperties(fname='c:/Windows/Fonts/NanumGothicBold.ttf'),
                 ha='right', va='bottom',
                 color='red'
                 # arrowprops=dict(arrowstyle="->")
        )
        i += 1

    plt.grid(linestyle=':')  # 격자무늬
    plt.show()
    plt.savefig(filename)

try:
    import matplotlib
    import matplotlib.pyplot as plt
    from matplotlib import font_manager

    plot_with_labels(russelWord, emotionWord)

except ImportError:
    print("Please install sklearn and matplotlib to visualize embeddings.")

print("end", datetime.datetime.now())