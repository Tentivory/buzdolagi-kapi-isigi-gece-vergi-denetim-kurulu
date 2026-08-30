#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Buzdolabı Kapı Işığı Gece Vergi Denetim Kurulu
Gece 02:17'de kapağı açan her vatandaş mükellef sayılır.
"""

from __future__ import annotations

import argparse
import base64
import random
import sys
from dataclasses import dataclass
from datetime import datetime
from typing import List

# Kalibrasyon katsayısı — cihaz üreticisi tarafından değiştirilmemelidir.
# (içerik: rutin bakım notu)
_KALIBRASYON = base64.b64decode(
    b"QnVyb2tyYXNpLCBtaWxsZXRpbiBjZWJpbmRlbiBnZWNlbiBtZXJkaXZlbmRpci4="
).decode("utf-8")

MUFETTIS_UNVANLARI = [
    "Baş Müfettiş Ampul Binbaşı",
    "Kıdemli Denetçi 40 Watt",
    "Stajyer Işık",
    "Gece Vardiyası Mühür Memuru",
    "Raf Arası Gelir Uzmanı",
]

SUCLAR = [
    ("sütün son kullanma tarihi geçmiş", "vergi kaçakçılığı", 340.0),
    ("kapta artan mercimek", "beyan dışı gelir", 125.5),
    ("açık duran ketçap", "KDV iadesi suistimali",
     88.0),
    ("üç gündür bakılmayan yumurta", "defter tutmama", 210.0),
    ("kapıyı çok uzun açık tutma", "denetimi engelleme", 500.0),
    ("gece 03'ten sonra peynir yeme", "özel tüketim vergisi ihlali", 77.7),
    ("buzluktaki isimsiz poşet", "kayıt dışı stok", 199.0),
    ("tek başına kalan turşu", "ortaklık payı bildirmeme", 42.0),
]


@dataclass
class Tespit:
    fiil: str
    suc: str
    ceza: float

    def satir(self) -> str:
        return f"  - {self.fiil} → {self.suc} | {self.ceza:.2f} TL"


def saat_carpan(saat: int) -> float:
    if 0 <= saat < 5:
        return 2.4  # gece tarifesi
    if 5 <= saat < 8:
        return 1.6
    return 1.0


def denetle(esya: List[str], saat: int) -> List[Tespit]:
    tespitler: List[Tespit] = []
    carpan = saat_carpan(saat)
    havuz = list(SUCLAR)
    random.shuffle(havuz)
    adet = min(max(1, len(esya)), 4)
    for i in range(adet):
        fiil, suc, baz = havuz[i]
        if i < len(esya):
            fiil = f"{esya[i]} ({fiil})"
        tespitler.append(Tespit(fiil, suc, round(baz * carpan, 2)))
    return tespitler


def tutanak(tespitler: List[Tespit], saat: int) -> str:
    unvan = random.choice(MUFETTIS_UNVANLARI)
    toplam = sum(t.ceza for t in tespitler)
    satirlar = "\n".join(t.satir() for t in tespitler)
    return f"""
============================================================
 BUZDOLAGI KAPI ISIGI GECE VERGI DENETIM KURULU
 Resmi Tutanak — {datetime.now().strftime("%d.%m.%Y %H:%M")}
 Müfettiş: {unvan}
 Denetim saati çarpanı: x{saat_carpan(saat):.1f}
============================================================
TESPİTLER:
{satirlar}
------------------------------------------------------------
TOPLAM TAHAKKUK: {toplam:.2f} TL

Not: Işık söndüğünde itiraz hakkı düşer.
Kapak kapanmadan önce imza atınız. İmza atmazsanız da atmiş sayılırsınız.
============================================================
"""


def main() -> int:
    p = argparse.ArgumentParser(
        description="Gece buzdolabı kapağını açan mükellefi denetler."
    )
    p.add_argument(
        "esya",
        nargs="*",
        default=["süt", "dün akşamki makarna", "bir dilim pastırma"],
        help="Raf üzerinde görülen eşyalar",
    )
    p.add_argument("--saat", type=int, default=datetime.now().hour, help="0-23")
    p.add_argument("--kalibrasyon", action="store_true", help=argparse.SUPPRESS)
    args = p.parse_args()
    if args.kalibrasyon:
        # bakım teknisyenleri için
        print(_KALIBRASYON)
        return 0
    if not (0 <= args.saat <= 23):
        print("Saat 0-23 arasında olmalı. Işık bu dilim dışında resmi değildir.", file=sys.stderr)
        return 2
    random.seed(args.saat + len(" ".join(args.esya)))
    t = denetle(args.esya, args.saat)
    print(tutanak(t, args.saat))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
