# import os
# import streamlit as st
# from dotenv import load_dotenv
# from src.utils.helpers import *
# from src.generator.question_generator import QuestionGenerator
# load_dotenv()


# def main():
#     st.set_page_config(page_title="studdy Buddy AI" , page_icon="🎧🎧")

#     if 'quiz_manager'not in st.session_state:
#         st.session_state.quiz_manager = QuizManager()

#     if 'quiz_generated'not in st.session_state:
#         st.session_state.quiz_generated = False

#     if 'quiz_submitted'not in st.session_state:
#         st.session_state.quiz_submitted = False

#     if 'rerun_trigger'not in st.session_state:
#         st.session_state.rerun_trigger = False
        

#     st.title("Quiz Generator")

#     st.sidebar.header("Quiz Settings")

#     question_type = st.sidebar.selectbox(
#         "Select Question Type" ,
#         ["Multiple Choice" , "Fill in the Blank"],
#         index=0
#     )

#     topic = st.sidebar.text_input("Ennter Topic" , placeholder="Indian History, geography")

#     difficulty = st.sidebar.selectbox(
#         "Dificulty Level",
#         ["Easy" , "Medium" , "Hard"],
#         index=1
#     )

#     num_questions=st.sidebar.number_input(
#         "Number of Questions",
#         min_value=1,  max_value=10 , value=5
#     )

    

    
#     if st.sidebar.button("Generate Quiz"):
#         st.session_state.quiz_submitted = False

#         generator = QuestionGenerator()
#         succces = st.session_state.quiz_manager.generate_questions(
#             generator,
#             topic,question_type,difficulty,num_questions
#         )

#         st.session_state.quiz_generated= succces
#         rerun()

#     if st.session_state.quiz_generated and st.session_state.quiz_manager.questions:
#         st.header("Quiz")
#         st.session_state.quiz_manager.attempt_quiz()

#         if st.button("Submit Quiz"):
#             st.session_state.quiz_manager.evaluate_quiz()
#             st.session_state.quiz_submitted = True
#             rerun()

#     if st.session_state.quiz_submitted:
#         st.header("Quiz Results")
#         results_df = st.session_state.quiz_manager.generate_result_dataframe()

#         if not results_df.empty:
#             correct_count = results_df["is_correct"].sum()
#             total_questions = len(results_df)
#             score_percentage = (correct_count/total_questions)*100
#             st.write(f"Score : {score_percentage}")

#             for _, result in results_df.iterrows():
#                 question_num = result['question_number']
#                 if result['is_correct']:
#                     st.success(f"✅ Question {question_num} : {result['question']}")
#                 else:
#                     st.error(f"❌ Question {question_num} : {result['question']}")
#                     st.write(f"Your answer : {result['user_answer']}")
#                     st.write(f"Correct answer : {result['correct_answer']}")
                
#                 st.markdown("-------")

            
#             if st.button("Save Results"):
#                 saved_file = st.session_state.quiz_manager.save_to_csv()
#                 if saved_file:
#                     with open(saved_file,'rb') as f:
#                         st.download_button(
#                             label="Downlaod Results",
#                             data=f.read(),
#                             file_name=os.path.basename(saved_file),
#                             mime='text/csv'
#                         )
#                 else:
#                     st.warning("No results avialble")

# if __name__=="__main__":
#     main()

import os
import streamlit as st
import pandas as pd
from dotenv import load_dotenv
from src.utils.helpers import *
from src.generator.question_generator import QuestionGenerator

# Load Environment Secrets
load_dotenv()

# --- UI CONFIGURATION ---
st.set_page_config(
    page_title="Quiz Generator AI", 
    page_icon="🎓", 
    layout="centered"
)

