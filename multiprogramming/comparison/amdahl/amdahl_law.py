S = float(input("Seri kısım oranını giriniz (0-1): "))
N = int(input("Çekirdek sayısını giriniz: "))

sonuc = 1 / (S + (1 - S) / N)

print("Amdahl Yasasına göre hızlanma:", round(sonuc, 2))
