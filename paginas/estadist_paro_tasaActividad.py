import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import geopandas as gpd
from mpl_toolkits.axes_grid1 import make_axes_locatable
#import os



mapping = {
    '01 Andalucía': 'Andalucía',
    '02 Aragón': 'Aragón',
    '03 Asturias, Principado de': 'Principado de Asturias',
    '04 Balears, Illes': 'Illes Balears',
    '05 Canarias': 'Canarias',
    '06 Cantabria': 'Cantabria',
    '07 Castilla y León': 'Castilla y León',
    '08 Castilla - La Mancha': 'Castilla-La Mancha',
    '09 Cataluña': 'Cataluña/Catalunya',
    '10 Comunitat Valenciana': 'Comunitat Valenciana',
    '11 Extremadura': 'Extremadura',
    '12 Galicia': 'Galicia',
    '13 Madrid, Comunidad de': 'Comunidad de Madrid',
    '14 Murcia, Región de': 'Región de Murcia',
    '15 Navarra, Comunidad Foral de': 'Comunidad Foral de Navarra',
    '16 País Vasco': 'País Vasco/Euskadi',
    '17 Rioja, La': 'La Rioja',
    '18 Ceuta': 'Ciudad Autónoma de Ceuta',
    '19 Melilla': 'Ciudad Autónoma de Melilla'
}

