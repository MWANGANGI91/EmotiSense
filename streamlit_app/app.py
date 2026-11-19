
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import streamlit as st


# ==================================================
# 1. PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="EmotiSense | Emotion AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

APP_DIR = Path(__file__).resolve().parent
ARTIFACT_DIR = APP_DIR.parent / "model_artifacts"



# ==================================================
# 2. PREMIUM EMOTISENSE DESIGN
# ==================================================

st.markdown("""
<style>

/* MAIN APPLICATION BACKGROUND */

.stApp {
    background: linear-gradient(
        135deg,
        #080D1B 0%,
        #101A32 55%,
        #15102B 100%
    );
    color: #F8FAFC !important;
}

/* GENERAL TEXT VISIBILITY */

html, body, p, span, label, li,
div[data-testid="stMarkdownContainer"] {
    color: #E2E8F0;
}

h1, h2, h3, h4, h5 {
    color: #FFFFFF !important;
    font-weight: 700 !important;
}

p {
    color: #DCE6F5 !important;
    line-height: 1.65;
}

/* SIDEBAR */

[data-testid="stSidebar"] {
    background: #111A30;
    border-right: 1px solid #344365;
}

[data-testid="stSidebar"] h1 {
    color: #C4B5FD !important;
}

[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] span {
    color: #E2E8F0 !important;
}

/* HERO BANNER */

.hero {
    padding: 35px;
    border-radius: 20px;
    background: linear-gradient(
        120deg,
        #35206B,
        #1D3B70,
        #164E63
    );
    border: 1px solid #8B5CF6;
    margin-bottom: 28px;
    box-shadow: 0 12px 35px rgba(0, 0, 0, 0.3);
}

.hero h1 {
    color: #FFFFFF !important;
    font-size: 46px;
    font-weight: 800;
    margin-bottom: 10px;
}

.hero p {
    color: #F1F5F9 !important;
    font-size: 17px;
}

.hero .small-muted {
    color: #D8CCFF !important;
    font-size: 13px;
}

/* METRIC CARDS */

div[data-testid="stMetric"] {
    background: linear-gradient(
        145deg,
        #1C2945,
        #202B4B
    );
    border: 1px solid #53658D;
    border-radius: 15px;
    padding: 19px;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.2);
}

div[data-testid="stMetricLabel"] {
    color: #C4B5FD !important;
}

div[data-testid="stMetricValue"] {
    color: #FFFFFF !important;
    font-weight: 800 !important;
}

/* INPUT BOXES */

.stTextArea textarea,
.stTextInput input {
    background-color: #17233D !important;
    color: #FFFFFF !important;
    border: 1px solid #6476A3 !important;
    border-radius: 10px !important;
    font-size: 16px !important;
}

.stTextArea textarea::placeholder {
    color: #AAB8D0 !important;
    opacity: 1;
}

/* BUTTONS */

.stButton > button {
    background: linear-gradient(
        90deg,
        #7C3AED,
        #4F46E5
    ) !important;
    color: #FFFFFF !important;
    border: 1px solid #A78BFA !important;
    border-radius: 10px !important;
    padding: 10px 20px !important;
    font-weight: 700 !important;
    transition: 0.2s ease;
}

.stButton > button:hover {
    background: linear-gradient(
        90deg,
        #9333EA,
        #6366F1
    ) !important;
    border: 1px solid #DDD6FE !important;
}

/* DATA TABLES */

[data-testid="stDataFrame"] {
    border: 1px solid #475569;
    border-radius: 12px;
    overflow: hidden;
}

/* TABS AND NAVIGATION */

.stTabs [data-baseweb="tab"] {
    color: #DCE6F5 !important;
}

.stTabs [aria-selected="true"] {
    color: #C4B5FD !important;
    border-bottom-color: #A78BFA !important;
}

/* EXPANDERS */

[data-testid="stExpander"] {
    background: #17233D;
    border: 1px solid #475569;
    border-radius: 12px;
}

[data-testid="stExpander"] summary {
    color: #FFFFFF !important;
}

/* ALERTS */

[data-testid="stAlert"] {
    border-radius: 12px;
}

/* DIVIDERS */

hr {
    border-color: #394867 !important;
}

/* CAPTIONS */

.stCaption,
[data-testid="stCaptionContainer"] {
    color: #B6C5DC !important;
}

/* RADIO BUTTONS */

[data-testid="stRadio"] label {
    color: #E2E8F0 !important;
}

/* FOOTER */

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)
# ==================================================
# 3. LOAD MODEL AND RESULTS
# ==================================================

@st.cache_resource
def load_model_bundle():
    path = ARTIFACT_DIR / "goemotions_emotion_classifier.joblib"

    if not path.exists():
        raise FileNotFoundError(f"Model not found: {path}")

    return joblib.load(path)


@st.cache_data
def load_results():
    path = ARTIFACT_DIR / "per_emotion_test_results.csv"

    if not path.exists():
        return pd.DataFrame()

    return pd.read_csv(path)


try:
    bundle = load_model_bundle()
    model = bundle["model"]
    emotions = bundle["emotion_labels"]
    thresholds = np.asarray(
        bundle["individual_thresholds"]
    )

    per_emotion_results = load_results()

except Exception as error:
    st.error(f"Unable to load the model or results: {error}")
    st.stop()


# ==================================================
# 4. PREDICTION FUNCTION
# ==================================================

def analyse_text(text):

    probabilities = model.predict_proba([text])[0]

    selected = np.where(probabilities >= thresholds)[0]

    selected = sorted(
        selected,
        key=lambda index: probabilities[index],
        reverse=True
    )

    top_indices = np.argsort(probabilities)[::-1][:5]

    predictions = [
        {
            "Emotion": emotions[i].capitalize(),
            "Probability (%)": round(
                float(probabilities[i]) * 100, 2
            )
        }
        for i in selected
    ]

    suggestions = [
        {
            "Emotion": emotions[i].capitalize(),
            "Probability (%)": round(
                float(probabilities[i]) * 100, 2
            ),
            "Threshold met": bool(
                probabilities[i] >= thresholds[i]
            )
        }
        for i in top_indices
    ]

    return predictions, suggestions


# ==================================================
# 5. SIDEBAR NAVIGATION
# ==================================================

with st.sidebar:

    st.markdown("# 🧠 EmotiSense")
    st.caption("AI-powered emotion analysis")

    st.markdown("---")

    page = st.radio(
        "NAVIGATION",
        [
            "Overview",
            "Emotion Studio",
            "Model Insights",
            "Research & Business"
        ]
    )

    st.markdown("---")

    st.markdown("### Model information")
    st.caption("TF-IDF + One-vs-Rest Logistic Regression")
    st.caption("28 emotion categories")
    st.caption("Multi-label classification")

    st.markdown("---")

    st.caption("EmotiSense | Portfolio Edition")


# ==================================================
# 6. OVERVIEW PAGE
# ==================================================

if page == "Overview":

    st.markdown("""
    <div class="hero">
        <h1>EmotiSense 🧠</h1>
        <p>
        Understand emotional expressions in written text
        using machine learning and natural language processing.
        </p>
        <p class="small-muted">
        An experimental AI platform for researchers,
        businesses and data enthusiasts.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Platform overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Emotion categories", "28")
    col2.metric("Training records", "43,410")
    col3.metric("Test records", "5,427")
    col4.metric("Test Micro F1", "53.75%")

    st.markdown("---")

    st.subheader("Explore EmotiSense")

    left, right = st.columns(2)

    with left:
        st.markdown("### ✍️ Emotion Studio")
        st.write(
            "Enter text and explore the emotions "
            "identified by the trained model."
        )

    with right:
        st.markdown("### 📊 Model Insights")
        st.write(
            "Review model performance, compare emotion "
            "categories and understand model limitations."
        )

    st.info(
        "EmotiSense analyses emotional language patterns. "
        "It cannot determine a person's true emotional state "
        "or diagnose a mental-health condition."
    )


# ==================================================
# 7. EMOTION STUDIO PAGE
# ==================================================

elif page == "Emotion Studio":

    st.title("✍️ Emotion Studio")

    st.write(
        "Enter a sentence or paragraph to explore "
        "the model's emotion predictions."
    )

    user_text = st.text_area(
        "Your text",
        placeholder=(
            "Example: I am excited about my new opportunity!"
        ),
        height=160,
        max_chars=5000
    )

    if st.button("Analyse Emotions", use_container_width=True):

        if not user_text.strip():

            st.warning("Please enter some text first.")

        else:

            with st.spinner("Analysing your text..."):

                predictions, suggestions = analyse_text(
                    user_text.strip()
                )

            st.markdown("---")
            st.subheader("Analysis results")

            if predictions:

                st.success(
                    f"{len(predictions)} threshold-qualified "
                    "emotion(s) identified."
                )

                result_df = pd.DataFrame(predictions)

                st.dataframe(
                    result_df,
                    use_container_width=True,
                    hide_index=True
                )

                chart_df = result_df.set_index("Emotion")

                st.markdown("### Emotion probability chart")

                st.bar_chart(
                    chart_df,
                    y="Probability (%)"
                )

            else:

                st.warning(
                    "No emotion passed its individual "
                    "classification threshold."
                )

            st.markdown("### Top five suggestions")

            suggestion_df = pd.DataFrame(suggestions)

            st.dataframe(
                suggestion_df,
                use_container_width=True,
                hide_index=True
            )

            st.caption(
                "Probabilities are model scores, not calibrated "
                "confidence estimates or measurements of a person's "
                "psychological state."
            )


# ==================================================
# 8. MODEL INSIGHTS PAGE
# ==================================================

elif page == "Model Insights":

    st.title("📊 Model Insights")

    st.write(
        "Evaluation results from the held-out GoEmotions test set."
    )

    st.subheader("Overall performance")

    col1, col2, col3 = st.columns(3)

    col1.metric("Micro F1", "53.75%")
    col2.metric("Macro F1", "45.86%")
    col3.metric("Micro Precision", "48.28%")

    col4, col5, col6 = st.columns(3)

    col4.metric("Micro Recall", "60.63%")
    col5.metric("Hamming Loss", "4.35%")
    col6.metric("Exact Match", "33.78%")

    st.markdown("---")

    st.subheader("Performance by emotion")

    if not per_emotion_results.empty:

        results = per_emotion_results.copy()
        results.columns = [
            str(column).strip().lower()
            for column in results.columns
        ]

        emotion_col = next(
            (c for c in ["emotion", "label", "class"] if c in results),
            None
        )

        f1_col = next(
            (c for c in ["f1", "f1_score", "f1-score"] if c in results),
            None
        )

        if emotion_col and f1_col:

            results[f1_col] = pd.to_numeric(
                results[f1_col], errors="coerce"
            )

            results = results.dropna(subset=[f1_col])
            results = results.sort_values(f1_col, ascending=False)

            chart = results[[emotion_col, f1_col]].copy()
            chart[f1_col] = chart[f1_col] * 100
            chart = chart.set_index(emotion_col)

            st.bar_chart(chart)

            st.dataframe(
                results,
                use_container_width=True,
                hide_index=True
            )

        else:
            st.warning(
                "The emotion results file has unexpected column names."
            )

    else:

        st.warning("Per-emotion evaluation file was not found.")

    with st.expander("Understanding these metrics"):

        st.write("""
        - Micro F1 combines performance across all emotion labels.
        - Macro F1 gives each emotion equal weight.
        - Precision measures the proportion of positive predictions
          that were correct.
        - Recall measures the proportion of actual positive labels
          that were identified.
        - Hamming Loss measures incorrect individual label decisions.
        - Exact Match requires the complete predicted label set
          to match the actual label set.
        """)

    st.info(
        "These are held-out test results for the selected "
        "individual-threshold model. They should not be interpreted "
        "as evidence of clinical validity."
    )


# ==================================================
# 9. RESEARCH AND BUSINESS PAGE
# ==================================================

elif page == "Research & Business":

    st.title("🔬 Research & Business")

    st.subheader("About the project")

    st.write("""
    EmotiSense is an experimental natural language processing
    application that classifies emotional expressions in text.

    It uses the Google Research GoEmotions dataset and a
    TF-IDF feature extraction pipeline combined with
    One-vs-Rest Logistic Regression.
    """)

    st.subheader("Potential applications")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🏢 Business")
        st.write("""
        - Exploring customer feedback
        - Analysing product reviews
        - Summarising survey responses
        - Supporting customer-experience research
        """)

    with col2:
        st.markdown("### 🎓 Research")
        st.write("""
        - Exploring emotion classification
        - NLP experimentation
        - Comparing machine-learning models
        - Studying multi-label evaluation
        """)

    st.subheader("Methodology")

    st.write("""
    1. Text data preparation
    2. Multi-label target encoding
    3. TF-IDF feature extraction
    4. One-vs-Rest Logistic Regression
    5. Validation-based threshold selection
    6. Held-out test evaluation
    """)

    st.subheader("Limitations and responsible use")

    st.warning("""
    EmotiSense is not a mental-health diagnostic system.

    The training data consists of English Reddit comments.
    Its predictions may not generalise to Kenyan languages,
    cultural expressions or all forms of communication.

    Model predictions can be incorrect and should not be used
    to make consequential decisions about individuals.
    """)

    st.caption(
        "Dataset: Google Research GoEmotions. "
        "Research and demonstration use."
    )


# ==================================================
# 10. FOOTER
# ==================================================

st.markdown("---")

st.markdown(
    """
    <p style="text-align:center; color:#94A3B8; font-size:13px;">
    EmotiSense | AI-powered emotion classification
    <br>
    Developed by R. Mbinya | Data Science Portfolio Project
    </p>
    """,
    unsafe_allow_html=True
)
