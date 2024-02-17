import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from pathlib import Path
from statsmodels.graphics.gofplots import qqplot

colors = ['#4285F4', '#34A853', '#FBBC05', '#EA4335']
# Set Seaborn style and color palette
sns.set_style("darkgrid")
sns.set_palette("pastel")
sns.set(style='whitegrid', palette=sns.color_palette(colors))


# Load data
df = pd.read_csv(str(Path(__file__).resolve().parent)+"/hour.csv") # Assuming "hour.csv" is in the same directory as the script
df = df.rename(columns={'weathersit':'weather',
                       'yr':'year',
                       'mnth':'month',
                       'hr':'hour',
                       'hum':'humidity',
                       'cnt':'count'})
df = df.drop(columns = ['instant' , 'dteday' , 'year']) # Drop unnecessary columns
cols = ['season' , 'month' , 'hour' , 'holiday' , 'weekday' , 'workingday' , 'weather']
for col in cols:
    df[col] = df[col].astype('category')

st.title("Prediksi Jumlah Kebutuhan Peminjaman Sepeda Menggunakan Methode Regresi")

st.markdown("### 1. Pengaruh Hari Kerja dan Hari Libur Penggunaaan Sepeda")
# Melihat pengaruh penggunaaan sepeda selama hari kerja dan hari libur
fig, ax = plt.subplots(figsize=(20,5))
sns.pointplot(data=df, x='hour', y='count', hue='weekday', ax=ax, alpha=0.5)
ax.patch.set_alpha(0)
ax.set(title='Jumlah sepeda selama weekdays dan weekends')
# Set transparent background
fig.patch.set_alpha(0.0)
st.pyplot(fig)
st.markdown(f"<p style='font-size:12px; font-color:#868686;'>Dari grafik ini kita dapat lihat jika penggunaan sepeda dominan ada dihari kerja, tepatnya pada jam berangkat kerja dan pulang kerja. Informasi ini dapat digunakan untuk memprediksi kenaikan kebutuhan peminjaman sepeda pada jam berangkat kerja dan pulang kerja.</p>", unsafe_allow_html = True)

st.markdown("### 2. Pengaruh Hari Kerja dan Hari Libur Pada Penggunaaan Sepeda Terdaftar")
# Melihat pengaruh penggunaaan sepeda selama hari kerja dan hari libur pada pengguna yang tidak terdaftar
fig, ax = plt.subplots(figsize=(20,5))
sns.pointplot(data=df, x='hour', y='casual', hue='weekday', ax=ax, alpha=0.5)
ax.patch.set_alpha(0)
ax.set(title='Jumlah sepeda selama weekdays dan weekends pada pengguna yang tidak terdaftar')
# Set transparent background
fig.patch.set_alpha(0.0)
st.pyplot(fig)
st.markdown(f"<p style='font-size:12px; font-color:#868686;'>Dari grafik ini kita dapat lihat jika penggunaan sepeda yang tidak terdaftar dominan ada dihari libur. Informasi ini dapat digunakan untuk memprediksi kenaikan kebutuhan peminjaman pengguna yang tidak terdaftar pada hari libur dan penurunan kebutuhan peminjaman sepeda pada pengguna yang tidak terdaftar.</p>", unsafe_allow_html = True)

st.markdown("### 3. Pengaruh Hari Kerja dan Hari Libur Pada Penggunaaan Sepeda Tidak Terdaftar")
# Melihat pengaruh penggunaaan sepeda selama hari kerja dan hari libur pada pengguna yang terdaftar
fig, ax = plt.subplots(figsize=(20,5))
sns.pointplot(data=df, x='hour', y='registered', hue='weekday', ax=ax, alpha=0.5)
ax.patch.set_alpha(0)
ax.set(title='Jumlah sepeda selama weekdays dan weekends pada pengguna yang tidak terdaftar')
# Set transparent background
fig.patch.set_alpha(0.0)
st.pyplot(fig)
st.markdown(f"<p style='font-size:12px; font-color:#868686;'>Dari grafik ini kita dapat lihat jika penggunaan sepeda yang terdaftar dominan ada dihari kerja. Informasi ini dapat digunakan untuk memprediksi kenaikan dan penurunan kebutuhan peminjaman sepeda pada pengguna yang terdaftar.</p>", unsafe_allow_html = True)

st.markdown("### 4. Pengaruh Setiap Kondisi Cuaca Pada Penggunaaan Sepeda")
# Melihat pengaruh penggunaaan sepeda pada setiap cuaca
fig, ax = plt.subplots(figsize=(20,5))
sns.pointplot(data=df, x='hour', y='count', hue='weather', ax=ax, alpha=0.5)
ax.patch.set_alpha(0)
ax.set(title='Jumlah sepeda pada setiap cuaca')
# Set transparent background
fig.patch.set_alpha(0.0)
st.pyplot(fig)
st.markdown(f"<p style='font-size:12px; font-color:#868686;'>Dari grafik ini kita dapat lihat jika tren penggunaan sepeda menurun cukup banyak pada musim dingin. Informasi ini dapat digunakan untuk memprediksi penurunan tren peminjaman sepeda pada musim dingin.</p>", unsafe_allow_html = True)

