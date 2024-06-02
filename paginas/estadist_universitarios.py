import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from mpl_toolkits.axes_grid1 import make_axes_locatable
import geopandas as gpd


@st.cache_data
def cargarDatosUniversitarios():
    df_tasasUniversitarios = pd.read_csv('./datasets/Tasa_ActividadEmpleoParo_UniversitariosEspanya.csv', sep='\t')
    df_tasasUniversitarios = df_tasasUniversitarios[df_tasasUniversitarios['CCAA de su universidad'] != 'Universidades de ámbito nacional']

    df_tasasUniversitarios_estudios = df_tasasUniversitarios[(df_tasasUniversitarios['Ámbito de estudio'] == '01 - EDUCACIÓN') |
                                                         (df_tasasUniversitarios['Ámbito de estudio'] == '02 - ARTES Y HUMANIDADES') |
                                                         (df_tasasUniversitarios['Ámbito de estudio'] == '03 - CIENCIAS SOCIALES, PERIODISMO Y DOCUMENTACIÓN') |
                                                         (df_tasasUniversitarios['Ámbito de estudio'] == '04 - NEGOCIOS, ADMINISTRACIÓN Y DERECHO') |
                                                         (df_tasasUniversitarios['Ámbito de estudio'] == '05 - CIENCIAS') |
                                                         (df_tasasUniversitarios['Ámbito de estudio'] == '06 - INFORMÁTICA') |
                                                         (df_tasasUniversitarios['Ámbito de estudio'] == '07 - INGENIERÍA, INDUSTRIA Y CONSTRUCCIÓN') |
                                                         (df_tasasUniversitarios['Ámbito de estudio'] == '08 - AGRICULTURA, GANADERÍA, SILVICULTURA, PESCA Y VETERINARIA') |
                                                         (df_tasasUniversitarios['Ámbito de estudio'] == '09 - SALUD Y SERVICIOS SOCIALES') |
                                                         (df_tasasUniversitarios['Ámbito de estudio'] == '10 - SERVICIOS')]
    mapping_estudios = {
        '01 - EDUCACIÓN': 'Educación',
        '02 - ARTES Y HUMANIDADES': 'Artes y Humanidades',
        '03 - CIENCIAS SOCIALES, PERIODISMO Y DOCUMENTACIÓN': 'Ciencias Sociales, Periodismo y Documentación',
        '04 - NEGOCIOS, ADMINISTRACIÓN Y DERECHO': 'Negocios, Administración y Derecho',
        '05 - CIENCIAS': 'Ciencias',
        '06 - INFORMÁTICA': 'Informática',
        '07 - INGENIERÍA, INDUSTRIA Y CONSTRUCCIÓN': 'Ingeniería, Industria y Construcción',
        '08 - AGRICULTURA, GANADERÍA, SILVICULTURA, PESCA Y VETERINARIA': 'Agricultura, Ganadería, Silvicultura, Pesca y Veterinaria',
        '09 - SALUD Y SERVICIOS SOCIALES': 'Salud y Servicios Sociales',
        '10 - SERVICIOS': 'Servicios'
    }

    df_tasasUniversitarios_estudios['Ámbito de estudio'] = df_tasasUniversitarios_estudios['Ámbito de estudio'].replace(mapping_estudios)

    df_tasasUniversitarios_estudios.rename(columns={'CCAA de su universidad': 'CCAA'}, inplace=True)

    mapping_CCAAS = {
        'Andalucía': 'Andalucía',
        'Aragón': 'Aragón',
        'Asturias, Principado de': 'Principado de Asturias',
        'Balears, Illes': 'Illes Balears',
        'Canarias': 'Canarias',
        'Cantabria': 'Cantabria',
        'Castilla y León': 'Castilla y León',
        'Castilla - La Mancha': 'Castilla-La Mancha',
        'Cataluña': 'Cataluña/Catalunya',
        'Comunitat Valenciana': 'Comunitat Valenciana',
        'Extremadura': 'Extremadura',
        'Galicia': 'Galicia',
        'Madrid, Comunidad de': 'Comunidad de Madrid',
        'Murcia, Región de': 'Región de Murcia',
        'Navarra, Comunidad Foral de': 'Comunidad Foral de Navarra',
        'País Vasco': 'País Vasco/Euskadi',
        'Rioja, La': 'La Rioja',
        'Ceuta': 'Ciudad Autónoma de Ceuta',
        'Melilla': 'Ciudad Autónoma de Melilla'
    }

    df_tasasUniversitarios_estudios['CCAA'] = df_tasasUniversitarios_estudios['CCAA'].replace(mapping_CCAAS)
    return df_tasasUniversitarios_estudios

