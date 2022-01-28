#setup noteboob
import pandas as pd
pd.plotting.register_matplotlib_converters()#menghapus formater dan converter dari pandas sehingga bisa di plot dengan baik dengan matplotlip
import matplotlib.pyplot as plt
import seaborn as sns
print("Setup complate")

#load the data
file_path="Visualisasi_data/fifa.csv"
data=pd.read_csv(file_path,index_col='Date',parse_dates=True)
#=>parse_dates->digunakan untuk mengenali label baris sebagai dates
#->index_col => column yang digunakan sebagai row
#->file_path=>alamat dari file csv sebagai data mentah
print(data.head())

#float the data

#->set weight and height of the figure
plt.figure(figsize=(16,6))
#set up jenis visualisasinya->line chart yang akan menggambarkan sebuah rangking fifa dunia
sns.lineplot(data=data)
plt.show()