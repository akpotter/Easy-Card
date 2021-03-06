#悠遊卡餘額明細查詢

[![作者](https://img.shields.io/badge/作者-Zhi--Wei_Cai-red.svg?style=flat-square)](http://vox.vg/)  ![版本](https://img.shields.io/badge/版本-v0.3-green.svg?style=flat-square)   [![授權](https://img.shields.io/badge/授權-MIT-blue.svg?style=flat-square)][License]

###不受硬體限制

智慧卡公司對悠遊卡進行加密來禁止對卡片直接的餘額讀取功能，官方提供的查詢程式又僅支援少部分手機，且未對外開放 API 供大眾使用，十分不便。

![有卡號就能查詢！](demo.png)

讓 **悠遊卡餘額明細查詢** 讓你可以在任何支援 Python 的平台查詢你的悠遊卡餘額以及明細。

###使用說明

您的系統必須安裝 **Python 2.x** 及相關套件方能使用本程式。

您可以使用下列指令安裝缺少的模組：

```bash
pip install pycrypto pytz
```

> Mac OS X 已內建 Python，使用者僅需安裝額外的套件即可。

執行方式為：

```bash
python easycard.pyc [悠遊卡背面上的卡號]
```

> 由於程式碼本身存在讓有心人士作為惡意用途的可能（例如：干擾付費相關功能），在完全確定之前暫時不提供原始碼（.py）檔案。

###版權聲明

詳見 [`LICENSE`][License] 檔案。

[License]: https://github.com/x43x61x69/Easy-Card/blob/master/LICENSE