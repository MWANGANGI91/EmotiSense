\# EmotiSense — Technical Architecture



\## 1. System Overview



EmotiSense uses a machine-learning pipeline to transform written text into multi-label emotion predictions.



The system has two main workflows:



\- \*\*Model development:\*\* Dataset preparation, feature extraction, model training, validation and evaluation.

\- \*\*Application inference:\*\* User text input, preprocessing, prediction and presentation of results.



\## 2. Technical Architecture Diagram



```mermaid

flowchart TD



&#x20;   subgraph TRAIN\["MODEL DEVELOPMENT PIPELINE"]

&#x20;       A\["GoEmotions Dataset<br/>54,263 English comments"]

&#x20;       B\["Data Inspection<br/>Cleaning and Label Analysis"]

&#x20;       C\["Official Train / Validation / Test Splits"]

&#x20;       D\["TF-IDF Feature Extraction<br/>50,000 Features"]

&#x20;       E\["One-vs-Rest<br/>Logistic Regression"]

&#x20;       F\["Validation-Based<br/>Threshold Optimisation"]

&#x20;       G\["Held-Out Test Evaluation"]

&#x20;       H\["Saved Model Artifacts<br/>Classifier, Metadata and Thresholds"]



&#x20;       A --> B --> C

&#x20;       C --> D --> E

&#x20;       E --> F

&#x20;       E --> G

&#x20;       F --> H

&#x20;       G --> H

&#x20;   end



&#x20;   subgraph DEPLOY\["DEPLOYED APPLICATION"]

&#x20;       I\["User Enters Text"]

&#x20;       J\["Streamlit Interface"]

&#x20;       K\["Text Preprocessing"]

&#x20;       L\["Saved TF-IDF Vectoriser<br/>and Classifier"]

&#x20;       M\["Emotion-Specific<br/>Decision Thresholds"]

&#x20;       N\["Predicted Emotion Labels<br/>and Model Scores"]

&#x20;       O\["Interactive Results<br/>and Model Insights"]



&#x20;       I --> J --> K --> L --> M --> N --> O

&#x20;   end



&#x20;   H --> L

```



\## 3. Architecture Components



| Component | Purpose |

|---|---|

| GoEmotions dataset | Supplies labelled text for model development |

| Data preparation | Inspects records, labels and data quality |

| TF-IDF | Converts text into numerical features |

| Logistic Regression | Learns emotion classification patterns |

| Threshold optimisation | Selects decision thresholds using validation data |

| Test evaluation | Measures performance on unseen test data |

| Model artifacts | Stores the trained model and supporting configuration |

| Streamlit | Provides the interactive user interface |

| Prediction engine | Generates emotion labels and scores |

| Results dashboard | Displays predictions and model insights |



\## 4. Prediction Workflow



When a user submits text:



1\. The Streamlit application receives the text.

2\. The text is processed using the model's preprocessing pipeline.

3\. TF-IDF transforms the text into numerical features.

4\. The trained classifier generates scores for the 28 emotion categories.

5\. Emotion-specific thresholds determine which labels are selected.

6\. The application displays the predicted labels and corresponding model scores.



\## 5. Deployment Architecture



The application is deployed using Streamlit Community Cloud and connected to its GitHub repository.



The deployed application loads the saved model artifacts and uses them to generate predictions without retraining the model for each user request.



\## 6. Design Considerations



\- Training and inference are separated.

\- The official dataset splits are retained.

\- Threshold selection uses validation data rather than the held-out test set.

\- Model artifacts are stored separately from application code.

\- The application provides an accessible interface for exploring predictions.

\- Predictions are exploratory text classifications, not clinical assessments.



\*\*Developer:\*\* R. Mbinya  

\*\*Project:\*\* EmotiSense — AI-Powered Emotion Analysis

