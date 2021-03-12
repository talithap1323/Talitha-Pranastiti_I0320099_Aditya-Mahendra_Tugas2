print ("SOAL 1")
print ("=============")

print ("Soal yang Akan Dihitung")
print ("1. Luas Persegi Panjang")
print ("2. Luas Lingkaran")
print ("3. Luas Kubus")
print ("4. Konversi Suhu (Celcius ke Fahrenheit)")
print ("5. Konversi Suhu (Reamur ke Kelvin)")

choice= input("Pilih soal yang akan dihitung: ")

if choice == "1":
    panjang = float(input("Panjang Persegi Panjang: "))
    lebar = float(input("Lebar Persegi Panjang: "))
    luas = panjang * lebar
    print("Luas Persegi Panjang adalah", luas, "satuan kuadrat")

elif choice == "2":
    jarijari = float(input("Jari-Jari Lingkaran: "))
    luas = (22/7) * (jarijari**2)
    print ("luas Lingkaran adalah", luas, "satuan kuadrat")

elif choice == "3":
    sisi = float(input("Sisi Kubus: "))
    luas = 6 * (sisi**2)
    print ("Luas Kubus adalah: ", luas, "satuan kuadrat")

elif choice == "4":
    suhu = float(input("Suhu dalam Celcius: "))
    fahrenheit = ((9/5) * suhu) + 32
    print ("Suhu dalam Fahrenheit adalah", fahrenheit)

elif choice == "5":
    suhu = float(input("Suhu dalam Reamur: "))
    kelvin = ((5/4) * suhu) + 273
    print ("Suhu dalam kelvin adalah", kelvin)

else:
    print ("=x=Input tidak ditemukan=x=")
