import streamlit as st
import pandas as pd
import statsmodels.formula.api as smf
from sklearn.linear_model import LinearRegression
import numpy as np
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor




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
st.header("THE REGRESSION MODEL")
st.write("For this part of the project, I selected all the variables from the Datasets related with Economic, Social and Demographic indicators, and use Web Scrapping to select some booleans as well. The first objective was to find the best model that fits the whole nation")
         
tab17, tab18, tab19, tab20, tab22 = st.tabs(["Qualitative Variables", "Booleans", "First Model", "Correlation", "Final Model"])
with tab17:
   st.header("Qualitative Variables")
   st.markdown('''INSERT ALL VARIABLES''')

with tab18:
   st.header("Booleans")
   st.markdown('''INSERT ALL BOOLEANS''')

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
st.markdown('''Then, I try to implement the final model into every autonomous community and see if the factors that affect the whole country also affect each territory separately.''')

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