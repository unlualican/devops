Bu proje, DevOps alanındaki becerilerimi sergilemek amacıyla geliştirilmiş bir uygulamadır. Projede bir API geliştirilmiş, Docker kullanılarak konteynerleştirilmiş ve Kubernetes kullanılarak dağıtılmıştır. Aşağıda, proje kapsamında gerçekleştirdiğim adımlar detaylı bir şekilde açıklanmıştır.

1. API Geliştirilmesi
API Özellikleri:

GET /: Bu endpoint, "{"msg":"BC4M"}" cevabını döner.
GET /health: Bu endpoint, uygulamanın sağlık durumunu kontrol eder ve sağlık durumunu döner.
POST /echo: Bu endpoint, body'de gelen verileri geri döner

2. Dockerfile Oluşturulması

my_api.dockerfile dosyamı oluşturdum , gereksinimleri ve çalışma pathlerini kontrol ettim

3. Docker Image Oluşturulması ve Docker Hub'a Yüklenmesi

Docker Hub'daki imaj adresi: unlualican/myapi  # 'docker pull unlualican/myapi' pull etmek için image yi
Google Cloud Platform'daki GCP imaj adresi: us.gcr.io/spacture/myapi # halihazırda gcp kullandığım için gcp kullandım

4. Kubernetes Kurulumu ve Deployment
Google Cloud Platform (GCP) üzerinde bir Kubernetes cluster kurdum. Kubernetes kullanarak uygulamayı dağıttım ve deployment'ı sağladım. Ayrıca, uygulama sağlıksız olduğunda otomatik olarak restart olması için bir health check yapılandırdım.

5. Dışarıdan Erişim Sağlanması
Uygulamaya dışarıdan erişim sağlamak için bir Load Balancer yapılandırdım. Böylece uygulamanın URL üzerinden erişilmesi mümkün hale geldi. İşte erişim test komutları:
curl http://34.46.112.3   {"msg":"BC4M"}
curl http://34.46.112.3/health (Sağlık kontrolü)
curl -X POST http://34.46.112.3/echo -H "Content-Type: application/json" -d '{"key": "value"}' (Body verisi testi)





