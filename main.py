import plotly.express as px
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go


# Set the page title and favicon (optional)
st.set_page_config(
    page_title="Dashboard",
page_icon=":dashboard.png:",
)



# Apply the custom theme

# Your Streamlit app content goes here



# More app content...


# Load the dataset
df = pd.read_csv('ElectricCarData_Clean_Me.csv')
df['FullName'] = df['Brand'] + '-' + df['Model']
df_1 = df.loc[df['PriceEuro'] <= 50000]
df_2 = df.loc[df['PriceEuro'] > 50000]



# Set the page title
st.title('Dashboard')

def overall():
    # st.title('Overall Analysis')
    st.subheader('Top 5 coloumn of data ')
    st.dataframe(df.head(5))

    Row = df.shape[0]
    no_col = df.shape[1]
    st.subheader('Shape of the data : \n')
    col1, col2 = st.columns(2)

    with col1:
        st.metric('Number of row', str(Row))
    with col2:
        st.metric('Number of column', str(no_col))

    st.subheader('Price Range: \n')
    minimum = df['PriceEuro'].min()
    maximum= df['PriceEuro'].max()
    col1, col2 = st.columns(2)

    with col1:
        st.metric('Minimum Price of a car ', str(minimum))
    with col2:
        st.metric('Maximum Price of a car', str(maximum))

# Relationship between Price and top speed of car
    st.subheader('Relation between Price and Top speed')
    st.write(px.bar(df, x='TopSpeed_KmH', y='PriceEuro', color='FullName', width=1000))


    st.subheader('Ranges of cars which are available  : \n')
    mini = df['Range_Km'].min()
    maxi= df['Range_Km'].max()
    col1, col2 = st.columns(2)

    with col1:
        st.metric('Minimum range of a car ', str(mini))
    with col2:
        st.metric('Maximum range of a car', str(maxi))
# Relationship between Price and range of car
    st.subheader('Relation between Price and Range')
    st.write(px.scatter(df,x='Range_Km',y='PriceEuro',color='FullName',size='TopSpeed_KmH',range_y=[18000,219000],width=1000))
    st.subheader('It has only top 5 coloumn which tells that which bodystyle made by how many brands ')
    Bodystle = df.groupby('BodyStyle').count()
    number = Bodystle['Brand'].sort_values(ascending=False)
    st.write(number.head(5))
    st.subheader('Relation between Body Style and price')
    st.write(px.bar(df, y='PriceEuro', x='BodyStyle', color='FullName', width=1000))
    st.subheader('Relationship between Power with segment and seats')
    fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(10, 6))
    ax[0].bar(df['PowerTrain'], df['Segment'], color='red')
    ax[1].bar(df['PowerTrain'], df['Seats'])

    ax[0].set_title('Power vs segment')
    ax[0].set_ylabel('Segment')

    ax[1].set_title('Power vs seats')
    ax[1].set_ylabel('Seats')
    ax[1].set_xlabel('Power')

    fig.show()

    st.write(fig, width=1000)
    st.subheader('Range of acceleration in one second of cars which are available  : \n')
    mini_a = df['AccelSec'].min()
    maxi_a = df['AccelSec'].max()
    col1, col2 = st.columns(2)

    with col1:
        st.metric('Minimum acceleration of a car ', str(mini_a))
    with col2:
        st.metric('Maximum acceleration of a car', str(maxi_a))
    st.subheader('Acceleration')
    st.write(px.bar(df,y='AccelSec',x='FullName',width=1000))
    st.subheader('FastCharging')
    st.write(px.bar(df,y='FastCharge_KmH',x='FullName',width=1000))
    st.subheader('Brand Tree map')
    st.write(px.treemap(df, path=['Brand','Model','Range_Km'], color='PriceEuro',width=1200))
    st.header('Conclusion')
    st.write('''1-Range of vehicle is proportional to Battery Pack Capacity

                2-Price of vehicle is proportional battery pack capacity

                3-High performance EV's have lower efficiency

                4-Most of the vehicles costing over 50,000 Euros are either All wheel drive or Rear wheel drive and have better acceleration

                5-High performance EV's have lower efficiency''')



