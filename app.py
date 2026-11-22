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
# CUSTOM DESIGN
# ==========================================

st.html("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=DM+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@500;600;700;800&display=swap');

:root {
    --cream: #FAF7F0;
    --paper: #FFFEFA;
    --red: #B94036;
    --dark: #302C29;
    --muted: #827A70;
    --yellow: #F2D994;
    --blue: #DCE8ED;
    --green: #E1E9DA;
    --border: #E8DFD1;
}

.stApp {
    background-color: var(--cream);
    color: var(--dark);
    font-family: 'DM Sans', sans-serif;
}

.block-container {
    max-width: 1050px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

/* Typography */

h1, h2, h3 {
    font-family: 'Playfair Display', serif !important;
    color: var(--dark) !important;
}

p, label, span {
    font-family: 'DM Sans', sans-serif;
}

/* Header */

.brand-strip {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid var(--border);
    padding-bottom: 16px;
    margin-bottom: 55px;
}

.brand-name {
    font-family: 'DM Sans', sans-serif;
    font-weight: 800;
    font-size: 17px;
    color: var(--dark);
    letter-spacing: -0.5px;
}

.brand-tag {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    color: var(--red);
    letter-spacing: 2px;
}

/* Hero */

.hero-eyebrow {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    letter-spacing: 3px;
    color: var(--red);
    text-transform: uppercase;
    margin-bottom: 20px;
}

.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(45px, 7vw, 76px);
    font-weight: 700;
    line-height: 1.05;
    letter-spacing: -3px;
    color: var(--dark);
    margin: 0;
}

.hero-title span {
    color: var(--red);
    font-style: italic;
}

.hero-description {
    color: var(--muted);
    font-size: 17px;
    line-height: 1.8;
    max-width: 520px;
    margin-top: 20px;
}

.hero-note {
    display: inline-block;
    margin-top: 20px;
    padding: 9px 15px;
    background: var(--yellow);
    border-radius: 5px;
    font-size: 12px;
    color: #62543A;
    transform: rotate(-1deg);
}

/* Section headings */

.section-label {
    font-family: 'DM Mono', monospace;
    color: var(--red);
    font-size: 11px;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 10px;
}

.section-heading {
    font-family: 'Playfair Display', serif;
    font-size: 27px;
    font-weight: 600;
    color: var(--dark);
    margin-bottom: 5px;
}

.section-description {
    color: var(--muted);
    font-size: 14px;
    margin-bottom: 20px;
}

/* Upload section */

[data-testid="stFileUploader"] {
    background: var(--paper);
    border: 1px dashed #C9A69C;
    border-radius: 15px;
    padding: 20px;
}

[data-testid="stFileUploader"] section {
    background: transparent;
}

/* Buttons */

.stButton > button,
.stFormSubmitButton > button {
    background: var(--red);
    color: white;
    border: 1px solid var(--red);
    border-radius: 8px;
    padding: 10px 22px;
    font-weight: 700;
    transition: all 0.2s ease;
}

.stButton > button:hover,
.stFormSubmitButton > button:hover {
    background: #96342C;
    color: white;
    border-color: #96342C;
    transform: translateY(-2px);
}

/* Input fields */

.stTextInput input {
    background: var(--paper);
    color: var(--dark);
    border: 1px solid #D8CFC1;
    border-radius: 9px;
    padding: 13px;
}

.stTextInput input:focus {
    border-color: var(--red);
    box-shadow: 0 0 0 1px var(--red);
}

/* Metrics */

[data-testid="stMetric"] {
    background: var(--paper);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 18px;
}

[data-testid="stMetricLabel"] {
    color: var(--muted);
}

[data-testid="stMetricValue"] {
    color: var(--red);
    font-family: 'Playfair Display', serif;
}

/* Alerts */

.stAlert {
    border-radius: 10px;
}

/* Expanders */

[data-testid="stExpander"] {
    background: var(--paper);
    border: 1px solid var(--border);
    border-radius: 10px;
}

/* Dividers */

hr {
    border-color: var(--border);
    margin-top: 30px;
    margin-bottom: 30px;
}

/* Footer */

.footer {
    text-align: center;
    padding: 30px 10px 10px;
    color: var(--muted);
    font-size: 12px;
    line-height: 2;
}

.footer strong {
    color: var(--red);
}

</style>
""")


# ==========================================
# HEADER
# ==========================================

st.html("""
<div class="brand-strip">
    <div class="brand-name">lowk<span style="color:#B94036">.</span>chud</div>
    <div class="brand-tag">A DOCUMENT QUESTIONING MACHINE</div>
</div>
""")


# ==========================================
# HERO SECTION
# ==========================================

st.html("""
<div style="padding: 5px 0 45px 0;">

    <div class="hero-eyebrow">
        ✳ THE KNOWLEDGE CARNIVAL · EST. 2026
    </div>

    <div class="hero-title">
        Lowkenuinely<br>
        <span>Chud.</span>
    </div>

    <div class="hero-description">
        You bring the document. You ask the questions.
        Chud does the reading, finds the facts,
        and connects the dots.
    </div>

    <div class="hero-note">
        bro just read the document.
    </div>

</div>
""")


# ==========================================
# DOCUMENT UPLOAD
# ==========================================

st.html("""
<div class="section-label">01 / THE INPUT</div>
<div class="section-heading">First, bring the receipts.</div>
<div class="section-description">
    Upload a document and let Chud get acquainted with it.
</div>
""")

uploaded_file = st.file_uploader(
    "Drop your document here",
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

        st.success("Chud has read the document. We're so back.")

        st.write("")

        # ==========================================
        # DOCUMENT STATISTICS
        # ==========================================

        st.html("""
        <div class="section-label">02 / THE BREAKDOWN</div>
        <div class="section-heading">A little document intelligence.</div>
        <div class="section-description">
            Here's what Chud found inside your document.
        </div>
        """)

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

        st.html("""
        <div class="section-label">03 / THE INTERROGATION</div>
        <div class="section-heading">Okay, what's the question?</div>
        <div class="section-description">
            Ask Chud anything about the uploaded document.
        </div>
        """)

        with st.form("question_form"):

            question = st.text_input(
                "Your question",
                placeholder="What information are you looking for?"
            )

            submitted = st.form_submit_button(
                "Find my answer  →"
            )

        if submitted:

            if not question.strip():

                st.warning("Come on, ask Chud something.")

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

                st.write("")

                st.html("""
                <div class="section-label">04 / THE VERDICT</div>
                <div class="section-heading">Chud's got something for you.</div>
                """)

                st.info(answer)

                # ==========================================
                # SUPPORTING INFORMATION
                # ==========================================

                with st.expander("📚 Explore retrieved information"):

                    if search_results:

                        for result in search_results[:10]:

                            st.caption(
                                f"RELEVANCE SCORE: "
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

                with st.expander("🔍 Explore question analysis"):

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
        "Your document is waiting. Upload a PDF, DOCX or TXT "
        "file to get started."
    )


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.html("""
<div class="footer">

    Made with questionable levels of enthusiasm.

    <br>

    <strong>LowkenuinelyChud</strong>
    · Knowledge. Chaos. Carnival. 🎪

    <br>

    © 2026 · Built to make reading less of a chore.

</div>
""")