mapping_PAISES = {
    'Aruba': 'Aruba',
    'Afghanistan': 'Afghanistan',
    'Angola': 'Angola',
    'Albania': 'Albania',
    'Andorra': 'Andorra',
    'United Arab Emirates': 'United Arab Emirates',
    'Argentina': 'Argentina',
    'Armenia': 'Armenia',
    'American Samoa': 'American Samoa',
    'Antigua and Barbuda': 'Antigua and Barbuda',
    'Australia': 'Australia',
    'Austria': 'Austria',
    'Azerbaijan': 'Azerbaijan',
    'Burundi': 'Burundi',
    'Belgium': 'Belgium',
    'Benin': 'Benin',
    'Burkina Faso': 'Burkina Faso',
    'Bangladesh': 'Bangladesh',
    'Bulgaria': 'Bulgaria',
    'Bahrain': 'Bahrain',
    'Bahamas, The': 'Bahamas',
    'Bosnia and Herzegovina': 'Bosnia and Herz.',
    'Belarus': 'Belarus',
    'Belize': 'Belize',
    'Bermuda': 'Bermuda',
    'Bolivia': 'Bolivia',
    'Brazil': 'Brazil',
    'Barbados': 'Barbados',
    'Brunei Darussalam': 'Brunei',
    'Bhutan': 'Bhutan',
    'Botswana': 'Botswana',
    'Central African Republic': 'Central African Rep.',
    'Canada': 'Canada',
    'Central Europe and the Baltics': 'Central Europe and the Baltics',
    'Switzerland': 'Switzerland',
    'Channel Islands': 'Channel Islands',
    'Chile': 'Chile',
    'China': 'China',
    "Cote d'Ivoire": "Côte d'Ivoire",
    'Cameroon': 'Cameroon',
    'Congo, Dem. Rep.': 'Dem. Rep. Congo',
    'Congo, Rep.': 'Congo',
    'Colombia': 'Colombia',
    'Comoros': 'Comoros',
    'Cabo Verde': 'Cabo Verde',
    'Costa Rica': 'Costa Rica',
    'Caribbean small states': 'Caribbean small states',
    'Cuba': 'Cuba',
    'Curacao': 'Curacao',
    'Cayman Islands': 'Cayman Islands',
    'Cyprus': 'Cyprus',
    'Czechia': 'Czechia',
    'Germany': 'Germany',
    'Djibouti': 'Djibouti',
    'Dominica': 'Dominica',
    'Denmark': 'Denmark',
    'Dominican Republic': 'Dominican Rep.',
    'Algeria': 'Algeria',
    'East Asia & Pacific (excluding high income)': 'East Asia & Pacific (excluding high income)',
    'Early-demographic dividend': 'Early-demographic dividend',
    'East Asia & Pacific': 'East Asia & Pacific',
    'Europe & Central Asia (excluding high income)': 'Europe & Central Asia (excluding high income)',
    'Europe & Central Asia': 'Europe & Central Asia',
    'Ecuador': 'Ecuador',
    'Egypt, Arab Rep.': 'Egypt',
    'Euro area': 'Euro area',
    'Eritrea': 'Eritrea',
    'Spain': 'Spain',
    'Estonia': 'Estonia',
    'Ethiopia': 'Ethiopia',
    'European Union': 'European Union',
    'Fragile and conflict affected situations': 'Fragile and conflict affected situations',
    'Finland': 'Finland',
    'Fiji': 'Fiji',
    'France': 'France',
    'Faroe Islands': 'Faroe Islands',
    'Micronesia, Fed. Sts.': 'Micronesia, Fed. Sts.',
    'Gabon': 'Gabon',
    'United Kingdom': 'United Kingdom',
    'Georgia': 'Georgia',
    'Ghana': 'Ghana',
    'Gibraltar': 'Gibraltar',
    'Guinea': 'Guinea',
    'Gambia, The': 'Gambia',
    'Guinea-Bissau': 'Guinea-Bissau',
    'Equatorial Guinea': 'Eq. Guinea',
    'Greece': 'Greece',
    'Grenada': 'Grenada',
    'Greenland': 'Greenland',
    'Guatemala': 'Guatemala',
    'Guam': 'Guam',
    'Guyana': 'Guyana',
    'High income': 'High income',
    'Hong Kong SAR, China': 'Hong Kong SAR, China',
    'Honduras': 'Honduras',
    'Heavily indebted poor countries (HIPC)': 'Heavily indebted poor countries (HIPC)',
    'Croatia': 'Croatia',
    'Haiti': 'Haiti',
    'Hungary': 'Hungary',
    'IBRD only': 'IBRD only',
    'IDA & IBRD total': 'IDA & IBRD total',
    'IDA total': 'IDA total',
    'IDA blend': 'IDA blend',
    'Indonesia': 'Indonesia',
    'IDA only': 'IDA only',
    'Isle of Man': 'Isle of Man',
    'India': 'India',
    'Not classified': 'Not classified',
    'Ireland': 'Ireland',
    'Iran, Islamic Rep.': 'Iran',
    'Iraq': 'Iraq',
    'Iceland': 'Iceland',
    'Israel': 'Israel',
    'Italy': 'Italy',
    'Jamaica': 'Jamaica',
    'Jordan': 'Jordan',
    'Japan': 'Japan',
    'Kazakhstan': 'Kazakhstan',
    'Kenya': 'Kenya',
    'Kyrgyz Republic': 'Kyrgyzstan',
    'Cambodia': 'Cambodia',
    'Kiribati': 'Kiribati',
    'St. Kitts and Nevis': 'St. Kitts and Nevis',
    'Korea, Rep.': 'South Korea',
    'Kuwait': 'Kuwait',
    'Latin America & Caribbean (excluding high income)': 'Latin America & Caribbean (excluding high income)',
    'Lao PDR': 'Laos',
    'Lebanon': 'Lebanon',
    'Liberia': 'Liberia',
    'Libya': 'Libya',
    'St. Lucia': 'St. Lucia',
    'Latin America & Caribbean': 'Latin America & Caribbean',
    'Least developed countries: UN classification': 'Least developed countries: UN classification',
    'Low income': 'Low income',
    'Liechtenstein': 'Liechtenstein',
    'Sri Lanka': 'Sri Lanka',
    'Lower middle income': 'Lower middle income',
    'Low & middle income': 'Low & middle income',
    'Lesotho': 'Lesotho',
    'Late-demographic dividend': 'Late-demographic dividend',
    'Lithuania': 'Lithuania',
    'Luxembourg': 'Luxembourg',
    'Latvia': 'Latvia',
    'Macao SAR, China': 'Macao SAR, China',
    'St. Martin (French part)': 'St. Martin (French part)',
    'Morocco': 'Morocco',
    'Monaco': 'Monaco',
    'Moldova': 'Moldova',
    'Madagascar': 'Madagascar',
    'Maldives': 'Maldives',
    'Middle East & North Africa': 'Middle East & North Africa',
    'Mexico': 'Mexico',
    'Marshall Islands': 'Marshall Islands',
    'Middle income': 'Middle income',
    'North Macedonia': 'North Macedonia',
    'Mali': 'Mali',
    'Malta': 'Malta',
    'Myanmar': 'Myanmar',
    'Middle East & North Africa (excluding high income)': 'Middle East & North Africa (excluding high income)',
    'Montenegro': 'Montenegro',
    'Mongolia': 'Mongolia',
    'Northern Mariana Islands': 'Northern Mariana Islands',
    'Mozambique': 'Mozambique',
    'Mauritania': 'Mauritania',
    'Mauritius': 'Mauritius',
    'Malawi': 'Malawi',
    'Malaysia': 'Malaysia',
    'North America': 'North America',
    'Namibia': 'Namibia',
    'New Caledonia': 'New Caledonia',
    'Niger': 'Niger',
    'Nigeria': 'Nigeria',
    'Nicaragua': 'Nicaragua',
    'Netherlands': 'Netherlands',
    'Norway': 'Norway',
    'Nepal': 'Nepal',
    'Nauru': 'Nauru',
    'New Zealand': 'New Zealand',
    'OECD members': 'OECD members',
    'Oman': 'Oman',
    'Other small states': 'Other small states',
    'Pakistan': 'Pakistan',
    'Panama': 'Panama',
    'Peru': 'Peru',
    'Philippines': 'Philippines',
    'Palau': 'Palau',
    'Papua New Guinea': 'Papua New Guinea',
    'Poland': 'Poland',
    'Pre-demographic dividend': 'Pre-demographic dividend',
    'Puerto Rico': 'Puerto Rico',
    "Korea, Dem. People's Rep.": 'North Korea',
    'Portugal': 'Portugal',
    'Paraguay': 'Paraguay',
    'West Bank and Gaza': 'Palestine',
    'Pacific island small states': 'Pacific island small states',
    'Post-demographic dividend': 'Post-demographic dividend',
    'French Polynesia': 'French Polynesia',
    'Qatar': 'Qatar',
    'Romania': 'Romania',
    'Russian Federation': 'Russia',
    'Rwanda': 'Rwanda',
    'South Asia': 'South Asia',
    'Saudi Arabia': 'Saudi Arabia',
    'Sudan': 'Sudan',
    'Senegal': 'Senegal',
    'Singapore': 'Singapore',
    'Solomon Islands': 'Solomon Is.',
    'Sierra Leone': 'Sierra Leone',
    'El Salvador': 'El Salvador',
    'San Marino': 'San Marino',
    'Somalia': 'Somalia',
    'Serbia': 'Serbia',
    'Sub-Saharan Africa (excluding high income)': 'Sub-Saharan Africa (excluding high income)',
    'South Sudan': 'S. Sudan',
    'Sub-Saharan Africa': 'Sub-Saharan Africa',
    'Small states': 'Small states',
    'Sao Tome and Principe': 'Sao Tome and Principe',
    'Suriname': 'Suriname',
    'Slovak Republic': 'Slovakia',
    'Slovenia': 'Slovenia',
    'Sweden': 'Sweden',
    'Eswatini': 'eSwatini',
    'Sint Maarten (Dutch part)': 'Sint Maarten (Dutch part)',
    'Seychelles': 'Seychelles',
    'Syrian Arab Republic': 'Syria',
    'Turks and Caicos Islands': 'Turks and Caicos Islands',
    'Chad': 'Chad',
    'East Asia & Pacific (IDA & IBRD countries)': 'East Asia & Pacific (IDA & IBRD countries)',
    'Europe & Central Asia (IDA & IBRD countries)': 'Europe & Central Asia (IDA & IBRD countries)',
    'Togo': 'Togo',
    'Thailand': 'Thailand',
    'Tajikistan': 'Tajikistan',
    'Turkmenistan': 'Turkmenistan',
    'Latin America & the Caribbean (IDA & IBRD countries)': 'Latin America & the Caribbean (IDA & IBRD countries)',
    'Timor-Leste': 'Timor-Leste',
    'Middle East & North Africa (IDA & IBRD countries)': 'Middle East & North Africa (IDA & IBRD countries)',
    'Tonga': 'Tonga',
    'South Asia (IDA & IBRD)': 'South Asia (IDA & IBRD)',
    'Sub-Saharan Africa (IDA & IBRD countries)': 'Sub-Saharan Africa (IDA & IBRD countries)',
    'Trinidad and Tobago': 'Trinidad and Tobago',
    'Tunisia': 'Tunisia',
    'Turkiye': 'Turkey',
    'Tuvalu': 'Tuvalu',
    'Tanzania': 'Tanzania',
    'Uganda': 'Uganda',
    'Ukraine': 'Ukraine',
    'Upper middle income': 'Upper middle income',
    'Uruguay': 'Uruguay',
    'United States': 'United States of America',
    'Uzbekistan': 'Uzbekistan',
    'St. Vincent and the Grenadines': 'St. Vincent and the Grenadines',
    'Venezuela, RB': 'Venezuela',
    'British Virgin Islands': 'British Virgin Islands',
    'Virgin Islands (U.S.)': 'Virgin Islands (U.S.)',
    'Viet Nam': 'Vietnam',
    'Vanuatu': 'Vanuatu',
    'World': 'World',
    'Samoa': 'Samoa',
    'Kosovo': 'Kosovo',
    'Yemen, Rep.': 'Yemen',
    'South Africa': 'South Africa',
    'Zambia': 'Zambia',
    'Zimbabwe': 'Zimbabwe',
}


