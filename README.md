## Sahaf.AI

## Projenin Amacı

Bu projenin amacı, RAG (Retrieval Augmented Generation) mimarisi kullanarak belirli bir bilgi kaynağı (kitap özetleri ve detayları) hakkında uzmanlaşmış bir chatbot geliştirmektir. Chatbot, kullanıcıların sorularını, sağlanan metin verilerini referans alarak yanıtlayacak ve geliştirilen bu sistem, bir web arayüzü üzerinden sunulacaktır.

## Veri Seti Hakkında Bilgi

Bu projede, chatbot'un bilgi kaynağı olarak Kaggle üzerinde Muhammed İbrahim Top tarafından paylaşılan **"Turkish Book Data Set"** kullanılmıştır. Veri setindeki kitap açıklamaları, güçlü bir embedding modeli (`BAAI/bge-m3`) kullanılarak önceden işlenmiş ve bir ChromaDB vektör veritabanına dönüştürülmüştür. Bu hazır veritabanı, projenin hızlı bir şekilde çalıştırılabilmesi için depo içerisinde sunulmaktadır.

### Veri Seti Künyesi

* **Veri Seti Adı:** Turkish Book Data Set
* **Oluşturan:** Muhammed İbrahim Top
* **Kaynak:** [Kaggle](https://www.kaggle.com/datasets/muhammedbrahimtop/turkish-book-data-set)
* **Lisans:** [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)

## Kullanılan Yöntemler ve Teknolojiler

Projenin çözüm mimarisini oluşturan temel teknolojiler şunlardır:

* **Hibrit RAG Mimarisi:** Proje, hibrit bir model üzerine kurulmuştur. Arama (Retrieval) işlemi yerel olarak çalışırken, cevap üretme (Generation) işlemi bulut tabanlı bir API üzerinden gerçekleştirilir.
* **LLM (Generation Model):** Cevap üretimi için **Google Gemini API** (`gemma-3-27b-it`) kullanılmıştır.
* **Embedding Model:** Anlamsal arama ve vektörleştirme işlemi için, yerel olarak çalışan ve yüksek performanslı **`BAAI/bge-m3`** Hugging Face modeli tercih edilmiştir.
* **Vektör Veritabanı:** **ChromaDB**, metin parçalarının vektör temsillerini depolamak ve verimli bir şekilde aramak için kullanılmıştır.
* **Pipeline Framework:** **LangChain**, RAG mimarisinin tüm bileşenlerini (retriever, prompt, LLM) birbirine bağlayan ana çatı olarak görev yapmıştır.
* **Web Arayüzü:** Uygulama, **Streamlit** kütüphanesi kullanılarak interaktif bir web arayüzüne dönüştürülmüştür.
* **Paket Yöneticisi:** Projenin bağımlılıkları, modern ve hızlı bir paket yöneticisi olan **`uv`** ile yönetilmiştir.

## Elde Edilen Sonuçlar

Proje sonucunda, belirlenen veri setindeki kitaplar hakkında sorulan sorulara akıcı ve doğru cevaplar üretebilen, kullanıcı dostu bir web uygulaması başarıyla geliştirilmiştir. Geliştirme sürecinde karşılaşılan API yapılandırma ve kütüphane bağımlılık sorunları, hibrit bir mimari ve belirli kütüphane versiyonlarının `requirements.txt` ile sabitlenmesi sayesinde aşılmıştır.

## Web Uygulaması Linki

> Deployed web uygulamasına erişim linki buraya eklenecektir.

## Çalışma Kılavuzu

Bu proje, önceden oluşturulmuş veritabanı sayesinde hızlı bir şekilde çalıştırılabilir.

### 1. Kurulum Öncesi

* **Depoyu Klonlayın:**
    ```bash
    git clone [https://github.com/KULLANICI_ADINIZ/Sahaf.AI.git](https://github.com/hayritalhaozkan/Sahaf.AI.git)
    cd Sahaf.AI
    ```
* **API Anahtarı:** Projenin ana dizininde `.env` adında bir dosya oluşturun ve içine Google AI Studio'dan aldığınız API anahtarınızı aşağıdaki formatta ekleyin:
    ```bash
    GOOGLE_API_KEY="AIzaSy..."
    ```

### 2. Ortam Kurulumu

* **Sanal Ortamı Kurun ve Aktive Edin (`uv` ile):**
    ```bash
    uv venv
    source .venv/bin/activate
    ```
* **Gerekli Kütüphaneleri Yükleyin:**
    ```bash
    uv pip install -r requirements.txt
    ```

### 3. Uygulamayı Çalıştırma

* **Uygulamayı Başlatın:** Artık hazırsınız! Veritabanı oluşturma adımlarına gerek kalmadan direkt uygulamayı çalıştırabilirsiniz.
    ```bash
    streamlit run app.py
    ```