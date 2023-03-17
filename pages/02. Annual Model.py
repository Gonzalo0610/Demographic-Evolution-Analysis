import streamlit as st
import pandas as pd
import statsmodels.formula.api as smf
from sklearn.linear_model import LinearRegression
import numpy as np
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
import streamlit.components.v1 as components




model=pd.read_csv("RegModel.csv")
andalucia=pd.read_csv("andalucia.csv")
aragon=pd.read_csv("aragon.csv")
asturias=pd.read_csv("asturias.csv")
baleares=pd.read_csv("baleares.csv")
cantabria=pd.read_csv("cantabria.csv")
leon=pd.read_csv("leon.csv")
mancha=pd.read_csv("mancha.csv")
catalunya=pd.read_csv("catalunya.csv")
valencia=pd.read_csv("valencia.csv")
extremadura=pd.read_csv("extremadura.csv")
galicia=pd.read_csv("galicia.csv")
madrid=pd.read_csv("madrid.csv")
murcia=pd.read_csv("murcia.csv")
navarra=pd.read_csv("navarra.csv")
euskadi=pd.read_csv("euskadi.csv")
rioja=pd.read_csv("rioja.csv")
model.drop("Unnamed: 0", inplace=True, axis=1)

def ols (var):
    return smf.ols("Natality ~  Women_Age + Masculinity_Ratio + Marriages + Unemployment_Women + Economic_Crisis + Instagram_Tinder", data=var).fit()

resultsand= ols(andalucia)
resultsara= ols(aragon)
resultsast = ols(asturias)
resultsbal = ols(baleares)
resultscan = ols(cantabria)
resultsleo = ols(leon)
resultsman = ols(mancha)
resultscat = ols(catalunya)
resultsval = ols(valencia)
resultsext = ols(extremadura)
resultsgal = ols(galicia)
resultsmad = ols(madrid)
resultsmur = ols(murcia)
resultsnav = ols(navarra)
resultseus = ols(euskadi)
resultsrio = ols(rioja)

st.set_page_config(page_title="Regression Model", page_icon=":bar_chart:", layout="wide")
st.header("Regression Model Analysis")
st.write("For this part of the project, I selected all the variables from the Datasets related with economic, social and demographic indicators, and use Webscrapping to select some booleans as well. The first objective was to find the best variables in the OLS/Regression Model that fits the whole nation:")
         
tab17, tab18, tab19, tab20, tab22 = st.tabs(["Qualitative Variables", "Booleans", "First Model", "Correlation Issues", "Final Model"])
with tab17:
   st.header("Qualitative Variables")
   st.markdown('''
   - **Periodo**: The range of years taken into account (2002-2021)
   - **Natality**: The Natality Rate, measured in number of newborn per 1000 habitants. 
   - **Men_Age**: The average of the men's age. 
   - **Women_Age**: The average of the women's age. 
   - **Population_Growth**: The population growth year to year. 
   - **Foreigners_Ratio**: The ratio of foreigners population out of the whole population
   - **Foreigners_Women**: The ratio of foreigner women with biological facilities to give birth (between 18 and 35 years)
   - **Masculinity_Ratio**: The percentage of men per each woman
   - **Marriages**: The number of marriages of the whole country
   - **Unemployment_Ratio**
   - **Unemployment_Women**: The ratio of unemployed women with biological facilities to give birth (between 18 and 35 years)
   ''')

with tab18:
   st.header("Booleans")
   st.markdown('''
   - **Economic_Crisis**: The Economic Crisis period (2008-2014). 
   - **Confination**: The confination due to the covid-19 period (2020-2021)
   - **Facebook**: The period from the arrival of Facebook to Spain until the present (2008-2021)
   - **Instagram_Tinder**: The period from the arrival of Instagram and Tinder to Spain until the present (2012-2021)
   - **Law_Change**: The change of the Abortion Law in the whole country (2010-2021)
   ''')

with tab19:
   st.header("First Model")
   results = smf.ols("Natality ~ Periodo + Men_Age + Women_Age + Population_Growth + Foreigners_Ratio + Foreigner_Women + Masculinity_Ratio + Marriages + Unemployment_Ratio + Unemployment_Women + Economic_Crisis + Confination + Facebook + Instagram_Tinder + Law_Change", data=model).fit()
   st.write(results.summary())

with tab20:
   st.header("Correlation")
   matrix = model.corr()
   st.write(matrix.style.background_gradient(cmap='coolwarm'))


with tab22:
   st.header("Final Model")
   final = ols(model)
   st.write(final.summary())
st.markdown(''' ''')
st.markdown('''Once I established my model, finally with just 6 significant variables taken into account, I tried to implement the final model into every autonomous community and see if the factors that affect the whole country also have a similar effect in each territory:''')

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13, tab14, tab15, tab16 = st.tabs(["Andalucía", "Cataluña", "Madrid", "Valencia", "Galicia", "Euskadi", "Castilla y León", "Murcia", "Castilla la Mancha", "Aragón", "Baleares", "Extremadura", "Asturias", "Navarra", "Cantabria", "La Rioja"])

with tab1:
   st.header("Andalucia Regression")
   st.write(resultsand.summary())

with tab2:
   st.header("Catalunya Regression")
   st.write(resultscat.summary())

with tab3:
   st.header("Madrid Regression")
   st.write(resultsmad.summary())

with tab4:
   st.header("Valencia Regression")
   st.write(resultsval.summary())

with tab5:
   st.header("Galicia Regression")
   st.write(resultsgal.summary())

with tab6:
   st.header("Euskadi Regression")
   st.write(resultseus.summary())

with tab7:
   st.header("Castilla-León Regression")
   st.write(resultsleo.summary())

with tab8:
   st.header("Murcia Regression")
   st.write(resultsmur.summary())

with tab9:
   st.header("Castilla y la Mancha Regression")
   st.write(resultsman.summary())

with tab10:
   st.header("Aragón Regression")
   st.write(resultsara.summary())

with tab11:
   st.header("Balear Islands Regression")
   st.write(resultsbal.summary())

with tab12:
   st.header("Extremadura Regression")
   st.write(resultsext.summary())

with tab13:
   st.header("Asturias Regression")
   st.write(resultsast.summary())

with tab14:
   st.header("Navarra Regression")
   st.write(resultsnav.summary())

with tab15:
   st.header("Cantabria Regression")
   st.write(resultscan.summary())

with tab16:
   st.header("La Rioja Regression")
   st.write(resultsrio.summary())

st.markdown('''Unfortunately, not a single region had the 6 coefficients; the maximum were 4, and the most repeated both the Women's Age and the Masculinity Rate. Here I set a map filtering it by how many coefficients from the original model have its null hypothesis rejected:''')

def main():
        html_temp = '''<div class='tableauPlaceholder' id='viz1678988441278' style='position: relative'><noscript><a href='#'><img alt='Number of significant values of the model per CCAA ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Nu&#47;NumberofsignificantvaluesofthemodelperCCAA&#47;Sheet27&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='NumberofsignificantvaluesofthemodelperCCAA&#47;Sheet27' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Nu&#47;NumberofsignificantvaluesofthemodelperCCAA&#47;Sheet27&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='es-ES' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1678988441278');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>'''
        components.html(html_temp, width=800, height=800)
        
if __name__ == '__main__':
    main()