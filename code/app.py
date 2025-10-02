import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Geospatial Analysis of Hospitals in Peru", layout="wide")


# Importacion de hospitales operativos por departamento (para el bar chart)

hosp_dist = pd.read_csv('../output/operationao_hospitals_by_department.csv')

# Importacion de foloum cloropeth 

 



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
    
    st.subheader('Análisis por Distrito')

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


    st.subheader('Análisis por Departamento')

    with st.container():
        # columnas
        f,g,h = st.columns(3, border= True)
        
        with f:
            st.subheader('Tabla Resumen')
            st.dataframe(hosp_dist)
            
        with g:
            st.subheader('Cantidad de Hospitales publicos operativos por Departamento')
            st.bar_chart(hosp_dist, x= 'DEPARTAMENTO', y = 'TOTAL_HOSPITALES', horizontal= True, sort= '-TOTAL_HOSPITALES')

        with h:
            st.subheader('Mapa de coropletas')
            st.image('../output/map_department_level_choropleth_map.png')
    
    st.subheader('Análisis de Proximidad')

    with st.container():
        #columnas
        (i,) = st.columns(1, border= True)

        with i:

            with st.container():

                st.subheader('Lima')
                with open("../output/lima_proximity.html", 'r', encoding='utf-8') as f:
                    fol_1 = f.read()

                st.components.v1.html(fol_1, height = 800)


                st.subheader('Loreto')
                with open("../output/loreto_proximity.html", 'r', encoding='utf-8') as f:
                    fol_2 = f.read()

                st.components.v1.html(fol_2, height = 800)

with tab3:

    j, k, l = st.columns(3, border= True)

    with j:
        st.subheader('Mapa de coropletas Nacional (A nivel de Distrito)')

        with open("../output/folium_choropleth_distritos.html", 'r', encoding='utf-8') as f:
                    fol_3 = f.read()

        st.components.v1.html(fol_3, height = 800)

    with k:
        st.subheader('Lima')

        with open("../output/folium_proximidad_Lima.html", 'r', encoding='utf-8') as f:
                    fol_4 = f.read()

        st.components.v1.html(fol_4, height = 800)

    with l:
         st.subheader('Loreto')

         with open("../output/folium_proximidad_Loreto.html", 'r', encoding='utf-8') as f:
                    fol_5 = f.read()

         st.components.v1.html(fol_5, height = 800)
    
    (m, ) = st.columns(1, border= True)

    with m:
        st.markdown("""
#### Lima

* El mapa muestra una **fuerte concentración en el área urbana**: en el *Barrio Obrero Industrial* (cerca de Lima Metropolitana) hay **243 hospitales en un radio de 10 km**.
* En contraste, en *Yanapampa* no hay hospitales dentro del mismo radio, lo que refleja el aislamiento de estas comunidades rurales en términos de servicios de salud.
* Esto confirma que la capital acumula la mayor parte de la infraestructura hospitalaria en unas pocas áreas, mejorando el acceso en el centro pero dejando desatendidas las áreas periféricas.


#### Loreto

* En Loreto la situación es diferente: en la *localidad Tres de Octubre* (Iquitos) hay **28 hospitales en un radio de 10 km**, lo que muestra cómo la infraestructura se acumula en la ciudad principal.
* Sin embargo, localidades como *Pueblo Nuevo* no tienen **ningún hospital cercano** dentro del mismo radio, evidenciando el **aislamiento geográfico típico de la Amazonía**.
* El patrón revela que la red hospitalaria en Loreto depende de unos pocos centros urbanos, mientras que **la dispersión poblacional y las barreras naturales (ríos, selva)** dificultan seriamente el acceso a los servicios de salud.

""")
    