def create(positiveCount, nagativeCount):
    try:
        import matplotlib.pyplot as plt
        from matplotlib import font_manager, rc
        from matplotlib import style
        font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
        rc('font', family=font_name)
        style.use('ggplot')

        colors = ['lightskyblue', 'lightcoral']
        labels = ['긍정', '부정']
        sizes = [positiveCount, nagativeCount]
        explode = (0.1, 0)

        plt.rcParams['font.size'] = 18.0

        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=70,
                wedgeprops={"edgecolor": "k", 'linewidth': 1, 'antialiased': True})

        plt.show()

    except ImportError:
        print("Please install sklearn and matplotlib to visualize embeddings.")