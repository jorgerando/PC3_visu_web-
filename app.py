import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="El Huésped Fantasma",
    page_icon="👻",
    layout="wide"
)

st.markdown("""
    <style>
    /* Importamos fuentes elegantes */
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;800&family=Cormorant+Garamond:wght@400;600&display=swap');

    /* Fondo limpio */
    .stApp {
        background-color: #FFFFFF;
    }

    .block-container {
        max-width: 1400px;
        padding-top: 2rem;
        padding-bottom: 5rem;
        margin: auto;
    }

    /* TÍTULO GIGANTE */
    .main-title {
        font-family: 'Cinzel', serif;
        color: #1a1a1a;
        font-size: 80px !important;
        line-height: 1;
        text-align: center;
        text-transform: uppercase;
        font-weight: 800;
        margin-top: 10px;
        margin-bottom: 10px;
    }

    /* TEXTO NARRATIVO MUY GRANDE (30px) */
    .narrative-text {
        font-family: 'Cormorant Garamond', serif;
        font-size: 30px !important; /* Letra muy grande */
        color: #2c3e50;
        line-height: 1.5;
        text-align: justify;
        padding: 0 10px;
    }

    /* Aseguramos que las listas también sean grandes */
    .narrative-text ul, .narrative-text li {
        font-size: 30px !important;
        line-height: 1.5;
        margin-bottom: 10px;
    }

    /* SUBTÍTULOS DE SECCIÓN (Ahora en NEGRO) */
    h2 {
        font-family: 'Cinzel', serif !important;
        color: #1a1a1a !important; /* <--- CAMBIO: Negro intenso */
        font-size: 40px !important;
        font-weight: 800 !important;
    }

    /* Líneas divisorias doradas */
    hr {
        border: 0;
        height: 1px;
        background-image: linear-gradient(to right, rgba(0, 0, 0, 0), rgba(184, 134, 11, 0.75), rgba(0, 0, 0, 0));
        margin-top: 40px;
        margin-bottom: 40px;
    }
    </style>
""", unsafe_allow_html=True)


import os
from PIL import Image
import streamlit as st

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

img_city = Image.open(os.path.join(BASE_DIR, "FantasmaVerano.png"))
img_resort = Image.open(os.path.join(BASE_DIR, "FantasmaUrbano.png"))



@st.cache_data
def load_data():
    return pd.read_csv("hotel_bookings.csv")

try:
    df = load_data()
except FileNotFoundError:
    df = pd.DataFrame({'hotel': ['City Hotel']*79330 + ['Resort Hotel']*40060})

st.markdown("<p style='text-align: center; color: #888; font-family: sans-serif; letter-spacing: 3px; font-size: 14px; margin-bottom:0;'>Por Jorge Rando Hernández</p>", unsafe_allow_html=True)

