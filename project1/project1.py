import matplotlib.pyplot as plot
import pandas as p

def readFile():
    dataArray = p.read_csv('top50.csv')
    return dataArray

def scatterplot():
    dataArray = readFile()
    x = dataArray['Energy'].values.tolist()
    y = dataArray[['Danceability']].values.tolist()
    plot.xlabel("Energy Rating")
    plot.ylabel("Danceability")
    plot.title("Scatter plot of Energy Rating vs Danceability")
    plot.scatter(x, y)
    plot.show()

def linegraph():
    dataArray = readFile()
    x = dataArray['index'].values.tolist()
    y = dataArray['Popularity'].values.tolist()
    plot.xlabel("Place on the top 50")
    plot.ylabel("Popularity ranking")
    plot.title("Line graph of top 50 ranking and the popularity rating")
    plot.plot(x, y, linewidth=2, linestyle='solid', color='black')
    plot.show()

def bargraph():
    dataArray = readFile()
    artists = dataArray['Genre'].values.tolist()
    artists_count = dataArray['Genre'].value_counts()
    res = []
    for i in artists:
        if i not in res:
            res.append(i)
    x=[]
    for i in range(1, len(res)+1):
        x.append(i)
    y = artists_count.tolist()
    
    plot.barh(res, y)
    plot.xlabel("Genre")
    plot.ylabel('Count')
    plot.title("Generes in the Top 50")
    plot.show()

def circlegraph():
    dataArray = readFile()
    artists_count = dataArray['Artist.Name'].value_counts()
    y = artists_count.tolist()
    plot.title("Times artists are repeated in the Top 50")
    plot.pie(y,labels=artists_count)
    plot.show()

def histogram():
    dataArray = readFile()
    data = dataArray['Energy'].values.tolist()
    plot.xlabel("Energy Rating")
    plot.ylabel("Count")
    plot.title("Histogram of the Energy Rating of the Top 50")
    plot.hist(data)
    plot.show()

scatterplot()
linegraph()
bargraph()
circlegraph()
histogram()