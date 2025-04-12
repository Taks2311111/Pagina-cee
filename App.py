import streamlit as st
import base64
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import plotly.graph_objs as go
# Diseño de la página
# Ecuación paramétrica para el corazón 3D con relleno

def heart_3d_filled(u, v):
        # Ajustamos la magnitud para hacerlo más grande y darle mayor profundidad
    y = 16 * np.sin(u)**3  # X como la "anchura" del corazón
    z = 13 * np.cos(u) - 5 * np.cos(2*u) - 2 * np.cos(3*u) - np.cos(4*u)  # Y como la "altura"
    x = v  # Profundidad de la figura (relleno a lo largo del eje Z)
    return x, y, z


# Leer la imagen local como base64
def get_base64_image(path):
    with open(path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def show_member(image_path, nombre, cargo):
    base64_img = get_base64_image(image_path)
    st.markdown(f"""
        <div style="display: flex; align-items: center; margin-bottom: 20px;">
            <img src="data:image/png;base64,{base64_img}" style="width: 130px; height: 130px; border-radius: 50%; margin-right: 20px;">
            <div style="color: white;">
                <h4 style="margin: 0;">{nombre}</h4>
                <p style="margin: 0;">{cargo}</p>
            </div>
        </div>
    """, unsafe_allow_html=True)



# Ruta de la imagen
image_path1 = "imgs/Logo1.png"
image_logo1 = get_base64_image(image_path1)

image_path20 = "imgs/Logo2.jpeg"
image_logo2  = get_base64_image(image_path20)



st.set_page_config(
    page_title="Ciencia de Datos-Centro de Alumnos",
    page_icon=f"data:image/png;base64,{image_logo2}"  # Incluir la imagen base64 en el page_icon
)


st.markdown(
    f"""
    <div style="
        position: absolute;
        top: -100px;
        left: -350px;
        z-index: 10;
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        padding: 10px;
        border-radius: 12px;
    ">
        <img src="data:image/png;base64,{image_logo1}" width="200" style="border-radius: 8px;">
    </div>
    """,
    unsafe_allow_html=True
)


# Barra lateral con opciones
st.sidebar.title("Navegación")
#opcion = st.sidebar.radio("Selecciona una opción", ("Bienvenida", "Drive de Estudio", "Avisos","Conocenos"))

st.markdown("""
    <style>
        .css-18e3th9 {
            background-color: #f0f8ff; /* Color de fondo suave */
            color: #2c3e50; /* Color del texto */
            font-family: 'Courier New', monospace; /* Estilo de la fuente */
            padding: 20px;
        }
        .css-1d391kg {
            background-color: #2980b9; /* Color del fondo del radio */
            border-radius: 10px; /* Bordes redondeados */
            padding: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Barra lateral con opciones
opcion = st.sidebar.radio(
    "Selecciona una opción", 
    ("Bienvenida", "Drive de Estudio", "Avisos", "Conocenos"),
    index=0,
    key="opciones",
)

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

    st.subheader("📢 Avisos ")
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

    ## corazon
 
# Ecuación paramétrica para el corazón 3D con relleno
# Ecuación paramétrica para el corazón 3D con relleno
    st.title("Corazon para nuestras bases ❤️ ")
    # Definir los valores de u y v (rango para los parámetros)
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(-10, 10, 40)  # Extender el rango de v para llenar la figura

    # Crear mallas para u y v
    U, V = np.meshgrid(u, v)

    # Calcular las coordenadas x, y, z usando la ecuación del corazón
    X, Y, Z = heart_3d_filled(U, V)

    # Crear la figura 3D con Plotly
    fig = go.Figure(data=[go.Surface(
        x=X, y=Y, z=Z, colorscale='reds', opacity=1,showscale=False 
    )])

    # Configuración del layout para el gráfico
    fig.update_layout(
        
        scene=dict(
            xaxis_title="X",
            yaxis_title="Y",
            zaxis_title="Z",
            xaxis=dict(range=[-20, 20]),
            yaxis=dict(range=[-20, 20]),
            zaxis=dict(range=[-20, 20]),
        )
    )

    # Mostrar la animación en Streamlit
    st.plotly_chart(fig, use_container_width=False,theme="streamlit")


elif opcion == "Drive de Estudio":
    # Título de la página
    st.title("Accede a nuestro Drive de Estudio")

    # Mensaje de contacto
    st.write("Aquí puedes acceder a los recursos de estudio compartidos en nuestro Google Drive.")
    st.write("Ingresar con el correo institucional de nuestra universidad")

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
            <a href="https://drive.google.com/drive/folders/1Q505dFbrA1FYVnRMqswJMDX4iOAqV-BV?usp=sharing" target="_blank">
                <i class="fab fa-google-drive">📂</i> Google Drive
            </a>
        </div>
    """, unsafe_allow_html=True)


elif opcion == "Avisos":
    st.title("📣 Avisos")
    st.subheader("Aquí encontrarás los avisos importantes.")
    st.write("Esta sección se actualizará pronto con los avisos del centro de alumnos.")

elif opcion == "Conocenos":
    st.title("Centro de Estudiantes de Ingeniería Civil en Ciencia de Datos")


    st.write("""
    Somos el Centro de Estudiantes de la carrera de Ingeniería Civil en Ciencia de Datos de la Universidad Metropolitana. Nuestra misión es representar y apoyar a nuestros compañeros, promoviendo la colaboración, el bienestar y el crecimiento académico y profesional dentro de nuestra comunidad.
    """)

    st.header("Directiva 2024-2026")
    
    show_member("imgs/andres.jpeg", "Andres Nicolas Vega Moraga", "Presidente")
    show_member("imgs/bruno.jpeg", "Bruno Eduardo Sainz Silva", "Vicepresidente")
    show_member("imgs/benjamin.jpeg", "Benjamin Ignacio Saavedra Contreras", "Secretario")
    show_member("imgs/juan.jpeg", "Juan Cristóbal Toledo Fierro", "Tesorero")
    show_member("imgs/juan.jpeg", "Glenn Deimian Lanyon Alarcón", "Bienestar Estudiantil y Género")
    show_member("imgs/welinton.jpeg", "Welinton Antonio Barrera Mondaca", "Comunicación")
    show_member("imgs/joaquin.jpeg", "Joaquín Ignacio Araya Bustos", "Delegado de Recreación")



