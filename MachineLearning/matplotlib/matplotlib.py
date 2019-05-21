import matplotlib.pyplot as plt
import pandas as pd

if __name__ == '__main__':
    unrate = pd.read_csv('unrate.csv')
    unrate['DATE'] = pd.to_datetime(unrate['DATE'])
    print(unrate.head(12))
    # plt.plot()
    # plt.show()
    first_twelve = unrate[0:12]
    plt.plot(first_twelve['DATE'], first_twelve['VALUE'])
    # x坐标值显示旋转45度
    plt.xticks(rotation=45)
    # x轴标签
    plt.xlabel('Month')
    # y轴标签
    plt.ylabel('Unemployment Rate')
    # 标题
    plt.title('Monthly Unemployment Trends, 1948')

    plt.show()

    # fig = plt.figure()
    # ax1 = fig.add_subplot(3, 2, 1)
    # ax2 = fig.add_subplot(3, 2, 2)
    # ax2 = fig.add_subplot(3, 2, 6)
    # plt.show()
