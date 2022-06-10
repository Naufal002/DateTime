#Library
import datetime as dt
import calendar as kalender

#DateTime
hari_ini = dt.date.today()
print("\n")
print(hari_ini, "\n")
print("="*22)
print(f"hari ini adalah: {hari_ini:%A}\n")

#Kalender
year = 2021
month = 1
print(kalender.month(year, month))

#Tanggal Lahir
print("="*22)
tanggal = int(input("Tanggal: "))
bulan = int(input("Bulan: ")) # Masukkan bulan menggunakan tipe data INT misalnya januari berarti bulan 01
tahun = int(input("Tahun: "))

print("="*22)

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f"Tanggal lahir Anda: {tanggal_lahir}")
print(f"Anda lahir pada hari: {tanggal_lahir:%A}")

umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
print(f"Umur anda adalah: {umur_tahun} tahun")
print("="*22)

Copyright = "="*3, " © Naufal Rizqi Ilham Gibran ", "="*3
print(Copyright)
print("\n")
