import streamlit as st

from streamlit_option_menu import option_menu

from paginas import inicio, estadist_universitarios, estadist_paro_tasaActividad


st.set_page_config(
        page_title="Trabajo de Visualización de Datos",
        layout="wide",
)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #5B5A5A;
    }
    </style>
    """,
    unsafe_allow_html=True
)


class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })


    def run():
        
        with st.sidebar:        
            app = option_menu(
                menu_title='Menú',
                options=['Inicio', 'Estadísticas de los Universitarios','Tasas de Actividad laboral y Paro'],
                icons=['box-arrow-in-right','journal-bookmark-fill','bar-chart-line'],
                menu_icon='list',
                default_index=1,
                
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "20px",}, 
        "nav-link": {"color":"white","font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#BA973D"},
        "nav-link-selected": {"background-color": "#A97A00", "color":"white"},}
                
                )
        
        
        if app == "Inicio":
            inicio.app()
        if app == "Estadísticas de los Universitarios":
            estadist_universitarios.app()
        if app == "Tasas de Actividad laboral y Paro":
            estadist_paro_tasaActividad.app()
    
            
             
    run()            
         