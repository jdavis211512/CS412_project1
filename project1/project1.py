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
    artists = dataArray['Artist.Name'].values.tolist()
    artists_count = dataArray['Artist.Name'].value_counts()
    y = artists_count.tolist()
    plot.bar(artists, y)
    plot.xlabel("artist")
    plot.ylabel('count')
    plot.show()
bargraph()
