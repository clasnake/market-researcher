import streamlit as st

from researcher import MarketResearcherV1
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

researcher = MarketResearcherV1()

def render_page():
    st.title("Market Researcher")

    if 'result' not in st.session_state:
        st.session_state.result = ""

    def on_submit():
        logger.info('Submitting...')
        report = researcher.research_for_company_type(st.session_state.user_input)
        logger.info(report)
        st.session_state.result = report

    input_container = st.container()
    with input_container:
        col1, col2 = st.columns([5, 1])
        with col1:
            user_input = st.text_input("Enter the company type here", 
                                     label_visibility="collapsed",
                                     key="user_input")
        with col2:
            submit_button = st.button("Submit", 
                                    use_container_width=True, 
                                    type="primary",
                                    on_click=on_submit)

    result_area = st.text_area("Results", value=st.session_state.result, height=200, disabled=True)


if __name__ == "__main__":
    render_page()