st.markdown("### 5. Tren Penggunaaan Sepeda Setiap Bulan")
# Melihat pengaruh penggunaaan sepeda pada setiap bulan
fig, ax = plt.subplots(figsize=(20,5))
sns.barplot(data=df, x='month', y='count', ax=ax ,alpha=0.5)
ax.patch.set_alpha(0)
ax.set(title='Jumlah sepeda pada setiap bulan')
# Set transparent background
fig.patch.set_alpha(0.0)
st.pyplot(fig)
st.markdown(f"<p style='font-size:12px; font-color:#868686;'>Dari grafik ini kita dapat lihat jika tren penggunaan sepeda menurun pada awal dan akhir tahun. Informasi ini dapat digunakan untuk memprediksi penurunan tren peminjaman sepeda pada awal dan akhir tahun.</p>", unsafe_allow_html = True)

st.markdown("### 6. Tren Penggunaaan Sepeda Setiap Hari")
# Melihat pengaruh penggunaaan sepeda pada setiap hari
fig, ax = plt.subplots(figsize=(20,5))
sns.barplot(data=df, x='weekday', y='count', ax=ax, alpha=0.5)
ax.patch.set_alpha(0)
ax.set(title='Jumlah sepeda pada setiap hari')
# Set transparent background
fig.patch.set_alpha(0.0)
st.pyplot(fig)
st.markdown(f"<p style='font-size:12px; font-color:#868686;'>Dari grafik ini kita dapat lihat tidak ada perbedaan signifikan pada tren penggunaan sepeda pada tiap hari</p>", unsafe_allow_html = True)

st.markdown("### 7. Relasi Antara Temperatur dan Kelembapan Pada Jumlah Peminjaman Sepeda")
# Melihat relasi antara temperatur dan kelembapan pada jumlah peminjaman sepeda
fig, (ax1,ax2) = plt.subplots(ncols=2, figsize=(20,5))
sns.regplot(x=df['temp'], y=df['count'], ax=ax1 ,color='red')
ax.patch.set_alpha(0)
ax1.set(title="Relasi antara temperatur dan pengguna")
sns.regplot(x=df['humidity'], y=df['count'], ax=ax2)
ax2.set(title="Relasi antara kelembapan dan pengguna")
# Set transparent background
fig.patch.set_alpha(0.0)
st.pyplot(fig)
st.markdown(f"<p style='font-size:12px; font-color:#868686;'>Grafik ini menunjukan tidak ada relasi yang sangat kuat pada temperatur dan kelembapan pada jumlah peminjaman sepeda, terbukti titik sangat jauh dari garis linear regresi.</p>", unsafe_allow_html = True)

st.markdown("### Distribusi Peminjaman Sepeda")
# Melihat distribusi user
fig, (ax1,ax2) = plt.subplots(ncols=2, figsize=(20,5))
sns.histplot(df['count'], ax=ax1 , color ='red', kde=True , alpha=0.5)
ax.patch.set_alpha(0)
ax1.set(title='Distribusi user')
qqplot(df['count'], ax=ax2, line='s')
ax2.set(title='Kuantil teoritis')
# Set transparent background
fig.patch.set_alpha(0.0)
st.pyplot(fig)
st.markdown(f"<p style='font-size:12px; font-color:#868686;'>Grafik ini menunjukan distribusi user dan kuantil teoritis. Terlihat jika data cukup linear dengan garis linear, menujukan pegaruh yang cukup kuat antar variable pada jumlah peminjaman sepeda.</p>", unsafe_allow_html = True)

st.markdown("### Pelatihan Model")

st.markdown("Pelatihan model menggunakan algoritma Random Forest Regressor. Kami menggunakan algoritma ini dikarenakan diantara algoritma yang lain Random Forest Regressor memiliki nilai Cross Validation yang paling kecil.")
st.markdown('''~~~
Model: LinearRegression()
CV score: 0.6313038164418382
Model: Ridge()
CV score: 0.6304079414191406
Model: HuberRegressor()
CV score: 0.6603301753477131
Model: ElasticNetCV()
CV score: 0.6252222784219456
Model: DecisionTreeRegressor()
CV score: 0.6046202335241623
Model: RandomForestRegressor()
CV score: 0.39121729269057365
Model: ExtraTreesRegressor()
CV score: 0.40459031301949205
Model: GradientBoostingRegressor()
CV score: 0.4714340374748951
~~~''')
st.markdown("Selanjutnya untuk data train dan data test kami bagi menjadi 75 persen data train dan 25 persen data test.")
st.markdown('''~~~
# Memecah data untuk data train dan data test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
~~~''')
st.markdown("Selanjutnya melatih model dengan data, dan melakukan prediksi.")
st.markdown('''~~~
# Memilih model pelatihan RandomForestRegressor() dikarena hasil regresi yang didapatkan kecil
model = RandomForestRegressor()
model.fit(X_train, y_train)
            
# Membuat prediksi dari model
y_pred = model.predict(X_test)
            
# Melihat error yang dihasilkan prediksi
error = y_test - y_pred
            
# Menampilkan Hasil error regresi
fig, ax = plt.subplots()
ax.scatter(y_test, error ,color = 'red')
ax.axhline(lw=3, color='black')
ax.set_xlabel('Observed')
ax.set_ylabel('Error')
plt.show()
~~~''')

st.markdown("### Hasil Prediksi Menggunakan Algoritma Random Forest Regressor")
# Define the image path
st.image(str(Path(__file__).resolve().parent)+"/regresion-result.png")
st.markdown(f"<p style='font-size:12px; font-color:#868686;'>Grafik ini adalah hasil regresi dari prediksi model latih menggunakan algoritma Random Forest Regressor. Jika dilihat dari data titik terhadap garis regresi cukup berdekatan yang mengindikasi jika prediksi model cukup akurat.</p>", unsafe_allow_html = True)
