def create(categoryCountList):
    try:
        import matplotlib.pyplot as plt
        from math import pi

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

        ax.set_title('최순실 국정 농단 사건')
        plt.show()

    except ImportError:
        print("Please install sklearn and matplotlib to visualize embeddings.")