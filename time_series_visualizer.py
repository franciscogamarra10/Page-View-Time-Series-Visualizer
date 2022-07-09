import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import datetime
# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')

# Clean data
val1=float(df['value'].quantile(0.025))
val2=float(df['value'].quantile(0.975))
df = df.query(" value >= @val1 and  value <= @val2 ")


def draw_line_plot():
    # Draw line plot
  df2=df.copy()  
  df2.date = pd.to_datetime(df.date, dayfirst = True)
# df.set_index("date", inplace=True)
# df_comp = pd.to_datetime(df.date, dayfirst = True)
# df_comp.set_index("date", inplace=True)
  ## corregir el error de subscriptable
  fig, axs = plt.subplots(1)
  plt.plot(df['date'],df['value'],c="red")
  # ax = plt.axes()

 
  # ax = plt.axes()
  # df2.plot(c="red",legend=None)
  
  # sns.lineplot(df['date'],df['value'],palette="r")

# df.plot(figsize = (20,5))
  plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019", size= 12)
# plt.legend(bbox_to_anchor = (1.0, 1), loc = 'upper center')
  # fig=plt
  plt.xlabel("Date")
  plt.ylabel("Page Views")
  # plt.show()
  # fig=plt
  




    
    # Save image and return fig (don't change this part)
  fig.savefig('line_plot.png')
  return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.date = pd.to_datetime(df_bar.date, dayfirst = True)
    months_in_year = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    df_bar['month'] =df_bar['date'].dt.month

# df['month']=df['month'].cat.reorder_categories(range(11))   
    def fun_m(n):
      return months_in_year[n-1]

    df_bar['month']=df_bar['month'].apply(fun_m)



    df_bar['year'] =df_bar['date'].dt.year
    # Draw bar plot
    auxi2=df_bar[['value','month','year']]
    auxi2=auxi2.melt(id_vars = ['month','year'],value_vars=['value'])
# auxi2

    auxi2=auxi2.groupby(['month','year','value']).mean().reset_index()
    auxi2.head()

    auxi2['month']=pd.Categorical(auxi2['month'], months_in_year, ordered = True)
# fig=sns.catplot(x='year',y='value',hue='month',data=auxi2,legend=False,kind='bar',ci=None,palette="tab10").fig
    fig=sns.catplot(x='year',y='value',hue='month',data=auxi2,legend=False,kind='bar',ci=None,palette="tab10").fig### el .fig corrige error de x label hue le da el valor para cada x de categorias
    
# plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019", size= 12)
# plt.legend(bbox_to_anchor = (1.0, 1), loc = 'upper left')
    plt.legend(title="Months",loc='upper left')
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")





    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    # df_box = df.copy()
    # df_box.reset_index(inplace=True)
    # df_box['year'] = [d.year for d in df_box.date]
    # df_box['month'] = [d.strftime('%b') for d in df_box.date]
    # Copy and modify data for monthly bar plot
    df_box = df.copy()
    df_box.date = pd.to_datetime(df_box.date, dayfirst = True)
    months_in_year = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    df_box['month'] =df_box['date'].dt.month

# df['month']=df['month'].cat.reorder_categories(range(11))   
    def fun_m(n):
      return months_in_year[n-1]

    df_box['month']=df_box['month'].apply(fun_m)



    df_box['year'] =df_box['date'].dt.year
    # Draw bar plot
    auxi2=df_box[['value','month','year']]
    auxi2=auxi2.melt(id_vars = ['month','year'],value_vars=['value'])
    
# auxi2

    auxi2=auxi2.groupby(['month','year','value']).mean().reset_index()
    auxi2['month']=pd.Categorical(auxi2['month'], months_in_year, ordered = True)
     # Draw box plots (using Seaborn)
    # fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
    fig, axes = plt.subplots(1, 2, figsize=(15, 5), sharey=True)
# fig.suptitle('Initial Pokemon - 1st Generation')

# Bulbasaur
    sns.boxplot( x=auxi2["year"], y=auxi2["value"],ax=axes[0]).set(
    xlabel='Year', 
    ylabel='Page Views'
)
# plt.xlabel("Year")
# plt.ylabel("Average Page Views")

# sns.barplot(ax=axes[0], x=bulbasaur.index, y=bulbasaur.values)
    axes[0].set_title('Year-wise Box Plot (Trend)')

# Charmander
    sns.boxplot(ax=axes[1],  x=auxi2["month"], y=auxi2["value"])
    plt.xlabel("Month")
    plt.ylabel("Page Views")
# axes[1].set_title(charmander.name)
    axes[1].set_title('Month-wise Box Plot (Seasonality)')




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig