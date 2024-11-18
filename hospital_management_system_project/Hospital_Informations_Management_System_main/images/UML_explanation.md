# Person Sınıfı:
# Özellikler: 
- id (kimlik numarası), 

- name (isim), gender (cinsiyet), 

- dob (doğum tarihi), 

- phone (telefon numarası), 

- email (e-posta adresi).

# Açıklama: 

- Person sınıfı, hastane sistemindeki kişileri temsil eder.

- Bu sınıf, doktorlar, çalışanlar ve hastalar gibi farklı rolleri içerebilir.

# Employee Sınıfı:
# Özellikler: 
- salary (maaş), 

- dept (departman).

# Açıklama: 
- Employee sınıfı, Person sınıfından türetilmiştir ve hastane personelini temsil eder. 

- Çalışanların maaşları ve departmanları bu sınıf altında yönetilir.

# Doctor ve Worker Alt Sınıfları:
# Özellikler: 
- Her ikisi de isMedical adında bir boolean özelliğe sahiptir. 

- Doctor için bu değer True iken Worker için False’tur.

# Açıklama: 
- Doctor ve Worker sınıfları, Employee sınıfından türetilmiştir. 

- Doctor sınıfı tıbbi personeli, Worker sınıfı ise tıbbi olmayan personeli temsil eder.

# Patient Sınıfı:
# Özellikler: 
- illness (hastalık), 

- debt (borç).
# Açıklama: 
- Patient sınıfı, hastaları temsil eder. 

- Bu sınıf, hastaların sağlık durumunu ve finansal bilgilerini içerir.

# Medicine Sınıfı:
# Özellikler: 
- id, name (isim), 

- price (fiyat), stock (stok).

# Açıklama: 
- Medicine sınıfı, hastanede kullanılan ilaçları temsil eder. 

- İlaçların kimlik numaraları, isimleri, fiyatları ve stok miktarları bu sınıf altında yönetilir.