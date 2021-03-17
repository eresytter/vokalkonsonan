word = input('Masukkan teks: ') # Program tanya input dari user
vowels = 'aeiou'

### Menyetel semua variabel integer (bilangan bulat) jadi 0 ###
### Ini akan membantu ketika menghitung huruf ke huruf dalam satu input ###
consonant = 0
vowel_counter = 0
vowelcount = 0
consonant_counter = 0

### Operasi untuk menghitung jumlah huruf vokal mulai ###
while vowel_counter < len(word): # Program cek apakah vowel_counter lebih kecil
#dari jumlah huruf di input
  if word[vowel_counter] in vowels: # Program cek apakah huruf di input merupakan
#huruf vokal atau bukan
      vowelcount += 1 # Jika ya, jumlah huruf vokal bertambah 1
  vowel_counter += 1 # Program lanjut ke huruf selanjutnya
print('Ada',vowelcount,'huruf vokal di kata ini.')

### Operasi untuk menghitung jumlah huruf konsonan mulai ###
while consonant_counter < len (word): # Program cek apakah consonant_counter
#lebih kecil dari jumlah huruf di input
  if word[consonant_counter] not in vowels: # Program cek apakah huruf di input
#adalah huruf vokal atau bukan
    consonant += 1 # Jika bukan, jumlah huruf konsonan bertambah 1
  consonant_counter += 1 # Program lanjut ke huruf selanjutnya
print('Ada',consonant,'huruf konsonan di kata ini.')