@st.cache_data
def cargarDatosParoCCAAEspanya():


    df_paro_espanya = pd.read_csv('./datasets/paro_Espanya.csv', sep='\t')
    #df_paro_espanya = df_paro_espanya[df_paro_espanya['Comunidades y Ciudades Autónomas'] != 'Total Nacional']
   
    df_paro_espanya['Total'] = df_paro_espanya['Total'].str.replace(',', '.')
    #df_paro_espanya['Total'] = df_paro_espanya['Total'].astype(float)

    df_paro_espanya['Comunidades y Ciudades Autónomas'] = df_paro_espanya['Comunidades y Ciudades Autónomas'].replace(mapping)
    df_paro_espanya = df_paro_espanya.rename(columns={'Comunidades y Ciudades Autónomas': 'CCAA', "Total": "Tasa Paro"})

    return df_paro_espanya

@st.cache_data
def cargarDatosActividadCCAAEspanya():

    df_actividad_espanya = pd.read_csv('./datasets/tasa_actividad_Espanya.csv', sep='\t')
    #df_actividad_espanya = df_actividad_espanya[df_actividad_espanya['Comunidades y Ciudades Autónomas'] != 'Total Nacional']
   
    df_actividad_espanya['Total'] = df_actividad_espanya['Total'].str.replace(',', '.')
    #df_actividad_espanya['Total'] = df_actividad_espanya['Total'].astype(float)

    df_actividad_espanya['Comunidades y Ciudades Autónomas'] = df_actividad_espanya['Comunidades y Ciudades Autónomas'].replace(mapping)
    df_actividad_espanya = df_actividad_espanya.rename(columns={'Comunidades y Ciudades Autónomas': 'CCAA', "Total": "Tasa Actividad"})

    return df_actividad_espanya