def cargarGraficoHeatMapFiltradoCCA(df, tipo_tasa, CCAA):
    df = df[df['Tasas de actividad, empleo y paro'] == tipo_tasa]

    df = df[df['Total'] != '.']
    df['Total'] = df['Total'].str.replace(',', '.').astype(float)

    df = df[df['CCAA'] == CCAA]

    heatmap_data = df.pivot(index="Ámbito de estudio", columns="CCAA", values="Total")

    fig = px.imshow(heatmap_data, 
                #labels=dict(x=CCAA, y="Ámbito de estudio", color="Total"),
                x=heatmap_data.columns, 
                y=heatmap_data.index,
                color_continuous_scale="YlGnBu",
                text_auto=True)

    fig.update_layout(
        title=f"Heatmap de la Tasa de Actividad en {CCAA} por Ámbito de Estudio",
        #xaxis_title=CCAA,
        #yaxis_title="Ámbito de estudio",
        width=1000, 
        height=600,  
        plot_bgcolor='#5B5A5A',  
        paper_bgcolor='#5B5A5A',  
        font_color='white'  
    )

    st.plotly_chart(fig)

def cargarGraficoBarrasFiltradoEstudios(mapa_ccaa, df, tipo_tasa, ambito_estudio):
    df_tasasUniversitarios_estudios_tipoEstudio = df[(df["Ámbito de estudio"] == ambito_estudio) & (df["Tasas de actividad, empleo y paro"] == tipo_tasa)]

    df_tasasUniversitarios_estudios_tipoEstudio = df_tasasUniversitarios_estudios_tipoEstudio[df_tasasUniversitarios_estudios_tipoEstudio['Total'] != '.']
    df_tasasUniversitarios_estudios_tipoEstudio['Total'] = df_tasasUniversitarios_estudios_tipoEstudio['Total'].str.replace(',', '.').astype(float)

    fig = px.bar(
        df_tasasUniversitarios_estudios_tipoEstudio,
        x='CCAA',
        y='Total',
        labels={'Comunidades y Ciudades Autónomas': 'CCAA', 'Total': tipo_tasa},
        title=f'{tipo_tasa} por CCAA y estudios {ambito_estudio}'
    )

    fig.update_traces(marker_color='#A97A00')

    fig.update_layout(
        xaxis_title='CCAA',
        yaxis_title=tipo_tasa,
        title={'x': 0.5}, 
        xaxis_tickangle=-45,
        plot_bgcolor='#5B5A5A',  
        paper_bgcolor='#5B5A5A',  
        font_color='white'  
    )

    st.plotly_chart(fig)

    
    mapa_ccaa_tipoTasa = pd.merge(mapa_ccaa, df_tasasUniversitarios_estudios_tipoEstudio[['CCAA', 'Total']], on='CCAA', how='left')

    fig, axis = plt.subplots(1, 1, figsize=(10, 10))

    fig.patch.set_alpha(0.0)
    axis.set_axis_off()
    axis.patch.set_alpha(0.0)

    divider = make_axes_locatable(axis)
    cax = divider.append_axes("bottom", size="5%", pad=0.1)

    mapa_ccaa_tipoTasa.plot(
            ax=axis, 
            cmap='inferno_r', 
            column='Total', 
            legend=True, 
            cax=cax,    
        )

    cbar = axis.get_figure().colorbar(axis.collections[0], cax=cax, orientation='horizontal')
    cbar.set_label(f"{tipo_tasa} en cada CCAA para {ambito_estudio}", color='white')

    cbar.ax.tick_params(labelcolor='white')
    cbar.outline.set_edgecolor('white')


    plt.setp(cbar.ax.xaxis.get_label(), color='white')

    st.pyplot(fig)


