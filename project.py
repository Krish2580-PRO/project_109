import pandas as pa
import csv
import statistics as st
import plotly.figure_factory as pf
import plotly.graph_objects as go

# ---------------------------------------------------------------------------------------

data = pa.read_csv("project.csv")

val = data["reading score"].to_list()

total = len(val)

# ----------------------------- mean/median/mode/stdev -----------------------------------

mean = st.mean(val)
mode = st.mode(val)
median = st.median(val)
stdev = st.stdev(val)


print("------------------------------------")
print("Mean of the population : " , mean)
print("Median of the population : " , median)
print("Mode of the population : " , mode)

print("------------------------------------")
print("Std Dev of the population : " , stdev)


# ---------------------------------- one/two/three standard deviations -------------------------------------------

oneStdevStart , oneStdevEnd = mean - stdev , mean + stdev

twoStdevStart , twoStdevEnd = mean - ( 2 * stdev ) , mean + ( 2 * stdev )

threeStdevStart , threeStdevEnd = mean - (3 * stdev) , mean + (3 * stdev)


# -------------------------------- list of data lying within one/two/three stdevs ----------------------------------------------

listOfDataWithinOneStdev = [ res for res in val if res > oneStdevStart and res < oneStdevEnd]

listOfDataWithinTwoStdev = [ res for res in val if res > twoStdevStart and res < twoStdevEnd]

listOfDataWithinThreeStdev = [ res for res in val if res > threeStdevStart and res < threeStdevEnd]



# --------------------------------------------------- percentage --------------------------------------------------------------

p1 = (len (listOfDataWithinOneStdev)*100) / total

p2 = (len (listOfDataWithinTwoStdev)*100) / total

p3 = (len (listOfDataWithinThreeStdev)*100) / total

print("----------------------------------------------------------")

print("Percentage of data lying within 1 stdev : ", p1)

print("Percentage of data lying within 2 stdev : ", p2)

print("Percentage of data lying within 3 stdev : ", p3)


# -------------------------------- plotting distplot ----------------------------------

fig = pf.create_distplot( [val] , ["Graph of data"] , show_hist = False )

fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))

fig.add_trace(go.Scatter(x=[oneStdevStart, oneStdevStart], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 START"))
fig.add_trace(go.Scatter(x=[oneStdevEnd, oneStdevEnd], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))

fig.add_trace(go.Scatter(x=[twoStdevStart, twoStdevStart], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 START"))
fig.add_trace(go.Scatter(x=[twoStdevEnd, twoStdevEnd], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))

fig.show()









