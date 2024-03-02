import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import plotly.express as px
from streamlit_extras.metric_cards import style_metric_cards
@st.cache_data

#Load Data CSV
# -+----------------------------------------------------------------------------------------+-
def load_data(url) :
    df = pd.read_csv(url)
    return df

# Analisis Customer
# -+----------------------------------------------------------------------------------------+-

def jumlah_pelanggan(df_customer_dataset):
    jumlah_pelanggan = df_customer_dataset.groupby('customer_city').size().reset_index(name='jumlah_pelanggan')

    total_pelanggan = jumlah_pelanggan['jumlah_pelanggan'].sum()

    return total_pelanggan

def jumlah_kota_pelanggan(df_customer_dataset):
    jumlah_kota = df_customer_dataset['customer_city'].nunique()

    return jumlah_kota


def jumlah_pelanggan_per_kota(df_customer_dataset):
    customer_count_per_city = df_customer_dataset.groupby('customer_city').size().reset_index(name='jumlah_pelanggan')

    return customer_count_per_city

def average_customer_per_city(df_customer_dataset):
    seller_count_per_city = df_customer_dataset.groupby('customer_city').size().reset_index(name='jumlah_penjual')

    avg_sellers = seller_count_per_city['jumlah_penjual'].mean()

    return avg_sellers