def data():
    st.title('Data')
    st.dataframe(df)
    st.title('Properties')
    # shape of data
    Row = df.shape[0]
    no_col=df.shape[1]
    st.write('Shape of the data : \n')
    col1, col2 = st.columns(2)

    with col1:
        st.metric('Number of row', str(Row))
    with col2:
        st.metric('Number of column', str(no_col) )

# coloumn of data

    coloumn = df.columns
    list=[]
    for i in coloumn:
        list.append(i)

    st.write('Coloumns which are present in the data -> \n', list)

# Null values
    null=df.isnull().sum()
    st.write('Is any null value is present-> \n', null)

# Describe the data
    df_description = df.describe()
    st.write('Describe the data -> \n', df_description)


    with st.container():
# number of the vehicle made by each Brand
        companies = df.groupby('Brand').count()
        vehicle_number=companies['Model'].sort_values(ascending=False)
        st.write('Number of vehicle produced by componies ->\n', vehicle_number)

# Cars which are present in this data
        cars=df['FullName']
        st.write('Cars which are present in this data->\n', cars)


def relation_top_speed_vs_price():
    st.title('Relation between TopSpeed_KmH vs PriceEuro')
    st.header('About graph:-')
    st.write('''This bar chart essentially shows the relationship between the top speed of electric cars and their prices, with each bar representing a specific electric car model (FullName), and the color of the bar indicating the model.\n
    y-axis-> Price in euro\n
    x-axis-> Top speed of cars\n
    Color-> Colors shows the name of the car'''
                 )

    st.header('Graph:-\t')
    st.write(px.bar(df,x='TopSpeed_KmH',y='PriceEuro',color='FullName',width=1000))
    st.subheader('Conclusion')
    st.write('''

                 1-Tesla Roadster has maximum top_high speed 410KmH with decent price\n
                 2-Tesla model-X has costly car with 250KmH TopSpeed_kmH\n
                 3-Nissan-e-Nv200 Evalia has minimum Topspeed in thsese car which are present in this dataset\n
                 4- we can visually compare the top speeds of different electric car models with their respective prices.\n
                 5-The use of colors to represent different models (FullName) allows we to see how many unique electric car models are in the dataset 
                 ''')
    # Add content for this analysis here.

def relation_range_price():
    st.title('Relation between Range and price')
    st.header('About graph:-')
    st.write('''we can see how the range of electric cars relates to their price. Generally, there's a positive correlation, meaning that cars with a longer range tend to be more expensive. However, there are exceptions, as indicated by the spread of data points. Some cars with shorter ranges might be relatively expensive, and some with longer ranges might be more affordable.\n
    y-axis-> Price in euro\n
    x-axis-> Range\n
    Color-> Colors shows the name of the car\n
    Size-> TopSpeed_KmH'''
             )

    st.header('Graph:-\t')
    st.write(px.scatter(df,x='Range_Km',y='PriceEuro',color='FullName',size='TopSpeed_KmH',range_y=[18000,219000],width=1000))
    st.subheader('Conclusion')
    st.write('''

                     1-we can observe how the price of electric cars varies with their range.\n
                     2-The size of data points is based on the top speed of each car. we can see if cars with higher top speeds are associated with longer ranges or higher prices.\n
                     3-Tesla Roadster has highest speed and highest range with highest price\n
                     4- we can visually compare the top speeds and range of different electric car models with their respective prices.\n
                     5- It shows positive correaltion which means when x increase so y also increase 
                     ''')


def to_range():
    st.title('Know more about Range')
    st.header('About graph:-')
    st.write('''The histogram shows the distribution of electric cars' ranges.we can see how many electric cars fall into different range categories\n
    y-axis-> Number of cars\n
    x-axis-> Range\n
   ''')


    st.header('Graph:-\t')
    st.write(px.histogram(df, x='Range_Km',width=900))
    st.subheader('Describe')
    describe=df['Range_Km'].describe()
    st.write(describe)
    st.subheader('Conclusion')
    st.write('''

                        1-This histogram tells that maximum number of electric cars have 300 to 450 kmH of range_km.\n
                        2-Only one car has more than 900 kmh of range\n
                        3-This histogram is skewed to the left (tail on the left), it means that there are more electric cars with shorter ranges\n
                        4- This histogram provides insights into consumer preferences. we can see which range categories are more popular or how the market is distributed across different range options.\n
                        
                        ''')


