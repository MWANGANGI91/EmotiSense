\# EmotiSense: Business Value and Measurable Results



\*\*Project:\*\* EmotiSense — AI-Powered Emotion Analysis  

\*\*Developer:\*\* R. Mbinya  

\*\*Technology:\*\* Python, Natural Language Processing, Scikit-learn, TF-IDF, Logistic Regression, Streamlit



\---



\## 1. Executive Summary



EmotiSense is an end-to-end machine-learning project that explores how written communication can be analysed to identify multiple possible emotional expressions.



The project demonstrates how unstructured text can be transformed into structured analytical outputs using Natural Language Processing and multi-label classification.



Beyond model development, EmotiSense includes an interactive Streamlit application, model evaluation insights and technical documentation.



Its potential business value lies in supporting exploratory analysis of large volumes of written feedback, helping organisations identify patterns that may warrant further investigation.



\## 2. Business Problem



Organisations receive written feedback through customer reviews, surveys, support messages and other communication channels.



Manually reviewing large volumes of text can be time-consuming and may make it difficult to identify recurring themes efficiently.



Traditional sentiment analysis often focuses on broad categories such as positive, negative or neutral. However, written communication can express several emotions simultaneously.



EmotiSense explores a more detailed approach by identifying possible emotional expressions across 28 categories.



\## 3. Proposed Business Applications



\### Customer Experience Analysis



A future implementation could help customer experience teams explore emotional patterns in customer feedback, alongside conventional sentiment and topic analysis.



\### Feedback and Survey Research



Researchers could use emotion predictions as an additional exploratory feature when examining large collections of written responses.



\### Communication Trend Analysis



Aggregated predictions could help identify changes in emotional language over time, provided that data quality, privacy and appropriate validation requirements are addressed.



\### Service Improvement



Organisations could investigate recurring emotional patterns alongside complaints, service categories and customer feedback to identify areas requiring attention.



These are potential applications. They have not yet been validated through a commercial deployment.



\## 4. Measurable Technical Results



The project was developed and evaluated using the GoEmotions dataset.



| Measurement | Result |

|---|---:|

| Total dataset records | 54,263 |

| Emotion categories | 28 |

| Training records | 43,410 |

| Validation records | 5,426 |

| Test records | 5,427 |

| TF-IDF feature limit | 50,000 |

| Classification approach | One-vs-Rest Logistic Regression |



\### Held-out Test Performance



The selected per-emotion threshold configuration achieved:



| Metric | Result |

|---|---:|

| Micro F1-score | 0.5375 |

| Macro F1-score | 0.4586 |

| Precision | 0.4828 |

| Recall | 0.6063 |

| Hamming Loss | 0.0435 |

| Exact Match | 0.3378 |



\### Threshold Optimisation Findings



The default threshold of 0.50 was compared with the selected per-emotion thresholds.



| Metric | Default Threshold | Tuned Thresholds |

|---|---:|---:|

| Micro F1 | 0.3850 | 0.5375 |

| Macro F1 | 0.1979 | 0.4586 |

| Precision | 0.7384 | 0.4828 |

| Recall | 0.2604 | 0.6063 |

| Hamming Loss | 0.0346 | 0.0435 |



Threshold tuning increased Micro F1 from 0.3850 to 0.5375, an absolute improvement of 0.1525.



Recall increased from 0.2604 to 0.6063. However, precision decreased, and Hamming Loss increased slightly.



This demonstrates the importance of selecting evaluation metrics and decision thresholds according to the intended application.



\## 5. Business Value Demonstrated



The project has delivered measurable technical outputs:



\- An implemented multi-label emotion classification model.

\- Evaluation using a held-out test dataset.

\- A comparison of default and optimised decision thresholds.

\- An interactive application for testing text predictions.

\- Model artifacts and supporting configuration files.

\- Technical documentation and an interview presentation.

\- A publicly accessible application deployment.



These outputs demonstrate an end-to-end machine-learning workflow.



They do not establish measured financial savings, revenue growth or improved customer satisfaction.



\## 6. Potential Business KPIs for a Pilot



If EmotiSense were adapted and tested within an organisation, the following indicators could be evaluated:



| KPI | What It Would Measure |

|---|---|

| Review time | Time required to analyse a defined volume of feedback |

| Emotion classification F1 | Quality of predictions against human-labelled examples |

| Feedback coverage | Proportion of eligible feedback analysed |

| Human review agreement | Agreement between model outputs and human reviewers |

| Trend detection time | Time taken to identify recurring patterns |

| User adoption | Usage by intended organisational teams |



Baseline measurements and pilot results would be required before claiming improvements in these indicators.



\## 7. Risks and Limitations



\### Dataset Representation



The model was trained using English-language Reddit comments. Its performance has not been established for Kenyan languages, Sheng or code-switching.



\### Model Performance



Performance varies across emotion categories. Stronger results in some categories do not imply equally reliable predictions across all 28 categories.



\### Evaluation Considerations



Duplicate text across dataset splits was identified during data auditing. Future evaluation should include group-aware splitting to better investigate potential overlap and generalisation.



\### Interpretation and Responsible Use



The model identifies possible emotional expressions in text. It does not establish a person's actual psychological state and is not a clinical or diagnostic tool.



Predictions should be reviewed in context and should not be used as the sole basis for consequential decisions about individuals.



\## 8. Recommended Next Steps



1\. Conduct group-aware evaluation to investigate the effect of duplicate text across splits.

2\. Improve performance on weaker-performing emotion categories.

3\. Investigate support for Kenyan languages, Sheng and code-switching using appropriately labelled local data.

4\. Test the system on representative organisational feedback with suitable consent and privacy safeguards.

5\. Conduct a controlled pilot with human review and agreed business KPIs.

6\. Evaluate whether the system adds value beyond existing sentiment and text analytics methods.



\## 9. Conclusion



EmotiSense demonstrates how machine learning and Natural Language Processing can be applied to a practical text analytics problem.



The project combines data preparation, feature engineering, multi-label classification, threshold optimisation, model evaluation, application development and deployment.



Its strongest contribution is the demonstration of a complete technical solution and a foundation for further research into emotion-aware text analytics.



\*\*The project establishes technical feasibility on the selected dataset, while real-world business value remains an opportunity for future validation.\*\*

