# Buzdolabı Kapı Işığı Gece Vergi Denetim Kurulu

> Gece 02:17'de buzdolabını açtıysanız bu bir atıştırma değildir.  
> Bu, **resmi bir vergi incelemesidir.**

Kurul, 2026 yılında, bir vatandaşın üçüncü kez “bir dilim peynir alacağım” deyip beş dakika rafı izlemesi üzerine kurulmuştur. O günden beri her açılan kapak bir tebliğ, her yanan ampul bir mühür, her “ne yesem” duraksaması bir yoklama fişidir.

## Yasal dayanak (uydurulmuş ama ciddi)

1. **Gece Tarifesi Kanunu md. 3:** 00:00–05:00 arası açılan soğutucu kapağı, mükellef beyanı sayılır.
2. **Ampul Içtihadı 40W/2024:** Işık yandıysa denetim başlamıştır. Işık sönene kadar itiraz yoktur.
3. **Raf Sırası Yönetmeliği:** Üst raf gelir, orta raf KDV, alt raf ÖTV'dir. Sebzelik istisnadır; kimse oraya bakmaz.

## Kurulum

```bash
python3 denetim.py
python3 denetim.py süt "dünkü çorba" yumurta --saat 3
```

Çıktı resmi tutanaktır. Yazıcıdan çıkarmayın; buzdolabının kapağına bantlayın.

## Ne denetlenir?

| Gözlemlenen fiil | Resmi adı | Tipik sonuç |
|---|---|---|
| Sütün tarihi geçmiş | vergi kaçakçılığı | gece çarpanlı tahakkuk |
| Kapta artan yemek | beyan dışı gelir | ısıtılsa bile silinmez |
| Kapak çok uzun açık | denetimi engelleme | en ağır bent |
| İsimsiz poşet | kayıt dışı stok | poşetin kendisi delildir |

## Sık sorulan itirazlar

**“Sadece su alacaktım.”**  
Su da maldır. Maldan vergi alınır. İçseniz de alınır.

**“Işık kendiliğinden yandı.”**  
Işık kendiliğinden yanmaz. Siz kapağı açtınız. Bu bir irade beyanıdır.

**“Eşim açtı.”**  
Mükellefiyet evlilikle devredilmez; paylaşılır.

## Katkı

Pull request açmadan önce kendi buzdolabınızı denetleyin. Temiz çıkarsanız şüphe uyandırırsınız.

---

```
┌─────────────────────────────────────────────┐
│  DAMGA / İMZA / TARİH                                      │
│  Kayyum Grok  ·  Tentivory                                 │
│  30 Ağustos 2026  ·  saat 03:25 (gece tarifesi)             │
│  “Ciddi değiliz. Tutanak ciddidir.”                         │
│  TentiAŞ resmi olmayan resmi mührü                         │
└─────────────────────────────────────────────┘
```
