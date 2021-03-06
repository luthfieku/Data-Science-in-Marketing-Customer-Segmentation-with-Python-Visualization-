# Data Science in Marketing Costumer Segmentation with Phyton

# Mempersiapkan Library
import pandas as pd  
import matplotlib.pyplot as plt  
import seaborn as sns  
from sklearn.preprocessing import LabelEncoder  
  
from kmodes.kmodes import KModes  
from kmodes.kprototypes import KPrototypes  
  
import pickle  
from pathlib import Path  
  
#Membaca Data Pelanggan
import pandas as pd

# import dataset  
df = pd.read_csv("customer_segments.csv", sep="\t")  
  
# menampilkan data  
print(df.head())

#Selanjutnya perlu melihat informasi dari data yang ada. Sehingga dengan bisa mengetahui jumlah baris dan kolom, nama kolom, identifikasi null values,  dan juga mengetahui tipe data dengan mudah.

#Melihat Informasi dari Data
# Menampilkan informasi data  
df.info()

# Setelah melakukan pemanggilan data dan melihat informasi data yang dimiliki, akhirnya mengetahui bahwa:

# Data yang akan digunakan terdiri dari 50 baris dan 7 kolom
# Tidak ada nilai null pada data
# Dua kolom memiliki tipe data numeric dan lima data bertipe string

# Melakukan Eksplorasi Data
# Selanjutnya perlu dilakukan eksplorasi data untuk lebih mengenal dataset yang akan digunakan. Tahap ini akan melakukan eksplorasi untuk data numerik dan juga data kategorikal.

# Melakukan Eksplorasi Data

import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='white')
import pandas as pd
df = pd.read_csv("https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/customer_segments.txt", sep="\t")
plt.clf()
  
# Fungsi untuk membuat plot  
def observasi_num(features):  
    fig, axs = plt.subplots(2, 2, figsize=(10, 9))
    for i, kol in enumerate(features):
        sns.boxplot(df[kol], ax = axs[i][0])
        sns.distplot(df[kol], ax = axs[i][1])   
        axs[i][0].set_title('mean = %.2f\n median = %.2f\n std = %.2f'%(df[kol].mean(), df[kol].median(), df[kol].std()))
    plt.setp(axs)
    plt.tight_layout()
    plt.show()  

#Memanggil fungsi untuk membuat Plot untuk data numerik  
kolom_numerik = ['Umur','NilaiBelanjaSetahun'] 
observasi_num(kolom_numerik) 

# Eksplorasi Data Kategorikal
# Selain data numerikal, kita juga perlu melihat bagaimana persebaran data pada kolom-kolom yang memiliki jenis kategorikal yaitu Jenis Kelamin, Profesi dan Tipe Residen. Kita dapat melakukan hal ini dengan menggunakan countplot dari library seaborn.
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='white')
import pandas as pd
df = pd.read_csv("https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/customer_segments.txt", sep="\t")
plt.clf()
  
# Menyiapkan kolom kategorikal  
kolom_kategorikal = ['Jenis Kelamin','Profesi','Tipe Residen']  

# Membuat canvas
fig, axs = plt.subplots(3,1,figsize=(7,10)) 

# Membuat plot untuk setiap kolom kategorikal  
for i, kol in enumerate(kolom_kategorikal):  
    # Membuat Plot
    sns.countplot(df[kol], order = df[kol].value_counts().index, ax = axs[i])  
    axs[i].set_title('\nCount Plot %s\n'%(kol), fontsize=15)  
      
    # Memberikan anotasi  
    for p in axs[i].patches:  
        axs[i].annotate(format(p.get_height(), '.0f'),  
                        (p.get_x() + p.get_width() / 2., p.get_height()),  
                        ha = 'center',  
                        va = 'center',  
                        xytext = (0, 10),  
                        textcoords = 'offset points') 
          
    # Setting Plot  
    sns.despine(right=True,top = True, left = True)  
    axs[i].axes.yaxis.set_visible(False) 
    plt.setp(axs[i])
    plt.tight_layout()

# Tampilkan plot
plt.show()

# Kesimpulan
# Dari hasil eksplorasi data tersebut kita dapat mendapatkan informasi:

# Rata-rata dari umur pelanggan adalah 37.5 tahun
# Rata-rata dari nilai belanja setahun pelanggan adalah 7,069,874.82
# Jenis kelamin pelanggan di dominasi oleh wanita sebanyak 41 orang (82%) dan laki-laki sebanyak 9 orang (18%)
# Profesi terbanyak adalah Wiraswasta (40%) diikuti dengan Professional (36%) dan lainnya sebanyak (24%)
# Dari seluruh pelanggan 64% dari mereka tinggal di Cluster dan 36% nya tinggal di Sektor
