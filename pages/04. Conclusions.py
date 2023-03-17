import streamlit as st

st.set_page_config(page_title="Conclusions", page_icon=":baby:", layout="wide")

st.title("Conclusions")
st.markdown("To sum up, here is a brief synthesis of the most important conclusions I observed in this project:")

st.header("Annual Factors")
st.markdown('''
- From all the exogenous variables taken into account, only six were considered in a regression model that worked rejecting the Ho: 
    - The women average age 
    - The masculinity ratio 
    - The number of marriages 
    - The unemployment of fertile women ratio 
    - The economic crisis (boolean) 
    - The creation of both Instagram and Tinder (boolean).
- Both the women age and the economic crisis are the variables with a negative marginal effect on the natality rate.
- Once we try to apply the same model to each autonomous community, it does not fully work: 
    - The only variables that are robust in the majority of the cases are the women average age, the masculinity ratio, and, to a lesser extent, the number of marriages (which is also less relevant than the first two mentioned). 
- Although my original hypothesis stated that the model would function better in regions with higher population, with this set of data I must reject it: 
    - The highest population CCAA, Andalucia, has just two relevant variables from the original model. 
    - The next two regions in terms of population, Cataluña and Madrid, match the original hypothesis.
''')

st.header("Monthly Patterns")
st.markdown('''
- If we consider each month to have the same number of days, September is the month with the highest number of newborns, nine months after the Christmas Holidays. 
- Following this pattern, the majority of CCAA have their highest peak of newborns in September and in some cases, in May (nine months after Summer Holidays). 
- There is a slight correlation between the CCAAs with a peak of births in May and marriages in the summer: it could be caused by warmer temperatures during the summer. 
- Of all the CCAAs, the three outliers with more babies than expected, looking at the total population, are the regions of Navarra, Cantabria, and Castilla la Mancha. 
- Two of these three outliers are nine months after the celebration of the region's festivity. 
''')
