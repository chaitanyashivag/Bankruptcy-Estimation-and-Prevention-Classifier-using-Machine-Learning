
import pickle
import streamlit as st


pickle_in = open("G:\DS\Excel r\Project\decision_tree_model.pkl","rb")
classifier=pickle.load(pickle_in)


def predict_bankruptcy(industrial_risk,management_risk,financial_flexibility,credibility,competitiveness,operating_risk):
     prediction=classifier.predict([[industrial_risk,management_risk,financial_flexibility,credibility,competitiveness,operating_risk]])
     print(prediction)
     return prediction





def main():
    st.title("Bankruptcy Predictor")
    industrial_risk = st.text_input("industrial_risk","")
    management_risk = st.text_input("management_risk","")
    financial_flexibility = st.text_input("financial_flexibility","")
    credibility = st.text_input("credibility","")
    competitiveness = st.text_input("competitiveness","")
    operating_risk = st.text_input("operating_risk","")
    result=""
    if st.button("Predict"):
        result=predict_bankruptcy(industrial_risk,management_risk,financial_flexibility,credibility,competitiveness,operating_risk)
    st.success('The output is {}'.format(result))

if __name__=='__main__':
    main()