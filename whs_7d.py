#
# Quick plot of seven day rolling average of student and staff new covid cases at
# Westside High School
#
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import plotly.graph_objects as go


df = pd.read_csv("data.tsv", sep='\t', index_col="Date",parse_dates=["Date"])
df = df.sort_index()

print(df)

df['Students_7D'] = df.rolling('7D').Students.mean()
df['Staff_7D'] = df.rolling('7D').Staff.mean()
df['Students_sum'] = df['Students'].cumsum()
df['Staff_sum'] = df['Staff'].cumsum()


print(df)

fig = plt.figure()
plt.plot_date(x=df.index, y=df['Students_7D'], fmt='bo-', tz=None, xdate=True,
      ydate=False, label="Students 7D rolling avg", color='red')

plt.plot_date(x=df.index, y=df['Staff_7D'], fmt='ro-', tz=None, xdate=True,
      ydate=False, label="Staff 7D rolling avg", color='blue')

fig.autofmt_xdate()
plt.legend()
plt.ylabel("Count")
plt.xlabel("Date")
plt.title("7 day rolling average of new cases at WHS")



plt.show()
current_date = datetime.date.today().isoformat()
plt.savefig("WHS_COVID_"+current_date)


#Use plotly instead of matplotlib for the bar charts
pfig = go.Figure(data = [
    go.Bar(name='Students', x = df.index, y=df['Students_sum']),
    go.Bar(name='Staff', x=df.index, y=df['Staff_sum'])
])
pfig.update_layout(barmode = 'group',
                   title = "WHS Cumulative COVID Cases ",
                   xaxis_title = 'Date',
                   yaxis_title = 'Count'
                   )
pfig.show()
pfig.write_image('WHS_CUMULATIVE_COVID_'+current_date+'.png')