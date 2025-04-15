def tentukan_kelulusan(score):
    if score >= 90 and score <= 100:
        nilai_huruf = "A"
        predikat = "Dengan Pujian"
    elif score >= 80 and score <= 89:
        nilai_huruf = "B"
        predikat = "Sangat Memuaskan"
    elif score >= 70 and score <= 79:
        nilai_huruf = "C"
        predikat = "Memuaskan"
    elif score >= 60 and score <= 69:
        nilai_huruf = "D"
        predikat = "Tidak Memuaskan"
    elif score >= 0 and score <= 59:
        nilai_huruf = "E"
        predikat = "Tidak LULUS"
    else:
        return "Input skor tidak valid. Skor harus antara 0 hingga 100."

    return f"Nilai Huruf: {nilai_huruf}\nPredikat: {predikat}"

# Input dari user
try:
    skor_input = int(input("Masukkan skor Anda (0-100): "))
    hasil = tentukan_kelulusan(skor_input)
    print(hasil)
except ValueError:
    print("Input tidak valid. Masukkan angka bulat antara 0 hingga 100.")

