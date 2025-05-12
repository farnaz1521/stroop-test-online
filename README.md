# تست جامع استروپ تحت وب – Stroop Test Web App

این پروژه یک پلتفرم روان‌شناسی آنلاین برای اجرای تست جامع استروپ است شامل چهار نوع تست:

1. تست کلاسیک (رنگ–کلمه)
2. تست هیجانی (کلمات با بار عاطفی)
3. تست مکانی (عدم تطابق موقعیت–جهت)
4. تست چهره‌ای (با تصاویر یا ایموجی + صدا)

## 🎯 قابلیت‌ها:

- فرم ثبت‌نام کامل با نام، کد داوطلب، سن، شغل و ...
- تست با زمان‌سنج و ثبت پاسخ‌ها
- خروجی فایل Excel و نمودار واکنش
- نسخه صوتی و تصویری برای دسترسی‌پذیری بهتر
- مناسب برای اجرای پایان‌نامه یا پژوهش آنلاین

---

## 🔧 Technologies Used

- Python 3.x
- Flask
- HTML5, JavaScript
- Pandas, Openpyxl, Matplotlib
- قابل استقرار روی Render یا هر پلتفرم Python WSGI

---

## 🚀 راه‌اندازی محلی (local)

```bash
git clone https://github.com/yourusername/stroop-test-online.git
cd stroop-test-online
pip install -r requirements.txt
python server.py