def relationship_price_bodystyle():
    st.title('Relation between Body Style and price')
    st.header('About graph:-')
    st.write('''A bar chart is a graphical representation of categorical data where the categories are displayed as bars, and the height (or length) of each bar is proportional to the value it represents.\n
    y-axis-> Price Euro\n
    x-axis-> BodyStyle\n
    color-> Name of the cars
   ''')

    st.header('Graph:-\t')
    st.write(px.bar(df,y='PriceEuro',x='BodyStyle',color='FullName',width=1000))
    st.subheader('The number of bodystyle->\n')
    st.write('This table tells that which Bodystyle made by how many brands')
    Bodystle= df.groupby('BodyStyle').count()
    number= Bodystle['Brand'].sort_values(ascending=False)
    st.write(number)
    st.subheader('Conclusion')
    st.write('''

                        1-By looking at the height of the bars, we can assess the price range within each body style.\n
                        2-we can observe how the prices of electric cars vary across different body styles\n
                        3-The use of colors for different car models within each body style allows you to see how prices vary within a particular body style. we can identify which models are more expensive or cheaper within each category.\n
                        4-we can compare the average or median prices of electric cars within each body style category.\n

                        ''')


def relationship_Power_with_segment_seats():
    st.title('Relationship between Power with segment and seats')
    st.header('About graph:-')
    st.write(''' 1-The bars represent the count or frequency of electric cars in each powertrain category within each segment. The color of the bars is set to red.\n
    2-The bars represent the count or frequency of electric cars in each powertrain category, with the height of the bars indicating the number of seats.\n
    y-axis-> Segments\n
    x-axis-> Power\n
    y-axis->seats
   ''')

    st.header('Graph:-\t')

    fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(10, 6))
    ax[0].bar(df['PowerTrain'], df['Segment'], color='red')
    ax[1].bar(df['PowerTrain'], df['Seats'])

    ax[0].set_title('Power vs segment')
    ax[0].set_ylabel('Segment')

    ax[1].set_title('Power vs seats')
    ax[1].set_ylabel('Seats')
    ax[1].set_xlabel('Power')

    fig.show()

    st.write(fig,width = 1000)

    st.subheader('Conclusion')
    st.write('''

                        1-This chart shows how the distribution of electric cars varies across different segments for each powertrain type.\n
                        2-This chart allows you to see how the number of seats varies among different powertrain types. we can determine which powertrain types tend to have more or fewer seats on average.\n
                        3-Both subplots can help you understand the distribution of segments and seats in electric cars\n
                        4-These plots can be valuable for market analysis\n

                        ''')


def acceleration():
    st.title('Acceleration')
    st.header('About graph:-')
    st.write('''we can visually compare the acceleration performance of various electric car models. Shorter bars indicate faster acceleration times, while taller bars indicate slower acceleration times.\n
    y-axis-> Acceleration per second \n
    x-axis-> Full Name\n
   ''')

    st.header('Graph:-\t')
    st.write(px.bar(df,y='AccelSec',x='FullName',width=1000))
    st.subheader('Describe')
    describe = df['AccelSec'].describe()
    st.write(describe)
    st.subheader('This data set tells the maximum or minium  acceleration car')
    max=df[(df['AccelSec'] == 22.400000) | (df['AccelSec'] == 2.100000)]
    st.dataframe(max)
    st.subheader('Vehicles which have maximum acceleration under 50,000 Euros')
    acceleration = df_1.sort_values(by='AccelSec')
    a=acceleration[['FullName', 'AccelSec', 'Range_Km', 'Battery_Pack Kwh', 'PriceEuro']]
    st.write(a)
    st.subheader('Vehicles which have maximum acceleration above 50,000 Euros')
    acceleration_2 = df_2.sort_values(by='AccelSec')
    a2=acceleration_2[['FullName', 'AccelSec', 'Range_Km', 'Battery_Pack Kwh', 'PriceEuro']]
    st.write(a2)
    st.subheader('Conclusion')
    st.write('''

                        1-The bar chart allows you to compare the acceleration performance of different electric car models. You can see which models have faster acceleration times (shorter bars) and which ones have slower acceleration times (taller bars).\n
                        2-Tesla Roadster has minimum acceleration it has 2.1 sec\n
                        3-Renault Kangoo Maxi ZE 33 has maximum it has 22.4 sec\n
                       

                        ''')


