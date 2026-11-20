# EmotiSense — AI-Powered Emotion Analysis

**Project Developer:** R. Mbinya  
**Project Type:** Machine Learning | Natural Language Processing | Applied AI  
**Status:** Completed and deployed  
**Live Application:** https://emotisense-ikjvg3tbej7h5whswryugn.streamlit.app/  
**GitHub Repository:** https://github.com/MWANGANGI91/EmotiSense

## Project Overview

EmotiSense is an interactive machine-learning application that analyses written text and identifies possible emotional expressions across 28 emotion categories.

The project demonstrates how Natural Language Processing (NLP) and multi-label classification can be applied to unstructured text to generate structured, interpretable emotion predictions.

The application allows users to submit text, explore predicted emotions and examine model performance through an interactive Streamlit dashboard.

## Problem Statement

Written communication contains emotional information that can be difficult to analyse consistently at scale.

EmotiSense explores how machine learning can help organise and analyse emotional expressions in text, potentially supporting research, exploratory text analytics and communication insights.

## Technical Approach

The project follows an end-to-end machine-learning workflow:

1. **Data acquisition:** Used the GoEmotions dataset, containing 54,263 English Reddit comments across official training, validation and test splits.
2. **Data preparation:** Inspected data quality, labels, duplicate text and class distribution.
3. **Text representation:** Applied TF-IDF vectorisation with up to 50,000 features, including unigrams and bigrams.
4. **Model development:** Trained a One-vs-Rest Logistic Regression classifier for multi-label emotion prediction.
5. **Threshold optimisation:** Tuned emotion-specific decision thresholds using validation data.
6. **Evaluation:** Assessed performance on the held-out test set.
7. **Deployment:** Built and published an interactive Streamlit application.

## Model Performance

The selected per-emotion threshold configuration achieved the following results on the held-out test set:

| Metric | Result |
|---|---:|
| Micro F1-score | 0.5375 |
| Macro F1-score | 0.4586 |
| Precision | 0.4828 |
| Recall | 0.6063 |
| Hamming Loss | 0.0435 |
| Exact Match Ratio | 0.3378 |

Threshold tuning improved the balance between precision and recall compared with the default 0.50 threshold.

The results also reveal differences in how well the model recognises individual emotion categories, highlighting the importance of class-level evaluation rather than relying on one overall metric.

## Technology Stack

- Python
- Pandas and NumPy
- Scikit-learn
- TF-IDF
- Logistic Regression
- Natural Language Processing
- Multi-label classification
- Streamlit
- Git and GitHub
- Anaconda

## Business and Practical Relevance

The project demonstrates a potential approach to transforming unstructured text into structured analytical information.

Possible exploratory applications include:

- Analysing themes and emotional expressions in customer feedback.
- Supporting research into patterns in written communication.
- Exploring sentiment and emotion trends in text collections.
- Developing dashboards for aggregated text analytics.

These are potential applications, not outcomes established through a live business deployment.

## Skills Demonstrated

- Data cleaning and exploratory analysis.
- Text preprocessing and feature engineering.
- Machine-learning model development.
- Multi-label classification.
- Hyperparameter and decision-threshold optimisation.
- Model evaluation and interpretation.
- Interactive dashboard development.
- Application deployment.
- Technical documentation and version control.

## Limitations and Responsible Use

EmotiSense is an experimental text-classification application, not a clinical or diagnostic system.

The model was developed using English-language Reddit comments. Its performance has not been established for Kenyan languages, Sheng, code-switching or other local communication contexts.

Predicted emotions should be interpreted as model-generated text classifications, not verified descriptions of a person's psychological state.

## Project Outcome

EmotiSense demonstrates an end-to-end applied machine-learning workflow, from dataset preparation and model evaluation to an accessible, deployed application.

It provides a practical example of combining data science, NLP, software development and analytical communication in one portfolio project.

**Developed by R. Mbinya**