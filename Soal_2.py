import pandas as pd

# Membuat DataFrame dari array 2 dimensi
data = {
    'Nama': ['Mahasiswa 1', 'Mahasiswa 2', 'Mahasiswa 3'],
    'Algoritma dan Struktur Data 2': [90, 50, 65],
    'Matematika Numerik': [80, 60, 70]
}

df = pd.DataFrame(data)

# Tampilkan DataFrame
print("Data Nilai Mahasiswa:")
print(df)

# Menghitung rata-rata nilai untuk setiap mata kuliah
average_per_subject = df.mean(numeric_only=True)
print("\nRata-rata nilai untuk setiap mata kuliah:")
print(average_per_subject)

# Menghitung rata-rata nilai untuk setiap mahasiswa
df['Rata-rata'] = df.mean(axis=1, numeric_only=True)
average_per_student = df[['Nama', 'Rata-rata']]
print("\nRata-rata nilai untuk setiap mahasiswa:")
print(average_per_student)