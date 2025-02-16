import streamlit as st
import pandas as pd
import pickle
import datetime


st.title("🎓 Jaya Jaya Institute")

with st.sidebar:
        st.subheader("Disclaimer")
        st.markdown("This document is created for academic purposes and is not intended to represent any specific individuals or organizations. Any similarities in names or events are purely coincidental.")



tab1, tab2, tab3 = st.tabs([
    "👨‍🎓 Student Assessment",
    "📊 Dashboard",
    "ℹ️ About"
])

with tab1:
    st.subheader("👨‍🎓 Student Prediction using Machine Learning")

    # Load model
    def load_model(model_name):
        if model_name == 'Random Forest':
            model = pickle.load(open('models/Random Forest.pkl', 'rb'))
        elif model_name == 'Decision Tree':
            model = pickle.load(open('models/Decision Tree.pkl', 'rb'))
        elif model_name == 'Logistic Regression':
            model = pickle.load(open('models/Logistic Regression.pkl', 'rb'))
        elif model_name == 'SVM':
            model = pickle.load(open('models/SVM.pkl', 'rb'))
        elif model_name == 'XGB':
            model = pickle.load(open('models/XGB.pkl', 'rb'))
        elif model_name == 'GBM':
            model = pickle.load(open('models/Gradient Boosting.pkl', 'rb'))       
        return model


    # Fungsi prediksi
    def predict_status(model, data):
        predict = model.predict(data)
        return predict

    # Fungsi color
    def cpred(col):
        color = 'pink' if col == 'Dropout' else 'blue'
        return f'color: {color}'


    
        
    with st.expander("### 📌 How to run the prediction:"):
        st.markdown(
            """
            - 🏷 Choose machine learning model
            - 📂 Upload `Filetest.csv`in browse files 
            - 👨‍🎓 input count of student 
            - 🚀 Click predict button  
            - ☁️ Result will appear and can be 'Download (.csv)'📥
            """, unsafe_allow_html=True
        )



    
    def main():



        
        st.markdown("### Choose a Machine Learning Model 🤖 ")
        model_name = st.selectbox("", 
                        ("Random Forest", "Decision Tree", "Logistic Regression", 
                        "XGB", "GBM", "SVM"))




        st.sidebar.markdown("📁 Upload Filetest:")
        upload = st.sidebar.file_uploader(" ", type=["csv"])

        if upload is not None:
            data = pd.read_csv(upload)

            counting = st.number_input("input count of student", min_value=0, max_value=99, step=1)

            st.write(data.head(counting))

            # ID dan StudentName
            ID = data['ID']
            StudentName = data['Name']
            data = data.drop(columns=['ID', 'Name'])

            # Load model
            model = load_model(model_name)

            # click button
            if st.button('✨Predict'):
                # Prediction
                predict = predict_status(model, data)

                # Labelling
                labelling = ['Graduate' if pred == 1 else 'Dropout' for pred in predict]

                # Result
                result = pd.DataFrame({
                    'ID': ID,
                    'Name': StudentName,
                    'Status Prediction': labelling
                })

                
                st.write("Prediction result:") 
                st.dataframe(result.style.map(cpred, subset=['Status Prediction']))

                
                csv = result.to_csv(index=False) # Download result
                st.download_button(
                    label="Download Prediction Result 📥",
                    data=csv,
                    file_name='Prediction result.csv',
                    mime='text/csv'
                )

    if __name__ == '__main__':
        main()



with tab2:
    st.subheader("Student dashboard")
    st.markdown("[View Dashboard on Tableau Public](https://public.tableau.com/app/profile/win.wikind/viz/studentdashboard_17394505558280/Dashboard1?publish=yes)")

    st.image("https://github.com/user-attachments/assets/e808d9fa-6c30-45fb-9d21-a5161f42cf98")


    with st.expander("Summary: "):
        st.write(
            """
            1. High Dropout Rate (32.12%)

            Main contributing factors: academic debt, low admission scores, and delayed tuition payments.
            Students with scholarships have a higher graduation rate compared to those without scholarships.
            
            2. Large Number of Displaced Students (54.84%)

            Additional support, both financial and academic, is needed to improve their retention.
            
            3. Financial Issues Affect Academic Status

            Students with academic debt are more vulnerable to dropping out compared to those without debt.
            
            4. Some Study Programs Have High Dropout Rates

            Nursing and Management programs have a significant dropout rate.
            Study programs with a small number of students need to be evaluated to enhance their appeal.
            
            """
        )


    with st.expander("Recommendation: "):
            st.write(
                """
                Proposed Strategies to Reduce Dropout Rates

                1. Expansion of Scholarship Programs

                    Focus on students at risk of dropping out based on their financial status.
                2. Flexible Payment Options

                    Provide installment payment plans with 0% interest or partial debt/tuition forgiveness programs for high-achieving students.
                3. Gap Year Program with Academic Support

                    Offer a structured gap year program with special orientation for returning students to help them adjust to changes in the environment, technology, or curriculum.
                4. Academic Guidance for Students with Low Grades

                    Additional learning programs for students with low admission scores, especially for older and married students.
                5. Psychological & Counseling Support

                    Establish a psychological support and academic counseling center for students experiencing financial or academic stress.
                6. Monitoring and Predicting Dropouts

                    Conduct further review and monitoring of currently enrolled students.
                    Utilize machine learning technology to predict dropout risks, enabling early intervention.
                
                """
            )

    st.write("Based on this analysis, the university must strengthen its financial, academic, and psychological support programs to improve student success. By implementing more flexible and data-driven strategies, dropout rates can be significantly reduced, and the quality of education at Jaya Jaya Institute will continue to improve."
            )
    

with tab3:
    
    st.write(
            """
            
            Jaya Jaya Institute is a higher education institution that has been established since the year 2000. Over the years, it has produced many graduates with an excellent reputation. However, a significant number of students fail to complete their education and drop out.
            The high dropout rate is a major concern for an educational institution. Therefore, Jaya Jaya Institute aims to detect students at risk of dropping out as early as possible so that they can receive specialized guidance.

            """
            )





year_now = datetime.date.today().year
year = year_now if year_now == 2025 else f'2025 - {year_now}'
name = "[Wick|B244044F]"
copyright = 'Copyright © ' + str(year) + ' ' + name
st.caption(copyright)