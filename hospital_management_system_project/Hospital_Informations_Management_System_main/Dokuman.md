# Hastane Yönetim Sistemi

Merhaba!

Ben Doğukan Öztürk, bu belgeyi Hastane Yönetim Sistemi adlı bir proje için oluşturdum. 
Bu proje, hastane yönetimini kolaylaştırmak için geliştirilmiş bir yazılımın parçalarını içeriyor. 
İçerideki sınıflar ve metotlar, hastane personeli, hastalar, ilaçlar ve hastane ile ilgili 
diğer verilerin yönetimini sağlamak için tasarlandı.

# Tanımlar
# Medicine Sınıfı

id: İlaç kimlik numarası

name: İlaç adı

price: İlaç fiyatı

stock: İlaç stok miktarı

description: İlaç hakkında açıklama

# Person Sınıfı

id: Kişi kimlik numarası

name: Kişi adı

gend: Kişinin cinsiyeti

dob: Kişinin doğum tarihi

phone: Kişinin telefon numarası

email: Kişinin e-posta adresi

Employee Sınıfı (Person sınıfından türetilmiştir)

salary: Çalışanın maaşı

dept: Çalışanın departmanı

# Doctor Sınıfı (Employee sınıfından türetilmiştir)

IsMedical: Doktorun tıbbi olup olmadığını belirten boolean değer

Worker Sınıfı (Employee sınıfından türetilmiştir)

IsMedical: Çalışanın tıbbi olup olmadığını belirten boolean değer

# Patient Sınıfı (Person sınıfından türetilmiştir)

illness: Hasta hastalığı

debt: Hasta borcu

Pa_Med Sınıfı

PatientID: Hastanın kimlik numarası

MedicineID: İlacın kimlik numarası

Pa_Doc Sınıfı

PatientID: Hastanın kimlik numarası

DoctorID: Doktorun kimlik numarası

# Metotlar
# Dosya İşlemleri

save_doctors: Doktor listesini dosyaya kaydeder

save_workers: Çalışan listesini dosyaya kaydeder

save_patients: Hasta listesini dosyaya kaydeder

save_medicines: İlaç listesini dosyaya kaydeder

save_pa_doc: Doktor-hasta eşleştirmelerini dosyaya kaydeder

save_pa_med: Hasta-ilac eşleştirmelerini dosyaya kaydeder


zip_data: Verileri bir ZIP dosyasına sıkıştırır

load_doctors: Doktor listesini dosyadan yükler

load_workers: Çalışan listesini dosyadan yükler

load_patients: Hasta listesini dosyadan yükler

load_medicines: İlaç listesini dosyadan yükler

load_pa_doc: Doktor-hasta eşleştirmelerini dosyadan yükler

load_pa_med: Hasta-ilac eşleştirmelerini dosyadan yükler

unzip_data: Verileri bir ZIP dosyasından çıkarır

# Diğer Metotlar


invalid_id: Geçersiz kimlik numarası kontrolü yapar

invalid_gend: Geçersiz cinsiyet kontrolü yapar

invalid_dob: Geçersiz doğum tarihi kontrolü yapar

invalid_phone: Geçersiz telefon numarası kontrolü yapar

invalid_salary: Geçersiz maaş kontrolü yapar

invalid_debt: Geçersiz borç kontrolü yapar

invalid_price: Geçersiz fiyat kontrolü yapar

invalid_stock: Geçersiz stok miktarı kontrolü yapar

sort_people_list_by_column: Kişi listesini sütuna göre sıralar

sort_medicines_list_by_column: İlaç listesini sütuna göre sıralar

# Kullanıcı Arayüzü Metotları

credits_press: Kredi bilgilerini göstermek için alt pencere açar

# Diğer Metotlar


main: Ana fonksiyon, programı başlatır

on_ready: Programın başlaması için hazırlıkları yapar

on_close: Program kapatıldığında dosyaları kaydeder ve sıkıştırır

# Kod Dökümanı
Hastane Yönetim Sistemi kod dökümanı, 
projenin Python kodlarını içerir. 
Bu kodlar, belirli sınıfların ve metotların nasıl oluşturulduğunu, 
işlevlerini ve kullanımlarını açıklar.

# Sonuç

Bu proje, hastane yönetimini otomatize etmek ve 
verimliliği artırmak için geliştirilmiş bir yazılım çözümüdür. 
Umarım bu belge, projeyi anlamanıza yardımcı olur.

# Yazar: Doğukan Öztürk