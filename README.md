# دعوة زفاف عبدالرحمن بن عمر الدايل

صفحة دعوة واحدة، ملف مستقل بلا أي بناء أو تبعيات.

## النشر

المستودع `D-M-26/D-M-26.github.io` يُنشر تلقائيًا من الفرع `main` على:
<https://d-m-26.github.io/>

أي تعديل يُدفع إلى `main` يظهر على الرابط خلال دقيقة تقريبًا.

> لو تغيّر عنوان النشر، شغّل `./set-domain.sh https://العنوان-الجديد` ثم ارفع.

## فحص المعاينة قبل الإرسال

- فيسبوك/واتساب: <https://developers.facebook.com/tools/debug/>
- تويتر: <https://cards-dev.twitter.com/validator>

واتساب يحتفظ بالمعاينة في ذاكرته، فإذا عدّلت الصورة أعد الفحص من أداة فيسبوك (Scrape Again) قبل إعادة الإرسال.

## الملفات

| الملف | الغرض |
|---|---|
| `index.html` | الدعوة كاملة (يجب رفعه) |
| `share-v3.png` | صورة معاينة الرابط 1200×630 (يجب رفعه) |
| `share-card.html` | مصدر صورة المعاينة، لإعادة توليدها |
| `NotoNaskhArabic.ttf` | خط لتوليد الصورة محليًا فقط |
| `set-domain.sh` | يضبط روابط og على عنوانك |
| `زواج-عبدالرحمن-عمر-الدايل.ics` | ملف التقويم الذي يفتحه زر «أضف الموعد لتقويمك» (يجب رفعه) |
| `make-ics.py` | يولّد ملف التقويم؛ عدّل النصوص فيه ثم شغّل `python3 make-ics.py` |
| `v1-najdi.html` | تصميم أول مرفوض، محفوظ للرجوع |

### إعادة توليد صورة المعاينة

```
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu \
  --allow-file-access-from-files --window-size=1200,630 --virtual-time-budget=15000 \
  --screenshot=share-v3.png share-card.html
```
