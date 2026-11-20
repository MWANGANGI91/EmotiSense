# EmotiSense: AI-Powered Emotion Analysis

**Developed by R. Mbinya**  
**Project type:** Natural language processing (NLP) · Multi-label text classification · Streamlit deployment

[**Launch the live application**](https://emotisense-ikjvg3tbej7h5whswryugn.streamlit.app/) · [**GitHub repository**](https://github.com/MWANGANGI91/EmotiSense)

---

## 1. Executive summary

EmotiSense is an experimental machine-learning application that analyses written text and predicts possible emotional expressions across 28 emotion categories. It uses a TF-IDF text representation and a One-vs-Rest Logistic Regression classifier. The model was trained and evaluated using the GoEmotions dataset, and the resulting application was deployed with Streamlit Community Cloud.

The project demonstrates an end-to-end data science workflow: dataset inspection, text preparation, exploratory analysis, model development, threshold selection, evaluation, packaging, and deployment. It is intended as a research and portfolio demonstration—not as a clinical or psychological assessment tool.

## 2. Problem and project objectives

Written feedback, comments, and other text can contain more than one emotional expression. A single-label classifier would force each text into only one category, even when several labels may be relevant.

EmotiSense explores a multi-label approach: for each input, the model estimates scores for multiple emotion categories and applies decision thresholds to determine which labels qualify for output.

Project objectives:

- Build a reproducible multi-label text-classification pipeline.
- Explore the distribution and characteristics of emotion-labelled text.
- Compare default and tuned decision-threshold strategies.
- Evaluate performance using metrics suitable for multi-label classification.
- Package the trained model in an interactive application.
- Communicate limitations and responsible-use considerations clearly.

## 3. Dataset

The project uses **GoEmotions**, an English-language dataset of Reddit comments annotated with 27 emotion labels plus a neutral category (28 categories in total).

The official dataset splits used in this project contain:

| Split | Records |
|---|---:|
| Training | 43,410 |
| Validation / development | 5,426 |
| Test | 5,427 |
| **Total** | **54,263** |

The official splits were retained for model development and evaluation.

### Data-quality observations

The dataset audit found:

- No missing text, labels, or comment IDs in the inspected records.
- No empty text entries.
- No duplicate comment IDs.
- 269 duplicate text instances.
- 71 unique text strings appearing across different splits, representing 215 records.
- 27 cross-split text strings had differing labels.

These repeated texts are a potential source of evaluation leakage or ambiguity. The official splits were retained for this project, and the overlap should be considered when interpreting the evaluation. A supplementary group-aware evaluation that keeps identical text strings together across splits would be a useful robustness check.

## 4. Methodology

### 4.1 Text representation: TF-IDF

The text was transformed into numerical features using Term Frequency–Inverse Document Frequency (TF-IDF). The configuration used:

- Maximum features: 50,000
- N-grams: unigrams and bigrams
- Minimum document frequency: 2
- Maximum document frequency: 0.95
- Sublinear term frequency: enabled
- Unicode accent stripping

This representation gives greater weight to terms that are informative within the corpus while reducing the influence of very common terms.

### 4.2 Classifier: One-vs-Rest Logistic Regression

A Logistic Regression classifier was trained for each emotion category through a One-vs-Rest strategy. This supports multi-label prediction because each emotion is treated as a separate binary classification task.

The classifier used the `liblinear` solver and a maximum of 1,000 iterations.

### 4.3 Decision-threshold selection

The model produces a score for each emotion. A threshold determines whether a score is treated as a positive prediction. The default threshold of 0.50 was evaluated as a baseline.

Thresholds were then tuned using the development split. The selected primary strategy used individual thresholds for each emotion. A global threshold of 0.175 was also evaluated as an alternative.

The test split was kept separate from threshold selection and used for final evaluation.

## 5. Evaluation results

The selected per-emotion threshold strategy produced the following test results:

| Metric | Test result |
|---|---:|
| Micro F1 | **0.5375** |
| Macro F1 | **0.4586** |
| Precision | 0.4828 |
| Recall | 0.6063 |
| Hamming Loss | 0.0435 |
| Exact Match | 0.3378 |

### Comparison with the default threshold

| Metric | Default threshold (0.50) | Tuned per-emotion thresholds |
|---|---:|---:|
| Micro F1 | 0.3850 | **0.5375** |
| Macro F1 | 0.1979 | **0.4586** |
| Precision | 0.7384 | 0.4828 |
| Recall | 0.2604 | **0.6063** |
| Hamming Loss | **0.0346** | 0.0435 |
| Exact Match | 0.2530 | **0.3378** |

Threshold tuning substantially improved Micro F1, Macro F1, recall, and exact-match accuracy, while precision decreased and Hamming Loss increased. This illustrates the trade-off between identifying more relevant labels and making additional false-positive predictions. The preferred threshold strategy therefore depends on the intended use and the relative costs of false positives and false negatives.

For context, the global-threshold alternative (0.175) achieved test Micro F1 of 0.5360, Macro F1 of 0.3627, precision of 0.5065, recall of 0.5691, Hamming Loss of 0.0410, and Exact Match of 0.3700. The per-emotion strategy was selected as the primary configuration, while the global strategy remains a useful comparison.

### Per-emotion observations

The strongest reported F1 scores included:

- Gratitude: 0.9088
- Amusement: 0.7879
- Love: 0.7611

Some of the weakest reported scores included:

- Relief: 0.2000
- Disappointment: 0.2427
- Caring: 0.2697
- Nervousness: 0.2778
- Realization: 0.2951
- Annoyance: 0.2983

Performance varies substantially by category. Rare labels and limited examples are important considerations when interpreting class-level results.

## 6. Application and deployment

The trained model and supporting configuration were packaged for inference. The Streamlit application provides four main areas:

- **Overview:** introduces the application and summarises key model information.
- **Emotion Studio:** accepts user text and displays predicted emotion labels and model scores.
- **Model Insights:** presents model evaluation information and emotion-level performance.
- **Research & Business:** communicates the research context, potential applications, and limitations.

The application is deployed on Streamlit Community Cloud.

**Live application:** https://emotisense-ikjvg3tbej7h5whswryugn.streamlit.app/  
**Source repository:** https://github.com/MWANGANGI91/EmotiSense

## 7. Potential business and research applications

Subject to appropriate validation, privacy safeguards, and human oversight, multi-label emotion analysis may help teams explore patterns in large collections of written feedback.

Potential exploratory use cases include:

- Summarising emotional themes in customer feedback.
- Exploring themes in product reviews and service comments.
- Supporting researchers conducting text-based studies.
- Helping organisations identify topics in feedback that may warrant closer human review.

These are potential applications, not validated outcomes of this project. The current model has been trained on an English-language Reddit dataset and has not been established as reliable for any particular organisation's operational decisions.

## 8. Limitations and responsible use

- **Not a diagnostic tool:** EmotiSense does not diagnose mental-health conditions, assess risk, or establish a person's actual emotional state.
- **Dataset domain:** GoEmotions consists of English Reddit comments. Its language, topics, and annotation conventions may not represent other settings.
- **Kenyan context:** The model has not been validated for Kenyan languages, Sheng, local cultural expressions, or code-switching. Local adaptation and evaluation would be necessary before making claims about performance in Kenya.
- **Scores are not calibrated confidence:** Displayed probabilities are model scores and should not be interpreted as calibrated probabilities or measurements of psychological state.
- **Class imbalance:** Some emotion categories have relatively few examples, which can contribute to uneven performance.
- **Threshold trade-offs:** Threshold tuning changes precision and recall. The chosen thresholds should not be assumed optimal for every application.
- **Repeated text across splits:** The dataset audit identified repeated text strings across official splits. This warrants additional group-aware evaluation.
- **Human interpretation:** Predictions should be treated as uncertain indicators of language patterns, not definitive labels about a person.

Users should avoid entering identifiable, confidential, or sensitive personal information into a public demonstration application.

## 9. Future improvements

Potential next steps include:

1. Conduct a group-aware evaluation that prevents identical text strings from crossing data splits.
2. Evaluate transformer-based models and compare them with the TF-IDF baseline.
3. Investigate class imbalance and improve performance on rare emotion categories.
4. Assess probability calibration and threshold stability.
5. Collect or identify appropriately governed, locally relevant evaluation data before making claims about Kenyan-language performance.
6. Conduct error analysis with representative examples and careful human review.
7. Add clear privacy information and operational safeguards before any real-world deployment.

## 10. Technology stack

- Python
- pandas and NumPy
- scikit-learn
- TF-IDF
- Logistic Regression
- One-vs-Rest multi-label classification
- joblib
- Streamlit
- Git and GitHub
- Streamlit Community Cloud

## 11. Conclusion

EmotiSense demonstrates an end-to-end applied NLP project, from dataset auditing and model development to evaluation, packaging, and public deployment. The results show the value of tuning decision thresholds for a multi-label task, while also highlighting trade-offs in precision, recall, and class-level performance.

The project is best understood as an experimental text-analysis application and a foundation for further research—not a system that can determine a person's true feelings or provide clinical conclusions.

---

**Author:** R. Mbinya  
**Project:** EmotiSense — AI-Powered Emotion Analysis