def fastCharging():
    st.title('FastCharging')
    st.header('About graph:-')
    st.write('''This bar chart represents the relationship between the 'FullName' and the length of each bar is proportional to the value it represents.\n
    y-axis-> Fast Charge\n
    x-axis-> Full name\n
   ''')

    st.header('Graph:-\t')
    st.write(px.bar(df,y='FastCharge_KmH',x='FullName',width=1000))
    st.subheader('This data tells which car has maximum Fastcharging speed')
    max =df[df['FastCharge_KmH'] ==940.000000]
    st.dataframe(max)

    st.subheader('Describe')
    describe = df['FastCharge_KmH'].describe()
    st.write(describe)
    st.subheader('Conclusion')
    st.write('''

                        1-The bar chart allows we to see how fast charging speeds vary across different electric car models. \n
                        2-Tesla Model 3 Long Range Dual Moto has highest fast charging\n
                        3-we can compare the fast charging speeds of different electric car models directly.\n
                        4-Electric car manufacturers, this data can inform future product development. If there is a strong demand for fast charging, manufacturers may prioritize improving this feature in their vehicles.

                        ''')


def treeMap():
    st.title('About Brand')
    st.header('About graph:-')
    st.write('''The treemap shows a hierarchical structure starting with 'Brand' as the top-level categories. Each 'Brand' contains 'Model' subcategories, and within each 'Model,' there are further subdivisions based on 'Range_Km.' This allows we to see how electric cars are categorized based on these attributes.
   ''')

    st.header('Graph:-\t')
    st.write(px.treemap(df, path=['Brand','Model','Range_Km'], color='PriceEuro',width=1200))
    st.subheader('Conclusion')
    st.write('''

                            1-The treemap provides a hierarchical view of how different electric car brands are divided into models, and how each model is further divided into different ranges. we can see the composition of brands, models, and ranges within the \n
                            2-The size of the rectangles can indicate the number of electric cars within each brand and model. Larger rectangles represent a higher number of cars. we can see which brands and models have a more extensive variety of offerings.\n
                            3-: The color of each rectangle represents the price of electric cars in Euros. This allows we to visualize how prices vary across different brands, models, and ranges.
                            ''')




st.sidebar.title('Dashboard')
st.sidebar.title('More Info')
option = st.sidebar.selectbox('Select one', ['Overall Analysis', 'Data and Properties', 'Relation between TopSpeed_KmH vs PriceEuro', 'Relation between Range and Price', 'To Know about Range', 'Relationship between price and bodystyle', 'Relationship between Power with segment and seats', 'Acceleration (0-100)', 'FastCharging', 'About Brand'])
st.sidebar.title(option)
# Use if statements to display the selected option
if option == 'Overall Analysis':
    overall()
elif option == 'Data and Properties':
    data()
elif option == 'Relation between TopSpeed_KmH vs PriceEuro':
    relation_top_speed_vs_price()
elif option == 'Relation between Range and Price':
    relation_range_price()
elif option == 'To Know about Range':
    to_range()
elif option == 'Relationship between price and bodystyle':
    relationship_price_bodystyle()
elif option == 'Relationship between Power with segment and seats':
    relationship_Power_with_segment_seats()
elif option == 'Acceleration (0-100)':
    acceleration()
elif option == 'FastCharging':
    fastCharging()
elif option == 'About Brand':
    treeMap()

