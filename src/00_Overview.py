# streamlit を使用するために import します
import streamlit as st
st.set_page_config(page_icon=":shark:", layout="wide")

content_en = """
## Data Visualization Projects

This Streamlit application is designed to showcase a variety of data visualizations across multiple projects, with a focus on maritime and environmental data analysis. Here are the key areas of focus:

- **Fish Catch Data**: Analysis and visualization of fish catch data, helping to understand trends in fish populations, catch volumes by species, and the impact of fishing on marine ecosystems.
        
- **Ship Operational Data**: Visualizations related to the operations of ships, including fuel consumption, CO2 emissions. This area aims to provide insights into the efficiency and environmental impact of maritime transport.

The goal of this app is not only to present data in an interactive and informative manner but also to highlight the importance of sustainable practices and effective operations in  shipping and fishing industries.

## Connect With Me

Interested in learning more about my work or collaborating on future projects? Connect with me through my portfolio site or LinkedIn:

- [Portfolio](https://tatsuhirot.github.io/react-portfolio/)
- [LinkedIn](https://www.linkedin.com/in/tatsuhiroterada/)

"""

content_jp = """
## データ可視化プロジェクト

このStreamlitアプリケーションは、海事および環境データ分析に焦点を当てた複数のプロジェクトにわたるさまざまなデータ可視化を紹介するために設計されています。ここでは、重点的に扱う主な分野を紹介します：

- **魚の漁獲データ**：魚の漁獲データの分析と可視化を行い、魚の個体群の傾向、種別の漁獲量、および漁業が海洋生態系に与える影響を理解するのに役立ちます。

- **船舶運航データ**：船舶の運航に関連する可視化、燃料消費量、CO2排出量などを含みます。この分野は、海上輸送の効率性と環境への影響についての洞察を提供することを目指しています。

このアプリの目標は、データをインタラクティブに提示するだけでなく、船舶および漁業の業界における持続可能な実践と効果的な運用の重要性を強調することです。

## 連絡先

私の仕事についてもっと知りたい、または将来のプロジェクトで協力したいと思われる方はご連絡ください：

- [ポートフォリオ](https://tatsuhirot.github.io/react-portfolio/)
- [LinkedIn](https://www.linkedin.com/in/tatsuhiroterada/)
"""

content_es = """
## Proyectos de Visualización de Datos

Esta aplicación Streamlit está diseñada para mostrar una variedad de visualizaciones de datos en múltiples proyectos, con un enfoque en el análisis de datos marítimos y ambientales. Aquí están las áreas clave de enfoque:

- **Datos de Captura de Peces**: Análisis y visualización de datos de captura de peces, ayudando a comprender las tendencias en las poblaciones de peces, los volúmenes de captura por especie y el impacto de la pesca en los ecosistemas marinos.

- **Datos Operativos de Barcos**: Visualizaciones relacionadas con las operaciones de los barcos, incluyendo el consumo de combustible, las emisiones de CO2. Esta área tiene como objetivo proporcionar información sobre la eficiencia y el impacto ambiental del transporte marítimo.

El objetivo de esta aplicación no es solo presentar datos de manera interactiva e informativa, sino también destacar la importancia de las prácticas sostenibles y las operaciones efectivas en las industrias de envío y pesca.

## Conéctate Conmigo

¿Interesado en aprender más sobre mi trabajo o colaborar en futuros proyectos? Conéctate conmigo a través de mi sitio de portfolio o LinkedIn:

- [Portfolio](https://tatsuhirot.github.io/react-portfolio/)
- [LinkedIn](https://www.linkedin.com/in/tatsuhiroterada/)
"""

translations = {
    "en": {
        "choose_language": "Choose your language:",
        "title": "About This App",
        "content": content_en
        # Add more translations here
    },
    "jp": {
        "choose_language": "言語を選択してください:",
        "title": "このアプリについて",
        "content": content_jp
        # Add more translations here
    },
    "es": {
        "choose_language": "Elige tu idioma:",
        "title": "Sobre esta aplicación",
        "content": content_es
        # Add more translations here
    },
}

def get_translation(lang_code, key):
    return translations[lang_code].get(key, "")

# Language options mapped to codes
language_options = {
    "English": "en",
    "日本語": "jp",
    "Español": "es",
}

# Initialize session state for language if not already set
if 'language' not in st.session_state:
    st.session_state['language'] = 'en'  # Default language code

# Reverse mapping for displaying the current language in the dropdown
current_language_label = [label for label, code in language_options.items() if code == st.session_state['language']][0]

# Language selection
language_label = st.sidebar.selectbox(
    get_translation(st.session_state['language'], 'choose_language'),
    options=list(language_options.keys()),
    index=list(language_options.keys()).index(current_language_label)
)

# Update session state with the selected language code
st.session_state['language'] = language_options[language_label]


def show_about_page():
    st.title(get_translation(st.session_state['language'], 'title'))
    st.markdown(get_translation(st.session_state['language'], 'content'))

# Call the function to render the page
if __name__ == "__main__":
    show_about_page()
