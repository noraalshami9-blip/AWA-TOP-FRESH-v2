# 🚀 إعداد النشر التلقائي إلى Google Cloud Storage

## الخطوة 1️⃣: إنشاء حساب Google Cloud
1. اذهب إلى [Google Cloud Console](https://console.cloud.google.com)
2. أنشئ مشروع جديد (مثل: `awa-top-fresh`)
3. فعّل **Cloud Storage API**

## الخطوة 2️⃣: إنشاء Bucket
```bash
gsutil mb gs://awa-top-fresh-bucket
```

أو من خلال Console:
1. اذهب إلى **Cloud Storage > Buckets**
2. اضغط **Create Bucket**
3. اسم: `awa-top-fresh-bucket`
4. الموقع: اختر الأقرب إليك
5. اضغط **Create**

## الخطوة 3️⃣: إنشاء Service Account
1. اذهب إلى **IAM & Admin > Service Accounts**
2. اضغط **Create Service Account**
3. الاسم: `github-deployer`
4. اضغط **Create and Continue**
5. أضفة الدور: **Storage Admin**
6. اضغط **Continue** ثم **Done**

## الخطوة 4️⃣: إنشاء JSON Key
1. اذهب إلى Service Account الذي أنشأته
2. اختر **Keys** 
3. اضغط **Add Key > Create new key**
4. اختر **JSON**
5. سيُحمل ملف JSON - احفظه بأمان

## الخطوة 5️⃣: إضافة Secrets في GitHub
1. اذهب إلى مستودعك: `AWA-TOP-FRESH-v2`
2. اذهب إلى **Settings > Secrets and variables > Actions**
3. اضغط **New repository secret**

أضفة 3 secrets:
```
1. GCP_SA_KEY = (محتوى ملف JSON كاملاً)
2. GCP_PROJECT_ID = (معرف مشروعك)
3. GCS_BUCKET_NAME = awa-top-fresh-bucket
```

## الخطوة 6️⃣: تحديث الملفات HTML
استبدل روابط الصور:
```html
<!-- من -->
<img src="logo.png">

<!-- إلى -->
<img src="https://storage.googleapis.com/awa-top-fresh-bucket/logo.png">
```

## الخطوة 7️⃣: الاختبار
1. ارفع تغيير على `main` branch
2. اذهب إلى **Actions** في GitHub
3. شاهد الـ workflow يعمل تلقائياً ✅

## 📊 النتيجة
كل ما ترفعه على GitHub سيُنشر تلقائياً على Google Cloud Storage! 🚀

---

**ملاحظات مهمة:**
- ✅ يعمل تلقائياً عند كل push على `main`
- ✅ يرفع جميع: `.html`, `.png`, `.py`, `.json`
- ⚠️ تأكد من حفظ JSON key بأمان
- 💡 يمكنك ربط Google Cloud CDN للسرعة الأفضل
