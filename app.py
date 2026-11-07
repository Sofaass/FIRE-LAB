
import streamlit as st
import pandas as pd
import plotly.express as px

import plotly.io as pio
import plotly.graph_objects as go

# ======================================
# ЕДИНЫЙ СТИЛЬ ГРАФИКОВ FIRE LAB
# ======================================

fire_lab_template = go.layout.Template(
    layout=go.Layout(
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#FFFFFF",
        font=dict(
            family="Arial, sans-serif",
            color="#142D4E",
            size=13
        ),
        title=dict(
            font=dict(
                size=19,
                color="#142D4E"
            )
        ),
        colorway=[
            "#2374AB",
            "#E98A45",
            "#8CBFCE",
            "#142D4E",
            "#75A99C"
        ],
        xaxis=dict(
            showgrid=False,
            linecolor="#DDE6EF",
            zeroline=False
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor="#E9EEF4",
            zeroline=False
        ),
        margin=dict(
            l=35,
            r=25,
            t=65,
            b=45
        )
    )
)

pio.templates["fire_lab"] = fire_lab_template
pio.templates.default = "fire_lab"


st.set_page_config(
    page_title="FIRE LAB | Спутниковый мониторинг",
    page_icon="🛰️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ======================================
# СВЕТЛОЕ ОФОРМЛЕНИЕ FIRE LAB
# ======================================

st.markdown("""
<style>

/* =====================================
   FIRE LAB — NEBULA THEME
   ===================================== */

/* =====================================
   NEBULA — НЕПОДВИЖНОЕ ЗВЁЗДНОЕ НЕБО
   ===================================== */

html,
body,
.stApp,
[data-testid="stAppViewContainer"] {
    background-color: #101126 !important;
}

/* =====================================
   NEBULA — ЗВЁЗДНОЕ НЕБО
   ===================================== */

.stApp {
    background-color: #101126 !important;

    background-image:
        /* Мягкое космическое свечение */
        radial-gradient(ellipse at 8% 22%,
            rgba(103, 86, 162, 0.18), transparent 38%),
        radial-gradient(ellipse at 92% 78%,
            rgba(74, 65, 145, 0.15), transparent 35%),

        /* Яркие звёзды */
        radial-gradient(2px 2px at 12% 18%, #FFFFFF 95%, transparent),
        radial-gradient(2px 2px at 73% 15%, #FFFFFF 95%, transparent),
        radial-gradient(2px 2px at 43% 76%, #FFFFFF 95%, transparent),
        radial-gradient(2px 2px at 94% 85%, #FFFFFF 95%, transparent),
        radial-gradient(2px 2px at 52% 8%, #FFFFFF 95%, transparent),
        radial-gradient(2px 2px at 8% 64%, #FFFFFF 95%, transparent),
        radial-gradient(2px 2px at 84% 44%, #FFFFFF 95%, transparent),

        /* Лавандовые звёзды */
        radial-gradient(1.5px 1.5px at 28% 42%, #B7A1FF 95%, transparent),
        radial-gradient(1.5px 1.5px at 87% 62%, #B7A1FF 95%, transparent),
        radial-gradient(1.5px 1.5px at 18% 89%, #B7A1FF 95%, transparent),
        radial-gradient(1.5px 1.5px at 61% 37%, #B7A1FF 95%, transparent),
        radial-gradient(1.5px 1.5px at 35% 12%, #B7A1FF 95%, transparent),
        radial-gradient(1.5px 1.5px at 79% 91%, #B7A1FF 95%, transparent),

        /* Маленькие далёкие звёзды */
        radial-gradient(1px 1px at 5% 9%, #D8CEFF 95%, transparent),
        radial-gradient(1px 1px at 17% 31%, #D8CEFF 95%, transparent),
        radial-gradient(1px 1px at 24% 68%, #D8CEFF 95%, transparent),
        radial-gradient(1px 1px at 39% 54%, #D8CEFF 95%, transparent),
        radial-gradient(1px 1px at 46% 23%, #D8CEFF 95%, transparent),
        radial-gradient(1px 1px at 58% 83%, #D8CEFF 95%, transparent),
        radial-gradient(1px 1px at 67% 59%, #D8CEFF 95%, transparent),
        radial-gradient(1px 1px at 76% 28%, #D8CEFF 95%, transparent),
        radial-gradient(1px 1px at 91% 11%, #D8CEFF 95%, transparent),
        radial-gradient(1px 1px at 96% 48%, #D8CEFF 95%, transparent),
        radial-gradient(1px 1px at 11% 96%, #D8CEFF 95%, transparent),
        radial-gradient(1px 1px at 33% 92%, #D8CEFF 95%, transparent);

    background-attachment: fixed !important;
    background-repeat: no-repeat !important;
    background-size: 100% 100% !important;
}

/* Основной контент остаётся прозрачным */
[data-testid="stMain"],
[data-testid="stMainBlockContainer"] {
    background: transparent !important;
}

/* Прозрачные слои поверх звёздного фона */
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
[data-testid="stMainBlockContainer"] {
    background-color: transparent !important;
    background-image: none !important;
}

/* Основные заголовки */
.stApp h1,
.stApp h2,
.stApp h3,
.stApp h4,
.stApp h5,
.stApp h6 {
    color: #F4F0FF !important;
    font-family: Arial, sans-serif;
    font-weight: 700;
}

/* Подчёркивание заголовков */
.stApp h2::after,
.stApp h3::after {
    content: "";
    display: block;
    width: 85px;
    height: 3px;
    margin-top: 9px;
    background: linear-gradient(90deg, #B7A1FF, #7864B8);
    border-radius: 10px;
}

/* Основной текст на тёмном фоне */
.stApp p {
    color: #E5E0F3;
}

/* =====================================
   ВЕРХНЕЕ МЕНЮ
   ===================================== */

/* Неактивные пункты */
.stApp button[data-variant="segmented_control"] {
    background-color: #F4F0FF !important;
    color: #252342 !important;
}

.stApp button[data-variant="segmented_control"] p {
    color: #252342 !important;
}

/* Активный пункт */
.stApp button[data-variant="segmented_control"][aria-checked="true"],
.stApp button[data-variant="segmented_control"][aria-pressed="true"] {
    background-color: #4D467A !important;
}

.stApp button[data-variant="segmented_control"][aria-checked="true"] p,
.stApp button[data-variant="segmented_control"][aria-pressed="true"] p {
    color: #FFFFFF !important;
}

/* =====================================
   КАРТОЧКА АВТОРА
   ===================================== */

.st-key-author_card {
    background-color: #E9E3F8 !important;
    border: 1px solid #D8CDEF !important;
    border-radius: 14px !important;
    padding: 16px !important;
}

.st-key-author_card p,
.st-key-author_card span {
    color: #252342 !important;
}

/* =====================================
   КАРТОЧКИ ПОКАЗАТЕЛЕЙ
   ===================================== */

[data-testid="stMetric"] {
    background-color: #FAF9FF;
    border: 1px solid #DFD7EF;
    border-radius: 14px;
    padding: 22px;
    box-shadow: 0 3px 12px rgba(20, 20, 50, 0.08);
}

.stApp [data-testid="stMetricLabel"] p,
.stApp [data-testid="stMetricLabel"] span {
    color: #514D67 !important;
}

.stApp [data-testid="stMetricValue"],
.stApp [data-testid="stMetricValue"] * {
    color: #6756A2 !important;
    font-weight: 700;
}

/* =====================================
   КНОПКИ
   ===================================== */

.stApp [data-testid="stButton"] button {
    background-color: #E9E3F8 !important;
    border: 1px solid #D5C9EE !important;
    color: #252342 !important;
}

.stApp [data-testid="stButton"] button p,
.stApp [data-testid="stButton"] button span {
    color: #252342 !important;
}

/* =====================================
   ДОПОЛНИТЕЛЬНЫЕ ЭЛЕМЕНТЫ
   ===================================== */

/* Боковая панель */
[data-testid="stSidebar"] {
    background-color: #E9E3F8;
    border-right: 1px solid #D5C9EE;
}

[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] span {
    color: #252342 !important;
}

/* Разделители */
hr {
    border-color: #494367;
}

/* Поля выбора */
div[data-baseweb="select"] > div {
    background-color: #FAF9FF;
    border-color: #D5C9EE;
}
/* =====================================
   NEBULA — СОЗВЕЗДИЯ
   ===================================== */

/* Неподвижный слой с созвездиями */
.stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 0;

    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1200 800'%3E%3Cg fill='none' stroke='%23B7A1FF' stroke-width='1.2' stroke-opacity='.48'%3E%3Cpolyline points='95,145 125,126 157,143 180,174 214,162 245,183 273,169'/%3E%3Cpolyline points='915,125 947,165 981,118 1015,160 1050,119'/%3E%3Cpolyline points='920,540 960,505 1000,530 1040,490 1075,540 1030,590 980,575 920,540'/%3E%3Cpolyline points='960,505 980,575'/%3E%3Cpolyline points='1000,530 1030,590'/%3E%3C/g%3E%3Cg fill='%23F4F0FF'%3E%3Ccircle cx='95' cy='145' r='2.5'/%3E%3Ccircle cx='125' cy='126' r='2'/%3E%3Ccircle cx='157' cy='143' r='2.5'/%3E%3Ccircle cx='180' cy='174' r='2'/%3E%3Ccircle cx='214' cy='162' r='2.5'/%3E%3Ccircle cx='245' cy='183' r='2'/%3E%3Ccircle cx='273' cy='169' r='2.5'/%3E%3Ccircle cx='915' cy='125' r='2'/%3E%3Ccircle cx='947' cy='165' r='2.5'/%3E%3Ccircle cx='981' cy='118' r='2'/%3E%3Ccircle cx='1015' cy='160' r='2.5'/%3E%3Ccircle cx='1050' cy='119' r='2'/%3E%3Ccircle cx='920' cy='540' r='2'/%3E%3Ccircle cx='960' cy='505' r='2.5'/%3E%3Ccircle cx='1000' cy='530' r='2'/%3E%3Ccircle cx='1040' cy='490' r='2.5'/%3E%3Ccircle cx='1075' cy='540' r='2'/%3E%3Ccircle cx='1030' cy='590' r='2.5'/%3E%3Ccircle cx='980' cy='575' r='2'/%3E%3C/g%3E%3C/svg%3E");

    background-size: 100% 100%;
    background-repeat: no-repeat;
    opacity: 0.85;
}

/* Основное содержимое поверх созвездий */
[data-testid="stAppViewContainer"] {
    position: relative;
    z-index: 1;
}
/* =====================================
   NEBULA — МАТЕМАТИЧЕСКАЯ ФОРМУЛА
   ===================================== */

.stApp .st-key-formula_card {
    background-color: #E9E3F8 !important;
    border: 1px solid #C7B8EA !important;
    border-radius: 16px !important;
    padding: 22px !important;
}

.stApp .st-key-formula_card [data-testid="stLatex"] {
    color: #4D467A !important;
}

.stApp .st-key-formula_card .katex,
.stApp .st-key-formula_card .katex * {
    color: #4D467A !important;
}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    fires = pd.read_csv(
        "data/kostanay_fires.csv",
        parse_dates=["acq_date"]
    )
    daily = pd.read_csv(
        "data/daily_weather_fires.csv",
        parse_dates=["time"]
    )
    return fires, daily

fires, daily = load_data()

# ======================================
# ВЕРХНЕЕ МЕНЮ НАВИГАЦИИ
# ======================================

st.markdown(
    """
    <div style="
        text-align: center;
        padding: 10px 0 5px 0;
    ">
        <div style="
            font-size: 26px;
            font-weight: 800;
            color: #F4F0FF;
            letter-spacing: 2px;
        ">
            FIRE LAB
        </div>
        <div style="
            font-size: 11px;
            color: #B7A1FF;
            letter-spacing: 2px;
        ">
            SATELLITE RESEARCH PLATFORM
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

with st.container(key="fire_navigation"):
 page = st.segmented_control(
    "Навигация",
    options=[
        "Главная",
        "Казахстан",
        "Костанайская область",
        "Метеоанализ",
        "Модель ИИ"
    ],
    default="Главная",
    key="navigation",
    label_visibility="collapsed",
    width="stretch"
)

st.divider()

# ======================================
# FIRE LAB — ОБНОВЛЁННЫЙ ДИЗАЙН
# ======================================

st.markdown("""
<style>
    /* Основной фон */
    .stApp {
        background-color: #F5F8FC;
        color: #142D4E;
    }

    /* Центральная часть сайта */
    .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    /* Заголовки */
    h1, h2, h3 {
        color: #142D4E !important;
        letter-spacing: -0.025em;
    }

    h1 {
        font-weight: 750 !important;
    }

    h2, h3 {
        font-weight: 650 !important;
    }

    /* Обычный текст */
    p {
        line-height: 1.7;
    }

    /* Карточки и контейнеры */
    [data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 16px;
    }

    /* Карточки с показателями */
    [data-testid="stMetric"] {
        background-color: #FFFFFF;
        border: 1px solid #E5EBF2;
        border-radius: 16px;
        padding: 18px;
    }

    [data-testid="stMetricValue"] {
        color: #142D4E;
        font-weight: 700;
    }

    [data-testid="stMetricLabel"] {
        color: #64748B;
    }

    /* Боковое меню */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF;
        border-right: 1px solid #E5EBF2;
    }

    /* Кнопки */
    .stButton > button {
        border-radius: 10px;
        font-weight: 600;
        transition: all 0.2s ease;
    }
    /* Основные синие кнопки */
    button[kind="primary"] {
        color: #FFFFFF !important;
        font-weight: 700 !important;
    }

    button[kind="primary"] p {
        color: #FFFFFF !important;
    }

    button[kind="primary"]:hover {
        color: #FFFFFF !important;
    }
    /* Разделительные линии */
    hr {
        border-color: #E5EBF2;
    }

    /* Обложка главной */
    .fire-hero {
        background: linear-gradient(
            125deg,
            #FFFFFF 0%,
            #EDF5FA 100%
        );
        border: 1px solid #E5EBF2;
        border-radius: 24px;
        padding: 42px 38px;
        margin-bottom: 28px;
    }

    .fire-eyebrow {
        color: #2374AB;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 2px;
        margin-bottom: 18px;
    }

    .fire-title {
        color: #142D4E;
        font-size: clamp(34px, 5vw, 56px);
        font-weight: 800;
        line-height: 1.12;
        letter-spacing: -1.5px;
        margin-bottom: 20px;
    }

    .fire-description {
        color: #52657A;
        font-size: 17px;
        line-height: 1.8;
        max-width: 740px;
        margin-bottom: 24px;
    }

    .fire-tag {
        display: inline-block;
        background: #E4F0F7;
        color: #2374AB;
        padding: 8px 14px;
        border-radius: 30px;
        font-size: 12px;
        font-weight: 600;
        margin: 0 8px 8px 0;
    }

    .fire-tag-orange {
        background: #FFF0E4;
        color: #B65F25;
    }
 /* =====================================
   NEBULA — УНИВЕРСАЛЬНЫЕ КАРТОЧКИ
   ===================================== */

/* Основные карточки — почти белые */
.stApp [class*="st-key-main_card_"] {
    background-color: #FAF9FF !important;
    border: 1px solid #DDD5F0 !important;
    border-radius: 16px !important;
    padding: 20px !important;
}

/* Дополнительные карточки — лавандовые */
.stApp [class*="st-key-secondary_card_"] {
    background-color: #E9E3F8 !important;
    border: 1px solid #D8CDEF !important;
    border-radius: 16px !important;
    padding: 20px !important;
}

/* Текст внутри обоих типов карточек */
.stApp [class*="st-key-main_card_"] p,
.stApp [class*="st-key-main_card_"] span,
.stApp [class*="st-key-secondary_card_"] p,
.stApp [class*="st-key-secondary_card_"] span {
    color: #252342 !important;
}

/* Заголовки внутри карточек */
.stApp [class*="st-key-main_card_"] h1,
.stApp [class*="st-key-main_card_"] h2,
.stApp [class*="st-key-main_card_"] h3,
.stApp [class*="st-key-main_card_"] h4,
.stApp [class*="st-key-secondary_card_"] h1,
.stApp [class*="st-key-secondary_card_"] h2,
.stApp [class*="st-key-secondary_card_"] h3,
.stApp [class*="st-key-secondary_card_"] h4 {
    color: #252342 !important;
}   
</style>
""", unsafe_allow_html=True)
# ======================================
# ПЛАВАЮЩАЯ КНОПКА «НАВЕРХ»
# ======================================

st.html("""
<style>
#fire-scroll-top {
    position: fixed;
    bottom: 28px;
    right: 28px;
    z-index: 999999;
    width: 46px;
    height: 46px;
    border-radius: 14px;
    background: #FFFFFF;
    border: 1px solid #DCE6F0;
    color: #2374AB;
    font-size: 24px;
    cursor: pointer;
    box-shadow: 0 4px 16px rgba(20, 45, 78, 0.10);
}

#fire-scroll-top:hover {
    background: #E4F0F7;
}
/* =====================================
   NEBULA — КАРТОЧКИ НА ВСЕХ СТРАНИЦАХ
   ===================================== */

/* Все обычные карточки с рамкой */
.stApp [data-testid="stVerticalBlockBorderWrapper"] {
    background-color: #E9E3F8 !important;
    border-radius: 16px !important;
}

/* Текст внутри обычных карточек */
.stApp [data-testid="stVerticalBlockBorderWrapper"] p,
.stApp [data-testid="stVerticalBlockBorderWrapper"] span {
    color: #252342 !important;
}

/* Заголовки внутри карточек */
.stApp [data-testid="stVerticalBlockBorderWrapper"] h1,
.stApp [data-testid="stVerticalBlockBorderWrapper"] h2,
.stApp [data-testid="stVerticalBlockBorderWrapper"] h3,
.stApp [data-testid="stVerticalBlockBorderWrapper"] h4 {
    color: #252342 !important;
}

/* Показатели на всех страницах */
.stApp [data-testid="stMetric"] {
    background-color: #FAF9FF !important;
    border: 1px solid #DDD5F0 !important;
    border-radius: 16px !important;
    padding: 22px !important;
}

/* Текст показателей */
.stApp [data-testid="stMetricLabel"] p,
.stApp [data-testid="stMetricLabel"] span {
    color: #514D67 !important;
}

/* Значения показателей */
.stApp [data-testid="stMetricValue"],
.stApp [data-testid="stMetricValue"] * {
    color: #6756A2 !important;
}
/* =====================================
   NEBULA — ТАБЛИЦЫ ДАННЫХ
   ===================================== */

/* Внешний контейнер таблицы */
.stApp [data-testid="stDataFrame"] {
    background-color: #FAF9FF !important;
    border: 1px solid #DDD5F0 !important;
    border-radius: 14px !important;
    overflow: hidden;
}

/* Панель инструментов таблицы */
.stApp [data-testid="stDataFrame"] [data-testid="stElementToolbar"] {
    background-color: #FAF9FF !important;
    border-radius: 10px;
}

/* Рамка таблицы */
.stApp [data-testid="stDataFrame"] canvas {
    border-radius: 10px;
}
/* =====================================
   NEBULA — ИНФОРМАЦИОННЫЕ СООБЩЕНИЯ
   ===================================== */

/* Общий стиль сообщений */
.stApp [data-testid="stAlert"] {
    border-radius: 14px !important;
    padding: 16px !important;
    border-width: 1px !important;
    border-style: solid !important;
}

/* =====================================
   NEBULA — ИНФОРМАЦИОННЫЕ СООБЩЕНИЯ
   ===================================== */

/* Общий стиль */
.stApp [data-testid="stAlert"] {
    border-radius: 14px !important;
    padding: 16px !important;
    background-color: #E9E3F8 !important;
    border: 1px solid #C7B8EA !important;
}

/* Внутренний фон уведомлений */
.stApp [data-testid="stAlert"] > div {
    background-color: transparent !important;
}

/* Текст сообщений */
.stApp [data-testid="stAlert"] p,
.stApp [data-testid="stAlert"] span {
    color: #252342 !important;
}

/* Иконки */
.stApp [data-testid="stAlert"] svg {
    color: #6756A2 !important;
}
</style>

<button id="fire-scroll-top" type="button" aria-label="Наверх">↑</button>

<script>
(function () {
    const button = document.getElementById("fire-scroll-top");
    if (!button) return;

    button.addEventListener("click", function () {
        const main = document.querySelector('[data-testid="stMain"]');

        if (main) {
            main.scrollTo({ top: 0, behavior: "smooth" });
        }

        window.scrollTo({ top: 0, behavior: "smooth" });
    });
})();
</script>
""", unsafe_allow_javascript=True)
if page == "Главная":
    
    
    import textwrap

    st.markdown(
        textwrap.dedent("""
        <div class="fire-hero">
        <div class="fire-eyebrow">
        SATELLITE FIRE RESEARCH / 2025
        </div>

        <div class="fire-title">
        FIRE LAB
        </div>

        <div class="fire-description">
        Интерактивная платформа для исследования
        тепловых аномалий Казахстана на основе
        спутниковых данных NASA FIRMS,
        метеорологического анализа и
        машинного обучения.
        </div>

        <span class="fire-tag">ИЮНЬ — АВГУСТ 2025</span>
        <span class="fire-tag">NOAA-21 / VIIRS</span>
        <span class="fire-tag fire-tag-orange">КАЗАХСТАН</span>
        </div>
        """),
        unsafe_allow_html=True
    )
    # ======================================
    # ОБ АВТОРЕ
    # ======================================

    st.markdown("### Об авторе")

    with st.container(border=True, key="author_card"):

        st.markdown("**София Сычева**")

        st.caption(
            "Ученица 10 класса | Автор исследовательского проекта"
        )

        st.write(
            "Исследовательский проект в области физики, "
            "спутникового мониторинга и анализа данных."
        )

        st.write(
            "FIRE LAB создан для изучения тепловых аномалий "
            "на территории Казахстана и исследования "
            "связи метеорологических условий с их "
            "спутниковым обнаружением. "
            "В проекте объединены обработка данных, "
            "программирование, визуализация "
            "и экспериментальное машинное обучение."
        )

        st.divider()

    #st.title("Спутниковый мониторинг тепловых аномалий")

   

    #st.caption("Костанайская область | Июнь — август 2025")


    # ======================================
    # О ПРОЕКТЕ
    # ======================================

    st.divider()
    st.subheader("О проекте")

    st.write(
        "FIRE LAB — исследовательская платформа для "
        "анализа спутниковых обнаружений тепловых аномалий "
        "на территории Казахстана. Проект объединяет "
        "спутниковые наблюдения, метеорологические данные "
        "и методы машинного обучения."
    )

    col_left, col_right = st.columns(2)

    with col_left:
        st.markdown("#### Цель исследования")
        st.write(
            "Изучить связь метеорологических условий "
            "со спутниковыми обнаружениями тепловых "
            "аномалий и исследовать возможности "
            "применения машинного обучения "
            "для анализа этих данных."
        )

    with col_right:
        st.markdown("#### Используемые технологии")
        st.write(
            "NASA FIRMS — спутниковые наблюдения VIIRS."
        )
        st.write(
            "Open-Meteo — исторические метеоданные."
        )
        st.write(
            "Python — обработка данных и машинное обучение."
        )
        st.write(
            "Streamlit и Plotly — интерактивная визуализация."
        )

    st.divider()

    st.subheader("Структура исследования")

    st.markdown("""
    **01 — Казахстан**  
    Сравнение спутниковых обнаружений по регионам страны.

    **02 — Костанайская область**  
    Интерактивная карта, распределение и динамика обнаружений.

    **03 — Метеоанализ**  
    Исследование связи погодных условий со спутниковыми данными.

    **04 — Модель ИИ**  
    Демонстрация экспериментальной модели машинного обучения.
    """)

    st.caption(
        "Период исследования: 01.06.2025–31.08.2025. "
        "Спутниковые обнаружения не обязательно "
        "соответствуют подтверждённым пожарам."
    )



    # ======================================
    # МЕТОДИКА ИССЛЕДОВАНИЯ
    # ======================================

    st.divider()
    st.subheader("Методика исследования")

    st.write(
        "Исследование проводилось в четыре этапа: "
        "от получения исходных данных до разработки "
        "и проверки модели машинного обучения."
    )

    stages = [
        (
            "01",
            "Сбор данных",
            "Получены спутниковые обнаружения тепловых "
            "аномалий NASA FIRMS (NOAA-21, VIIRS 375 м) "
            "за июнь–август 2025 года. "
            "Для метеоанализа использованы исторические "
            "данные Open-Meteo."
        ),
        (
            "02",
            "Обработка данных",
            "С помощью Python и pandas изучены "
            "15 409 спутниковых обнаружений. "
            "По полигональным границам регионов "
            "выделены наблюдения Костанайской области "
            "и сформированы таблицы для анализа."
        ),
        (
            "03",
            "Метеорологический анализ",
            "Исследована статистическая связь числа "
            "обнаружений с температурой, осадками, "
            "ветром и солнечной радиацией. "
            "Для оценки связи использован "
            "коэффициент корреляции Спирмена."
        ),
        (
            "04",
            "Машинное обучение",
            "Разработана экспериментальная модель "
            "линейной регрессии. Её результаты "
            "сравнивались с базовым прогнозом "
            "на последовательных временных выборках."
        )
    ]

    for i in range(0, len(stages), 2):
        col_left, col_right = st.columns(2)

        for col, (number, heading, description) in zip(
            [col_left, col_right],
            stages[i:i + 2]
        ):
            with col:
                with st.container(border=True, key=f"secondary_card_method_{number}"):
                    st.markdown(f"### {number}")
                    st.markdown(f"**{heading}**")
                    st.write(description)

    st.caption(
        "Важно: спутниковые тепловые аномалии "
        "не обязательно соответствуют отдельным "
        "подтверждённым природным пожарам. "
        "Метеоданные одной точки не описывают "
        "все погодные условия Костанайской области."
    )
    st.divider()

    col1, col2, col3 = st.columns(3)

    col1.metric("Обнаружения в Костанайской области", f"{len(fires):,}")
    col2.metric("Дней наблюдений", len(daily))
    col3.metric("Сумма значений FRP", f"{fires['frp'].sum():,.1f} МВт")
    st.caption(
        "Показатели относятся к Костанайской области. "
        "FRP характеризует мощность теплового излучения "
        "в момент спутникового наблюдения. "
        "Сумма значений FRP не является суммарной энергией пожаров."
    )
    st.subheader("Обнаружения по месяцам — Костанайская область")

    monthly = (
        fires.groupby(fires["acq_date"].dt.month)
        .size()
        .reset_index(name="Обнаружения")
    )

    monthly["Месяц"] = monthly["acq_date"].map({
        6: "Июнь",
        7: "Июль",
        8: "Август"
    })

    fig = px.bar(
        monthly,
        x="Месяц",
        y="Обнаружения",
        color="Месяц",
        text="Обнаружения",
        color_discrete_sequence=[
            "#69C4D8", "#E5A45C", "#D96C5F"
        ]
    )

   
    fig.update_layout(
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#FFFFFF",
        font_color="#19354F"
    )

    st.plotly_chart(fig, use_container_width=True, key="fire_lab_chart_386")

    st.info(
        "Спутниковые обнаружения тепловых аномалий "
        "не равны количеству отдельных подтверждённых пожаров."
    )




    # ======================================
    # КЛЮЧЕВЫЕ РЕЗУЛЬТАТЫ ИССЛЕДОВАНИЯ
    # ======================================

    st.divider()
    st.subheader("Ключевые результаты исследования")

    st.write(
        "В ходе исследования проанализированы "
        "спутниковые наблюдения тепловых аномалий "
        "на территории Казахстана за лето 2025 года. "
        "Ниже представлены основные результаты."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Обнаружений по Казахстану",
            "15 409"
        )

    with col2:
        st.metric(
            "Костанайская область",
            f"{len(fires):,}".replace(",", " ")
        )

    with col3:
        st.metric(
            "Дней исследования",
            len(daily)
        )

    st.markdown("#### Основные выводы")

    with st.container(border=True):
        st.markdown("**01 — Пространственное распределение**")
        st.write(
            "Спутниковые обнаружения распределены "
            "по регионам Казахстана неравномерно. "
            "Наибольшее количество в исследуемом "
            "наборе данных зарегистрировано "
            "в Актюбинской области."
        )

    with st.container(border=True):
        st.markdown("**02 — Костанайская область**")
        st.write(
            "За исследуемый период выделено "
            "1 690 спутниковых обнаружений. "
            "Наибольшее их количество пришлось "
            "на июнь — 1 147, а наименьшее "
            "на июль — 98."
        )

    with st.container(border=True):
        st.markdown("**03 — Метеорологические условия**")
        st.write(
            "Наиболее выраженная положительная "
            "корреляция Спирмена обнаружена "
            "для солнечной радиации (0,588). "
            "Для осадков получена отрицательная "
            "корреляция (около -0,300). "
            "Эти связи не доказывают "
            "причинно-следственную зависимость."
        )

    with st.container(border=True):
        st.markdown("**04 — Машинное обучение**")
        st.write(
            "Разработана экспериментальная модель "
            "линейной регрессии. При проверке "
            "на трёх временных периодах она "
            "уступила простому базовому методу. "
            "Это показало необходимость дальнейшего "
            "совершенствования модели."
        )

    st.info(
        "Главный результат исследования: "
        "создана интерактивная платформа FIRE LAB, "
        "объединяющая спутниковые данные, "
        "метеорологический анализ и экспериментальную "
        "модель машинного обучения."
    )

    st.caption(
        "Все выводы относятся к исследуемому "
        "набору данных за июнь–август 2025 года. "
        "Спутниковые обнаружения тепловых аномалий "
        "не равны числу подтверждённых пожаров."
    )


    # ======================================
    # КАК ПОЛЬЗОВАТЬСЯ FIRE LAB
    # ======================================

    st.divider()
    st.subheader("Как пользоваться FIRE LAB")

    st.write(
        "Платформа состоит из нескольких разделов. "
        "Выберите интересующее направление в верхнем меню "
        "или воспользуйтесь кнопками на карточках ниже."
    )

    col1, col2 = st.columns(2)

    with col1:
        # КАРТОЧКА 01 — КАЗАХСТАН
        with st.container(border=True):
            st.markdown("**01 / Казахстан**")
            st.write(
                "Интерактивная карта тепловых аномалий, "
                "сравнение регионов и общая статистика "
                "спутниковых обнаружений."
            )

            st.button(
                "Открыть Казахстан",
                key="open_kazakhstan",
                on_click=lambda: st.session_state.update(
                    navigation="Казахстан"
                )
            )

        # КАРТОЧКА 03 — МЕТЕОАНАЛИЗ
        with st.container(border=True):
            st.markdown("**03 / Метеоанализ**")
            st.write(
                "Исследование связи температуры, осадков, "
                "ветра и солнечной радиации с количеством "
                "спутниковых обнаружений."
            )

            st.button(
                "Открыть метеоанализ",
                key="open_meteo",
                on_click=lambda: st.session_state.update(
                    navigation="Метеоанализ"
                )
            )

    with col2:
        # КАРТОЧКА 02 — КОСТАНАЙСКАЯ ОБЛАСТЬ
        with st.container(border=True):
            st.markdown("**02 / Костанайская область**")
            st.write(
                "Подробная карта региона, сезонная динамика "
                "тепловых аномалий и показатели FRP."
            )

            st.button(
                "Открыть Костанайскую область",
                key="open_kostanay",
                on_click=lambda: st.session_state.update(
                    navigation="Костанайская область"
                )
            )

        # КАРТОЧКА 04 — МОДЕЛЬ ИИ
        with st.container(border=True):
            st.markdown("**04 / Модель ИИ**")
            st.write(
                "Экспериментальная модель машинного обучения. "
                "Можно изменять входные параметры и сравнивать "
                "результат с базовым прогнозом."
            )

            st.button(
                "Открыть модель ИИ",
                key="open_ai",
                on_click=lambda: st.session_state.update(
                    navigation="Модель ИИ"
                )
            )

    st.caption(
        "Для перехода между разделами используйте "
        "верхнее меню или кнопки на карточках."
    )
elif page == "Казахстан":

    st.title("Спутниковый мониторинг Казахстана")

    st.write(
        "Распределение тепловых аномалий, обнаруженных "
        "спутником NOAA-21 (VIIRS) на территории "
        "Казахстана с июня по август 2025 года."
    )

    @st.cache_data
    def load_kazakhstan():
        return pd.read_csv(
            "data/fire_nrt_J2V-C2_810147.csv",
            parse_dates=["acq_date"]
        )

    kz_fires = load_kazakhstan()

    st.divider()

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Спутниковые обнаружения",
        f"{len(kz_fires):,}"
    )

    col2.metric("Период исследования", "92 дня")

    col3.metric(
        "Сумма значений FRP",
        f"{kz_fires['frp'].sum():,.1f} МВт"
    )
    st.caption(
        "FRP (Fire Radiative Power) — мощность теплового "
        "излучения, зарегистрированная спутником при "
        "обнаружении тепловой аномалии. Сумма значений "
        "FRP объединяет отдельные спутниковые измерения "
        "и не является общей энергией пожаров за период."
    )

    st.subheader("Карта тепловых аномалий")

    months_kz = {
        "Все месяцы": 0,
        "Июнь": 6,
        "Июль": 7,
        "Август": 8
    }

    selected_kz = st.selectbox(
        "Выберите месяц",
        list(months_kz.keys()),
        key="kz_month"
    )

    if months_kz[selected_kz] == 0:
        filtered_kz = kz_fires.copy()
    else:
        filtered_kz = kz_fires[
            kz_fires["acq_date"].dt.month ==
            months_kz[selected_kz]
        ].copy()

    st.metric(
        "Обнаружений за выбранный период",
        len(filtered_kz)
    )

    fig_kz = px.scatter_map(
        filtered_kz,
        lat="latitude",
        lon="longitude",
        color="frp",
        size="frp",
        size_max=12,
        hover_data={
            "latitude": ":.4f",
            "longitude": ":.4f",
            "acq_date": "|%d.%m.%Y",
            "brightness": ":.1f",
            "confidence": True,
            "frp": ":.2f"
        },
        labels={
            "latitude": "Широта",
            "longitude": "Долгота",
            "acq_date": "Дата обнаружения",
            "brightness": "Яркостная температура, K",
            "confidence": "Уверенность",
            "frp": "FRP, МВт"
        },
        color_continuous_scale="YlOrRd",
        height=650
    )

    fig_kz.update_layout(
        map_style="open-street-map",
        map_center={"lat": 48.0, "lon": 67.0},
        map_zoom=3.7,
        margin=dict(l=0, r=0, t=0, b=0)
    )

    st.plotly_chart(fig_kz, width="stretch")

    st.caption(
        "Каждая точка — спутниковое обнаружение "
        "тепловой аномалии, а не обязательно "
        "отдельный подтверждённый пожар. "
        "Цвет и размер отражают FRP."
    )



    # ======================================
    # СРАВНЕНИЕ РЕГИОНОВ КАЗАХСТАНА
    # ======================================

    st.divider()
    st.subheader("Сравнение регионов Казахстана")

    st.write(
        "Спутниковые обнаружения распределены "
        "по административным регионам Казахстана "
        "на основании географических координат "
        "и полигональных границ областей."
    )

    import json
    from shapely.geometry import shape, Point
    from shapely.prepared import prep

    @st.cache_data
    def calculate_regions():

        with open(
            "data/kz_1.json",
            "r",
            encoding="utf-8"
        ) as file:
            geojson = json.load(file)

        # Подготавливаем полигоны регионов
        regions = []

        for feature in geojson["features"]:
            region_name = feature["properties"]["NAME_1"]
            polygon = prep(shape(feature["geometry"]))

            regions.append((region_name, polygon))

        # Копируем спутниковые данные
        result = kz_fires.copy()

        region_names = []

        # Определяем регион каждой точки
        for _, row in result.iterrows():

            point = Point(
                row["longitude"],
                row["latitude"]
            )

            found_region = None

            for region_name, polygon in regions:
                if polygon.covers(point):
                    found_region = region_name
                    break

            region_names.append(found_region)

        result["region"] = region_names

        # Статистика по регионам
        summary = (
            result.dropna(subset=["region"])
            .groupby("region")
            .agg(
                observations=("frp", "size"),
                total_frp=("frp", "sum"),
                high_confidence=(
                    "confidence",
                    lambda x: (x == "h").sum()
                )
            )
            .reset_index()
        )

        summary["share_percent"] = (
            summary["observations"]
            / len(result)
            * 100
        )

        summary = summary.sort_values(
            "observations",
            ascending=False
        )

        return result, summary

    with st.spinner(
        "Распределяем спутниковые обнаружения по регионам..."
    ):
        regional_fires, regional_summary = calculate_regions()
            # --------------------------------------
    # РУССКИЕ НАЗВАНИЯ РЕГИОНОВ
    # --------------------------------------

    region_translation = {
        "Aqtöbe": "Актюбинская область",
        "Qaraghandy": "Карагандинская область",
        "Pavlodar": "Павлодарская область",
        "Qostanay": "Костанайская область",
        "East Kazakhstan": "Восточно-Казахстанская область",
        "Almaty": "Алматинская область",
        "Atyrau": "Атырауская область",
        "Aqmola": "Акмолинская область",
        "Qyzylorda": "Кызылординская область",
        "West Kazakhstan": "Западно-Казахстанская область",
        "Zhambyl": "Жамбылская область",
        "South Kazakhstan": "Южно-Казахстанская область",
        "North Kazakhstan": "Северо-Казахстанская область",
        "Mangghystau": "Мангистауская область"
    }

    regional_summary_display = regional_summary.copy()

    regional_summary_display["region"] = (
        regional_summary_display["region"]
        .replace(region_translation)
    )

    # --------------------------------------
    # ДИАГРАММА
    # --------------------------------------

    fig_regions = px.bar(
        regional_summary_display,
        x="observations",
        y="region",
        orientation="h",
        color="observations",
        color_continuous_scale="Blues",
        labels={
            "observations": "Количество обнаружений",
            "region": "Регион"
        },
        title="Распределение спутниковых обнаружений"
    )

    fig_regions.update_layout(
        yaxis={
            "categoryorder": "total ascending",
            "gridcolor": "#E9E3F8",
            "zeroline": False
        },
        xaxis={
            "gridcolor": "#E9E3F8",
            "zeroline": False
        },
        height=650,
        paper_bgcolor="#FAF9FF",
        plot_bgcolor="#FAF9FF",
        font=dict(
            family="Arial",
            size=13,
            color="#252342"
        ),
        title_font=dict(
            size=19,
            color="#4D467A"
        ),
        coloraxis_showscale=False,
        margin=dict(l=15, r=25, t=70, b=35)
    )

    st.plotly_chart(
        fig_regions,
        width="stretch"
    )

    # --------------------------------------
    # ТАБЛИЦА
    # --------------------------------------

    st.subheader("Статистика по регионам")

    table_regions = regional_summary_display.rename(
        columns={
            "region": "Регион",
            "observations": "Обнаружения",
            "total_frp": "Сумма FRP, МВт",
            "high_confidence": "Высокая уверенность",
            "share_percent": "Доля, %"
        }
    )

    st.dataframe(
        table_regions,
        hide_index=True,
        width="stretch",
        column_config={
            "Сумма FRP, МВт":
                st.column_config.NumberColumn(format="%.2f"),
            "Доля, %":
                st.column_config.NumberColumn(format="%.2f")
        }
    )

    # --------------------------------------
    # КОСТАНАЙСКАЯ ОБЛАСТЬ
    # --------------------------------------

    kostanay_row = regional_summary[
        regional_summary["region"]
        .str.contains("ostanay", case=False, na=False)
    ]

    if not kostanay_row.empty:

        row = kostanay_row.iloc[0]

        rank = (
            regional_summary.reset_index(drop=True)
            .index[
                regional_summary.reset_index(drop=True)[
                    "region"
                ] == row["region"]
            ][0] + 1
        )

        st.info(
            f"Костанайская область занимает "
            f"{rank}-е место среди регионов "
            f"по количеству обнаружений: "
            f"{int(row['observations'])} "
            f"({row['share_percent']:.2f}% "
            f"от всех обнаружений Казахстана)."
        )

    unassigned = regional_fires["region"].isna().sum()

    st.caption(
        f"Точек, не отнесённых к регионам: {unassigned}. "
        "Доля рассчитана от общего количества "
        "спутниковых обнаружений в исходном файле NASA."
    )


    # ======================================
    # НАУЧНЫЕ РЕЗУЛЬТАТЫ ПО КАЗАХСТАНУ
    # ======================================

    st.divider()
    st.subheader("Научные результаты и выводы")

    st.write(
        "Анализ спутниковых данных NASA FIRMS "
        "позволил изучить пространственное распределение "
        "тепловых аномалий на территории Казахстана "
        "за июнь–август 2025 года."
    )

    # Основные показатели
    assigned_count = regional_fires["region"].notna().sum()

    top_region = regional_summary.iloc[0]

    col_a, col_b, col_c = st.columns(3)

    col_a.metric(
        "Всего обнаружений",
        f"{len(kz_fires):,}"
    )

    col_b.metric(
        "Отнесено к регионам",
        f"{assigned_count:,}"
    )

    col_c.metric(
        "Регионов с обнаружениями",
        len(regional_summary)
    )

    st.markdown("#### Основные наблюдения")

    st.write(
        f"Наибольшее количество спутниковых обнаружений "
        f"зарегистрировано в регионе {top_region['region']}: "
        f"{int(top_region['observations'])} "
        f"({top_region['share_percent']:.2f}% "
        f"от общего количества обнаружений)."
    )

    qostanay_data = regional_summary[
        regional_summary["region"].str.contains(
            "ostanay", case=False, na=False
        )
    ]

    if not qostanay_data.empty:
        qostanay = qostanay_data.iloc[0]

        st.write(
            f"В Костанайской области выделено "
            f"{int(qostanay['observations'])} "
            f"спутниковых обнаружений, что составляет "
            f"{qostanay['share_percent']:.2f}% "
            f"от общего числа наблюдений по Казахстану."
        )

    st.markdown("#### Научная интерпретация")

    st.write(
        "Распределение спутниковых обнаружений "
        "по регионам неоднородно. Это может быть связано "
        "с различиями природных условий, погодных факторов, "
        "землепользования и интенсивности возникновения "
        "источников теплового излучения."
    )

    st.write(
        "Однако количество обнаружений не является "
        "прямым показателем числа отдельных пожаров "
        "или площади выгоревшей территории. "
        "Один пожар может фиксироваться спутником "
        "несколько раз."
    )

    st.info(
        "Вывод: спутниковые данные VIIRS позволяют "
        "сравнивать пространственное распределение "
        "зарегистрированных тепловых аномалий "
        "и выделять регионы для дальнейшего анализа. "
        "Для оценки реального масштаба пожаров "
        "необходимы дополнительные данные."
    )

    st.caption(
        "Распределение выполнено по полигональным "
        "границам 17 регионов из используемого GeoJSON. "
        "Точки вне этих границ учитываются в общем "
        "количестве обнаружений, но не входят "
        "в региональную статистику."
    )

elif page == "Костанайская область":
    st.title("Костанайская область")
    st.write(
        "Анализ спутниковых обнаружений тепловых аномалий "
        "на территории Костанайской области за июнь–август "
        "2025 года по данным NOAA-21 (VIIRS). "
        "Раздел позволяет изучить пространственное распределение "
        "обнаружений и их изменение во времени."
    )
    months = {
        "Все месяцы": 0,
        "Июнь": 6,
        "Июль": 7,
        "Август": 8
    }

    selected = st.selectbox(
        "Выберите месяц",
        list(months.keys())
    )

    if months[selected] == 0:
        filtered = fires.copy()
    else:
        filtered = fires[
            fires["acq_date"].dt.month == months[selected]
        ].copy()

    st.metric("Обнаружения", len(filtered))

    fig_map = px.scatter_map(
        filtered,
        lat="latitude",
        lon="longitude",
        color="frp",
        size="frp",
        size_max=16,
        hover_data={
            "latitude": ":.4f",
            "longitude": ":.4f",
            "acq_date": "|%d.%m.%Y",
            "brightness": ":.1f",
            "confidence": True,
            "frp": ":.2f"
        },
        labels={
            "latitude": "Широта",
            "longitude": "Долгота",
            "acq_date": "Дата обнаружения",
            "brightness": "Яркостная температура, K",
            "confidence": "Уверенность",
            "frp": "FRP, МВт"
        },
        color_continuous_scale="YlOrRd",
        height=600
    )
    fig_map.update_layout(
        map_style="open-street-map",
        map_center={"lat": 51.5, "lon": 64.0},
        map_zoom=5.5,
        margin=dict(l=0, r=0, t=0, b=0)
    )

    st.plotly_chart(fig_map, use_container_width=True)

    st.subheader("Динамика обнаружений")

    fig_daily = px.line(
        daily,
        x="time",
        y="detections",
        markers=True,
        labels={
            "time": "Дата",
            "detections": "Количество обнаружений"
        }
    )

    fig_daily.update_traces(
        line_color="#9275D2",
        line_width=3,
        marker=dict(
            color="#9275D2",
            size=6
        )
    )

    fig_daily.update_layout(
        paper_bgcolor="#FAF9FF",
        plot_bgcolor="#FAF9FF",
        font=dict(
            family="Arial",
            size=13,
            color="#252342"
        ),
        xaxis=dict(
            gridcolor="#E9E3F8",
            zeroline=False
        ),
        yaxis=dict(
            gridcolor="#E9E3F8",
            zeroline=False
        ),
        margin=dict(l=35, r=25, t=40, b=40)
    )

    st.plotly_chart(fig_daily, use_container_width=True)


    # ======================================
    # НАУЧНЫЕ РЕЗУЛЬТАТЫ КОСТАНАЙСКОЙ ОБЛАСТИ
    # ======================================

    st.divider()
    st.subheader("Научные результаты и выводы")

    st.write(
        "Для Костанайской области проанализированы "
        "спутниковые обнаружения тепловых аномалий "
        "за июнь–август 2025 года."
    )

    # Статистика по месяцам
    monthly_results = (
        fires.groupby(fires["acq_date"].dt.month)
        .agg(
            observations=("frp", "size"),
            total_frp=("frp", "sum"),
            mean_frp=("frp", "mean")
        )
        .reset_index()
    )

    month_names = {
        6: "Июнь",
        7: "Июль",
        8: "Август"
    }

    monthly_results["Месяц"] = (
        monthly_results["acq_date"].map(month_names)
    )

    monthly_results = monthly_results.rename(
        columns={
            "observations": "Обнаружения",
            "total_frp": "Сумма FRP, МВт",
            "mean_frp": "Средняя FRP, МВт"
        }
    )

    st.markdown("#### Сезонное распределение")

    fig_monthly = px.bar(
        monthly_results,
        x="Месяц",
        y="Обнаружения",
        text="Обнаружения",
        color="Месяц",
        color_discrete_sequence=[
            "#9275D2",
            "#6E9BCB",
            "#E6A15B"
        ],
        title="Количество обнаружений по месяцам"
    )

    fig_monthly.update_layout(
        paper_bgcolor="#FAF9FF",
        plot_bgcolor="#FAF9FF",
        font=dict(
            family="Arial",
            size=13,
            color="#252342"
        ),
        title_font=dict(
            size=19,
            color="#4D467A"
        ),
        xaxis=dict(
            showgrid=False,
            zeroline=False
        ),
        yaxis=dict(
            gridcolor="#E9E3F8",
            zeroline=False
        ),
        showlegend=False,
        margin=dict(l=35, r=25, t=70, b=40)
    )

    st.plotly_chart(
        fig_monthly,
        width="stretch"
    )

    st.markdown("#### Показатели теплового излучения")

    st.dataframe(
        monthly_results[
            [
                "Месяц",
                "Обнаружения",
                "Средняя FRP, МВт",
                "Сумма FRP, МВт"
            ]
        ],
        hide_index=True,
        width="stretch",
        column_config={
            "Средняя FRP, МВт":
                st.column_config.NumberColumn(format="%.2f"),
            "Сумма FRP, МВт":
                st.column_config.NumberColumn(format="%.2f")
        }
    )

    st.caption(
        "FRP (Fire Radiative Power) — оценка "
        "мгновенной мощности теплового излучения "
        "источника, выраженная в мегаваттах. "
        "Сумма FRP по обнаружениям не равна "
        "общей энергии пожаров."
    )

    st.markdown("#### Основные выводы")

    st.write(
        "Наибольшее число спутниковых обнаружений "
        "пришлось на июнь — 1 147. "
        "В июле зарегистрировано 98 обнаружений, "
        "в августе — 445."
    )

    st.write(
        "По рассчитанным показателям средняя FRP "
        "в июне была выше, чем в июле и августе. "
        "Это указывает на различия в мощности "
        "зарегистрированных источников теплового "
        "излучения в рассматриваемые месяцы."
    )
    st.info(
        "Пик спутниковых обнаружений зафиксирован "
        "31 августа 2025 года — 425 наблюдений. "
        "Это составляет около 95,5% всех обнаружений "
        "за август. Показатель отражает количество "
        "спутниковых регистраций тепловых аномалий, "
        "а не число отдельных подтверждённых пожаров."
    )
    st.info(
        "Вывод: спутниковые данные выявили "
        "выраженную неравномерность обнаружений "
        "тепловых аномалий по месяцам. "
        "Для объяснения причин различий необходимо "
        "учитывать метеорологические условия, "
        "особенности спутниковых наблюдений "
        "и характеристики территории."
    )

elif page == "Метеоанализ":

    st.title("Метеорологический анализ")

    st.write(
        "Исследование статистической связи между "
        "погодными условиями и количеством спутниковых "
        "обнаружений тепловых аномалий VIIRS."
    )

    st.caption(
        "Костанайская область | 1 июня — 31 августа 2025 года"
    )

    st.divider()

    # --------------------------------------
    # НАСТРОЙКИ ПОКАЗАТЕЛЕЙ
    # --------------------------------------

    weather_columns = {
        "Средняя температура воздуха":
            "temperature_2m_mean (°C)",
        "Сумма осадков":
            "precipitation_sum (mm)",
        "Максимальная скорость ветра":
            "wind_speed_10m_max (km/h)",
        "Солнечная радиация":
            "shortwave_radiation_sum (MJ/m²)"
    }

    units = {
        "Средняя температура воздуха": "°C",
        "Сумма осадков": "мм",
        "Максимальная скорость ветра": "км/ч",
        "Солнечная радиация": "МДж/м²"
    }

    # --------------------------------------
    # ОБЩИЕ ПОКАЗАТЕЛИ
    # --------------------------------------

    col1, col2, col3 = st.columns(3)

    col1.metric("Дней наблюдений", len(daily))

    col2.metric(
        "Средняя температура",
        f"{daily['temperature_2m_mean (°C)'].mean():.1f} °C"
    )

    col3.metric(
        "Сумма осадков за период",
        f"{daily['precipitation_sum (mm)'].sum():.1f} мм"
    )

    st.divider()

    # --------------------------------------
    # ВЫБОР МЕТЕОПОКАЗАТЕЛЯ
    # --------------------------------------

    st.subheader("Динамика метеорологических условий")

    selected_weather = st.selectbox(
        "Выберите показатель для анализа:",
        list(weather_columns.keys())
    )

    selected_column = weather_columns[selected_weather]
    # Цвета метеопоказателей в стиле Nebula
    weather_colors = {
        "Средняя температура воздуха": "#E77C65",
        "Сумма осадков": "#4B9BCB",
        "Максимальная скорость ветра": "#9275D2",
        "Солнечная радиация": "#D9A441"
    }

    selected_color = weather_colors[selected_weather]
    # График изменения погодного показателя
    fig_weather = px.line(
        daily,
        x="time",
        y=selected_column,
        markers=True,
        labels={
            "time": "Дата",
            selected_column:
                f"{selected_weather}, {units[selected_weather]}"
        },
        title=selected_weather
    )

    fig_weather.update_traces(
        line_color=selected_color,
        line_width=3,
        marker=dict(
            color=selected_color,
            size=6
        )
    )

    fig_weather.update_layout(
        paper_bgcolor="#FAF9FF",
        plot_bgcolor="#FAF9FF",
        font=dict(
            family="Arial",
            size=13,
            color="#252342"
        ),
        title_font=dict(
            size=19,
            color="#4D467A"
        ),
        xaxis=dict(
            gridcolor="#E9E3F8",
            zeroline=False
        ),
        yaxis=dict(
            gridcolor="#E9E3F8",
            zeroline=False
        ),
        margin=dict(l=35, r=25, t=70, b=40)
    )

    st.plotly_chart(
        fig_weather,
        use_container_width=True
    )

    # --------------------------------------
    # СРАВНЕНИЕ С ОБНАРУЖЕНИЯМИ
    # --------------------------------------

    st.subheader(
        "Связь погодных условий со спутниковыми обнаружениями"
    )

    st.write(
        "Каждая точка соответствует одному дню наблюдений. "
        "По горизонтали отображается погодный показатель, "
        "по вертикали — количество спутниковых обнаружений."
    )

    fig_scatter = px.scatter(
        daily,
        x=selected_column,
        y="detections",
        hover_data=["time"],
        labels={
            selected_column:
                f"{selected_weather}, {units[selected_weather]}",
            "detections": "Количество обнаружений"
        },
        title=f"{selected_weather} и спутниковые обнаружения"
    )

    fig_scatter.update_traces(
        marker=dict(
            color=selected_color,
            size=9,
            opacity=0.75,
            line=dict(
                color="#FFFFFF",
                width=0.7
            )
        )
    )

    fig_scatter.update_layout(
        paper_bgcolor="#FAF9FF",
        plot_bgcolor="#FAF9FF",
        font=dict(
            family="Arial",
            size=13,
            color="#252342"
        ),
        title_font=dict(
            size=19,
            color="#4D467A"
        ),
        xaxis=dict(
            gridcolor="#E9E3F8",
            zeroline=False
        ),
        yaxis=dict(
            gridcolor="#E9E3F8",
            zeroline=False
        ),
        margin=dict(l=35, r=25, t=70, b=40)
    )

    st.plotly_chart(
        fig_scatter,
        use_container_width=True
    )

    # --------------------------------------
    # КОРРЕЛЯЦИЯ СПИРМЕНА
    # --------------------------------------

    st.subheader("Статистическая связь")

    correlation = daily[
        [selected_column, "detections"]
    ].corr(method="spearman").iloc[0, 1]

    st.metric(
        "Коэффициент корреляции Спирмена",
        f"{correlation:.3f}"
    )

    if correlation > 0.3:
        st.write(
            "Наблюдается положительная статистическая связь: "
            "при увеличении показателя количество обнаружений "
            "в целом имеет тенденцию увеличиваться."
        )

    elif correlation < -0.3:
        st.write(
            "Наблюдается отрицательная статистическая связь: "
            "при увеличении показателя количество обнаружений "
            "в целом имеет тенденцию уменьшаться."
        )

    else:
        st.write(
            "Выраженная монотонная статистическая связь "
            "по выбранному показателю не наблюдается."
        )

    st.info(
        "Корреляция не доказывает причинно-следственную связь. "
        "Метеоданные относятся к одной точке около города Костанай "
        "и не отражают погодные условия одновременно "
        "во всех частях области."
    )
    st.info(
        "Особенность выборки: 31 августа 2025 года "
        "зарегистрировано 425 спутниковых обнаружений "
        "тепловых аномалий — максимальное суточное значение "
        "за исследуемый период. Этот день заметно выделяется "
        "на диаграмме рассеяния и может влиять на результаты "
        "корреляционного анализа. Для проверки устойчивости "
        "результатов полезно сравнить коэффициенты корреляции "
        "с учётом этого дня и без него."
    )
    st.markdown("#### Проверка устойчивости корреляции")

    daily_without_peak = daily[
        daily["time"].dt.date != pd.Timestamp("2025-08-31").date()
    ].copy()

    correlation_without_peak = daily_without_peak[
        [selected_column, "detections"]
    ].corr(method="spearman").iloc[0, 1]

    col_all, col_without = st.columns(2)

    with col_all:
        st.metric(
            "Все 92 дня",
            f"{correlation:.3f}"
        )

    with col_without:
        st.metric(
            "Без 31 августа (91 день)",
            f"{correlation_without_peak:.3f}"
        )

    st.caption(
        "Сравнение позволяет оценить чувствительность "
        "коэффициента Спирмена к исключению одного дня "
        "с максимальным количеством обнаружений. "
        "Это не доказывает наличие или отсутствие "
        "причинно-следственной связи."
    )
    st.markdown("#### Результат проверки устойчивости")

    st.success(
        "После исключения 31 августа 2025 года "
        "направление корреляций сохранилось для всех "
        "четырёх метеорологических показателей. "
        "Положительные связи с температурой и солнечной "
        "радиацией, а также отрицательная связь с осадками "
        "стали сильнее по абсолютной величине. "
        "Корреляция со скоростью ветра осталась близкой к нулю. "
        "Следовательно, основные направления выявленных "
        "статистических связей не определяются исключительно "
        "наблюдением 31 августа."
    )
    st.markdown("#### Сравнение всех метеопоказателей")

    comparison_results = []

    for weather_name, column_name in weather_columns.items():

        corr_all = daily[
            [column_name, "detections"]
        ].corr(method="spearman").iloc[0, 1]

        corr_without = daily_without_peak[
            [column_name, "detections"]
        ].corr(method="spearman").iloc[0, 1]

        comparison_results.append({
            "Метеопоказатель": weather_name,
            "Все 92 дня": corr_all,
            "Без 31 августа": corr_without,
            "Изменение": corr_without - corr_all
        })

    comparison_df = pd.DataFrame(comparison_results)

    st.dataframe(
        comparison_df,
        hide_index=True,
        width="stretch",
        column_config={
            "Все 92 дня": st.column_config.NumberColumn(
                format="%.3f"
            ),
            "Без 31 августа": st.column_config.NumberColumn(
                format="%.3f"
            ),
            "Изменение": st.column_config.NumberColumn(
                format="%+.3f"
            )
        }
    )

    st.caption(
        "Изменение рассчитано как разность коэффициентов: "
        "значение без 31 августа минус значение по всем 92 дням. "
        "Отрицательное изменение не всегда означает ослабление "
        "связи: для отрицательных корреляций необходимо также "
        "учитывать абсолютную величину коэффициента."
    )
    # --------------------------------------
    # ТАБЛИЦА ДАННЫХ
    # --------------------------------------

    with st.expander("Посмотреть исходные данные"):
        st.dataframe(
            daily[
                ["time", selected_column, "detections"]
            ],
            use_container_width=True
        )

# ======================================
# СТРАНИЦА МОДЕЛИ ИИ
# ======================================



    # ======================================
    # ИТОГОВЫЙ МЕТЕОРОЛОГИЧЕСКИЙ АНАЛИЗ
    # ======================================

    st.divider()
    st.subheader("Научные результаты метеоанализа")

    st.write(
        "Для сравнения погодных показателей рассчитаны "
        "коэффициенты ранговой корреляции Спирмена "
        "между каждым метеопараметром и ежедневным "
        "количеством спутниковых обнаружений."
    )

    correlation_columns = {
        "Температура": "temperature_2m_mean (°C)",
        "Осадки": "precipitation_sum (mm)",
        "Ветер": "wind_speed_10m_max (km/h)",
        "Солнечная радиация":
            "shortwave_radiation_sum (MJ/m²)"
    }

    correlation_results = []

    for name, column in correlation_columns.items():
        coefficient = daily[
            [column, "detections"]
        ].corr(method="spearman").iloc[0, 1]

        correlation_results.append({
            "Показатель": name,
            "Корреляция": coefficient
        })

    correlation_df = pd.DataFrame(correlation_results)

    fig_correlations = px.bar(
        correlation_df,
        x="Показатель",
        y="Корреляция",
        color="Корреляция",
        color_continuous_scale="RdBu",
        color_continuous_midpoint=0,
        text="Корреляция",
        title="Связь погодных условий с обнаружениями"
    )

    fig_correlations.update_traces(
        texttemplate="%{text:.3f}",
        textposition="outside"
    )

    fig_correlations.update_layout(
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#FFFFFF",
        font_color="#19354F",
        coloraxis_showscale=False,
        yaxis_range=[-1, 1]
    )

    st.plotly_chart(fig_correlations, width="stretch")

    st.markdown("#### Интерпретация результатов")

    st.write(
        "Наиболее выраженная положительная связь "
        "в исследуемой выборке наблюдается "
        "с солнечной радиацией. "
        "Температура также имеет положительную "
        "корреляцию с количеством обнаружений."
    )

    st.write(
        "Для осадков выявлена отрицательная "
        "корреляция, а связь с максимальной "
        "скоростью ветра близка к нулю."
    )

    st.info(
        "Научный вывод: погодные показатели имеют "
        "различную статистическую связь с числом "
        "спутниковых обнаружений. Однако корреляция "
        "не доказывает причинно-следственную зависимость "
        "и не позволяет самостоятельно оценить "
        "точность спутникового обнаружения пожаров."
    )

    st.caption(
        "Метеоданные получены для одной точки "
        "около города Костанай. Спутниковые "
        "обнаружения относятся ко всей области. "
        "Результаты следует интерпретировать "
        "с учётом этого пространственного ограничения."
    )

elif page == "Модель ИИ":

    import joblib

    st.title("Модель машинного обучения")

    st.write(
        "Интерактивная демонстрация экспериментальной "
        "модели, обученной на спутниковых данных NASA FIRMS "
        "и метеорологических данных Open-Meteo."
    )

    st.caption(
        "Метод: линейная регрессия | "
        "Регион: Костанайская область | "
        "Период обучения: лето 2025 года"
    )

    st.divider()

    # ======================================
    # ЗАГРУЗКА МОДЕЛИ
    # ======================================

    @st.cache_resource
    def load_model():
        return joblib.load("fire_model.joblib")

    model_data = load_model()

    model = model_data["model"]
    features = model_data["features"]

    # ======================================
    # НАСТРОЙКА ПОГОДНЫХ УСЛОВИЙ
    # ======================================

    st.subheader("Настройка условий")

    st.write(
        "Измените значения параметров, чтобы "
        "исследовать реакцию модели на разные сценарии."
    )

    col1, col2 = st.columns(2)

    with col1:

        temperature = st.slider(
            "Средняя температура воздуха, °C",
            min_value=-5.0,
            max_value=40.0,
            value=20.0,
            step=0.5
        )

        precipitation = st.slider(
            "Сумма осадков, мм",
            min_value=0.0,
            max_value=30.0,
            value=2.0,
            step=0.5
        )

        wind = st.slider(
            "Максимальная скорость ветра, км/ч",
            min_value=0.0,
            max_value=60.0,
            value=15.0,
            step=1.0
        )

    with col2:

        radiation = st.slider(
            "Солнечная радиация, МДж/м²",
            min_value=0.0,
            max_value=35.0,
            value=20.0,
            step=0.5
        )

        previous_day = st.number_input(
            "Обнаружений за предыдущий день",
            min_value=0,
            max_value=500,
            value=10,
            step=1
        )

    # ======================================
    # ФОРМИРОВАНИЕ ДАННЫХ ДЛЯ МОДЕЛИ
    # ======================================

    input_values = {
        "temperature_2m_mean (°C)": temperature,
        "precipitation_sum (mm)": precipitation,
        "wind_speed_10m_max (km/h)": wind,
        "shortwave_radiation_sum (MJ/m²)": radiation,
        "previous_day": previous_day
    }

    input_df = pd.DataFrame(
        [input_values]
    )

    # Порядок столбцов соответствует обучению
    input_df = input_df[features]

    # ======================================
    # РАСЧЁТ МОДЕЛИ
    # ======================================

    st.divider()
    st.subheader("Результат моделирования")

    if st.button(
        "Рассчитать",
        type="primary",
        use_container_width=True
    ):

        raw_prediction = float(
            model.predict(input_df)[0]
        )

        prediction = max(
            0,
            round(raw_prediction)
        )
        if raw_prediction < 0:
            st.warning(
                "Модель рассчитала отрицательное значение "
                f"({raw_prediction:.2f}). Поскольку количество "
                "спутниковых обнаружений не может быть "
                "отрицательным, отображаемый прогноз "
                "ограничен нулём. Это указывает на "
                "ограничения используемой линейной регрессии."
            )
        
        # ======================================
        # СРАВНЕНИЕ МОДЕЛИ И БАЗОВОГО МЕТОДА
        # ======================================

        baseline_prediction = previous_day

        col_ai, col_baseline = st.columns(2)

        with col_ai:
            st.metric(
                "Модель ИИ",
                f"{prediction} обнаружений"
            )

        with col_baseline:
            st.metric(
                "Базовый прогноз",
                f"{baseline_prediction} обнаружений"
            )

        # Данные для диаграммы
        comparison_df = pd.DataFrame({
            "Метод": [
                "Линейная регрессия",
                "Базовый прогноз"
            ],
            "Количество обнаружений": [
                prediction,
                baseline_prediction
            ]
        })

        fig_comparison = px.bar(
            comparison_df,
            x="Метод",
            y="Количество обнаружений",
            color="Метод",
            text="Количество обнаружений",
            color_discrete_map={
                "Линейная регрессия": "#9275D2",
                "Базовый прогноз": "#E6A15B"
            },
            title="Сравнение результатов двух методов"
        )

        fig_comparison.update_traces(
            textposition="outside"
        )

        fig_comparison.update_layout(
            paper_bgcolor="#FAF9FF",
            plot_bgcolor="#FAF9FF",
            font=dict(
                family="Arial",
                size=13,
                color="#252342"
            ),
            title_font=dict(
                size=19,
                color="#4D467A"
            ),
            xaxis=dict(
                showgrid=False,
                zeroline=False
            ),
            yaxis=dict(
                gridcolor="#E9E3F8",
                zeroline=False,
                range=[
                    0,
                    max(prediction, baseline_prediction, 1) * 1.25
                ]
            ),
            showlegend=False,
            margin=dict(l=35, r=25, t=70, b=40)
        )

        st.plotly_chart(
            fig_comparison,
            width="stretch"
        )
        # ======================================
        # ОБЪЯСНЕНИЕ ПРОГНОЗА МОДЕЛИ
        # ======================================

        st.divider()
        st.subheader("Как модель получила этот результат?")

        st.write(
            "Линейная регрессия рассчитывает прогноз как "
            "сумму свободного члена и вкладов пяти признаков. "
            "Каждый вклад равен значению показателя, "
            "умноженному на соответствующий коэффициент модели."
        )

        # Математическая формула в карточке Nebula
        st.markdown("""
        <div style="
            background-color: #E9E3F8;
            border: 1px solid #C7B8EA;
            border-radius: 16px;
            padding: 18px 24px;
            margin: 20px 0;
            text-align: center;
            color: #4D467A;
            font-size: 17px;
            font-weight: 600;
        ">
            Математическая формула линейной регрессии
        </div>
        """, unsafe_allow_html=True)

        with st.container(border=True, key="formula_card"):
            st.latex(
                r"\hat{y} = b + w_1T + w_2P + w_3W + w_4R + w_5N"
            )

        st.caption(
            "T — температура воздуха; P — осадки; "
            "W — скорость ветра; R — солнечная радиация; "
            "N — количество обнаружений за предыдущий день. "
            "b — свободный член, w — коэффициенты модели."
        )

        # Получаем коэффициенты из обученной модели
        coefficients = model.coef_
        intercept = float(model.intercept_)

        feature_names = {
            "temperature_2m_mean (°C)": "Температура",
            "precipitation_sum (mm)": "Осадки",
            "wind_speed_10m_max (km/h)": "Скорость ветра",
            "shortwave_radiation_sum (MJ/m²)": "Солнечная радиация",
            "previous_day": "Обнаружения предыдущего дня"
        }

        # Формируем таблицу вкладов
        contributions = []

        for feature, coefficient in zip(features, coefficients):

            feature_value = float(input_df.iloc[0][feature])
            coefficient = float(coefficient)

            contribution = feature_value * coefficient

            contributions.append({
                "Компонент": feature_names.get(feature, feature),
                "Значение": feature_value,
                "Коэффициент": coefficient,
                "Вклад в прогноз": contribution
            })

        contributions.insert(0, {
            "Компонент": "Свободный член",
            "Значение": None,
            "Коэффициент": intercept,
            "Вклад в прогноз": intercept
        })

        contributions_df = pd.DataFrame(contributions)

        st.markdown("#### Вклад каждого показателя")

        st.dataframe(
            contributions_df,
            hide_index=True,
            width="stretch",
            column_config={
                "Значение": st.column_config.NumberColumn(
                    format="%.2f"
                ),
                "Коэффициент": st.column_config.NumberColumn(
                    format="%+.4f"
                ),
                "Вклад в прогноз": st.column_config.NumberColumn(
                    format="%+.2f"
                )
            }
        )

        # Проверяем сумму вкладов

        # ======================================
        # NEBULA — ДИАГРАММА ВКЛАДОВ ФАКТОРОВ
        # ======================================

        st.markdown("#### Визуализация вкладов факторов")

        st.write(
            "Положительные значения увеличивают расчётный "
            "прогноз модели, а отрицательные уменьшают его. "
            "Свободный член показан отдельно от погодных факторов."
        )

        chart_df = contributions_df.copy()

        chart_df["Направление"] = chart_df[
            "Вклад в прогноз"
        ].apply(
            lambda value: (
                "Положительный"
                if value >= 0
                else "Отрицательный"
            )
        )

        fig_contributions = px.bar(
            chart_df,
            x="Вклад в прогноз",
            y="Компонент",
            orientation="h",
            color="Направление",
            color_discrete_map={
                "Положительный": "#9275D2",
                "Отрицательный": "#E77C65"
            },
            hover_data={
                "Значение": ":.2f",
                "Коэффициент": ":.4f",
                "Вклад в прогноз": ":.2f"
            },
            labels={
                "Вклад в прогноз": "Вклад в расчёт модели",
                "Компонент": ""
            },
            title="Положительные и отрицательные вклады"
        )

        fig_contributions.update_layout(
            paper_bgcolor="#FAF9FF",
            plot_bgcolor="#FAF9FF",
            font=dict(
                family="Arial",
                size=13,
                color="#252342"
            ),
            title_font=dict(
                size=19,
                color="#4D467A"
            ),
            xaxis=dict(
                gridcolor="#E9E3F8",
                zeroline=True,
                zerolinecolor="#4D467A",
                zerolinewidth=2
            ),
            yaxis=dict(
                categoryorder="array",
                categoryarray=chart_df["Компонент"].tolist(),
                autorange="reversed",
                showgrid=False
            ),
            showlegend=False,
            height=410,
            margin=dict(l=30, r=25, t=70, b=45)
        )

        st.plotly_chart(
            fig_contributions,
            width="stretch"
        )

        st.caption(
            "Вклады рассчитаны по коэффициентам сохранённой "
            "линейной регрессии. Они объясняют математический "
            "расчёт, но не доказывают причинное влияние "
            "погодных условий на возникновение пожаров."
        )

        calculated_total = contributions_df[
            "Вклад в прогноз"
        ].sum()

        col_formula, col_result = st.columns(2)

        with col_formula:
            st.metric(
                "Результат формулы",
                f"{calculated_total:.2f}"
            )

        with col_result:
            st.metric(
                "Отображаемый прогноз",
                f"{prediction} обнаружений"
            )

        st.caption(
            "Результат формулы показан до округления. "
            "Для отображения количества обнаружений "
            "значение округляется до целого числа "
            "и ограничивается снизу нулём."
        )

        st.info(
            "Важно: положительный или отрицательный "
            "коэффициент показывает математическую связь "
            "в обученной модели, но не доказывает, "
            "что соответствующий погодный фактор "
            "непосредственно вызывает или предотвращает пожары."
        )

        st.markdown("#### Почему прогноз бывает неожиданным?")

        st.write(
            "Модель обучалась на ограниченном наборе "
            "наблюдений за лето 2025 года. "
            "Она использует статистические зависимости, "
            "а не физические законы возникновения пожаров. "
            "Поэтому при некоторых сочетаниях погодных "
            "условий прогноз может быть неожиданно высоким "
            "или низким."
        )

        st.write(
            "Дополнительные ограничения связаны с тем, "
            "что метеоданные характеризуют одну точку "
            "около города Костанай, а спутниковые "
            "обнаружения относятся ко всей области. "
            "Также некоторые погодные показатели "
            "могут быть взаимосвязаны."
        )
        difference = prediction - baseline_prediction

        if difference > 0:
            st.write(
                f"Модель ИИ рассчитала на {difference} "
                "обнаружений больше, чем базовый метод."
            )

        elif difference < 0:
            st.write(
                f"Модель ИИ рассчитала на {abs(difference)} "
                "обнаружений меньше, чем базовый метод."
            )

        else:
            st.write(
                "Оба метода дали одинаковый результат."
            )

        st.caption(
            "Разница между расчётами не означает, "
            "что один метод точнее другого. "
            "Для оценки точности необходимо сравнение "
            "с фактическими наблюдениями."
        )


        st.write(
            "Полученное значение показывает результат "
            "математической модели при выбранных параметрах. "
            "Это не подтверждённое количество пожаров "
            "и не надёжный оперативный прогноз."
        )

        if raw_prediction < 0:
            st.caption(
                "Исходная регрессия выдала отрицательное "
                "значение. Для отображения количество "
                "обнаружений ограничено нулём."
            )

        st.info(
            "Модель использует пять признаков: "
            "температуру, осадки, ветер, солнечную "
            "радиацию и число обнаружений "
            "за предыдущий день."
        )

    # ======================================
    # НАУЧНОЕ ПОЯСНЕНИЕ
    # ======================================

    st.divider()
    st.subheader("Как работает модель?")

    st.write(
        "Линейная регрессия устанавливает математическую "
        "зависимость между входными признаками и "
        "количеством спутниковых обнаружений. "
        "После обучения модель вычисляет результат "
        "для нового набора параметров."
    )

    st.warning(
        "Ограничения исследования: модель обучена "
        "на небольшом наборе данных за 92 дня. "
        "При проверке на последующих временных периодах "
        "она уступила простому базовому прогнозу, "
        "использующему количество обнаружений "
        "за предыдущий день. Поэтому результаты "
        "представлены исключительно как "
        "исследовательский эксперимент."
    )

    st.divider()
    st.subheader("Результаты проверки модели")
    st.markdown("#### Оценка точности на временных периодах")

    evaluation_results = pd.DataFrame({
        "Период": [
            "12–26 июля",
            "27 июля – 10 августа",
            "11–25 августа"
        ],
        "MAE модели ИИ": [7.05, 3.94, 2.84],
        "MAE базового метода": [3.27, 1.67, 0.33]
    })

    st.dataframe(
        evaluation_results,
        hide_index=True,
        width="stretch",
        column_config={
            "MAE модели ИИ": st.column_config.NumberColumn(
                format="%.2f"
            ),
            "MAE базового метода": st.column_config.NumberColumn(
                format="%.2f"
            )
        }
    )

    st.caption(
        "MAE — средняя абсолютная ошибка прогноза. "
        "Чем меньше значение, тем точнее метод. "
        "Модель заново обучалась перед каждым проверочным "
        "периодом на более ранних наблюдениях. "
        "Оценка выполнена с использованием фактических "
        "метеопоказателей проверочных дней."
    )
        # График сравнения точности методов
    evaluation_long = evaluation_results.melt(
        id_vars="Период",
        value_vars=[
            "MAE модели ИИ",
            "MAE базового метода"
        ],
        var_name="Метод",
        value_name="MAE"
    )

    fig_evaluation = px.bar(
        evaluation_long,
        x="Период",
        y="MAE",
        color="Метод",
        barmode="group",
        text_auto=".2f",
        labels={
            "Период": "Период проверки",
            "MAE": "Средняя абсолютная ошибка"
        },
        color_discrete_map={
            "MAE модели ИИ": "#9275D2",
            "MAE базового метода": "#E6A15B"
        }
    )

    fig_evaluation.update_layout(
        height=420,
        paper_bgcolor="#FAF9FF",
        plot_bgcolor="#FAF9FF",
        font=dict(
            family="Arial",
            size=13,
            color="#252342"
        ),
        xaxis=dict(
            showgrid=False,
            zeroline=False
        ),
        yaxis=dict(
            gridcolor="#E9E3F8",
            zeroline=False
        ),
        legend_title_text="",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="left",
            x=0
        ),
        margin=dict(l=35, r=25, t=70, b=40)
    )

    st.plotly_chart(
        fig_evaluation,
        use_container_width=True
    )
    st.markdown("#### Научный вывод")

    st.success(
        "Во всех трёх проверочных периодах базовый метод "
        "показал меньшую среднюю абсолютную ошибку, "
        "чем линейная регрессия."
    )

    st.write(
        "Средняя ошибка линейной регрессии составила "
        "**4,61 обнаружения**, а базового метода — "
        "**1,76 обнаружения**. Ошибка линейной регрессии "
        "оказалась примерно в **2,6 раза выше**."
    )

    st.info(
        "Результаты показывают, что применение машинного "
        "обучения не всегда повышает точность прогнозирования. "
        "Для улучшения модели необходимы дополнительные "
        "данные и проверка других алгоритмов."
    )

    st.caption(
        "Ограничение исследования: проверочные периоды "
        "не включают 31 августа 2025 года, когда было "
        "зарегистрировано 425 спутниковых обнаружений. "
        "Поэтому точность модели в условиях таких "
        "резких всплесков пока не оценена."
    )