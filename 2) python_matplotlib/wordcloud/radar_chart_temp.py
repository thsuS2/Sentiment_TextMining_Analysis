import pandas as pd
from math import pi
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc


def create(categoryCountList):
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)

    # Attributes = ["Defending", "Dribbling", "Pace", "Passing", "Physical", "Shooting"]
    Attributes = list(categoryCountList.keys())
    # data = [24, 91, 86, 81, 67, 85, 24]
    data = list(categoryCountList.values())
    data += data[:1]  # 맨뒤에 첫번째항을 하나 더 넣어줌

    angles = [n / len(categoryCountList) * 2 * pi for n in range(len(categoryCountList))]
    angles += angles[:1]

    ax = plt.subplot(111, polar=True)

    plt.xticks(angles[:-1], Attributes)
    ax.plot(angles, data)
    ax.fill(angles, data, 'blue', alpha=0.1)

    ax.set_title('')
    plt.show()


create({'기쁨': 11, '슬픔': 697, '공포': 296, '분노': 331, '혐오': 196, '놀람': 94, '흥미': 244, '지루함': 526, '통증': 359, '중성': 17})