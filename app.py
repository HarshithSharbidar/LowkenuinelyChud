import streamlit as st

from document_processor import extract_text, split_into_sentences
from knowledge_base import KnowledgeBase
from reasoning_engine import ReasoningEngine
from question_processor import process_question
from answer_generator import generate_answer


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="LowkenuinelyChud",
    page_icon="🎪",
    layout="wide"
)


# ==========================================
# CUSTOM CSS
# ==========================================

st.html("""
<style>

.stApp {
    background-color: #FAF6EB;
    color: #39352F;
}

.block-container {
    max-width: 1050px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Headings */

h1, h2, h3 {
    color: #39352F !important;
    font-family: "Trebuchet MS", sans-serif;
}

/* Buttons */

.stButton > button {
    background-color: #D96B59;
    color: white;
    border: 2px solid #39352F;
    border-radius: 12px;
    font-weight: bold;
    box-shadow: 3px 3px 0px #39352F;
    transition: 0.2s;
}

.stButton > button:hover {
    background-color: #BF5548;
    color: white;
    transform: translateY(-2px);
}

/* Text input */

.stTextInput input {
    background-color: #FFFEFA;
    color: #39352F;
    border: 2px solid #C8BDA9;
    border-radius: 12px;
}

/* File uploader */

[data-testid="stFileUploader"] {
    background-color: #FFFDF6;
    border: 2px dashed #D96B59;
    border-radius: 16px;
    padding: 15px;
}

/* Metrics */

[data-testid="stMetric"] {
    background-color: #F3E8C9;
    padding: 15px;
    border: 1px solid #D8CBA9;
    border-radius: 12px;
}

/* Alerts */

.stAlert {
    border-radius: 12px;
}

/* Dividers */

hr {
    border-color: #DED3BE;
}

</style>
""")


# ==========================================
# HOMEPAGE
# ==========================================

st.html("""
<div style="
    text-align: center;
    padding: 20px 10px 10px 10px;
">

    <div style="
        color: #D96B59;
        font-size: 17px;
        letter-spacing: 5px;
        margin-bottom: 12px;
    ">
        ★ ─── THE KNOWLEDGE CARNIVAL ─── ★
    </div>

    <h1 style="
        font-family: 'Trebuchet MS', sans-serif;
        font-size: clamp(34px, 6vw, 54px);
        font-weight: 900;
        color: #39352F;
        margin: 0;
    ">
        LowkenuinelyChud
    </h1>

    <p style="
        color: #A45B4D;
        font-size: 18px;
        font-style: italic;
        margin-top: 8px;
    ">
        bro just read the document.
    </p>

    <div style="
        display: inline-block;
        background: #F2D98F;
        padding: 8px 20px;
        border-radius: 10px;
        border: 1px dashed #B79B5C;
        color: #514633;
        font-size: 14px;
        margin-top: 8px;
    ">
        A little knowledge goes a long way.
    </div>

</div>
""")


st.write("")

st.markdown("""
### 🎟️ Welcome, curious human!

Bring a document. Ask a question. Let Chud do the reading.

No boring manual searching. No unnecessary drama.
""")

st.divider()


# ==========================================
# DOCUMENT UPLOAD
# ==========================================

st.markdown("### 📎 One document, please!")

uploaded_file = st.file_uploader(
    "Choose your document",
    type=["txt", "pdf", "docx"],
    help="Supported formats: PDF, DOCX and TXT."
)


if uploaded_file:

    try:

        # Extract document text
        text = extract_text(uploaded_file)

        if not text:
            st.error("The uploaded document is empty.")
            st.stop()

        # Split document into sentences
        sentences = split_into_sentences(text)

        # Build Knowledge Base
        kb = KnowledgeBase()
        kb.add_facts(sentences)

        # Initialize Reasoning Engine
        engine = ReasoningEngine()
        engine.load_rules(sentences)

        st.success("Chud has successfully processed your document!")

        # Document statistics
        st.markdown("### 🎠 Document statistics")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Total Sentences",
            len(sentences)
        )

        col2.metric(
            "Knowledge Base Facts",
            len(kb.facts)
        )

        col3.metric(
            "Rules Identified",
            len(engine.rules)
        )

        st.divider()


        # ==========================================
        # QUESTION INPUT
        # ==========================================

        st.markdown("### 💭 What's on your mind?")

        question = st.text_input(
            "Ask your document something:",
            placeholder="What information are you looking for?"
        )

        if st.button("Find my answer ✨"):

            if not question.strip():

                st.warning("Come on, ask Chud something!")

            else:

                # Process question
                processed_question = process_question(question)

                # Retrieve relevant information
                search_results = kb.search(
                    processed_question["original_question"]
                )

                # Select relevant facts
                relevant_facts = [
                    result["sentence"]
                    for result in search_results[:5]
                ]

                # Apply logical reasoning
                inferred_answers = engine.apply_rules(
                    question,
                    relevant_facts
                )

                # Generate final answer
                answer = generate_answer(
                    search_results,
                    inferred_answers
                )

                st.markdown("### 🎪 Here's what Chud found!")

                st.info(answer)


                # ==========================================
                # SUPPORTING INFORMATION
                # ==========================================

                with st.expander("📚 View retrieved information"):

                    if search_results:

                        for result in search_results[:10]:

                            st.write(
                                f"**Relevance:** "
                                f"{result['score']:.2f}"
                            )

                            st.write(result["sentence"])

                            st.divider()

                    else:

                        st.write(
                            "No relevant information retrieved."
                        )


                # ==========================================
                # QUESTION ANALYSIS
                # ==========================================

                with st.expander("🔍 Question analysis"):

                    st.write(
                        "Question Type:",
                        processed_question["question_type"]
                    )

                    st.write(
                        "Extracted Keywords:",
                        processed_question["keywords"]
                    )


    except Exception as error:

        st.error(f"An error occurred: {error}")


else:

    st.info(
        "Your document is waiting! Upload a PDF, DOCX or TXT "
        "file to get started."
    )


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.html("""
<div style="
    text-align: center;
    padding: 12px;
    color: #927F69;
    font-size: 13px;
">
    Made with questionable levels of enthusiasm.
    <br>
    <b>LowkenuinelyChud</b> · Knowledge. Chaos. Carnival. 🎪
</div>
""")