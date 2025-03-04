def hitung_biaya_pengiriman(berat, jarak, jenis_pengiriman, is_member):
    # Biaya dasar pengiriman
    biaya_dasar = 10000  # Misalnya Rp 10.000 sebagai biaya dasar

    # Konversi berat dan jarak ke satuan yang sesuai
    berat_paket_gram = berat * 1000  # Konversi kg ke gram
    jarak_pengiriman_meter = jarak * 1000  # Konversi km ke meter

    # Inisialisasi total pembayaran dengan biaya dasar
    total_pembayaran = biaya_dasar

    # Tambahan biaya jika berat melebihi 5000 gram (5 kg)
    if berat_paket_gram > 5000:
        total_pembayaran += 5000

    # Tambahan biaya jika jarak melebihi 10 km (10.000 meter)
    if jarak_pengiriman_meter > 10000:
        total_pembayaran += 8000

    # Tambahan biaya untuk pengiriman express
    if jenis_pengiriman.lower() == 'express':
        total_pembayaran += 20000

    # Diskon untuk member (10% dari total)
    if is_member:
        total_pembayaran -= total_pembayaran * 10 / 100  # Diskon 10%

    return int(total_pembayaran)  # Mengembalikan nilai sebagai integer
# =====================================================
# Program Utama (Meminta Input dari Pengguna)
# =====================================================
if __name__ == "__main__":
    print("=== Program Perhitungan Biaya Pengiriman ===")

    # 1. Memasukkan berat paket
    while True:
        try:
            berat_paket = float(input("Masukkan berat paket (kg): "))
            if berat_paket < 0:
                print("Berat paket tidak bisa negatif. Silakan masukkan kembali.")
                continue
            break
        except ValueError:
            print("Input tidak valid! Masukkan angka.")

    # 2. Memasukkan jarak pengiriman
    while True:
        try:
            jarak_pengiriman = float(input("Masukkan jarak pengiriman (km): "))
            if jarak_pengiriman < 0:
                print("Jarak tidak bisa negatif. Silakan masukkan kembali.")
                continue
            break
        except ValueError:
            print("Input tidak valid! Masukkan angka.")

    # 3. Memasukkan jenis pengiriman (biasa/express)
    while True:
        jenis_pengiriman = input("Masukkan jenis pengiriman (biasa/express): ").strip().lower()
        if jenis_pengiriman not in ["biasa", "express"]:
            print("Jenis pengiriman hanya bisa 'biasa' atau 'express'. Silakan masukkan kembali.")
        else:
            break

    # 4. Memasukkan status keanggotaan pelanggan (member atau bukan)
    while True:
        is_member_input = input("Apakah pelanggan member? (ya/tidak): ").strip().lower()
        if is_member_input in ["ya", "tidak"]:
            is_member = is_member_input == "ya"
            break
        else:
            print("Harap masukkan 'ya' atau 'tidak'.")

    # 5. Menghitung biaya pengiriman
    biaya = hitung_biaya_pengiriman(berat_paket, jarak_pengiriman, jenis_pengiriman, is_member)

    # 6. Menampilkan hasil
    print("\n=== Rincian Biaya Pengiriman ===")
    print(f"Berat paket         : {berat_paket} kg")
    print(f"Jarak pengiriman    : {jarak_pengiriman} km")
    print(f"Jenis pengiriman    : {jenis_pengiriman.capitalize()}")
    print(f"Status Member       : {'Ya' if is_member else 'Tidak'}")
    print(f"Total Biaya Pengiriman: Rp {biaya:,.0f}")

    print("="*64)
    print("NAMA : Alya Febrianti".center(64))
    print(f'NIM : {312410692}'.center(64))
    print("="*64)