from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

print("Veritabanı ve embedding modeli yükleniyor...")

# Arama için kullandığımız embedding modelini ve veritabanını yüklüyoruz
embedding_model_name = "sentence-transformers/all-MiniLM-L6-v2"
db_directory = "./chroma_db"
embeddings = HuggingFaceEmbeddings(model_name=embedding_model_name)
db = Chroma(persist_directory=db_directory, embedding_function=embeddings)

# Veritabanını bir "retriever" nesnesine dönüştürüyoruz
retriever = db.as_retriever(search_kwargs={"k": 4}) # En iyi 4 sonucu getir

# Test edeceğimiz soru
soru = "Bana 3 tane bilimkurgu romanı önerir misin?"

print(f"\n'Arama Beyni'ne sorulan soru: '{soru}'")
print("\n--- Bulunan Sonuçlar ---")

# Sadece arama işlemini yapıyoruz
retrieved_docs = retriever.invoke(soru)

# Bulunan sonuçların içeriğini yazdırıyoruz
if not retrieved_docs:
    print("Hiçbir sonuç bulunamadı.")
else:
    for i, doc in enumerate(retrieved_docs):
        print(f"--- Sonuç {i+1} ---\n")
        print(doc.page_content)
        print("\n---------------------\n")