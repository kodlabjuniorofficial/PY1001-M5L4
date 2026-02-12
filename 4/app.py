# M5L4/4/app.py (Taslak Kod)
import streamlit as st

st.set_page_config(layout="wide") # Sayfayı geniş modda kullanmak için
st.title("🎨 Gurme Kedi Mim Stüdyosu")

# --- YAN MENÜ (SIDEBAR) ---

# GÖREV 1: st.sidebar kullanarak 'cute', 'orange', 'funny', 'black' seçeneklerini içeren
# bir selectbox oluşturun ve seçilen değeri "tur" değişkenine atayın.
# İpucu: st.sidebar.selectbox("Etiket", ["seçenek1", "seçenek2"])

# KODU AŞAĞIYA YAZIN
tur = 

# GÖREV 2: st.sidebar.text_input ile kullanıcıdan bir mesaj alın ve "mesaj" değişkenine atayın.
# Varsayılan değer "Bana mama ver!" olabilir.

# KODU AŞAĞIYA YAZIN



# --- ANA SAYFA ---

# GÖREV 3: "Mimi Hazırla" adında bir buton oluşturun ve if ile kontrol edin.

# KODU AŞAĞIYA YAZIN
if 

    # GÖREV 4: Butonun içinde, yan menüden aldığınız "tur", "mesaj" 
    # değişkenlerini kullanarak tam URL'yi f-string ile oluşturun.
    # Örnek URL: f"https://cataas.com/cat/{tur}/says/{mesaj}"
    # Oluşturduğunuz URL'yi "final_url" adında bir değişkene atayın.

    # KODU AŞAĞIYA YAZIN
    final_url = f""

    # GÖREV 5: st.image() ile "final_url" değişkenindeki mim'i gösterin.

    # KODU AŞAĞIYA YAZIN
    st.image(final_url)

    # BONUS: st.success() ile bir başarı mesajı ve st.balloons() ile balon efekti ekleyin!

    # KODU AŞAĞIYA YAZIN
    
    