# Hrack (Hash Crack)
## أداة تخمين كلمات سر شبكات الـWi-Fi وحسابات الانستقرام

<img src="https://github.com/tlersa/Hrack/assets/111729973/ec7a16e1-057e-4bae-b4b9-e39084428998" width="1000" alt="واجهة الأداة">

### أوامر التثبيت (Linux, iSH, Termux)
```
git clone https://github.com/tlersa/Hrack.git
cd Hrack/
python3 Hrack.py
```

### المميزات
- مجانية ومفتوحة المصدر ✔️
- تخمين سريع يقدر بـ0.5ث لكل كلمة سر ✔️
- تدعم ميزة استخدام ملفات البروكسيات لخيار [2] - Instagram ✔️
- تدعم ميزة الإرسال للتليقرام لخيار [2] - Instagram ✔️
- إذا لم تكن مثبت المكاتب المطلوبة (requests, random, os, time, user_agent, ast, pywifi) سيتم تثبيتها تلقائياً ✔️

### الملاحظات ⚠️
- أي استخدام خاطئ للأداة فنحن غير مسؤولين
- في خيار [1] - Wi-Fi يجب أن تكون الشبكة المستهدفة قريبة منك
- خيار [1] - Wi-Fi لا يعمل على Linux بسبب مكتبة PyWiFi لا تدعم إلا نظام Windows

### تثبيت المكاتب (إذا كنت تستخدم Linux فلا تحتاج لتثبيتها)

```
pip install requests random os time user_agent ast pywifi
```
