import matplotlib.pyplot as plot
import pandas as p


def readFile():
    dataArray = p.read_csv('top50.csv')
    return dataArray


def scatterplot():
    dataArray = readFile()
    x = dataArray['index'].values.tolist()
    y = dataArray[['Popularity']].values.tolist()
    plot.xlabel("number on top 50")
    plot.ylabel("popularity score")
    plot.title("scatter plot of top 50 vs popularity score")
    plot.scatter(x, y)
    plot.show()




def linegraph():
    dataArray = readFile()
    x = dataArray['Loudness..dB..'].values.tolist()
    y = dataArray['Speechiness.'].values.tolist()
    plot.xlabel("Beats per minute")
    plot.ylabel("Energy score")
    plot.title("line graph of beats per minute and energy")
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
    plot.bar(x, y, width=.8 )
    plot.xlabel("genre")
    plot.ylabel('count')
    plot.show()

def circlegraph():
    dataArray = readFile()
    artists_count = dataArray['Artist.Name'].value_counts()
    y = artists_count.tolist()
    plot.pie(y)
    plot.show()

bargraph()