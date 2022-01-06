#Library
import datetime as dt
import calendar as kalender

#DateTime
hari_ini = dt.date.today()
print("\n")
print("Hari ini: ", hari_ini, "\n")
print("="*20)
print(f"hari ini adalah {hari_ini:%A}\n")

#Kalender
year = 2021
month = 1
print(kalender.month(year, month))

#Tanggal Lahir
tanggal = int(input("Tanggal: "))
bulan = int(input("Bulan: ")) # Masukkan bulan menggunakan tipe data INT misalnya januari berarti bulan 01
tahun = int(input("Tahun: "))

print("="*20)

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f"Tanggal lahir Anda: {tanggal_lahir}")
print(f"Anda lahir pada hari: {tanggal_lahir:%A}")

umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
print(f"Umur anda adalah: {umur_tahun} tahun")