def app():
    
    st.title("Estadísticas laborales de los universitarios en España")  
    st.write("#### Situación laboral en 2019 de los graduados universitarios del curso 2013-2014")
    st.write("<i>(Unidad de medida: Porcentaje de los titulados en la situación laboral indicada)</i>", unsafe_allow_html=True)

    df_universitarios = cargarDatosUniversitarios()
    ccaas_lista = df_universitarios['CCAA'].unique()
    ambitos_estudio_lista = df_universitarios['Ámbito de estudio'].unique()
    mapa_ccaa = gpd.read_file('./datasets/lineas_limite.zip!SHP_ETRS89/recintos_autonomicas_inspire_peninbal_etrs89')
    mapa_ccaa = mapa_ccaa.rename(columns={'NAMEUNIT': 'CCAA'})

    tipo_info_mostrar = st.selectbox('Selecciona el tipo de información a mostrar', ['Tasa de empleo', 'Tasa de paro', 'Tasa de actividad'])

    if tipo_info_mostrar == "Tasa de empleo":
        #st.write("Implementar gráfico y mapa de tasa de Empleo Universitarios por carrera")

        selected_filtrado = st.radio("##### Filtrar por: ", options = ["Comunidades Autónomas", "Ámbito de estudio"])

        if selected_filtrado == "Comunidades Autónomas":
            ccaa_escogida = st.selectbox("Selecciona la Comunidad Autónoma", options = ccaas_lista)

            
            cargarGraficoHeatMapFiltradoCCA(df_universitarios, tipo_info_mostrar, ccaa_escogida)


        elif selected_filtrado == "Ámbito de estudio":
            ambito_estudio = st.selectbox("Selecciona el Ámbito de estudio", options = ambitos_estudio_lista)

            cargarGraficoBarrasFiltradoEstudios(mapa_ccaa, df_universitarios, tipo_info_mostrar, ambito_estudio)

    elif tipo_info_mostrar == "Tasa de paro":
        #st.write("Implementar gráfico y mapa de tasa de Paro Universitarios por carrera")
        selected_filtrado = st.radio("##### Filtrar por: ", options = ["Comunidades Autónomas", "Ámbito de estudio"])
        
        if selected_filtrado == "Comunidades Autónomas":
            ccaa_escogida = st.selectbox("Selecciona la Comunidad Autónoma", options = ccaas_lista)
            cargarGraficoHeatMapFiltradoCCA(df_universitarios, tipo_info_mostrar, ccaa_escogida)

        elif selected_filtrado == "Ámbito de estudio":
            ambito_estudio = st.selectbox("Selecciona el Ámbito de estudio", options = ambitos_estudio_lista)
            cargarGraficoBarrasFiltradoEstudios(mapa_ccaa, df_universitarios, tipo_info_mostrar, ambito_estudio)

    elif tipo_info_mostrar == "Tasa de actividad":
        #st.write("Implementar gráfico y mapa de tasa de Actividad Universitarios por carrera")
        selected_filtrado = st.radio("##### Filtrar por: ", options = ["Comunidades Autónomas", "Ámbito de estudio"])

        if selected_filtrado == "Comunidades Autónomas":
            ccaa_escogida = st.selectbox("Selecciona la Comunidad Autónoma", options = ccaas_lista)
            cargarGraficoHeatMapFiltradoCCA(df_universitarios, tipo_info_mostrar, ccaa_escogida)

        elif selected_filtrado == "Ámbito de estudio":
            ambito_estudio = st.selectbox("Selecciona el Ámbito de estudio", options = ambitos_estudio_lista)
            cargarGraficoBarrasFiltradoEstudios(mapa_ccaa, df_universitarios, tipo_info_mostrar, ambito_estudio)

   