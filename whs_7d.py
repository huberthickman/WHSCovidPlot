#
# Quick plot of seven day rolling average of student and staff new covid cases at
# Westside High School
#
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import plotly.graph_objects as go


df = pd.read_csv("data.csv", sep=',', index_col="Date",parse_dates=["Date"])
df = df.sort_index()

print(df)

df['Students_7D'] = df.rolling('7D').Students.mean()
df['Staff_7D'] = df.rolling('7D').Staff.mean()
df['Students_sum'] = df['Students'].cumsum()
df['Staff_sum'] = df['Staff'].cumsum()


print(df)

fig = plt.figure()
plt.plot_date(x=df.index, y=df['Students_7D'], fmt='bo-', tz=None, xdate=True,
      ydate=False, label="Students 7D rolling avg", color='blue')

plt.plot_date(x=df.index, y=df['Staff_7D'], fmt='ro-', tz=None, xdate=True,
      ydate=False, label="Staff 7D rolling avg", color='red')

fig.autofmt_xdate()
plt.legend()
plt.ylabel("Count")
plt.xlabel("Date")
plt.title("7 day rolling average of new cases at WHS")



#plt.show()
current_date = datetime.date.today().isoformat()
plt.savefig("images/WHS_COVID_CURRENT")


#Use plotly instead of matplotlib for the bar charts
pfig = go.Figure(data = [
    go.Bar(name='Students', x = df.index, y=df['Students_sum']),
    go.Bar(name='Staff', x=df.index, y=df['Staff_sum'])
])
pfig.update_layout(barmode = 'group',
                   title = "WHS Cumulative COVID Cases ",
                   xaxis_title = 'Date',
                   yaxis_title = 'Count',
                   margin_b = 90,
                   annotations = [dict(xref = 'paper', yref= 'paper', x = 0.9, y = -0.1, font = dict(size = 8),
                                       showarrow = False, text = '<i>Chart Generated ' + current_date + "</i>")]
                   )
pfig.show()
pfig.write_image('images/WHS_CUMULATIVE_COVID_CURRENT.png', width=900)