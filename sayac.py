import time  # time modülünü içe aktarıyoruz

def geri_say(saniye):
    while saniye > 0:  # Sayaç sıfır olana kadar döngüyü çalıştır
        print(f"Kalan süre: {saniye} saniye") # "f" karakteri, bu stringin formatlama yapacağını belirtir. "{saniye}" ifadesi, "saniye" değişkeninin değerini yerleştireceğimiz yeri belirtir.
        time.sleep(1)  # 1 saniye beklet
        saniye -= 1  # Saniyeyi azalt

    print("Süre doldu!")

if __name__ == '__main__':
    try:
        girilen_sure = int(input("Geri sayım süresini saniye cinsinden girin: "))
        geri_say(girilen_sure)
    except ValueError:
        print("Geçerli bir sayı girilmedi.")
