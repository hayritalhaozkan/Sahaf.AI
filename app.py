import nest_asyncio
nest_asyncio.apply()

import streamlit as st
from src.chatbot import create_rag_chain 

# --- ARAYÜZ TASARIMI ---


st.set_page_config(page_title="Sahaf.AI",layout="centered")


# Ana başlık
st.markdown("<h1 style='text-align: center;'>SAHAF.AI</h1>", unsafe_allow_html=True)

# --- CHATBOT MANTIĞI ---


chain = create_rag_chain()


if "messages" not in st.session_state:
    st.session_state.messages = []


chat_container = st.container(height=500, border=True)

with chat_container:
    
    if not st.session_state.messages:
        st.markdown("### Merhaba, Ben Sahaf.AI! 👋")
        st.info(
            "Kitaplar, yazarları ve eserleri hakkında merak ettiklerini "
            "bana sorabilirsin. Sana yardımcı olmaktan mutluluk duyarım."
        )
        st.markdown("##### Örnek Sorular:")
        st.markdown("- *Ahmet Ümit'in İstanbul Hatırası romanının konusu nedir?*")
        st.markdown("- *Bana polisiye türünde 3 tane roman önerebilir misin?*")
    
   
    else:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])


if prompt := st.chat_input("Bir yazar veya kitap hakkında soru sorun..."):
   
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Chatbot'un cevabını oluştur
    with st.spinner("Düşünüyorum..."):
       
        try:
            
            result = chain.invoke({"query": prompt})
            response = result["result"]
        
        except Exception as e:
            
            response = "Üzgünüm, bir sorunla karşılaştım. Lütfen birkaç saniye sonra tekrar deneyin."
            print(f"HATA OLUŞTU: {e}") 
       
        
    
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    
    st.rerun()