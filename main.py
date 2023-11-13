# Este es el archivo main donde correra el streamlit
import streamlit as st
import pandas as pd
from system_recomend import get_recomendations

# Cargar el archivo CSV
file_path = 'data_limpia.csv'  
df = pd.read_csv(file_path)

# Encabezado de la aplicación
st.title('Explorador de Libros')

# Sidebar para seleccionar el libro
selected_book = st.sidebar.selectbox('Seleccione un libro:', df['title'].unique())

# Filtrar el DataFrame por el libro seleccionado
selected_book_data = df[df['title'] == selected_book].iloc[0]

# Mostrar información del libro seleccionado 
st.write('## Detalles del Libro Seleccionado')
st.write(f'**Título:** {selected_book_data["title"]}')
st.write(f'**Autor(es):** {selected_book_data["authors"]}')
st.write(f'**Categoría:** {selected_book_data["categories"]}')
st.write(f'**Año de Publicación:** {selected_book_data["published_year"]}')
st.write(f'**Número de Páginas:** {selected_book_data["num_pages"]}')
st.write(f'**Descripción:** {selected_book_data["description"]}')

# Mostrar la imagen de cada libro
st.image(selected_book_data["thumbnail"], caption='Portada del Libro', width=200)

# separador
st.markdown("---")


# Mostrar el sistema de recomendaciones
st.title('Sistema de Recomendaciones de Libros')

recommendations = get_recomendations(selected_book)
st.write('## Lista Recomendada')

# Iterar sobre las recomendaciones y mostrar títulos e imágenes
for book_title in recommendations['lista recomendada']:
    # Filtrar el DataFrame por el título del libro recomendado
    recommended_book_data = df[df['title'] == book_title].iloc[0]

    st.write(f'**Título:** {book_title}')

    # Mostrar la imagen del libro recomendado
    st.image(recommended_book_data["thumbnail"], caption=f'Portada de "{book_title}"', width=150)
    st.write("---")