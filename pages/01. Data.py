import streamlit as st
import streamlit.components.v1 as components

def main():
    st.title("The Data")
    st.markdown("I selected my data mostly from INE, CIS and Kaggle.")
    st.markdown("I set my project in a 20 year data analysis, a period of study from 2002 to 2021, the most recent past where more data is available.")
    st.markdown("I decided to drop Canarias from my final study to avoid confusion in the maps and visualizations. In addition, I dropped also Ceuta and Melilla as they are not properly Autonomous Communities, and the limited population could affect the results.")
    st.markdown("The first that I did after gathering the data was visualizing in order to try to obtain more information about the possible results and also about factors that I did not take into account. Here is an example:")

    with st.spinner("Loading data visualization..."):
        html_temp = '''<div class='tableauPlaceholder' id='viz1679000852594' style='position: relative'><noscript><a href='#'><img alt='Demographic Factors Evolution ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;C5&#47;C5K4HXKW4&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='shared&#47;C5K4HXKW4' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;C5&#47;C5K4HXKW4&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='es-ES' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1679000852594');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='700px';vizElement.style.height='707px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>'''
        components.html(html_temp, width=700, height=707)

    st.markdown("Looking at these different graphs, we can conclude the importance of foreigners in the natality rate, as well as the social impact of both the economic crisis and the COVID-19 pandemic.")

if __name__ == '__main__':
    main()

