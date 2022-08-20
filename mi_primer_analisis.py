import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import streamlit_theme as stt
import matplotlib.pyplot as plt

stt.set_theme({'primary': '#1b3388'})

c =st.container()
c.title('SEGUNDO ENTREGABLE BOOTCAM_MOJIX_V2')

c.write('Este es el primer caso de uso en el analisis que se realizo en clases')
c.write('del bootcamp de Mojix V2 :')
c.write('Se procedio a la lectura de los 2 dataset que contenian los valores a comparar')
c.write('En este caso se comparo un inventario hecho dentro de una empresa sobre el contenido')
c.write('de un determinado producto y el inventario generado con tecnologia Mojix')
c.write('Los cuales son los siguientes:')

df_expected = pd.read_csv("https://storage.googleapis.com/mojix-devops-wildfire-bucket/analytics/bootcamp_2_0/Bootcamp_DataAnalysis_Expected.csv", encoding="latin-1", dtype=str)
df_counted = pd.read_csv("https://storage.googleapis.com/mojix-devops-wildfire-bucket/analytics/bootcamp_2_0/Bootcamp_DataAnalysis_Counted.csv", encoding="latin-1", dtype=str)
st.dataframe(df_expected)
st.dataframe(df_counted)
	
st.markdown("---")
df_expected['Retail_Product_SKU'].nunique()
df_counted['RFID'].nunique()
df_counted = df_counted.drop_duplicates('RFID')
df_B = df_counted.groupby('Retail_Product_SKU').count()[['RFID']].reset_index()
df_B = df_counted.groupby('Retail_Product_SKU').count()[['RFID']].reset_index().rename(columns={'RFID':'Retail_CCQTY'})
my_cols_selected=['Retail_Product_Color',
'Retail_Product_Level1',
'Retail_Product_Level1Name',
'Retail_Product_Level2Name',
'Retail_Product_Level3Name',
'Retail_Product_Level4Name',
'Retail_Product_Name',
'Retail_Product_SKU',
'Retail_Product_Size',
'Retail_Product_Style',
'Retail_SOHQTY']
df_A = df_expected[my_cols_selected]
df_discrepancy = pd.merge(df_A, df_B, how='outer',left_on='Retail_Product_SKU', right_on='Retail_Product_SKU',indicator= True)
df_discrepancy['Retail_CCQTY']=df_discrepancy['Retail_CCQTY'].fillna(0)
df_discrepancy['Retail_CCQTY']=df_discrepancy['Retail_CCQTY'].astype(int)
df_discrepancy['Retail_SOHQTY']=df_discrepancy['Retail_SOHQTY'].fillna(0).astype(int)
df_discrepancy['Diff']=df_discrepancy['Retail_CCQTY']-df_discrepancy['Retail_SOHQTY']


p =st.container()
p.write('Posteriormente de realizados los analisis respectivos')
p.write('se obtuvieron los siguientes resultados :')
st.markdown("---")
st.write(" Tablas del diferencial entre el inventario del cliente y el de Mojix")

df_discrepancy=df_discrepancy.head()
if st.button('1. Resultado Final', key='1'):
    st.write(df_discrepancy)
    

st.markdown("---")

df_discrepancy.loc[df_discrepancy['Diff']<0, 'Unders']=df_discrepancy['Diff']*(-1)

df_discrepancy['Unders']=df_discrepancy['Unders'].fillna(0).astype(int)

df_discrepancy=df_discrepancy.head()


st.markdown("---")
if st.button('2. Resultado de comparacion de faltantes', key='2'):
    st.write(df_discrepancy)
    df_discrepancy=pd.DataFrame(
                   np.random.randn(10, 2),
                   columns=['Retail_Product_Level1Name','Unders'])
                    
    st.markdown("---")
    st.write('Grafico de barras de la comparacion')
    st.bar_chart(df_discrepancy)
  
  
st.markdown("---")  
if st.button('Ver la agregacion Retail Product Level2Name'):

   st.write(df_discrepancy.groupby('Retail_Product_Level2Name').sum()) #displayed when the button is clicked