@st.cache_data
def cargarDatosProyeccionActividadCCAAEspanya():

    df_proyeccionActividad_espanya = pd.read_csv('./datasets/Proyeccion_Tasa_Actividad_Espanya.csv', sep='\t')
   
    proyeccion_actividad_espanya = df_proyeccionActividad_espanya[df_proyeccionActividad_espanya["Comunidades y ciudades autónomas"] != "Ceuta y Melilla"]

    mapping = {
    'Andalucía': 'Andalucía',
    'Aragón': 'Aragón',
    'Asturias (Principado de)': 'Principado de Asturias',
    'Balears (Illes)': 'Illes Balears',
    'Canarias': 'Canarias',
    'Cantabria': 'Cantabria',
    'Castilla y León': 'Castilla y León',
    'Castilla - La Mancha': 'Castilla-La Mancha',
    'Cataluña': 'Cataluña/Catalunya',
    'Comunitat Valenciana': 'Comunitat Valenciana',
    'Extremadura': 'Extremadura',
    'Galicia': 'Galicia',
    'Madrid (Comunidad de)': 'Comunidad de Madrid',
    'Murcia (Región de)': 'Región de Murcia',
    'Navarra (Comunidad Foral de)': 'Comunidad Foral de Navarra',
    'País Vasco': 'País Vasco/Euskadi',
    'Rioja (La)': 'La Rioja'
    }
    mapping_sexo = {
        'Varones': 'Hombres',
        'Mujeres': 'Mujeres'
        }

    proyeccion_actividad_espanya = proyeccion_actividad_espanya.rename(columns={'Comunidades y ciudades autónomas': 'CCAA'})
    proyeccion_actividad_espanya['CCAA'] = proyeccion_actividad_espanya['CCAA'].replace(mapping)
    proyeccion_actividad_espanya['Sexo'] = proyeccion_actividad_espanya['Sexo'].replace(mapping_sexo)

    return proyeccion_actividad_espanya

@st.cache_data
def cargarMapaEspanyaCCAA():
    mapa_ccaa = gpd.read_file('./datasets/lineas_limite.zip!SHP_ETRS89/recintos_autonomicas_inspire_peninbal_etrs89')
    mapa_ccaa = mapa_ccaa.rename(columns={'NAMEUNIT': 'CCAA'})

    mapa_ccaa = mapa_ccaa[mapa_ccaa["NATLEVNAME"] == "Comunidad autónoma"]
    mapa_ccaa = mapa_ccaa[mapa_ccaa["CCAA"] != "Territorios no asociados a ninguna autonomía"]

    return mapa_ccaa


@st.cache_data
def cargarDatosParoMundo():
    df_world_unemployment = pd.read_csv('./datasets/UnemploymentRate_WorldStats.csv')
    df_world_unemployment['Country Name'] = df_world_unemployment['Country Name'].replace(mapping_PAISES)
    columns_to_drop = [str(year) for year in range(1960, 1992)]

    df_world_unemployment.drop(columns=columns_to_drop, inplace=True)

    return df_world_unemployment

