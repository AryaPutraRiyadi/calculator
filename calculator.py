def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y == 0:
        return "Error: Pembagian dengan nol"
    return x / y

while True:
    print("\nPilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")

    pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

    if pilihan == '5':
        print("Terima kasih telah menggunakan kalkulator ini.")
        break

    if pilihan in ('1', '2', '3', '4'):
        num1 = float(input("Masukkan angka pertama: "))
        num2 = float(input("Masukkan angka kedua: "))

        if pilihan == '1':
            print("Hasil:", tambah(num1, num2))
        elif pilihan == '2':
            print("Hasil:", kurang(num1, num2))
        elif pilihan == '3':
            print("Hasil:", kali(num1, num2))
        elif pilihan == '4':
            print("Hasil:", bagi(num1, num2))
    else:
        print("Input tidak valid")