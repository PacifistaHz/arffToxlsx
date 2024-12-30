import pandas as pd
import numpy as np

# Türkiye'nin 81 ilinin listesini oluşturma
iller = [
    'Adana', 'Adıyaman', 'Afyonkarahisar', 'Ağrı', 'Aksaray', 'Amasya', 'Ankara', 'Antalya', 'Ardahan', 'Artvin',
    'Aydın', 'Balıkesir', 'Bartın', 'Batman', 'Bayburt', 'Bilecik', 'Bingöl', 'Bitlis', 'Bolu', 'Burdur', 'Bursa',
    'Çanakkale', 'Çankırı', 'Çorum', 'Denizli', 'Diyarbakır', 'Düzce', 'Edirne', 'Elazığ', 'Erzincan', 'Erzurum',
    'Eskişehir', 'Gaziantep', 'Giresun', 'Gümüşhane', 'Hakkari', 'Hatay', 'Iğdır', 'Isparta', 'İstanbul', 'İzmir',
    'Kahramanmaraş', 'Karabük', 'Karaman', 'Kars', 'Kastamonu', 'Kayseri', 'Kırıkkale', 'Kırklareli', 'Kırşehir',
    'Kilis', 'Kocaeli', 'Konya', 'Kütahya', 'Malatya', 'Manisa', 'Mardin', 'Mersin', 'Muğla', 'Muş', 'Nevşehir',
    'Niğde', 'Ordu', 'Osmaniye', 'Rize', 'Sakarya', 'Samsun', 'Siirt', 'Sinop', 'Sivas', 'Şanlıurfa', 'Şırnak',
    'Tekirdağ', 'Tokat', 'Trabzon', 'Tunceli', 'Uşak', 'Van', 'Yalova', 'Yozgat', 'Zonguldak'
]

# Rastgele veri oluşturma
data = {
    'ProductID': np.random.randint(1, 1001, size=1000),
    'OrderID': np.random.randint(10000, 20000, size=1000),
    'CustomerID': np.random.randint(1000, 2000, size=1000),
    'Address': np.random.choice(iller, size=1000),
    'Quantity': np.random.randint(1, 10, size=1000),
    'OrderDate': pd.date_range(start='2023-01-01', periods=1000, freq='D'),
    'ProductPrice': np.random.uniform(10, 1000, size=1000).round(2),
    'Country': ['Türkiye'] * 1000,
    'ProductCategory': np.random.choice(['Elektronik', 'Giyim', 'Ev Eşyaları'], size=1000),
    'CustomerAge': np.random.randint(18, 70, size=1000),
    'CustomerGender': np.random.choice(['Erkek', 'Kadın', 'Diğer'], size=1000),
    'PaymentMethod': np.random.choice(['Kredi Kartı', 'Havale', 'Kapıda Ödeme'], size=1000),
    'PromotionApplied': np.random.choice(['Evet', 'Hayır'], size=1000)
}

# DataFrame oluşturma
df = pd.DataFrame(data)

# Veriyi Excel dosyası olarak kaydetme
df.to_excel('genisletilmis_hepsiburada_satis_veri_seti.xlsx', index=False)

print("Genişletilmiş veri seti oluşturuldu ve 'genisletilmis_hepsiburada_satis_veri_seti.xlsx' olarak kaydedildi.")