@st.cache_data
def cargrMapaMundo():
    mapamundi = gpd.read_file('./datasets/naturalearth_lowres.zip')
    mapamundi.rename(columns={'name': 'Country Name'}, inplace=True)

    return mapamundi



def app():


    #current_directory = os.getcwd()
    #print("Current working directory:", current_directory)
    df_paro_espanya = cargarDatosParoCCAAEspanya()
    df_actividad_espanya = cargarDatosActividadCCAAEspanya()
    df_proyeccionActividad_espanya = cargarDatosProyeccionActividadCCAAEspanya()
    mapa_ccaa = cargarMapaEspanyaCCAA()

    df_paro_mundo = cargarDatosParoMundo()
    mapa_mundo = cargrMapaMundo()

    st.title("Tasas de Actividad y Paro")

    tipo_info_mostrar = st.selectbox('Selecciona el tipo de información a mostrar', ['Tasa de Paro en España', 'Tasa de Actividad Laboral en España', 'Proyección Tasa de Actividad en España', 'Tasa de Paro en el Mundo'])

    if tipo_info_mostrar == "Tasa de Paro en España":

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            paro_sexo = st.selectbox('Selecciona el sexo', ['Hombres', 'Mujeres'])

        with col2:
            paro_edad = st.selectbox('Selecciona el rango de edad', ['Total', 'Menores de 25 años', '25 y más años', 'De 16 a 19 años', 'De 20 a 24 años', 'De 25 a 54 años', '55 y más años'])

        with col3:
            paro_ccaa = st.selectbox("Seleccionar CCAA (o mostrar TOTAL)", list(df_paro_espanya["CCAA"].unique()))

        if paro_ccaa == "Total Nacional":
            with col4:
                paro_trimestre = st.selectbox("Seleccionar Período (Trimestre)", list(df_paro_espanya["Periodo"].unique()))


        generar_graficoMapa = st.button("Generar gráfico y mapa")

        if generar_graficoMapa:
            #st.write("BOTÓN GENERAR GRAFICO Y MAPA PULSADO")

            if paro_ccaa == "Total Nacional":
               
                paro_espanya_mod = df_paro_espanya[(df_paro_espanya["Sexo"] == paro_sexo) & (df_paro_espanya["Edad"] == paro_edad) & (df_paro_espanya["Periodo"] == paro_trimestre)]
                paro_espanya_mod['Tasa Paro'] = paro_espanya_mod['Tasa Paro'].astype(float)
                fig = px.bar(
                    paro_espanya_mod,
                    x='CCAA',
                    y='Tasa Paro',
                    labels={'Comunidades y Ciudades Autónomas': 'CCAA', 'Total': 'Tasa de Paro'},
                    title=f'Tasa de paro por CCAA\tPeriodo: {paro_trimestre}\tEdad: {paro_edad}\tSexo: {paro_sexo}'
                )

                fig.update_traces(marker_color='#A97A00')

                fig.update_layout(
                    xaxis_title='CCAA',
                    yaxis_title='Tasa de Paro',
                    title={'x': 0.5}, 
                    xaxis_tickangle=-45,
                    plot_bgcolor='#5B5A5A',  
                    paper_bgcolor='#5B5A5A',  
                    font_color='white'  
                )

                st.plotly_chart(fig)

                st.write("#### Mapa de la tasa de paro en las CCAA de España")
                mapa_ccaa_paro = pd.merge(mapa_ccaa, paro_espanya_mod[['CCAA', 'Tasa Paro']], on='CCAA', how='left')
               
                fig, axis = plt.subplots(1, 1, figsize=(10, 10))

                fig.patch.set_alpha(0.0)
                axis.set_axis_off()
                axis.patch.set_alpha(0.0)

                divider = make_axes_locatable(axis)
                cax = divider.append_axes("bottom", size="5%", pad=0.1)

                mapa_ccaa_paro.plot(
                        ax=axis, 
                        cmap='inferno_r', 
                        column='Tasa Paro', 
                        legend=True, 
                        cax=cax, 
                        legend_kwds={'label': "Tasa de paro en cada CCAA", 'orientation': "horizontal"}
                    )
            
                cbar = axis.get_figure().colorbar(axis.collections[0], cax=cax, orientation='horizontal')
                cbar.set_label("Tasa de paro en cada CCAA", color='white')

                cbar.ax.tick_params(labelcolor='white')
                cbar.outline.set_edgecolor('white')


                plt.setp(cbar.ax.xaxis.get_label(), color='white')

                st.pyplot(fig)

            else:
                paro_espanya_mod = df_paro_espanya[(df_paro_espanya["Sexo"] == paro_sexo) & (df_paro_espanya["Edad"] == paro_edad) & (df_paro_espanya["CCAA"] == paro_ccaa)]
                paro_espanya_mod['Tasa Paro'] = paro_espanya_mod['Tasa Paro'].astype(float)
          
                paro_espanya_mod = paro_espanya_mod.iloc[::-1].reset_index(drop=True)
                fig = go.Figure()

                fig.add_trace(go.Scatter(
                    x=paro_espanya_mod['Periodo'],
                    y=paro_espanya_mod['Tasa Paro'],
                    mode='lines+markers',
                    marker=dict(color='skyblue'),
                    text=[f"Periodo: {periodo}<br>Tasa de Paro: {total}" for periodo, total in zip(paro_espanya_mod['Periodo'], paro_espanya_mod['Tasa Paro'])],
                    hoverinfo='text'
                ))

                fig.update_traces(marker_color='#A97A00')
                fig.update_layout(
                    title=f'Tasa de paro durante el periodo analizado<br>CCAA: {paro_ccaa}<br>Edad: {paro_edad}<br>Sexo: {paro_sexo}',
                    xaxis_title='Periodo',
                    yaxis_title='Tasa de Paro',
                    hovermode='closest',
                    plot_bgcolor='#5B5A5A',  
                    paper_bgcolor='#5B5A5A',  
                    font_color='white' 
                )

                st.plotly_chart(fig)
            #st.dataframe(df_paro_espanya)
        else:
            st.write("PULSA EL BOTÓN DE GENERAR GRAFICO Y MAPA")

    
    elif tipo_info_mostrar == "Tasa de Actividad Laboral en España":

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            actividad_sexo = st.selectbox('Selecciona el sexo', ['Hombres', 'Mujeres'])

        with col2:
            actividad_edad = st.selectbox('Selecciona el rango de edad', ['Total', 'Menores de 25 años', '25 y más años', 'De 16 a 19 años', 'De 20 a 24 años', 'De 25 a 54 años', '55 y más años'])

        with col3:
            actividad_ccaa = st.selectbox("Seleccionar CCAA (o mostrar TOTAL)", list(df_actividad_espanya["CCAA"].unique()))

        if actividad_ccaa == "Total Nacional":
            with col4:
                actividad_trimestre = st.selectbox("Seleccionar Período (Trimestre)", list(df_actividad_espanya["Periodo"].unique()))


        generar_graficoMapa = st.button("Generar gráfico y mapa")

        if generar_graficoMapa:
            #st.write("BOTÓN GENERAR GRAFICO Y MAPA PULSADO")

            if actividad_ccaa == "Total Nacional":
               
                actividad_espanya_mod = df_actividad_espanya[(df_actividad_espanya["Sexo"] == actividad_sexo) & (df_actividad_espanya["Edad"] == actividad_edad) & (df_actividad_espanya["Periodo"] == actividad_trimestre)]
                actividad_espanya_mod['Tasa Actividad'] = actividad_espanya_mod['Tasa Actividad'].astype(float)
                fig = px.bar(
                    actividad_espanya_mod,
                    x='CCAA',
                    y='Tasa Actividad',
                    labels={'Comunidades y Ciudades Autónomas': 'CCAA', 'Total': 'Tasa de Actividad'},
                    title=f'Tasa de actividad por CCAA\tPeriodo: {actividad_trimestre}\tEdad: {actividad_edad}\tSexo: {actividad_sexo}'
                )

                fig.update_traces(marker_color='#A97A00')

                fig.update_layout(
                    xaxis_title='CCAA',
                    yaxis_title='Tasa de Actividad',
                    title={'x': 0.5}, 
                    xaxis_tickangle=-45,
                    plot_bgcolor='#5B5A5A',  
                    paper_bgcolor='#5B5A5A',  
                    font_color='white'  
                )

                st.plotly_chart(fig)

                st.write("#### Mapa de la tasa de actividad en las CCAA de España")
                mapa_ccaa_actividad = pd.merge(mapa_ccaa, actividad_espanya_mod[['CCAA', 'Tasa Actividad']], on='CCAA', how='left')
               
                fig, axis = plt.subplots(1, 1, figsize=(10, 10))

                fig.patch.set_alpha(0.0)
                axis.set_axis_off()
                axis.patch.set_alpha(0.0)

                divider = make_axes_locatable(axis)
                cax = divider.append_axes("bottom", size="5%", pad=0.1)

                mapa_ccaa_actividad.plot(
                        ax=axis, 
                        cmap='inferno_r', 
                        column='Tasa Actividad', 
                        legend=True, 
                        cax=cax, 
                        legend_kwds={'label': "Tasa de actividad en cada CCAA", 'orientation': "horizontal"}
                    )
            
                cbar = axis.get_figure().colorbar(axis.collections[0], cax=cax, orientation='horizontal')
                cbar.set_label("Tasa de actividad en cada CCAA", color='white')

                cbar.ax.tick_params(labelcolor='white')
                cbar.outline.set_edgecolor('white')


                plt.setp(cbar.ax.xaxis.get_label(), color='white')

                st.pyplot(fig)

            else:
                actividad_espanya_mod = df_actividad_espanya[(df_actividad_espanya["Sexo"] == actividad_sexo) & (df_actividad_espanya["Edad"] == actividad_edad) & (df_actividad_espanya["CCAA"] == actividad_ccaa)]
                actividad_espanya_mod['Tasa Actividad'] = actividad_espanya_mod['Tasa Actividad'].astype(float)
          
                actividad_espanya_mod = actividad_espanya_mod.iloc[::-1].reset_index(drop=True)
                fig = go.Figure()

                fig.add_trace(go.Scatter(
                    x=actividad_espanya_mod['Periodo'],
                    y=actividad_espanya_mod['Tasa Actividad'],
                    mode='lines+markers',
                    marker=dict(color='skyblue'),
                    text=[f"Periodo: {periodo}<br>Tasa de Actividad: {total}" for periodo, total in zip(actividad_espanya_mod['Periodo'], actividad_espanya_mod['Tasa Actividad'])],
                    hoverinfo='text'
                ))

                fig.update_layout(
                    title=f'Tasa de actividad durante el periodo analizado<br>CCAA: {actividad_ccaa}<br>Edad: {actividad_edad}<br>Sexo: {actividad_sexo}',
                    xaxis_title='Periodo',
                    yaxis_title='Tasa de actividad',
                    hovermode='closest',
                    plot_bgcolor='#5B5A5A',  
                    paper_bgcolor='#5B5A5A',  
                    font_color='white'
                )

                st.plotly_chart(fig)
            #st.dataframe(df_actividad_espanya)
        else:
            st.write("PULSA EL BOTÓN DE GENERAR GRAFICO Y MAPA")


    elif tipo_info_mostrar == "Proyección Tasa de Actividad en España":
        #st.write("Implementar gráfico y mapa de proyección de tasa de actividad laboral en España")
        st.write("#### Porcentajes sobre la población de 16 a 64 años")
        tipo_grafico = st.selectbox('Selecciona el tipo de gráfico', ['Proyección por Sexo (Gráfico de Líneas)', 'Proyección por CCAA (Gráfico de Caja-Bigotes)', 'Proyección por Periodo y Sexo (Mapa de España)'])

        if tipo_grafico == "Proyección por Sexo (Gráfico de Líneas)":
            sexo_escogido = st.selectbox('Selecciona el sexo', ['Hombres', 'Mujeres'])
            proyeccion_actividad_espanya_hombres = df_proyeccionActividad_espanya[(df_proyeccionActividad_espanya["Sexo"] == sexo_escogido) & (df_proyeccionActividad_espanya["periodo"] >= 2023)]
            proyeccion_actividad_espanya_hombres["Total"] = proyeccion_actividad_espanya_hombres["Total"].str.replace(',', '.').astype(float)
            df_pivot = proyeccion_actividad_espanya_hombres.pivot(index='periodo', columns='CCAA', values='Total').reset_index()

            fig = px.line(df_pivot, x='periodo', y=df_pivot.columns[1:], markers=True)

            fig.update_layout(
                title='Serie Temporal por CCAA',
                xaxis_title='Periodo',
                yaxis_title='Proyección %',
                plot_bgcolor='#4A4949',  
                paper_bgcolor='#5B5A5A', 
                font_color='white'  
            )
            
            st.write('Interactúa con el gráfico a continuación para ver los datos de diferentes CCAA a lo largo del tiempo.')

            st.plotly_chart(fig)
        
        elif tipo_grafico == "Proyección por CCAA (Gráfico de Caja-Bigotes)":

            ccaa_escogida = st.selectbox('Selecciona la CCAA', list(df_proyeccionActividad_espanya["CCAA"].unique()))

            proyeccion_actividad_espanya_ccaa = df_proyeccionActividad_espanya[(df_proyeccionActividad_espanya["CCAA"] == ccaa_escogida) & (df_proyeccionActividad_espanya["periodo"] >= 2023)]
            proyeccion_actividad_espanya_ccaa['Total'] = proyeccion_actividad_espanya_ccaa['Total'].str.replace(',', '.').astype(float)

            fig = px.box(proyeccion_actividad_espanya_ccaa, x='Sexo', y='Total', title=f'Proyección de la Tasa de Actividad por Sexo en {ccaa_escogida} entre 2023 y 2029', height=600)

            fig.update_traces(marker_color='#A97A00', boxmean=True)
            
            fig.update_layout(
                plot_bgcolor='#4A4949',  
                paper_bgcolor='#5B5A5A', 
                font_color='white'  
            )

            st.plotly_chart(fig)

        else: # Mapa de España
            periodo_escogido = st.selectbox('Selecciona el periodo', df_proyeccionActividad_espanya[df_proyeccionActividad_espanya["periodo"] >= 2023]["periodo"].unique().tolist())
            sexo_escogido = st.selectbox('Selecciona el sexo', ['Hombres', 'Mujeres'])
            proyeccion_actividad_espanya_ccaas = df_proyeccionActividad_espanya[(df_proyeccionActividad_espanya["Sexo"] == sexo_escogido) & (df_proyeccionActividad_espanya["periodo"] == periodo_escogido)]
            proyeccion_actividad_espanya_ccaas["Total"] = proyeccion_actividad_espanya_ccaas["Total"].str.replace(',', '.').astype(float)

            mapa_ccaa_proyecActividad = pd.merge(mapa_ccaa, proyeccion_actividad_espanya_ccaas[['CCAA', 'Total']], on='CCAA', how='left')

            fig, axis = plt.subplots(1, 1, figsize=(10, 10))

            fig.patch.set_alpha(0.0)
            axis.set_axis_off()
            axis.patch.set_alpha(0.0)

            divider = make_axes_locatable(axis)
            cax = divider.append_axes("bottom", size="5%", pad=0.1)

            mapa_ccaa_proyecActividad.plot(
                    ax=axis, 
                    cmap='inferno_r', 
                    column='Total', 
                    legend=True, 
                    cax=cax, 
                    legend_kwds={'label': "Proyección del porcentaje de actividad sobre la población en cada CCAA", 'orientation': "horizontal"}
                )
        
            cbar = axis.get_figure().colorbar(axis.collections[0], cax=cax, orientation='horizontal')
            cbar.set_label("% Proyección de actividad en cada CCAA", color='white')

            cbar.ax.tick_params(labelcolor='white')
            cbar.outline.set_edgecolor('white')


            plt.setp(cbar.ax.xaxis.get_label(), color='white')

            st.pyplot(fig)
        
    
    elif tipo_info_mostrar == "Tasa de Paro en el Mundo":
        
        periodo = st.selectbox('Selecciona el periodo', sorted(df_paro_mundo.columns[4:], reverse=True))

        st.write("#### Tasa de Paro calculada en porcentaje de la población en edad y condiciones de trabajar en cada país")

        mapamundi_unemployment = pd.merge(mapa_mundo, df_paro_mundo[['Country Name', periodo]], on='Country Name', how='left')

        mapamundi_unemployment_filtrado = mapamundi_unemployment.drop_duplicates(subset=['Country Name'])
        mapamundi_unemployment_filtrado[periodo] = mapamundi_unemployment_filtrado[periodo] /1000
        mapamundi_unemployment_filtrado.rename(columns={'Country Name': 'NAME_COUNTRY', periodo: 'Unemployment Rate'}, inplace=True)
        

        fig, axis = plt.subplots(1, 1, figsize=(30, 30))

        mapamundi_unemployment_filtrado.boundary.plot(ax=axis, color='black', linewidth=0.4)

        fig.patch.set_alpha(0.0)
        axis.set_axis_off()
        axis.patch.set_alpha(0.0)

        mapamundi_unemployment_filtrado.apply(
            lambda x: axis.annotate(
                text=x.NAME_COUNTRY,
                xy=x.geometry.centroid.coords[0],
                ha='center',
                fontsize=6 if 'Territorio' not in x.NAME_COUNTRY else 12
            ),
            axis=1
        )

        divider = make_axes_locatable(axis)
        cax = divider.append_axes("bottom", size="5%", pad=0.1)

        mapamundi_unemployment_filtrado.plot(
            ax=axis,
            cmap='inferno_r',
            column='Unemployment Rate',
            legend=True,
            cax=cax,
            legend_kwds={'label': "Porcentaje de paro en el mundo", 'orientation': "horizontal"},
            missing_kwds={"color": "lightgrey", "edgecolor": "red", "hatch": "///", "label": "Missing values"}
        )

        st.pyplot(fig)