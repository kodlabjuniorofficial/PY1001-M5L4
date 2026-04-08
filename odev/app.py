import streamlit as st
import sqlite3
import pandas as pd

@st.cache_resource
def init_connection():
    return sqlite3.connect('top250.db', check_same_thread=False)

conn = init_connection()

@st.cache_data(ttl=600)
def fetch_data(query, params=None):
    return pd.read_sql(query, conn, params=params)

st.title("⭐ ÖDEV: Film Arama Çubuğu")
st.info("GÖREV: Yan menüye bir arama çubuğu ekleyerek filmleri başlığına göre arayın.")

# --- YAN MENÜ ---
st.sidebar.title("Arama Seçenekleri")

# !GÖREV 1: st.sidebar.text_input kullanarak bir arama çubuğu oluşturun.
arama_metni = st.sidebar.text_input("Film Başlığı Ara:", "")

# --- ANA SAYFA ---

# !GÖREV 2: Eğer arama_metni boş değilse, bu metni içeren filmleri filtreleyen bir SQL sorgusu oluşturun.
# Arama büyük/küçük harf duyarlı olmamalıdır. (LOWER() fonksiyonunu kullanın.)
# GÜVENLİ YÖNTEM: "SELECT name, genre, year, rating FROM top250 WHERE LOWER(name) LIKE ?"
# Parametre: ('%' + arama_metni.lower() + '%',)
# Eğer arama metni boşsa tüm filmleri getirin.
#
# if arama_metni:
#     query = "KODU BURAYA YAZIN"
#     params = (KODU BURAYA YAZIN,)
#     result_df = fetch_data(query, params=params)
# else:
#     query = "KODU BURAYA YAZIN"
#     result_df = fetch_data(query)


# !GÖREV 3: Sonuçları st.dataframe ile gösterin.
# if not result_df.empty:
#    st.dataframe(result_df, use_container_width=True)
# else:
#    st.warning("Film bulunamadı!")