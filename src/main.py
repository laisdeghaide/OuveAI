import streamlit as st
from backend.pipeline import Pipeline

st.markdown('<style>.st-emotion-cache-10trblm{width: 100px; background: -webkit-linear-gradient(right, #5FD7F1,#0594FA);-webkit-background-clip: text;-webkit-text-fill-color: transparent; font-weight:900;}.st-emotion-cache-19rxjzo:hover{color:#0E98FA; border-color: #0E98FA}</style>', unsafe_allow_html=True)

st.title('OuveAI')
form = st.form(key='script_form')


with form:
    script_file = st.file_uploader('Script:')
    generate_soundtrack = form.form_submit_button('Generate soundtrack')

    if generate_soundtrack:
        if not script_file:
            st.error('Você não subiu nenhum arquivo.')

        else:
            pip = Pipeline()
            tracklist = pip.execute_pipeline(script_file)
            for song in tracklist:
                st.markdown("""---""")
                st.markdown("####" + song.title)
                st.write(song.artist)