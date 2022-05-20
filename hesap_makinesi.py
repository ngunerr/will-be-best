from ast import Str
import string
from tkinter import N


kontrol = 1

    
while kontrol == 1:
    print("Toplama işlemi için 1'e basınız.\n","Çıkarma işlemi için 2'ye basınız.\n","Bölme işlemi için 3'e basınız,\n","Çarpma işlemi için 4'e basınız\n","Hesap makinesinden çıkmak için 5'e basınız.")
    islem = input("Seçiminiz:")
    while islem == "1":
        sayi1 = int(input("İlk sayıyı giriniz:"))
        sayi2 = int(input("ikinci sayıyı giriniz:"))
        print("Sayıların toplamı:", sayi1 + sayi2, "Üst menüye dönmek için 1'e basınız.","Toplama işlemine devam etmek için 2 ye basınız.")
        secim = input("Seçiminiz:")
        if secim == "1":
            islem = 0
            break
        else:
            continue
    while islem == "2":
        sayi1 = int(input("İlk sayıyı giriniz:"))
        sayi2 = int(input("ikinci sayıyı giriniz:"))
        print("Sayıların çıkarması:", sayi1 - sayi2, "Üst menüye dönmek için 1'e basınız.","Çıkarma işlemine devam etmek için 2 ye basınız.")
        secim = input("Seçiminiz:")
        if secim == "1":
            islem = 0
            break
        else:
            continue
    while islem == "3":
        sayi1 = int(input("İlk sayıyı giriniz:"))
        sayi2 = int(input("ikinci sayıyı giriniz:"))
        print("Sayıların bölümü:", sayi1 / sayi2, "Üst menüye dönmek için 1'e basınız.","Bölme işlemine devam etmek için 2 ye basınız.")
        secim = input("Seçiminiz:")
        if secim == "1":
            islem = 0
            break
        else:
            continue
    while islem == "4":
        sayi1 = int(input("İlk sayıyı giriniz:"))
        sayi2 = int(input("ikinci sayıyı giriniz:"))
        print("Sayıların Çarpması:", sayi1 * sayi2, "Üst menüye dönmek için 1'e basınız.","Çarpma işlemine devam etmek için 2 ye basınız.")
        secim = input("Seçiminiz:")
        if secim == "1":
            islem = 0
            break
        else:
            continue
    if islem >= "5":
        kontrol = 0
        print("Hesap makinesinden çıkış yapılıyor....")