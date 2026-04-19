# bulut2
Real-Time Weather & Max Temp Simulation
Bu proje, bir hava durumu istasyonundan gelen verileri simüle ederek anlık sıcaklık ve günlük maksimum sıcaklık verilerini takip eden bir Python uygulamasıdır. 

Özellikler
Anlık Veri Üretimi: Gerçekçi sıcaklık (15°C - 35°C) ve nem değerleri üretir.
Günlük Maksimum Takibi: Kod çalıştığı sürece o gün içindeki en yüksek sıcaklığı takip eder.
Otomatik Sıfırlama: Gün değiştiğinde maksimum sıcaklık değerini otomatik olarak sıfırlar.
Alarm Durumu: Sıcaklık 32°C eşiğini geçtiğinde otomatik olarak "HEAT_WAVE_ALERT" uyarısı verir.

Teknik Detaylar

Dil: Python
Veri Formatı: JSON
Kütüphaneler: json, random, time, datetime (Standart kütüphaneler)

Gün 1: 09.04.2026
Python ile anlık sıcaklık ve günlük en yüksek değerlerini üreten simülasyon motoru yazıldı.
AWS Kinesis entegrasyonu için gerekli veri yapıları tanımlandı.

Simülasyon Motoru: Python ile anlık sıcaklık ve "günlük maksimum sıcaklık" takibi yapan akıllı bir sensör simülasyonu geliştirildi.

Bulut Entegrasyonu: AWS Kinesis Data Stream yapılandırıldı. boto3 kütüphanesi kullanılarak lokal ortam ile AWS bulutu arasında canlı veri hattı kuruldu.

Veri Akışı Doğrulandı
Sistem başarıyla test edildi ve verilerin bilgisayarımdan AWS bulutuna ulaştığı kanıtlandı.
AWS Konsolu üzerindeki Data Viewer kullanılarak, gönderilen veriler canlı olarak görüntülendi.
Sonuç: Yazılan Python kodu ile AWS Kinesis arasında kesintisiz bir veri hattı kuruldu. Gönderilen her sıcaklık verisi, bulut tarafında anında kayıt altına alındı.

Karşılaşılan Teknik Engeller ve Çözümleri
Sorun: Lambda Kinesis Tetikleyici Hatası (Access Denied)
Lambda fonksiyonuna Kinesis Stream tetikleyicisi eklenmeye çalışıldığında şu hata ile karşılaşılmıştır:

"An error occurred when creating the trigger: Cannot access stream... Please ensure the role can perform the GetRecords, GetShardIterator... actions on your stream."


Gün 2: 10.04.2026
Çözüm:Lambda'nın bağlı olduğu IAM Rolüne AWSLambdaKinesisExecutionRole politikası tanımlanarak veri işleme izni sağlandı.

Gün 3: 19.04.2026
Genel Değerlendirme ve Sonuç
Amaç: Bu projenin amacı, gerçek zamanlı bir IoT (Nesnelerin İnterneti) hava durumu istasyonundan elde edilecek verilerin; modern ve sunucusuz (serverless) bulut teknolojileri kullanılarak toplanması, eşzamanlı olarak analiz edilmesi ve kalıcı olarak depolanmasıdır.

Sonuç: Geliştirilen mimari sayesinde; Python tabanlı simülatör ile üretilen anlık sensör verileri AWS Kinesis üzerinden başarılı bir şekilde bulut ortamına aktarılmıştır. AWS Lambda servisi, bu akışı dinleyerek gerçek zamanlı anomali tespiti (Yüksek Sıcaklık Alarmı) yapmış ve işlenen veriler NoSQL formatında AWS DynamoDB üzerinde kayıt altına alınmıştır. Sistem; bulut bilişim mimarisine, "Least Privilege" (En Düşük Ayrıcalık) güvenlik prensiplerine ve asenkron veri işleme standartlarına tam uygun olarak uçtan uca çalışır halde teslim edilmiştir.
