import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
import plotly.express as px
import matplotlib.pyplot as plt
@st.cache_data

#Load Data CSV
# -+----------------------------------------------------------------------------------------+-
def load_data(url) :
    df = pd.read_csv(url)
    return df

# Analisis Customer
# -+----------------------------------------------------------------------------------------+-

# Analisis Seller
# -+----------------------------------------------------------------------------------------+-
def tabel_seller(df_sellers):
    seller_count_per_city = df_sellers.groupby('seller_city').size().reset_index(name='jumlah penjual')

    # Mengurutkan berdasarkan jumlah penjual secara descending
    seller_count_per_city = seller_count_per_city.sort_values(by='jumlah penjual', ascending=False)

    # Mengambil 5 kota terbanyak
    top_5_cities = seller_count_per_city.head()

    # Menampilkan 5 kota terbanyak dalam bentuk tabel menggunakan Streamlit
    st.write("Top 5 Kota dengan Jumlah Penjual Terbanyak:")
    st.write(top_5_cities)

def graphs(df_sellers):
    # Menghitung jumlah penjual per kota
    seller_count_per_city = df_sellers.groupby('seller_city').size().reset_index(name='jumlah_penjual')

    # Mengambil 10 kota teratas
    top_10_cities = seller_count_per_city.nlargest(10, 'jumlah_penjual')

    # Membuat diagram tabung
    fig = px.bar(
       top_10_cities,
       x='jumlah_penjual',
       y='seller_city',
       orientation='h',
       title='<b>Top 10 Kota dengan Jumlah Penjual Terbanyak</b>',
       color_discrete_sequence=['#0083B8']*len(top_10_cities),
       template='plotly_white'
    )
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='black'),
        yaxis=dict(showgrid=True, gridcolor='#cecdcd'),  # Show y-axis grid and set its color  
        paper_bgcolor='rgba(0, 0, 0, 0)',  # Set paper background color to transparent
        xaxis=dict(showgrid=True, gridcolor='#cecdcd'),  # Show x-axis grid and set its color
    )

    st.plotly_chart(fig, use_container_width=True)

def jumlah(df_sellers):
    seller_count_per_city = df_sellers.groupby('seller_city').size().reset_index(name='jumlah_penjual')

    total_sellers = float(seller_count_per_city['jumlah_penjual'].sum())

    st.info('Total sellers')
    st.metric(label="Total sellers", value=f"{total_sellers:,.0f}")


def make_choropleth(input_df, input_id, input_column, input_color_theme):
    choropleth = px.choropleth(input_df, 
                               locations=input_id, 
                               color=input_column, 
                               locationmode="country names",
                               color_continuous_scale=input_color_theme,
                               range_color=(0, input_df[input_column].max()),
                               labels={input_column:'Population'},
                               title='Choropleth Map of Brazil by Seller State'
                              )
    choropleth.update_geos(projection_type="orthographic", 
                           lataxis_range=[-30, 10], 
                           lonaxis_range=[-75, -30]
                          )
    choropleth.update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        margin=dict(l=0, r=0, t=0, b=0),
        height=600
    )
    return choropleth
    
# Analisis kategori
# -+----------------------------------------------------------------------------------------+-


df_customer_dataset = load_data("https://raw.githubusercontent.com/RizkyReviyana/IF13---Plotly/main/customers_dataset.csv")
df_products_dataset= load_data("https://raw.githubusercontent.com/RizkyReviyana/IF13---Plotly/main/products_dataset.csv")
df_sellers = load_data("https://raw.githubusercontent.com/tkjfakhrian/LatihanAnalisisData/main/sellers_dataset.csv")





# Sidebar
# -+----------------------------------------------------------------------------------------+-
with st.sidebar :
    selected = option_menu('Menu',['Dashboard'],
    icons =["easel2", "graph-up"],
    menu_icon="cast",
    default_index=0)


# Dashboard
# -+----------------------------------------------------------------------------------------+-
if (selected == 'Dashboard') :
    st.header(f"Dashboard Analisis E-Commerce")
    tab1,tab2,tab3 = st.tabs(["Analisis Customer", "Analisis Seller", "Analisis Kategory" ])

    # analisis Customer
    # -+----------------------------------------------------------------------------------------+-
    with tab1 :
        st.write(df_customer_dataset)


    # analisis Seller
    # -+----------------------------------------------------------------------------------------+-
    with tab2 :
        st.write(df_sellers)
        jumlah(df_sellers)
        tabel_seller(df_sellers)
        graphs(df_sellers)
        choropleth_map = make_choropleth(df_sellers, 'seller_state', 'Population', 'Viridis')
        st.plotly_chart(choropleth_map)
  
    # analisis produk
    # -+----------------------------------------------------------------------------------------+-
    with tab3 :
        st.write(df_products_dataset)