st.markdown('<h1 class="main-title">EL PROBLEMA DEL<br>HUÉSPED FANTASMA </h1>', unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("""
<div class="narrative-text" style="text-align: center;">
    Imagina un hotel lleno de actividad. El teléfono suena, las reservas se acumulan y el sistema indica una <b>ocupación total</b>.
    Las habitaciones se limpian a conciencia, los suelos se pulen, los cocineros preparan los más deliciosos manjares y todo el personal está listo.
    Pero llega el día... y el lobby está vacío; nadie ha venido. ¡¿Qué ha ocurrido?!
    <br><br>
    Aunque esta situación pueda parecer digna del inicio de una novela de terror, es un fenómeno real que experimentan gran cantidad de hoteles.
    Entender las razones por las que los huéspedes cancelan sus reservas puede suponer la diferencia entre un negocio próspero y la más absoluta <b>quiebra</b>.
</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

st.header("Las Víctimas del Huésped Fantasma 💀 ")

conteo_hoteles = df['hotel'].value_counts().reset_index()
conteo_hoteles.columns = ['Hotel', 'Reservas']

st.markdown("""
<div class="narrative-text">
    Para entender este misterio, primero debemos hacer la <b>autopsia</b> a algunas de sus víctimas.
    Nuestro drama tiene dos protagonistas reales en Portugal que, aunque opuestos, sufren la misma maldición:
    el lujoso <b>Tivoli Marina Vilamoura</b> y el cosmopolita <b>Tivoli Oriente</b>.
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
col_real1, col_real2 = st.columns(2)

with col_real1:
    st.markdown("""
<div class="narrative-text" style="background-color: #f9f9f9; padding: 25px; border-radius: 10px; border-left: 8px solid #FF6B6B; height: 100%;">
<h3 style="font-family: 'Cinzel'; color: #1a1a1a; margin-top: 0; font-size: 36px;"> El City Hotel 🏨 </h3>
<a href="https://www.google.com/maps/search/Tivoli+Oriente+Lisboa" target="_blank" style="font-size: 22px; color: #FF6B6B; text-decoration: none; font-weight: bold;">
👉 Ver ubicación real en Lisboa 🇵🇹
</a>
<hr style="margin: 15px 0; border-color: #ddd;">
<p style="font-size: 40px !important; line-height: 1.5; color: #2c3e50;">
Este gigante de cristal y acero, situado en el moderno <i>Parque das Nações</i>, es el hogar de las prisas. Sus pasillos son transitados principalmente por <b>ejecutivos de negocios</b> con agendas apretadas, <b>asistentes a congresos</b> internacionales y viajeros urbanos en escapadas cortas de fin de semana.
</p>
<p style="font-size: 40px !important; line-height: 1.5; color: #2c3e50;">
Aquí la vida se mide en horas. Su mayor debilidad es lo imprevisible: una simple huelga de transporte o la cancelación de un evento corporativo pueden dejarlo vacío en cuestión de segundos.
</p>
</div>
""", unsafe_allow_html=True)

with col_real2:
    st.markdown("""
<div class="narrative-text" style="background-color: #f9f9f9; padding: 25px; border-radius: 10px; border-left: 8px solid #4ECDC4; height: 100%;">
<h3 style="font-family: 'Cinzel'; color: #1a1a1a; margin-top: 0; font-size: 36px;"> El Resort Hotel 🏖️ </h3>
<a href="https://www.google.com/maps/search/Tivoli+Marina+Vilamoura" target="_blank" style="font-size: 22px; color: #4ECDC4; text-decoration: none; font-weight: bold;">
👉 Ver ubicación real en El Algarve 🇵🇹
</a>
<hr style="margin: 15px 0; border-color: #ddd;">
<p style="font-size: 40px !important; line-height: 1.5; color: #2c3e50;">
Un oasis de 5 estrellas en el Algarve, anclado entre la playa dorada y el puerto deportivo. Es el territorio sagrado del descanso para <b>familias enteras en verano</b>, parejas en <b>luna de miel</b> y turistas del norte de Europa que buscan golf y sol durante largas estancias.
</p>
<p style="font-size: 40px !important; line-height: 1.5; color: #2c3e50;">
A diferencia de su hermano urbano, aquí el tiempo se detiene. Pero su dependencia del clima y las vacaciones es su talón de Aquiles: una cancelación aquí supone perder reservas de semanas enteras, un golpe financiero devastador.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("""
<div class="narrative-text">
    Al analizar sus constantes sus ingresos, descubrimos dos comportamientos muy diferentes:
    <ul>
        <li><b>El Resort (Línea Azul):</b> Sufre una <b>estacionalidad extrema</b>. Vive por y para el verano. Fíjate cómo su precio (ADR) se dispara en Julio y Agosto, llegando a triplicar sus tarifas de invierno.</li>
        <li><b>La Ciudad (Línea Roja):</b> Es el corredor de fondo. Mantiene una constancia durante todo el año, con picos más suaves dictados por eventos o temporadas de negocios (mayo/septiembre).</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# --- GRÁFICO 1: ADR POR MES ---
# Ordenamos los meses correctamente para que no salgan alfabéticos
month_order = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# Agrupamos datos
seasonal_data = df.groupby(['hotel', 'arrival_date_month'])['adr'].mean().reset_index()

# Aplicamos el orden
seasonal_data['arrival_date_month'] = pd.Categorical(seasonal_data['arrival_date_month'], categories=month_order, ordered=True)
seasonal_data = seasonal_data.sort_values('arrival_date_month')

# Creamos el gráfico
fig_adr = px.line(
    seasonal_data,
    x='arrival_date_month',
    y='adr',
    color='hotel',
    markers=True,
    labels={'arrival_date_month': 'Mes', 'adr': 'Precio Medio (€)', 'hotel': 'Tipo de Hotel'},
    color_discrete_map={'City Hotel': '#FF6B6B', 'Resort Hotel': '#4ECDC4'} # Mismos colores que las tarjetas
)
fig_adr.update_layout(plot_bgcolor="white", font=dict(family="Cormorant Garamond", size=18))
fig_adr.update_xaxes(showgrid=False)
fig_adr.update_yaxes(showgrid=True, gridcolor='#eee')

st.plotly_chart(fig_adr, use_container_width=True)


# -----------------------------------------------------------------------------
# SECCIÓN 2: LA ESCENA DEL CRIMEN (NORMALIZADO %)
# -----------------------------------------------------------------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.header("La Escena del Crimen 🔎 ")

st.markdown("""
<div class="narrative-text">
    Aquí es donde el drama se hace tangible. Al revisar los libros de registro, descubrimos una hemorragia masiva de ingresos.
    No estamos hablando de unos pocos cambios de planes... estamos hablando de una <b>epidemia de cancelaciones</b>.

</div>
""", unsafe_allow_html=True)

# --- 1. PROCESAMIENTO DEL GRÁFICO (NORMALIZADO) ---
df['status_desc'] = df['is_canceled'].map({0: '✅ Check-In', 1: '❌ Cancelado'})

# Agrupamos
crime_scene = df.groupby(['hotel', 'status_desc']).size().reset_index(name='count')

# Calculamos totales por hotel para sacar el %
total_hotel = df.groupby('hotel').size().reset_index(name='total')
crime_scene = crime_scene.merge(total_hotel, on='hotel')
crime_scene['percent'] = (crime_scene['count'] / crime_scene['total'] * 100)

# --- GRÁFICO MEJORADO (EJE Y ES %) ---
fig_conflict = px.bar(
    crime_scene,
    x="hotel",
    y="percent", # <--- AHORA USAMOS EL PORCENTAJE COMO EJE Y
    color="status_desc",

    text="percent",
    barmode="group", # Comparación lado a lado
    color_discrete_map={
        '✅ Check-In': '#27AE60',      # Verde sólido
        '❌ Cancelado': '#C0392B'      # Rojo oscuro intenso
    },
    labels={'percent': 'Porcentaje de Reservas (%)', 'hotel': '', 'status_desc': 'Estado'}
)

# ESTÉTICA DE ETIQUETAS
fig_conflict.update_traces(
    texttemplate='<b>%{text:.1f}%</b>', # Formato con 1 decimal y %
    textposition='inside',
    textfont=dict(color='white', size=16),
    insidetextanchor='middle'
)

fig_conflict.update_layout(
    plot_bgcolor="white",
    font=dict(family="Cormorant Garamond", size=18),
    yaxis=dict(showgrid=True, gridcolor='#f0f0f0', title="Porcentaje (%)"), # Título eje Y claro
    legend=dict(title=None, orientation="h", y=1.1),
    margin=dict(t=60)
)

st.plotly_chart(fig_conflict, use_container_width=True)


# --- 2. CÁLCULO ECONÓMICO: EL "MES DEL DESASTRE" ---

# A) Preparar datos económicos
df['total_nights'] = df['stays_in_weekend_nights'] + df['stays_in_week_nights']
df['revenue_estimated'] = df['adr'] * df['total_nights']

# B) Función para calcular la pérdida en el PEOR mes
def calcular_perdida_mes_pico(nombre_hotel):
    df_h = df[df['hotel'] == nombre_hotel]

    # Busamos el mes con más facturación POTENCIAL (suma total)
    monthly_revenue = df_h.groupby('arrival_date_month')['revenue_estimated'].sum()
    peak_month = monthly_revenue.idxmax()
    max_revenue = monthly_revenue.max()

    # Dinero de cancelaciones en ese mes
    df_peak = df_h[(df_h['arrival_date_month'] == peak_month) & (df_h['is_canceled'] == 1)]
    lost_revenue = df_peak['revenue_estimated'].sum()

    return peak_month, lost_revenue, max_revenue

month_resort, lost_resort, total_resort = calcular_perdida_mes_pico('Resort Hotel')
month_city, lost_city, total_city = calcular_perdida_mes_pico('City Hotel')

# --- 3. VISUALIZACIÓN DE LA PÉRDIDA ---
st.markdown("""
<div class="narrative-text">
    Si las bajas no se cubren a tiempo, puede que nuestras víctimas no lo cuenten...
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

col_loss1, col_loss2 = st.columns(2)

# Tarjeta Resort
with col_loss1:
    st.markdown(f"""
    <div style="background-color: #fff0f0; border: 2px solid #C0392B; padding: 20px; border-radius: 10px; text-align: center;">
        <h4 style="margin:0; color: #555;">RESORT HOTEL</h4>
        <p style="font-size: 16px;">Mes Crítico: <b>{month_resort}</b></p>
        <hr style="border-color: #eec;">
        <p style="margin:0; font-size: 14px;">Ingresos Perdidos (Mes Pico):</p>
        <p style="font-size: 40px; font-weight: bold; color: #C0392B; margin: 0;">
            {lost_resort:,.0f} €
        </p>
        <p style="font-size: 14px; color: #777;">
            <b>{lost_resort/total_resort*100:.1f}%</b> de la facturación se esfumó
        </p>
    </div>
    """, unsafe_allow_html=True)

# Tarjeta City
with col_loss2:
    st.markdown(f"""
    <div style="background-color: #fff0f0; border: 2px solid #C0392B; padding: 20px; border-radius: 10px; text-align: center;">
        <h4 style="margin:0; color: #555;">CITY HOTEL</h4>
        <p style="font-size: 16px;">Mes Crítico: <b>{month_city}</b></p>
        <hr style="border-color: #eec;">
        <p style="margin:0; font-size: 14px;">Ingresos Perdidos (Mes Pico):</p>
        <p style="font-size: 40px; font-weight: bold; color: #C0392B; margin: 0;">
            {lost_city:,.0f} €
        </p>
        <p style="font-size: 14px; color: #777;">
            <b>{lost_city/total_city*100:.1f}%</b> de la facturación se esfumó
        </p>
    </div>
    """, unsafe_allow_html=True)


import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# -----------------------------------------------------------------------------
# SECCIÓN 6: LAS PISTAS (NUMERADAS Y SIN ESPACIOS EXTRA)
# -----------------------------------------------------------------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.header("Las Pistas: Perfilando al Sospechoso 🧩")

st.markdown("""
<div class="narrative-text">
    Para descubrir al fantasma, debemos seguir sus movimientos: dónde y cómo reserva, con cuánta antelación y qué comportamientos son sospechosos.
    <br><br>
    Siguiendo el rastro de <b>migas de pan</b> que deja a su paso, presenta las siguientes evidencias:
</div>
<br>
""", unsafe_allow_html=True)

# =============================================================================
# PISTA 1: EL CANAL (BURBUJAS)
# =============================================================================
st.subheader("Pista 1: El Canal de Entrada")

st.markdown("""
<div class="narrative-text">
    En este gráfico analizamos qué tipo de cliente cancela más <b>según el canal que utilizó para reservar</b>.
    <br>
    <i>Pasa el ratón por encima de las burbujas para ver el perfil del huesped.</i>
</div>
""", unsafe_allow_html=True)


# --- PROCESAMIENTO PISTA 1 ---
df_risk = df.groupby(['hotel', 'market_segment'])['is_canceled'].agg(['count', 'mean']).reset_index()
df_risk['risk_percent'] = (df_risk['mean'] * 100).round(1)
df_risk = df_risk[df_risk['count'] > 50]

segment_map = {
    'Online TA': 'Online', 'Offline TA/TO': 'Agencias', 'Groups': 'Grupos',
    'Direct': 'Directo', 'Corporate': 'Empresas', 'Complementary': 'VIP', 'Aviation': 'Avión'
}
df_risk['label'] = df_risk['market_segment'].map(segment_map).fillna(df_risk['market_segment'])

desc_map = {
    'Online TA': '<b>El Cazador de Ofertas</b><br>Turistas digitales (Booking/Expedia).<br>Buscan flexibilidad y precio.<br><i>Ej: Pareja joven comparando 5 hoteles.</i>',
    'Offline TA/TO': '<b>El Turista Tradicional</b><br>Paquetes "Todo Incluido" en agencia física.<br>Buscan seguridad.<br><i>Ej: Jubilados o familias con Tour Operador.</i>',
    'Groups': '<b>El Colectivo</b><br>Reservas en bloque para eventos.<br>Riesgo binario: o vienen todos o nadie.<br><i>Ej: Bodas, congresos, equipos.</i>',
    'Direct': '<b>El Cliente Directo</b><br>Web oficial o teléfono.<br>Trato personal y condiciones específicas.<br><i>Ej: Familia fiel a la marca.</i>',
    'Corporate': '<b>El Ejecutivo</b><br>Viajes de empresa obligatorios.<br>Reserva a última hora por necesidad.<br><i>Ej: Comercial firmando contrato.</i>',
    'Complementary': '<b>El VIP</b><br>Invitados, influencers o cortesía.<br>Sin coste, sin presión.<br><i>Ej: Influencer promocionando hotel.</i>',
    'Aviation': '<b>La Tripulación</b><br>Pilotos y azafatas en escala.<br>Contrato fijo con aerolínea.<br><i>Ej: Tripulación descansando entre vuelos.</i>'
}
df_risk['description'] = df_risk['market_segment'].map(desc_map).fillna('')
df_risk['text_display'] = df_risk['label'] + "<br>" + df_risk['risk_percent'].astype(str) + "%"

def calculate_spread_x(data):
    data = data.sort_values('risk_percent')
    x_coords = []
    placed = []
    for i, row in data.iterrows():
        y = row['risk_percent']
        proposed_x = 0
        for (prev_y, prev_x) in placed:
            if abs(y - prev_y) < 12:
                if prev_x >= 0: proposed_x = - (abs(prev_x) + 1)
                else: proposed_x = (abs(prev_x) + 1)
        x_coords.append(proposed_x)
        placed.append((y, proposed_x))
    data['x_spread'] = x_coords
    return data

df_final = pd.concat([
    calculate_spread_x(df_risk[df_risk['hotel'] == 'Resort Hotel'].copy()),
    calculate_spread_x(df_risk[df_risk['hotel'] == 'City Hotel'].copy())
])
df_final['bubble_size'] = 25 + (df_final['risk_percent'] * 1.8)

fig_bubble_risk = px.scatter(
    df_final, x="x_spread", y="risk_percent", size="bubble_size", color="risk_percent",
    facet_col="hotel", text="text_display",
    color_continuous_scale=['#27AE60', '#F1C40F', '#E74C3C', '#922B21'],
    range_y=[-5, 115], title="", size_max=110, custom_data=['description', 'label']
)
fig_bubble_risk.update_layout(
    plot_bgcolor="white", font=dict(family="Cormorant Garamond", size=18), showlegend=False,
    height=600, margin=dict(t=30, b=10),
    xaxis=dict(visible=False), xaxis2=dict(visible=False),
    yaxis=dict(title="Probabilidad de Cancelación (%)", showgrid=True, gridcolor='#eee'),
    coloraxis_colorbar=dict(title="Riesgo %")
)
fig_bubble_risk.update_traces(
    textposition='middle center', textfont=dict(family="Cinzel", size=14, color="white", weight="bold"),
    marker=dict(line=dict(width=2, color='white')),
    hovertemplate="<b>%{customdata[1]}</b><br><br>%{customdata[0]}<extra></extra>"
)
fig_bubble_risk.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1], font=dict(size=25)))
st.plotly_chart(fig_bubble_risk, use_container_width=True)

# ---> CONCLUSIÓN PISTA 1
st.info("🕵️ **Deducción Pista 1:** Los canales digitales y los grupos masivos son volátiles e impersonales. En cambio, **el cliente que llama directamente o viene por empresa es mucho más fiel**.")


# =============================================================================
# PISTA 2: EL TIEMPO (VIOLIN)
# =============================================================================
st.markdown("<hr>", unsafe_allow_html=True)
st.subheader("Pista 2: El Factor Tiempo")

st.markdown("""
<div class="narrative-text">
    Otra pista que nos da información es el tiempo de reserva.
    <br>
    <i>Pasa el ratón por las siluetas para ver los detalles.</i>
</div>
""", unsafe_allow_html=True)

# --- PROCESAMIENTO PISTA 2 ---
df_violin = df[df['lead_time'] < 400].copy()
counts = df_violin.groupby(['hotel', 'is_canceled'])['hotel'].transform('count')
df_violin['total_count_str'] = counts.apply(lambda x: f"{x:,.0f}")

fig_time = go.Figure()
mask_ok = df_violin['is_canceled'] == 0
fig_time.add_trace(go.Violin(
    x=df_violin['hotel'][mask_ok], y=df_violin['lead_time'][mask_ok],
    name='✅ Vienen', side='negative', line_color='#2ECC71',
    meanline_visible=True, points=False, width=0.9, legendgroup='ok',
    customdata=df_violin['total_count_str'][mask_ok],
    hovertemplate="<b>✅ Vienen</b><br>Total: %{customdata}<br>Antelación: %{y} días<extra></extra>"
))
mask_cancel = df_violin['is_canceled'] == 1
fig_time.add_trace(go.Violin(
    x=df_violin['hotel'][mask_cancel], y=df_violin['lead_time'][mask_cancel],
    name='❌ Cancelan', side='positive', line_color='#E74C3C',
    meanline_visible=True, points=False, width=0.9, legendgroup='bad',
    customdata=df_violin['total_count_str'][mask_cancel],
    hovertemplate="<b>❌ Cancelan</b><br>Total: %{customdata}<br>Antelación: %{y} días<extra></extra>"
))
fig_time.update_layout(
    violingap=0, violinmode='overlay', plot_bgcolor="white",
    font=dict(family="Cormorant Garamond", size=18),
    margin=dict(l=20, r=20, t=60, b=20),
    yaxis=dict(showgrid=True, gridcolor='#f0f0f0', range=[0, 480], title="Días de Antelación"),
    xaxis=dict(showticklabels=False, title=""),
    legend=dict(orientation="h", yanchor="top", y=0.99, xanchor="center", x=0.5, font=dict(size=16), bgcolor="rgba(255,255,255,0.9)"),
    height=550
)
fig_time.add_annotation(x="Resort Hotel", y=460, text="RESORT HOTEL", showarrow=False, font=dict(size=24, family="Cinzel", color="black"))
fig_time.add_annotation(x="City Hotel", y=460, text="CITY HOTEL", showarrow=False, font=dict(size=24, family="Cinzel", color="black"))
st.plotly_chart(fig_time, use_container_width=True)

# ---> CONCLUSIÓN PISTA 2
st.info("⏳ **Deducción Pista 2:** El tiempo juega en nuestra contra. **Cuanto antes reservan, más tiempo tienen para arrepentirse.** Las reservas de última hora son mucho más seguras.")


# =============================================================================
# PISTAS 3 y 4: COMPORTAMIENTO
# =============================================================================
st.markdown("<hr>", unsafe_allow_html=True)
st.subheader("Pistas 3 y 4: El Comportamiento")

st.markdown("""
<div class="narrative-text">
    Ya tenemos identificado el <b>Quién</b> y el <b>Cuándo</b> parece que ocurren las cancelaciones.
    <br>
    Ahora analicemos el <b>Qué</b>. Hay dos comportamientos clave que diferencian a un cliente real de uno fantasma:
</div>
""", unsafe_allow_html=True)

# --- PROCESAMIENTO PISTAS 3 y 4 ---
df['requests_group'] = df['total_of_special_requests'].apply(lambda x: 'Con Peticiones (Seguro)' if x > 0 else '0 Peticiones (Riesgo)')
df['parking_group'] = df['required_car_parking_spaces'].apply(lambda x: 'Con Coche (Seguro)' if x > 0 else 'Sin Coche (Riesgo)')

req_risk = df.groupby('requests_group')['is_canceled'].mean().reset_index()
req_risk['percent'] = (req_risk['is_canceled'] * 100).round(1)

park_risk = df.groupby('parking_group')['is_canceled'].mean().reset_index()
park_risk['percent'] = (park_risk['is_canceled'] * 100).round(1)

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Pista 3: ¿Pidió algo especial?**")
    fig_req = px.bar(
        req_risk, x='requests_group', y='percent', text='percent', color='requests_group',
        color_discrete_map={'0 Peticiones (Riesgo)': '#E74C3C', 'Con Peticiones (Seguro)': '#2ECC71'},
        title=""
    )
    fig_req.update_layout(
        plot_bgcolor="white", font=dict(family="Cormorant Garamond", size=18),
        yaxis=dict(visible=False, range=[0, 100]), xaxis=dict(title=""), showlegend=False, height=300, margin=dict(t=10, b=10)
    )
    fig_req.update_traces(texttemplate='%{text}%', textposition='outside', width=0.5)
    st.plotly_chart(fig_req, use_container_width=True)
    # ---> CONCLUSIÓN PISTA 3
    st.info("🗣️ **Deducción Pista 3:** Un fantasma no pide cunas ni almohadas. **El silencio es sospechoso.**")

with col2:
    st.markdown("**Pista 4: ¿Necesita Parking?**")
    fig_park = px.bar(
        park_risk, x='parking_group', y='percent', text='percent', color='parking_group',
        color_discrete_map={'Sin Coche (Riesgo)': '#E74C3C', 'Con Coche (Seguro)': '#2ECC71'},
        title=""
    )
    fig_park.update_layout(
        plot_bgcolor="white", font=dict(family="Cormorant Garamond", size=18),
        yaxis=dict(visible=False, range=[0, 100]), xaxis=dict(title=""), showlegend=False, height=300, margin=dict(t=10, b=10)
    )
    fig_park.update_traces(texttemplate='%{text}%', textposition='outside', width=0.5)
    st.plotly_chart(fig_park, use_container_width=True)
    # ---> CONCLUSIÓN PISTA 4
    st.info("🚗 **Deducción Pista 4:** Prueba física definitiva. **Si traen coche, existen y vendrán.**")


# =============================================================================
# PISTAS 5 y 6: EL CONTEXTO
# =============================================================================
st.markdown("<hr>", unsafe_allow_html=True)
st.subheader("Pistas 5 y 6: El Contexto")

st.markdown("""
<div class="narrative-text">
    Por último, hemos detectado una pista crucial sobre el <b>origen</b> de los sospechosos, una marca que casi todos los huéspedes fantasma dejan a su paso.
    Además, hemos revisado sus <b>fichas policiales</b> para comprobar si tienen antecedentes.
    <br><br>
</div>
""", unsafe_allow_html=True)

# --- PROCESAMIENTO PISTAS 5 y 6 ---
df['origin_group'] = df['country'].apply(lambda x: 'Local (Portugal) ⚠️' if x == 'PRT' else 'Internacional (Turista) ✈️')
df['history_group'] = df['previous_cancellations'].apply(lambda x: 'Reincidente (Ya canceló) 💀' if x > 0 else 'Limpio (Sin antecedentes) ✨')

origin_risk = df.groupby(['hotel', 'origin_group'])['is_canceled'].mean().reset_index()
origin_risk['percent'] = (origin_risk['is_canceled'] * 100).round(1)

history_risk = df.groupby(['hotel', 'history_group'])['is_canceled'].mean().reset_index()
history_risk['percent'] = (history_risk['is_canceled'] * 100).round(1)

# Pista 5
st.markdown("**Pista 5: La Conexión Local (Portugal)**")
fig_origin = px.bar(
    origin_risk, x='origin_group', y='percent', text='percent', color='origin_group', facet_col='hotel',
    color_discrete_map={'Local (Portugal) ⚠️': '#E74C3C', 'Internacional (Turista) ✈️': '#2ECC71'},
    title=""
)
fig_origin.update_layout(
    plot_bgcolor="white", font=dict(family="Cormorant Garamond", size=18),
    yaxis=dict(visible=False, range=[0, 100]), xaxis=dict(title=""), xaxis2=dict(title=""),
    showlegend=True, legend=dict(title="", orientation="h", y=1.15, x=0.5, xanchor="center"),
    height=400, margin=dict(t=50, b=10)
)
fig_origin.update_traces(texttemplate='%{text}%', textposition='outside', width=0.6)
fig_origin.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1], font=dict(family="Cinzel", size=20)))
st.plotly_chart(fig_origin, use_container_width=True)

# ---> CONCLUSIÓN PISTA 5
st.info("🌍 **Deducción Pista 5:** La proximidad reduce el compromiso. **El local reserva 'por si acaso', el extranjero planea en serio.**")

# Pista 6
st.markdown("<br>**Pista 6: Antecedentes Penales**", unsafe_allow_html=True)
fig_hist = px.bar(
    history_risk, x='history_group', y='percent', text='percent', color='history_group', facet_col='hotel',
    color_discrete_map={'Reincidente (Ya canceló) 💀': '#E74C3C', 'Limpio (Sin antecedentes) ✨': '#2ECC71'},
    title=""
)
fig_hist.update_layout(
    plot_bgcolor="white", font=dict(family="Cormorant Garamond", size=18),
    yaxis=dict(visible=False, range=[0, 100]), xaxis=dict(title=""), xaxis2=dict(title=""),
    showlegend=True, legend=dict(title="", orientation="h", y=1.15, x=0.5, xanchor="center"),
    height=400, margin=dict(t=50, b=10)
)
fig_hist.update_traces(texttemplate='%{text}%', textposition='outside', width=0.6)
fig_hist.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1], font=dict(family="Cinzel", size=20)))
st.plotly_chart(fig_hist, use_container_width=True)

# ---> CONCLUSIÓN PISTA 6
st.info("💀 **Deducción Pista 6:** La historia se repite. **Si ya canceló antes, la probabilidad de que vuelva a hacerlo es altísima.**")


#------------------------------------------------------------------------------------------------------------------------------------------------------
import plotly.graph_objects as go
import streamlit as st

# -----------------------------------------------------------------------------
# SECCIÓN 7: DESENMASCARANDO AL FANTASMA (HEXÁGONO DE RIESGO)
# -----------------------------------------------------------------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.header("Desenmascarando al Fantasma 🎭")

st.markdown("""
<div class="narrative-text">
    La evidencia es concluyente. No nos enfrentamos a un solo enemigo, sino a dos perfiles opuestos de pendiendo de la naturaleza de sus estancias.
    Hemos generado un <b>retrato robot</b> basado en las 6 pistas clave para identificar sus motivaciones.
</div>
<br>
""", unsafe_allow_html=True)

# --- FUNCIÓN GRÁFICO (Misma lógica, solo visualización) ---
def create_radar_profile(stats, title_color):
    categories = [
        'Pista 1: Canal (Grupos/Offline)',
        'Pista 2: Antelación (+4 meses)',
        'Pista 3: Silencio (Sin cambios)',
        'Pista 4: Sin Coche',
        'Pista 5: Origen (Local)',
        'Pista 6: Historial (Reincidente)'
    ]

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=stats,
        theta=categories,
        fill='toself',
        name='Perfil de Riesgo',
        line_color=title_color,
        fillcolor=title_color,
        opacity=0.5,
        marker=dict(size=5)
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 10], showticklabels=False, linecolor='rgba(0,0,0,0.1)'),
            angularaxis=dict(tickfont=dict(size=11, color='black'), rotation=90, direction='clockwise'),
            bgcolor='rgba(0,0,0,0)'
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=45, r=45, t=30, b=30),
        height=350,
        showlegend=False
    )
    return fig

# --- LAYOUT DE FICHAS CRIMINALES ---
col1, col2 = st.columns(2)

# --- TRUCO CSS MEJORADO: CENTRADO + MARCO BONITO ---
st.markdown("""
<style>
/* Esto asegura que el contenedor de la imagen ocupe todo el ancho para poder centrar */
div[data-testid="stImage"] {
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 100%;
}

/* ESTILOS DEL MARCO DE LA IMAGEN */
div[data-testid="stImage"] > img {
    display: block;
    margin-left: auto;
    margin-right: auto;
    /* Bordes redondeados suaves */
    border-radius: 15px;
    /* Marco gris claro sutil (coherente con el tema) */
    border: 4px solid #f8f9fa;
    /* Sombra suave para dar profundidad (efecto "foto pegada") */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    /* Pequeño espacio interno entre la foto y el marco */
    padding: 2px;
    /* Color de fondo blanco para el pequeño espacio del padding */
    background-color: white;
}
</style>
""", unsafe_allow_html=True)
# ----------------------------------------------------------

# === FICHA 1: CITY HOTEL ===
with col1:
    with st.container(border=True):
        # Título
        st.markdown("""
        <div style="text-align: center; border-bottom: 3px solid #E74C3C; margin-bottom: 15px; padding-bottom: 10px;">
            <h2 style="font-family: serif; color: #E74C3C; margin:0; font-size: 32px; letter-spacing: 2px;">WANTED</h2>
            <span style="color: #333; font-weight: bold; font-size: 18px; text-transform: uppercase;">El "Estratega Urbano"</span>
        </div>
        """, unsafe_allow_html=True)

        # IMAGEN (El CSS de arriba la centra y le pone el marco automáticamente)
        # Ajusta el width si lo quieres más grande o pequeño
        st.image(img_resort, width=350)

        # Descripción
        st.markdown("""
        **📋 PERFIL PSICOLÓGICO:**
        Es un viajero profesional o corporativo que juega con el sistema.

        * **El Bloqueador:** Utiliza canales Offline o de Grupo para bloquear habitaciones "por si acaso".
        * **Sin Ataduras:** Al no llevar coche (**Pista 4**), no tiene compromiso logístico. Depende de vuelos o trenes.
        * **Reincidente:** Su historial (**Pista 6**) le delata. Ya ha cancelado antes.
        """, unsafe_allow_html=True)

        # Gráfico
        stats_city = [9, 9, 10, 10, 6, 9]
        fig_radar_city = create_radar_profile(stats_city, '#E74C3C')
        st.plotly_chart(fig_radar_city, use_container_width=True, config={'displayModeBar': False})

        # Nota
        st.markdown("""
        <div style="background-color: #fceceb; padding: 10px; border-radius: 5px; font-size: 13px; text-align: center; color: #8a1f11;">
            <i>"Reserva habitaciones como quien guarda sitio en una cola. Si no llega a tiempo, simplemente se va."</i>
        </div>
        """, unsafe_allow_html=True)

# === FICHA 2: RESORT HOTEL ===
with col2:
    with st.container(border=True):
        # Título
        st.markdown("""
        <div style="text-align: center; border-bottom: 3px solid #F39C12; margin-bottom: 15px; padding-bottom: 10px;">
            <h2 style="font-family: serif; color: #F39C12; margin:0; font-size: 32px; letter-spacing: 2px;">WANTED</h2>
            <span style="color: #333; font-weight: bold; font-size: 18px; text-transform: uppercase;">El "Especulador Solar"</span>
        </div>
        """, unsafe_allow_html=True)

        # IMAGEN (El CSS de arriba la centra y le pone el marco automáticamente)
        st.image(img_city, width=350)

        # Descripción
        st.markdown("""
        **📋 PERFIL PSICOLÓGICO:**
        Turista nacional que busca seguridad a bajo coste, pero con cero compromiso.

        * **El Previsor Indeciso:** Reserva en Enero para Agosto (**Pista 2**) buscando precio.
        * **Factor Local:** Su talón de Aquiles es su origen (**Pista 5**). Al ser portugués, cancelar no le cuesta vuelos.
        * **Volátil:** Usa el hotel como un "Plan B". Si hace mal tiempo, cancelará.
        """, unsafe_allow_html=True)

        # Gráfico
        stats_resort = [8, 8, 9, 5, 10, 4]
        fig_radar_resort = create_radar_profile(stats_resort, '#F39C12')
        st.plotly_chart(fig_radar_resort, use_container_width=True, config={'displayModeBar': False})

        # Nota
        st.markdown("""
        <div style="background-color: #fcf3cf; padding: 10px; border-radius: 5px; font-size: 13px; text-align: center; color: #7d6006;">
            <i>"Para este perfil, tu hotel es solo una opción de respaldo hasta que encuentra algo mejor."</i>
        </div>
        """, unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# SECCIÓN 8: CONCLUSIONES Y RECOMENDACIONES
# -----------------------------------------------------------------------------
st.markdown("<hr>", unsafe_allow_html=True)
# Título actualizado
st.header("Cómo protegernos de nuestros Huéspedes Fantasma")

# --- INTRODUCCIÓN AL VALOR DEL MODELO ---
st.markdown("""
<div class="narrative-text">
    Este análisis demuestra que
    <b>no todas las cancelaciones son iguales</b>. Dependiendo de la naturaleza de la reserva (negocios vs. placer)
    y del hotel (ciudad vs. resort), los motivos para abandonar son radicalmente distintos.
    <br><br>
    Entender y saber gestionar las cancelaciones es clave para el desarrollo de un proyecto hotelero exitoso.
</div>
<br>
""", unsafe_allow_html=True)

# --- RESUMEN DE MOTIVOS VS SOLUCIONES ---
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("💡 La Realidad")
    st.markdown("""
    Hemos descubierto que la cancelación es un comportamiento complejo con múltiples caras:

    * **En Ciudad:** Es un problema **logístico**. El huésped bloquea habitaciones "por si acaso" y cancela si su agenda cambia. La antelación excesiva y la falta de coche son sus señales.
    * **En Resort:** Es un problema **emocional/económico**. El huésped busca la mejor oferta hasta el último segundo. Su origen local le permite cancelar sin perder vuelos.
    """)

with col2:
    st.subheader("⚔️ La Estrategia")
    st.markdown("""
    Para proteger los ingresos, es imperativo abandonar las políticas estáticas e implementar **Políticas de Penalización Dinámicas**:

    * **Segmentación:** Aplicar tarifas no reembolsables estrictas a los perfiles de alto riesgo detectados (ej. Grupos sin coche en ciudad).
    * **Overbooking Inteligente:** Usar la probabilidad de cancelación para vender más habitaciones de las disponibles, sabiendo exactamente cuántas se liberarán.
    * **Incentivos:** Ofrecer flexibilidad solo a clientes con bajo historial de cancelación.
    """)
