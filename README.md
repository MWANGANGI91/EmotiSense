# \# EmotiSense 🧠

# \## AI-Powered Emotion Analysis

# 

# \*\*Developed by R. Mbinya\*\*

# 

# !\[Live App](https://img.shields.io/badge/Streamlit-Live%20App-FF4B4B?logo=streamlit\&logoColor=white)

# !\[Python](https://img.shields.io/badge/Python-3.11-blue?logo=python\&logoColor=white)

# !\[scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange?logo=scikitlearn\&logoColor=white)

# 

# \*\*\[Launch the Live Application](https://emotisense-ikjvg3tbej7h5whswryugn.streamlit.app/)\*\*

# 

# EmotiSense is an experimental machine-learning application that analyses written text and predicts possible emotional expressions across 28 categories using a multi-label classification model.

# 

# > EmotiSense analyses language patterns. It does not determine a person's actual emotional state or diagnose mental-health conditions.

# 

# \---

# 

# \## Project Overview

# 

# This project demonstrates an end-to-end Natural Language Processing workflow using the GoEmotions dataset: data auditing, text representation, multi-label model development, threshold tuning, evaluation, packaging and deployment.

# 

# \## Portfolio Documentation

# 

# Explore the project's technical development, business relevance and presentation materials.

# 

# | Deliverable | Description |

# |---|---|

# | \[Project Case Study](docs/EmotiSense\_Case\_Study.md) | Detailed problem definition, data audit, methodology, evaluation and limitations |

# | \[Professional Portfolio Entry](docs/Portfolio\_Entry.md) | Concise project summary for recruiters and employers |

# | \[Technical Architecture](docs/Technical\_Architecture.md) | System architecture and end-to-end workflow |

# | \[Business Value Report](docs/Business\_Value\_Report.md) | Potential organisational applications, measured results and pilot KPIs |

# | \[Interview Presentation](docs/presentation/EmotiSense\_Interview\_Presentation\_Public.pptx) | Eight-slide presentation without private speaker notes |

# 

# \## Application Screenshots

# 

# \### Overview

# !\[EmotiSense overview](docs/images/overview.png)

# 

# \### Emotion Studio

# !\[Emotion Studio](docs/images/emotion\_studio.png)

# 

# \### Model Insights

# !\[Model Insights](docs/images/model\_insights.png)

# 

# \### Research \& Business

# !\[Research and Business](docs/images/research\_business.png)

# 

# \## Key Features

# 

# \- Analyse user-submitted text.

# \- Predict multiple possible emotion categories.

# \- Display model scores and threshold-qualified predictions.

# \- Explore model evaluation and emotion-level performance.

# \- Review research context, potential applications and limitations.

# 

# \## Dataset

# 

# The project uses the GoEmotions English Reddit-comment dataset with 28 emotion categories.

# 

# | Split | Records |

# |---|---:|

# | Training | 43,410 |

# | Development | 5,426 |

# | Test | 5,427 |

# | \*\*Total\*\* | \*\*54,263\*\* |

# 

# \## Model and Methodology

# 

# \- \*\*Text features:\*\* TF-IDF, up to 50,000 features, unigrams and bigrams.

# \- \*\*Classifier:\*\* One-vs-Rest Logistic Regression (`liblinear`).

# \- \*\*Task:\*\* Multi-label classification across 28 emotion categories.

# \- \*\*Threshold selection:\*\* Per-emotion thresholds selected using the development split; the test split was reserved for final evaluation.

# 

# \## Test Performance

# 

# Selected per-emotion threshold configuration:

# 

# | Metric | Test Result |

# |---|---:|

# | Micro F1 | 0.5375 |

# | Macro F1 | 0.4586 |

# | Precision | 0.4828 |

# | Recall | 0.6063 |

# | Hamming Loss | 0.0435 |

# | Exact Match | 0.3378 |

# 

# Threshold tuning improved F1 and recall compared with the default 0.50 threshold, while reducing precision and slightly increasing Hamming Loss. See the \[project case study](docs/EmotiSense\_Case\_Study.md) for the full comparison and interpretation.

# 

# \## Technology Stack

# 

# Python · pandas · NumPy · scikit-learn · TF-IDF · Logistic Regression · joblib · Streamlit · Git · GitHub

# 

# \## Repository Structure

# 

# ```text

# EmotiSense\_Deploy/

# ├── model\_artifacts/

# ├── streamlit\_app/

# │   └── app.py

# ├── docs/

# │   ├── EmotiSense\_Case\_Study.md

# │   ├── Portfolio\_Entry.md

# │   ├── Technical\_Architecture.md

# │   ├── Business\_Value\_Report.md

# │   ├── images/

# │   └── presentation/

# │       └── EmotiSense\_Interview\_Presentation\_Public.pptx

# ├── requirements.txt

# └── README.md

# ```

# 

# \## Business Relevance

# 

# EmotiSense explores how emotion-aware text analytics could support:

# 

# \- Exploratory analysis of customer feedback.

# \- Research into written communication.

# \- Aggregated emotion trend analysis.

# \- Further investigation of customer experience patterns.

# 

# These are potential applications, not measured commercial outcomes. Real-world value would require validation using representative organisational data and agreed pilot KPIs.

# 

# \## Important Limitations and Responsible Use

# 

# \- The model was trained on English-language Reddit comments and has not been validated for Kenyan languages, Sheng or local code-switching.

# \- Emotion categories are predictions about text, not definitive statements about a person.

# \- Displayed scores are model scores, not calibrated confidence estimates.

# \- Class-level performance varies, particularly for less frequent categories.

# \- The application is experimental and is not a clinical or mental-health diagnostic tool.

# \- Do not submit identifiable, confidential or sensitive personal information to the public demonstration.

# 

# \## Author

# 

# \*\*R. Mbinya\*\*  

# Data Science Portfolio Project

# 

# \- \*\*Live application:\*\* https://emotisense-ikjvg3tbej7h5whswryugn.streamlit.app/

# \- \*\*GitHub repository:\*\* https://github.com/MWANGANGI91/EmotiSense

