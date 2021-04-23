import pandas as pd
import statistics
import plotly.figure_factory as pf
import random
import plotly.graph_objects as go

dataFrame = pd.read_csv("StudentMarks-0.csv")
dataList = dataFrame["Math_score"].tolist()

dataFrameOfClassScore1 = pd.read_csv("ClassScore-1.csv")
dataListOfClassScore1 = dataFrameOfClassScore1["Math_score"].tolist()

meanOfClassScore1 = statistics.mean(dataListOfClassScore1)

dataFrameOfClassScore2 = pd.read_csv("ClassScore-2.csv")
dataListofClassScore2 = dataFrameOfClassScore2["Math_score"].tolist()

meanOfClassScore2 = statistics.mean(dataListofClassScore2)

dataFrameOfClassScore3 = pd.read_csv("ClassScore-3.csv")
dataListOfClassScore3 = dataFrameOfClassScore3["Math_score"].tolist()

meanOfClassScore3 = statistics.mean(dataListOfClassScore3)

mean = statistics.mean(dataList)
print("The mean of the class score is {}".format(mean))

standardDeviation = statistics.stdev(dataList)
print("The standard deviation of the class score is {}".format(standardDeviation))

# graph = pf.create_distplot([dataList], ["Scores"])
# graph.show()


def getRandomSamples(counter):
    meanList = []

    for i in range(0, 1000):
        samples = []
        for x in range(0, counter):
            randomIndex = random.randint(0, len(dataList) - 1)
            samples.append(dataList[randomIndex])

        meanOfSamples = statistics.mean(samples)
        meanList.append(meanOfSamples)

    return meanList


def showGraph(meanOfSamples, standardDeviationOfSamples):
    standardDeviationStart1, standardDeviationEnd1 = mean - \
        standardDeviationOfSamples, mean + standardDeviationOfSamples

    standardDeviationStart2, standardDeviationEnd2 = mean - \
        2 * standardDeviationOfSamples, mean + (2 * standardDeviationOfSamples)

    standardDeviationStart3, standardDeviationEnd3 = mean - \
        3 * standardDeviationOfSamples, mean + (3 * standardDeviationOfSamples)

    graph = pf.create_distplot([meanOfSamples], ["Scores"], show_hist=False)
    graph.add_trace(go.Scatter(x=[mean, mean], y=[
                    0, 0.17], mode="lines", name="Mean"))

    graph.add_trace(go.Scatter(x=[standardDeviationStart1, standardDeviationStart1], y=[
                    0, 0.17], mode="lines", name="First Standard Deviation Start"))

    graph.add_trace(go.Scatter(x=[standardDeviationEnd1, standardDeviationEnd1], y=[
                    0, 0.17], mode="lines", name="First Standard Deviation End"))

    graph.add_trace(go.Scatter(x=[standardDeviationStart2, standardDeviationStart2], y=[
                    0, 0.17], mode="lines", name="Second Standard Deviation Start"))

    graph.add_trace(go.Scatter(x=[standardDeviationEnd2, standardDeviationEnd2], y=[
                    0, 0.17], mode="lines", name="Second Standard Deviation End"))

    graph.add_trace(go.Scatter(x=[standardDeviationStart3, standardDeviationStart3], y=[
                    0, 0.17], mode="lines", name="Third Standard Deviation Start"))

    graph.add_trace(go.Scatter(x=[standardDeviationEnd3, standardDeviationEnd3], y=[
                    0, 0.17], mode="lines", name="Third Standard Deviation End"))

    return graph


def main():
    meanSamples = getRandomSamples(100)

    meanOfSamplingDistribution = statistics.mean(meanSamples)
    print("The mean of the samples is " +
          " " + str(meanOfSamplingDistribution))

    standardDeviationOfSamplingDistribution = statistics.stdev(meanSamples)
    print("The standard deviation of the samples is {}".format(
        standardDeviationOfSamplingDistribution))

    graph = showGraph(meanSamples, standardDeviationOfSamplingDistribution)

    graph.add_trace(go.Scatter(
        x=[meanOfClassScore1, meanOfClassScore1], y=[0, 0.17], mode="lines", name="Mean of students who have gotten an iPad"))

    graph.add_trace(go.Scatter(x=[meanOfClassScore2, meanOfClassScore2], y=[
                    0, 0.17], mode="lines", name="Mean of Student who have gotten extra classes"))

    graph.add_trace(go.Scatter(x=[meanOfClassScore3, meanOfClassScore3], y=[
                    0, 0.17], mode="lines", name="Mean of Student who have gotten fun math sheets."))

    graph.show()

    zScoreForSample1 = (mean - meanOfClassScore1) / \
        standardDeviationOfSamplingDistribution
    print("The z score for sample 1 is" + " " + str(zScoreForSample1))

    zScoreForSample2 = (mean - meanOfClassScore2) / \
        standardDeviationOfSamplingDistribution
    print("The z score of sample 2 is {}".format(zScoreForSample2))

    zScoreForSample3 = (mean - meanOfClassScore3) / \
        standardDeviationOfSamplingDistribution
    print('The z score for sample 3 is {}'.format(zScoreForSample3))


main()
