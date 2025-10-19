
import os
from dotenv import load_dotenv
import streamlit as st 

# Gerekli LangChain bileşenleri
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA




@st.cache_resource
def create_rag_chain():

    load_dotenv()
    
    
    print("Bileşenler ilk defa yükleniyor ve önbelleğe alınıyor...")

    
    embedding_model_name = "BAAI/bge-m3"
    db_directory = "./chroma_db"
    embeddings = HuggingFaceEmbeddings(model_name=embedding_model_name)
    db = Chroma(persist_directory=db_directory, embedding_function=embeddings)
    print("Veritabanı başarıyla yüklendi.")

    # 2. SOHBET BEYNİ (LLM): Cevap üretimi için Gemini modelini başlatıyoruz
    llm = ChatGoogleGenerativeAI(model="gemma-3-27b-it") # Model adını güncelledim
    print("Gemini LLM başarıyla yüklendi.")

    # 3. PROMPT ve RAG ZİNCİRİ
    prompt_template = """Senin adın Sahaf ve kitaplar hakkında bilgi veren yardımcı bir yapay zeka asistanısın.

    Sana bir soru sorulduğunda şu kurallara göre cevap ver:
    1.  **Kendinle İlgili Sorular:** Eğer soru senin kim olduğun, ne olduğun veya ne işe yaradığınla ilgiliyse (örneğin: 'sen kimsin?', 'nesin?', 'ne yaparsın?'), BAĞLAMI dikkate alma. Kendini Sahaf olarak tanıt ve kitaplar hakkında bilgi vermek için tasarlandığını söyle.
    2.  **Kitaplarla İlgili Sorular:** Diğer tüm sorularda, cevabını mutlaka sana verilen BAĞLAM'a dayandır. Bağlamdaki bilgileri kullanarak soruyu cevapla.
    3.  **Bilgi Olmadığında:** Eğer bağlamda cevap yoksa, "Üzgünüm, veri setimde bu soruyla ilgili net bir bilgi bulamadım. Başka bir yazar veya kitap hakkında bilgi almak ister misiniz?" de.
    4.  **Dürüstlük:** Asla bilgi uydurma.

    Bağlam: {context}

    Soru: {question}

    Cevap:"""
    PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=db.as_retriever(),
        return_source_documents=False, 
        chain_type_kwargs={"prompt": PROMPT}
    )
    print("RAG Zinciri başarıyla kuruldu ve önbelleğe alındı.")
    
    return qa_chain