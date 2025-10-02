import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Geospatial Analysis of Hospitals in Peru", layout="wide")


# Importacion de hospitales operativos por departamento (para el bar chart)

hosp_dist = pd.read_csv('../output/operationao_hospitals_by_department.csv')



## Tabs 

tab1, tab2, tab3 = st.tabs([' 🗂️ Data Descripion', ' 🗺️ Static Maps & Departments Analysis', ' 🌍 Dynamic Maps'])



## Contenido de tab1

with tab1:
    st.title('Descripción de los Datos')

    st.subheader("📌 Unidad de Análisis")

    st.write("**Hospitales públicos operativos en el Perú**.")

    ## columnas de tab1
    a,b = st.columns(2)

    a.metric(label="Total de hospitales", value="1,873", border= True)
    b.metric(label = '**Total de hospitales públicos operativos en el Perú**', value= '1,812', border= True)
    
    

    st.subheader("📊 Fuentes de Datos")
    st.markdown("""
    - **MINSA – Registro Nacional de IPRESS** (subset de hospitales operativos).  
    - **INEI/IGN – Centros Poblados** para análisis espacial.  
    """)

    st.subheader("⚙️ Reglas de Filtrado")
    st.markdown("""
    - Se incluyen únicamente hospitales **públicos y operativos**.  
    - Se excluyen los registros de tipo **privado u “otros”**.  
    - Se consideran solo los hospitales con **coordenadas válidas (latitud/longitud)**.  
    """)




# contenido de tab2
with tab2:
    
    # columnas 

    c, d, e = st.columns(3, border= True)

    with c:    
        st.subheader(" 🏥 Total de Hospitales Públicos por Distrito")

        st.image('../output/map_1.png', width= 500)

    with d: 
        st.subheader(' 🏥 Distritos sin hospitales')

        st.image('../output/map_2.png', width= 500)

    with e:
        st.subheader(' 🏥 Top 10 distritos con mayor número de hospitales')
        
        st.image('../output/map_3.png', width= 500)


    


    
    st.bar_chart(hosp_dist, x= 'DEPARTAMENTO', y = 'TOTAL_HOSPITALES', horizontal= True, sort= '-TOTAL_HOSPITALES')