def graphs_cutomer(df_customer_dataset):
    # Menghitung jumlah  per kota
    seller_count_per_city = df_customer_dataset.groupby('customer_city').size().reset_index(name='jumlah_pelanggan')

    # Mengambil 10 kota teratas
    top_10_cities = seller_count_per_city.nlargest(10, 'jumlah_pelanggan')

    # Membuat diagram tabung
    fig = px.bar(
       top_10_cities,
       x='jumlah_pelanggan',
       y='customer_city',
       orientation='h',
       title='Diagram Top 10 Kota dengan Jumlah pelanggan terbanyak',
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


def Customer_dashboard(df_customer_dataset):
    # Create containers
    dash_1 = st.container()
    with dash_1:
        st.markdown("<h2 style='text-align: center;'>Customer Dashboard</h2>", unsafe_allow_html=True)
        st.write("")
        st.write("10122916 - M. Rizky Reviyana")
        st.write("")

    dash_2 = st.container()
    with dash_2:
    

        col1, col2, col3 = st.columns(3)
        col1.metric(label="Total Customers", value= jumlah_pelanggan(df_customer_dataset))
        col2.metric(label="Total Cities", value=jumlah_kota_pelanggan(df_customer_dataset))
        col3.metric(label="Average Customers per City",  value="{:.2f}".format(average_customer_per_city(df_customer_dataset)))

        style_metric_cards(border_left_color="#DBF227")
        # Styling
        st.write("")
        with st.expander("Penjelasan ") :
            st.write('Pada tiap kota terdapat banyak pembeli yang berbelanja melalui E-Commerce, melalui data yang kami analisa setidaknya terdapat 99441 pembeli diseluruh kota yang bertotal kan 4119 kota. Dengan menghitung total pembeli di seluruh kota kita dapat mengetahui bahwa rata-rata pembeli di setiap kota adalah sekitar 24.14 pembeli. Ini dapat kita simpulkan bawha peminat masih terbilang lumayan, mengingat kebutuhan yang diperlukan di tiap kota yang terbilang beragam dan dengan kemudahan berbelanja melalui E-Commerce, masih ada kemungkinan bahwa masih akan ada peningkatan pembeli di tiap kota.')


    dash_3 = st.container()
    with dash_3:
        graphs_cutomer(df_customer_dataset)

        with st.expander("Penjelasan diagram") :
            st.write('Jika melihat pada diagram diatas, kita bisa melihat bawa sao paulo mendapati urutan pertama dengan jumlah total pembeli sebesar 15,540 pembeli, dengan melihat data tersebut bisa kita simpulkan bahwa peminat pengguna E-Commerce mendominasi pada wilayah Sao Paulo. Namun, kita juga bisa melihat masih banyak juga pembeli dari masing-masing kota yang dapat kita perkirakan bahwa tidak dapat dipungkiri pula untuk kota lain akan bertambah secara bertahap seiring berjalannya waktu.')

        with st.expander("Kesimpulan") :
            st.write('Dengan melihat hasil review, didapatkan informasi bahwa jumlah seller akan mempengaruhi seberapa banyak jumlah customer, semakin banyak seller di kota tersebut maka akan mendapakatkan customer yang banyak juga. Agar kota-kota lainnya mendapat peningkatan jumlah customer maka harus dilakukan penambahan seller. Faktor lainnya adalah kota tersebut harus memiliki seller-seller yang menjual berbagai kategori produk agar customer memiliki banyak pilihan untuk melakukan order.')

        st.write("")
        



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
       title='Diagram Top 10 Kota dengan Jumlah Penjual Terbanyak',
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

    total_sellers = seller_count_per_city['jumlah_penjual'].sum()

    return total_sellers


def average_sellers_per_city(df_sellers):
    seller_count_per_city = df_sellers.groupby('seller_city').size().reset_index(name='jumlah_penjual')

    avg_sellers = seller_count_per_city['jumlah_penjual'].mean()

    return avg_sellers

def jumlah_sellers_per_city(df_sellers):
    seller_count_per_city = df_sellers.groupby('seller_city').size().reset_index(name='jumlah_penjual')

    return seller_count_per_city

def jumlah_kota(df_sellers):
    jumlah_kota = df_sellers['seller_city'].nunique()

    return jumlah_kota



def sales_dashboard(df_sellers):
    # Create containers
    dash_1 = st.container()
    with dash_1:
        st.markdown("<h2 style='text-align: center;'>Sales Dashboard</h2>", unsafe_allow_html=True)
        st.write("")
        st.write("10122902 - Silvi Oktaviani")
        st.write("")
    dash_2 = st.container()
    with dash_2:
    

        col1, col2, col3 = st.columns(3)
        col1.metric(label="Total Seller", value=jumlah(df_sellers))
        col2.metric(label="Total kota", value=jumlah_kota(df_sellers))
        col3.metric(label="Rata-rata seller per kota",  value="{:.2f}".format(average_sellers_per_city(df_sellers)))

        style_metric_cards(border_left_color="#DBF227")
        # Styling
        st.write("")
        with st.expander("Penjelasan ") :
            st.write('Bisa dilihat, terdapat total 3,095 penjual yang terdaftar di 611 kota. Ini menunjukan bahwa masih banyak penjual yang secara aktif menjual secara rata ke setiap kota. Dengan menghitung rata-rata penjual per kota, kita dapat menyimpulkan bahwa rata-rata penjual tiap kota adalah sekitar 5.07. Ini menunjukkan distribusi penjual yang relatif merata di antara kota-kota yang terlibat dalam data tersebut.')
       
    dash_3 = st.container()
    with dash_3:
        st.write("")
        graphs(df_sellers)
        with st.expander("Penjelasan Diagram") :
            st.write('Pada diagram diatas, bisa kita lihat total penjualan terbesar di 10 kota yang mana sao paulo adalah kota yang menduduki urutan pertama dengan penjualan sebesar 694 dan dapat mendominasi market. Tidak dapat dipungkiri bahwa jarak antara kota lain terbilang jauh, namun masih cukup banyak penjual di beberapa kota lainnya. Ini menunjukan juga bahwa masih mungkin untuk ada peningkatan penjual di beberapa kota lainnya secara bertahap dari waktu ke waktu.')
        with st.expander("Kesimpulan") :
            st.write('Sama seperti hasil review dari pertanyaan 1, antara seller dan customer saling berhubungan. Salah satu faktor agar setiap kota memiliki seller yang banyak adalah dengan banyaknya dan variasi produk yang akan dijual.')


def kategory_dashboard(df_sellers):
    # Create containers
    dash_1 = st.container()
    with dash_1:
        st.markdown("<h2 style='text-align: center;'>Sales Dashboard</h2>", unsafe_allow_html=True)
        st.write("10122905 -  Rayhandhika Yusuf Rafiansyah")

    dash_2 = st.container()
    with dash_2:
    

        col1, col2, col3 = st.columns(3)
        col1.metric(label="Total kategori", value=jumlah(df_sellers))
        col2.metric(label="Total Cities", value=jumlah_kota(df_sellers))
        col3.metric(label="Average Customers per City",  value="{:.2f}".format(average_sellers_per_city(df_sellers)))

        style_metric_cards(border_left_color="#DBF227")
        # Styling
        st.write("")
        with st.expander("Penjelasan ") :
            st.write('Bisa dilihat, terdapat total 3,095 penjual yang terdaftar di 611 kota. Ini menunjukan bahwa masih banyak penjual yang secara aktif menjual secara rata ke setiap kota. Dengan menghitung rata-rata penjual per kota, kita dapat menyimpulkan bahwa rata-rata penjual tiap kota adalah sekitar 5.07. Ini menunjukkan distribusi penjual yang relatif merata di antara kota-kota yang terlibat dalam data tersebut.')


    dash_3 = st.container()
    with dash_3:
        st.write("")
        graphs(df_sellers)
        with st.expander("Penjelasan Diagram") :
            st.write('Pada diagram diatas, bisa kita lihat total penjualan terbesar di 10 kota yang mana sao paulo adalah kota yang menduduki urutan pertama dengan penjualan sebesar 694 dan dapat mendominasi market. Tidak dapat dipungkiri bahwa jarak antara kota lain terbilang jauh, namun masih cukup banyak penjual di beberapa kota lainnya. Ini menunjukan juga bahwa masih mungkin untuk ada peningkatan penjual di beberapa kota lainnya secara bertahap dari waktu ke waktu.')




# Contoh penggunaan



# Contoh penggunaan

def jumlah_product(df_products_dataset):
    jumlah_product = df_products_dataset.groupby('product_category_name').size().reset_index(name='jumlah_product')

    total_product = jumlah_product['jumlah_product'].sum()

    return total_product


def average_product(df_products_dataset):
    rata_kategori = df_products_dataset.groupby('product_category_name').size().reset_index(name='jumlah_product')

    avg_product = rata_kategori['jumlah_product'].mean()

    return avg_product

def tabel_seller(df_sellers):
    seller_count_per_city = df_sellers.groupby('seller_city').size().reset_index(name='jumlah penjual')

    # Mengurutkan berdasarkan jumlah penjual secara descending
    seller_count_per_city = seller_count_per_city.sort_values(by='jumlah penjual', ascending=False)

    # Mengambil 5 kota terbanyak
    top_5_cities = seller_count_per_city.head()

    # Menampilkan 5 kota terbanyak dalam bentuk tabel menggunakan Streamlit
    st.write("Top 5 Kota dengan Jumlah Penjual Terbanyak:")
    st.write(top_5_cities)

def graphs_category(df_products_dataset):
    # Menghitung jumlah penjual per kota
    seller_count_per_city = df_products_dataset.groupby('product_category_name').size().reset_index(name='jumlah_kategori')

    # Mengambil 10 kota teratas
    top_10_cities = seller_count_per_city.nlargest(10, 'jumlah_kategori')

    # Membuat diagram tabung
    fig = px.bar(
       top_10_cities,
       x='jumlah_kategori',
       y='product_category_name',
       orientation='h',
       title='Diagram Top 10 Kota dengan Jumlah Kategori Barang terjual Terbanyak',
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




    
# Analisis kategori
# -+----------------------------------------------------------------------------------------+-
def kategory_dashboard(df_products_dataset):
    # Create containers
    dash_1 = st.container()
    with dash_1:
        st.markdown("<h2 style='text-align: center;'>Dashboard kategori </h2>", unsafe_allow_html=True)
        st.write("")
        st.write("10122905 -  Rayhandhika Yusuf Rafiansyah")
        st.write("")

    dash_2 = st.container()
    with dash_2:
    

        col1, col2, col3 = st.columns(3)
        col1.metric(label="Total kategori", value=jumlah_product(df_products_dataset))
        col2.metric(label="Total Cities",value=jumlah_product(df_products_dataset))
        col3.metric(label="Average Customers per City",  value="{:.2f}".format(average_product(df_products_dataset)))

        style_metric_cards(border_left_color="#DBF227")


        
        
        # Styling
        st.write("")
        with st.expander("Penjelasan Review Order") :
            st.write('Pada grafik penilaian oleh konsumen terhadap order yang pernah dilakukan, diketahui terdapat 11.424 order yang mendapatkan penilaian 1, namun dibandingkan dengan hasil review yang lain, dapat dilihat masih banyak yang memberikan penilaian 5 dengan total penilaian sebanyak 57.328. walaupun penilaian 1 masih rendah, diharapkan perusahaan mampu memperbaikin performa dari penjualan atau kualitas produk yang dijual')

      



    dash_3 = st.container()
    with dash_3:
        st.write("")
        graphs_category(df_products_dataset)
        with st.expander("Penjelasan Review Order") :
            st.write('Pada diagram diatas, menunjukan bahwa ada 10 kategori produk yang sangat diminati oleh para pembeli di setiap kotanya. Hal ini menunjukan cama mesa banho memiliki keunggulan dalam kategori produk dengan menduduki urutan pertama dengan total penjualan sebesar 3,029 produk yang terjual. Tidak lupa pula pada urutan kedua dan ketiga yang memiliki jarak begitu dekat dengan penjualan cama mesa banho dengan total penjualan untuk esporte lazer sebesar 2,867 dan untuk moveis decoracao sebesar 2,657. Dengan ini juga kita dapat menyimpulkan bahwa tiap pembeli dapat memiliki pilihan yang beragam sesuai dengan kebutuhan yang mereka miliki di setiap kotanya.')
        with st.expander("Kesimpulan") :
            st.write(' Tingkatkan jumlah kategori produk yang paling banyak diminati. Agar jumlah customer meningkat. Cari tahu mengapa kategori produk lainnya kurang diminati supaya bisa terjual')     



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
        
        Customer_dashboard(df_customer_dataset)

    # analisis Seller
    # -+----------------------------------------------------------------------------------------+-
    with tab2 :
        
        sales_dashboard(df_sellers)
        
    # analisis produk
    # -+----------------------------------------------------------------------------------------+-
    with tab3 :
        
        kategory_dashboard(df_products_dataset)
        



# Sample dataframe
# Function to calculate average customers per city

# Function to display the dashboard




