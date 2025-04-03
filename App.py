import streamlit as st

# Diseño de la página
st.set_page_config(page_title="Centro de Alumnos - Ciencia de Datos", page_icon="📚")

# Barra lateral con opciones
st.sidebar.title("Navegación")
opcion = st.sidebar.radio("Selecciona una opción", ("Bienvenida", "Drive de Estudio", "Avisos"))

# Contenido de la página dependiendo de la opción seleccionada
if opcion == "Bienvenida":
    # Título y mensaje de bienvenida
    st.title("Bienvenidos, Estudiantes de Ciencia de Datos")
    st.title("Página del Centro de Alumnos de Ingeniería Civil en Ciencia de Datos  UTEM! 👋")
    st.write("""
    Nos complace presentarles la página web oficial del Centro de Alumnos de la carrera de Ingeniería Civil en Ciencia de Datos de la Universidad Tecnológica Metropolitana (UTEM).
    Este espacio ha sido diseñado con el objetivo de mantener informada a nuestra comunidad estudiantil y fortalecer la colaboración entre estudiantes.
    """)

    st.header("¿Qué encontrarás en nuestra página web?")

    st.subheader("📢 Avisos y Noticias")
    st.write("Mantente al día con los eventos académicos, charlas, talleres y otras actividades relevantes para nuestra carrera.")


    st.subheader("📂 Repositorio de Material Académico")
    st.write("Accede a un repositorio en Google Drive con material de apoyo para las asignaturas de la carrera, incluyendo apuntes, guías de estudio y otros recursos útiles.")

    st.write("""
    Nuestro compromiso es brindar un canal de comunicación efectivo y una fuente de información confiable para todos los estudiantes de Ingeniería Civil en Ciencia de Datos de la UTEM.

    ¡Síguenos en nuestras redes y participa activamente en nuestra comunidad!
    """) 

        # Título de la página
    st.title("Contáctanos")

    # Mensaje de contacto
    st.write("¡Síguenos en nuestras redes sociales y contáctanos por correo!")

    # Enlaces a Instagram y Gmail con íconos
    st.markdown("""
        <style>
        .social-buttons {
            display: flex;
            justify-content: center;
            gap: 20px;
            font-size: 30px;
        }
        .social-buttons a {
            text-decoration: none;
        }
        .social-buttons i {
            color: #555;
            transition: color 0.3s;
        }
        .social-buttons i:hover {
            color: #0077B5;  /* Color para Instagram y Gmail en hover */
        }
        </style>

        <div class="social-buttons">
            <a href="https://www.instagram.com/ceedatos/" target="_blank">
                <i class="fab fa-instagram">📷</i> Instagram
            </a>
            <a href="mailto:ce.iccd@utem.cl" target="_blank">
                <i class="fas fa-envelope">📧</i> ce.iccd@utem.cl
            </a>
        </div>
    """, unsafe_allow_html=True)   




elif opcion == "Drive de Estudio":
    # Título de la página
    st.title("Accede a nuestro Drive de Estudio")

    # Mensaje de contacto
    st.write("Aquí puedes acceder a los recursos de estudio compartidos en nuestro Google Drive.")

    # Enlace a Google Drive con íconos
    st.markdown("""
        <style>
        .social-buttons {
            display: flex;
            justify-content: center;
            gap: 20px;
            font-size: 30px;
        }
        .social-buttons a {
            text-decoration: none;
        }
        .social-buttons i {
            color: #555;
            transition: color 0.3s;
        }
        .social-buttons i:hover {
            color: #4285F4;  /* Color para Google Drive en hover */
        }
        </style>

        <div class="social-buttons">
            <a href="https://drive.google.com/drive/folders/TU_CODIGO_DE_DRIVE" target="_blank">
                <i class="fab fa-google-drive">📂</i> Google Drive
            </a>
        </div>
    """, unsafe_allow_html=True)



elif opcion == "Avisos":
    st.title("📣 Avisos")
    st.subheader("Aquí encontrarás los avisos importantes.")
    st.write("Esta sección se actualizará pronto con los avisos del centro de alumnos.")