# Custom Styling: Modern Pakistani Tech Aesthetic (Emerald & Gold)
st.markdown("""
    <style>
    :root {
        --pak-green: #006633;
        --gold: #C5A059;
    }
    .stApp {
        background-color: #fcfcfc;
    }
    .main-header {
        color: var(--pak-green);
        font-family: 'Jameel Noori Nastaleeq', sans-serif;
        font-size: 3rem;
        text-align: center;
        margin-bottom: 0px;
    }
    .sub-text {
        text-align: center;
        color: #666;
        font-style: italic;
        margin-bottom: 2rem;
    }
    div.stButton > button:first-child {
        background-color: var(--pak-green);
        color: white;
        border-radius: 8px;
        width: 100%;
        border: none;
        height: 3em;
    }
    .result-card {
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid var(--pak-green);
        background-color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    # --- HEADER SECTION ---
    st.markdown('<h1 class="main-header">Quiz Generator AI</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-text">Empowering the youth of Pakistan with AI-driven learning</p>', unsafe_allow_html=True)

    # --- SESSION STATE INITIALIZATION ---
    if 'quiz_manager' not in st.session_state:
        st.session_state.quiz_manager = QuizManager()
    if 'quiz_generated' not in st.session_state:
        st.session_state.quiz_generated = False
    if 'quiz_submitted' not in st.session_state:
        st.session_state.quiz_submitted = False

    # --- SIDEBAR: SETTINGS ---
    with st.sidebar:
        # st.image("https://img.icons8.com/wired/512/006633/education.png", width=100)
        st.title("Settings")
        st.divider()
        
        topic = st.text_input("Enter Subject/Topic", placeholder="e.g. Pakistan Studies, AI, Physics")
        question_type = st.selectbox("Format", ["Multiple Choice", "Fill in the Blank"])
        difficulty = st.select_slider("Difficulty", options=["Easy", "Medium", "Hard"], value="Medium")
        num_questions = st.number_input("Questions", 1, 10, 5)
        
        st.divider()
        if st.button("✨ Generate New Quiz"):
            with st.spinner("Preparing your personalized quiz..."):
                st.session_state.quiz_submitted = False
                generator = QuestionGenerator()
                success = st.session_state.quiz_manager.generate_questions(
                    generator, topic, question_type, difficulty, num_questions
                )
                st.session_state.quiz_generated = success
                st.rerun()

    # --- MAIN CONTENT AREA ---
    if st.session_state.quiz_generated and st.session_state.quiz_manager.questions:
        if not st.session_state.quiz_submitted:
            st.markdown("### 📝 Knowledge Assessment")
            st.session_state.quiz_manager.attempt_quiz()
            
            if st.button("Finalize & Submit"):
                st.session_state.quiz_manager.evaluate_quiz()
                st.session_state.quiz_submitted = True
                st.rerun()
        
        else:
            # --- RESULTS DASHBOARD ---
            st.markdown("### 📊 Performance Analytics")
            results_df = st.session_state.quiz_manager.generate_result_dataframe()

            if not results_df.empty:
                correct = results_df["is_correct"].sum()
                total = len(results_df)
                score = int((correct/total)*100)

                # Big Score Metric
                cols = st.columns(3)
                cols[0].metric("Score", f"{score}%")
                cols[1].metric("Correct", f"{correct}/{total}")
                cols[2].metric("Status", "Passed" if score >= 50 else "Keep Trying")

                st.divider()

                # Result Cards
                for _, res in results_df.iterrows():
                    color = "#28a745" if res['is_correct'] else "#dc3545"
                    icon = "✅" if res['is_correct'] else "❌"
                    
                    with st.container():
                        st.markdown(f"""
                            <div class="result-card">
                                <strong>Question {res['question_number']}:</strong> {res['question']}<br>
                                <span style="color:{color}">{icon} Your Answer: {res['user_answer']}</span><br>
                                {"" if res['is_correct'] else f"<b>Correct:</b> {res['correct_answer']}"}
                            </div>
                        """, unsafe_allow_html=True)

                # Action Buttons
                col_a, col_b = st.columns(2)
                with col_a:
                    if st.button("🔄 Retake Quiz"):
                        st.session_state.quiz_submitted = False
                        st.rerun()
                with col_b:
                    saved_file = st.session_state.quiz_manager.save_to_csv()
                    if saved_file:
                        with open(saved_file, 'rb') as f:
                            st.download_button("📥 Download Report (CSV)", f, file_name=os.path.basename(saved_file))

if __name__ == "__main__":
    main()