import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

st.set_page_config(page_title="Monthly Patterns", page_icon=":bar_chart:", layout="wide")
st.title("Monthly Patterns Analysis")
st.markdown("In this Analysis I don't take into account the factors included in the regression model, just the total number of births per each month. As each month has different days, I first had to even this by setting the model as if every month have the same number of days (February is considered 28,25 as per the leap-years)")

def main():
        html_temp = '''<div class='tableauPlaceholder' id='viz1678990319422' style='position: relative'><noscript><a href='#'><img alt='Number of Births per Month (taking into account the number of days) ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Nu&#47;NumberofBirthsperMonthtakingintoaccountthenumberofdays&#47;Sheet28&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='NumberofBirthsperMonthtakingintoaccountthenumberofdays&#47;Sheet28' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Nu&#47;NumberofBirthsperMonthtakingintoaccountthenumberofdays&#47;Sheet28&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='es-ES' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1678990319422');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>'''
        components.html(html_temp, width=800, height=600)
        
if __name__ == '__main__':
    main()

st.markdown("As shown in the graph above, the most common month of birth in Spain is September, 9 months after the Christmas holidays. Is it the same per each community?")

def main2():
    html_temp = '''<div class='tableauPlaceholder' id='viz1678992866820' style='position: relative'><noscript><a href='#'><img alt='Top Born Months ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;4N&#47;4N4Z9P76T&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='shared&#47;4N4Z9P76T' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;4N&#47;4N4Z9P76T&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='es-ES' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1678992866820');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>'''
    components.html(html_temp, width=800, height=600)
        
if __name__ == '__main__':
    main2()

st.markdown("The answer is no, although the majority of the autonomous commmunities matches this premise. I then did the same process but with the total marriages to observe if there is any correlation between the months of the conception and the number of marriages:")

def main3():
    html_temp = '''<div class='tableauPlaceholder' id='viz1678992899419' style='position: relative'><noscript><a href='#'><img alt='Top Marriage Months ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;To&#47;TopMarriageMonths&#47;Sheet29&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='TopMarriageMonths&#47;Sheet29' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;To&#47;TopMarriageMonths&#47;Sheet29&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='es-ES' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1678992899419');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>'''
    components.html(html_temp, width=800, height=600)
        
if __name__ == '__main__':
    main3()

differences=pd.read_csv("differences.csv")
differences.set_index('Periodo', inplace=True)
tab3, tab4 = st.tabs(["Ratio difference", "Maximum differences"])

st.markdown("Finally, I wanted to stablish the outliers of the births: which CCAA has an unusual number of births, compared to the whole country. I set the ratio of births as a maximum of 1 and compare the total nation with each community, and then select the maximum relative values:")

with tab3:
     st.dataframe(differences)

with tab4:
    cols = differences.columns.tolist()
    max_values = differences.describe().loc['max'].tolist()
    result_df = pd.DataFrame({'Column Name': cols, 'Max Value': max_values})
    st.dataframe(result_df)

st.markdown("Out of the 3 biggest values, 2 of the autonomous commmunities (Navarra and Castilla la Mancha) with an unusual ratio of births (July and June) are 9 months after their biggest regional holiday festivity, San Fermines and La Feria de Albacete")