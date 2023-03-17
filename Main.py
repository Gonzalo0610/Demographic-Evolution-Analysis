import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="The Birth Rate Evolution in Spain: Factors and Patterns", page_icon=":baby:", layout="wide")

st.title("The Birth Rate Evolution in Spain: Factors and Patterns")
st.header("Introduction")
st.markdown("The aim of this project is to try to find demographic, social and economic factors that affect the Natality Rate in the country, and then check if these factors evolve the same way in every autonomous community. On the other hand, I want to observe if there is a historical monthly difference of newborns in Spain, find a pattern in each territory and try to understand the outliers.")

def main():
    html_temp = '''
        <div class='tableauPlaceholder' id='viz1678977058780' style='position: relative'>
            <noscript>
                <a href='#'>
                    <img alt='Natality Rate - 2006' src='https://public.tableau.com/static/images/J5/J5R75ZKFS/1_rss.png' style='border: none' />
                </a>
            </noscript>
            <object class='tableauViz'  style='display:none;'>
                <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
                <param name='embed_code_version' value='3' />
                <param name='path' value='shared&#47;J5R75ZKFS' />
                <param name='toolbar' value='yes' />
                <param name='static_image' value='https://public.tableau.com/static/images/J5/J5R75ZKFS/1.png' />
                <param name='animate_transition' value='yes' />
                <param name='display_static_image' value='yes' />
                <param name='display_spinner' value='yes' />
                <param name='display_overlay' value='yes' />
                <param name='display_count' value='yes' />
                <param name='language' value='es-ES' />
                <param name='filter' value='publish=yes' />
            </object>
            <script type='text/javascript'>
                var divElement = document.getElementById('viz1678977058780');
                var vizElement = divElement.getElementsByTagName('object')[0];
                vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';
                var scriptElement = document.createElement('script');
                scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
                vizElement.parentNode.insertBefore(scriptElement, vizElement);
            </script>
        </div>
    '''
    components.html(html_temp, width=800, height=800)

if __name__ == '__main__':
    main()
