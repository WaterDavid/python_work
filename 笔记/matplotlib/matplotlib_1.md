```python
折线图:以折线的上升或下降来表示统计数量的增减变化的统计图
特点:能够显示数据的变化趋势，反映事物的变化情况。(变化)

直方图:由一系列高度不等的纵向条纹或线段表示数据分布的情况。
一般用横轴表示数据范围，纵轴表示分布情况。
特点:绘制连续性的数据,展示一组或者多组数据的分布状况(统计)

条形图:排列在工作表的列或行中的数据可以绘制到条形图中。
特点:绘制连离散的数据,能够一眼看出各个数据的大小,比较数据之间的差别。(统计)

散点图:用两组数据构成多个坐标点，考察坐标点的分布,判断两变量
之间是否存在某种关联或总结坐标点的分布模式。
特点:判断变量之间是否存在数量关联趋势,展示离群点(分布规律)
```


##### 折线图 pyplot
```python
#画折线图
plt.plot(x,y)
#x坐标值显示旋转45度
plt.xticks(rotation=45)
#x轴标签
plt.xlabel('Month')
#y轴标签
plt.ylabel('Unemployment Rate')
#标题
plt.title('Monthly Unemployment Trends, 1948')

```
##### 子图 subplot
```python
    fig = plt.figure()
    #创建一个三行两列的空间  位置是1
    ax1 = fig.add_subplot(3, 2, 1)
    ax2 = fig.add_subplot(3, 2, 2)
    ax2 = fig.add_subplot(3, 2, 6)
    plt.show()
```

##### 柱状图bar(x,y) barh水平柱状图
```python
    reviews = pd.read_csv('fandango_scores.csv')
    cols = ['FILM', 'RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
    norm_reviews = reviews[cols]
    print(norm_reviews[:1])

    num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']

    bar_heights = norm_reviews.loc[0, num_cols].values
    # print bar_heights
    bar_positions = arange(5) + 0.75
    # print bar_positions
    fig, ax = plt.subplots()
    ax.bar(bar_positions, bar_heights, 0.5)
    plt.show()
```

##### 散点图scatter(x,y)
```python
  fig, ax = plt.subplots()
  ax.scatter(norm_reviews['Fandango_Ratingvalue'], norm_reviews['RT_user_norm'])
  ax.set_xlabel('Fandango')
  ax.set_ylabel('Rotten Tomatoes')
  plt.show()
```
####直方图 hist
```python
    reviews = pd.read_csv('fandango_scores.csv')
   cols = ['FILM', 'RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue']
   norm_reviews = reviews[cols]
   print(norm_reviews[:5])
   fandango_distribution = norm_reviews['Fandango_Ratingvalue'].value_counts()
   fandango_distribution = fandango_distribution.sort_index()

   imdb_distribution = norm_reviews['IMDB_norm'].value_counts()
   imdb_distribution = imdb_distribution.sort_index()

   print(fandango_distribution)
   print(imdb_distribution)

   fig, ax = plt.subplots()
   ax.hist(norm_reviews['Fandango_Ratingvalue'])
   # ax.hist(norm_reviews['Fandango_Ratingvalue'],bins=20)
   # ax.hist(norm_reviews['Fandango_Ratingvalue'], range=(4, 5),bins=20)
   plt.show()
```


##### 盒须图
```python
  fig, ax = plt.subplots()
  ax.boxplot(norm_reviews['RT_user_norm'])
  ax.set_xticklabels(['Rotten Tomatoes'])
  ax.set_ylim(0, 5)
  plt.show()

  num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue']
  fig, ax = plt.subplots()
  ax.boxplot(norm_reviews[num_cols].values)
  ax.set_xticklabels(num_cols, rotation=90)
  ax.set_ylim(0, 5)
  plt.show()
```
