import streamlit as st
import docx2txt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


st.set_page_config(layout='wide')

st.cache(allow_output_mutation=True)

def main():
    st.title('CV Scanner App')
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader('Paste your CV below')
        cv = st.text_area('')
    with right_column:
        st.subheader('Paste Job Description Here')
        description=st.text_area(' ')


    text=[cv, description]
    if st.button('Generate Score'):
        cv_1 = CountVectorizer()
        countmatrix = cv.fit_transform(text)

    #def similarity_test():
        #text = [cv, description]
        #cv_1 = CountVectorizer()
        #countmatrix = cv.fit_transform(text)
        #matchPercentage = cosine_similarity(countmatrix)[0][1]*100
        #matchPercentage = round(matchPercentage, 2)
        #a = print('Your resume has a score for' + str(matchPercentage)+ '%')
        #st.write(a)

    #if cv and description is not None:
        #if st.button('Generate Score'):
            #similarity_test()


if __name__=='__main__':
    main()
