# Literature Review

Approaches or solutions that have been tried before on similar projects.

**Summary of Each Work**:

- **Source 1**: Detecting Sleep Apnea from Raw Physiological Signals (Challenge Data)

  - **[Link](https://challengedata.ens.fr/challenges/45)**
  - **Objective:**
    The challenge asks participants to build an automatic model to detect sleep apnea events from multi-channel polysomnography (PSG) recordings by classifying 90-s windows into apnea vs non-apnea segments.
  - **Methods:**
    The dataset contains 44 nights, each split into 200 non-overlapping 90-second windows sampled at 100 Hz for 8 physiological signals (ECG, EEG, respiration, SpO₂, etc.). Typical approaches include preprocessing (filtering, resampling), feature extraction (HRV, SpO₂ desaturation, respiratory features), and supervised learning models such as 1D-CNNs, RNNs, or hybrid CNN–LSTM architectures.
  - **Outcomes:**
    The challenge provides a standard benchmark and evaluation protocol for event-level apnea detection and has been used as the basis for comparing classical feature-based methods and end-to-end deep learning methods.
  - **Relation to the Project:**
    This is the primary dataset and task definition for our project; all preprocessing, modeling, and evaluation must follow the dataset format and the challenge’s expected submission format and metrics. :contentReference[oaicite:2]{index=2}
    

- **Source 2**: Application of various machine learning techniques to predict obstructive sleep apnea syndrome severity

  - **[Link](https://www.nature.com/articles/s41598-023-33170-7)**
  - **Objective**:
    To evaluate the performance of different machine learning models in predicting the severity of Obstructive Sleep Apnea Syndrome (OSAS) using clinical, anthropometric, and questionnaire data instead of full polysomnography.
  - **Methods**:
    - Dataset of 4,014 patients from a sleep clinic.
    - Features included demographic, physical, and questionnaire data (e.g., Epworth Sleepiness Scale, Insomnia Severity Index).
    - Applied clustering (K-means, GMM, hierarchical) and classification algorithms (Random Forest, XGBoost, LightGBM, CatBoost).
    - Feature selection with mutual information and recursive feature elimination; hyperparameter tuning via Bayesian optimization (Optuna).
  - **Outcomes**:
    - Best models achieved accuracies of ~88% (AHI ≥ 5), ~88% (AHI ≥ 15), and ~91% (AHI ≥ 30).
    - LightGBM and CatBoost showed the best overall performance.
    - Combining clustering, feature engineering, and hyperparameter tuning improved prediction accuracy.  
  - **Relation to the Project**:
    This study is highly relevant because it applies ML to sleep apnea detection using physiological and clinical indicators. Its modeling approach (boosting algorithms, clustering, and feature engineering) provides useful methodological insights for improving apnea detection models like the one in the ENS challenge.

- **Source 3**: SAGSleepNet: A deep learning model for sleep staging based on self-attention graph of polysomnography

  - **[Link](https://www.sciencedirect.com/science/article/abs/pii/S1746809423004950)**
  - **Objective**: The study aims to investigate a machine-learning based method for detecting or classifying Obstructive Sleep Apnea (OSA) (or Sleep Apnea more generally) using physiological or wearable signals/data.
  - **Methods**:
    - The paper uses a dataset (likely from home-monitoring or a wearable device) and applies signal processing plus machine learning techniques to distinguish apnea vs non-apnea (or different severities).
    - It involves feature extraction from physiological time series (e.g., respiration, SpO₂, ECG/PPG) and design/training of classifiers.
    - Performance metrics such as accuracy, sensitivity, specificity or AUC are used to evaluate the model. 
  - **Outcomes**:
    - The model demonstrates feasible performance in detecting sleep apnea.
    - The authors discuss limitations such as wearable vs full polysomnography, generalisability, sample size, or signal quality. 
  - **Relation to the Project**:
    - This article is highly relevant because our project focuses on detection of sleep-apnea events using ML on physiological signals.
    - The use of wearable or simpler signals is directly informative since our dataset is less complex than full polysomnography.
    - The paper provides methodological insights (signal types, preprocessing, feature engineering, classifier choices) that could inform your own modelling.
    - It can help set benchmarks: we can compare your model’s performance to theirs and address limitations they found.

- **Source 4**: A deep learning algorithm model to automatically score and grade obstructive sleep apnea in adult polysomnography

  - **[Link](https://journals.sagepub.com/doi/10.1177/20552076241291707)**
  - **Objective**:To develop and evaluate a deep-learning model that automatically scores and grades adult obstructive sleep apnea (OSA) events from full polysomnography data.
  - **Methods**:
    - Adult subjects undergoing polysomnography were used to train the model.
    - A deep neural network architecture was employed to detect and grade respiratory events (apnea/hypopnea) from PSG signals.
    - The ground truth scoring was done via conventional manual annotation of respiratory events from PSG.
    - Model performance was assessed by comparing automatic scores with manual ones, likely using metrics such as agreement, accuracy, perhaps F1-score (though exact metrics not available in detail).
  - **Outcomes**:
    - The deep learning model demonstrated feasibility for automatic scoring of OSA events from polysomnography.
    - It suggests potential for reducing manual workload in sleep labs and facilitating more efficient event detection in OSA diagnosis.
    - Limitations include full‐PSG requirement, dependence on high‐quality annotated data, and possibly generalizability yet to be proven.
  - **Relation to the Project**:
    - Very relevant: our project aims at event detection of sleep apnea (via ML) from physiological signals, and this work uses deep learning on full polysomnography signals for the same purpose.
    - This article offers a methodological reference for building an automatic scoring model (“event detection + grading”) and may provide inspiration for architecture choices, training strategies, and evaluation metrics.
    - The work underscores that full PSG signals allow higher fidelity models; we may compare whether our dataset (with perhaps fewer channels) aligns, or how to adapt the approach to your available signals.
    - Also, it highlights practical limitations (need for annotated events, generalization) that should be consider in our project’s design and discussion of limitations.

-**Source 5**: Towards automatic home-based sleep apnea estimation using deep learning
  -**Link**:[Link](https://www.nature.com/articles/s41746-024-01139-z)
  -**Objective**:
    -To develop and validate a deep-learning model (DRIVEN) for automatic detection, segmentation, and quantification of apnea–hypopnea index (AHI) events in home-based
     sleep monitoring using physiological signals.
  -**Methods**:
    -Raw abdominal and thoracic movement, plus SpO₂ signals, from large databases (MESA, MROS) were analyzed with both single- and multi-channel deep CNNs. 
    -Features extracted from CNNs were combined and classified with LightGBM; window sizes and sensor combinations were rigorously compared.

  -**Outcomes**:
    -Best results were achieved with combined abdominal movement and pulse oximetry signals, reaching an F1-score of 72% for AHI detection. 
    -Combining deep learning and boosting generalized well across sensor configurations and databases. Home-based solutions are feasible with careful model tuning.

  -**Relation to the Project**:
    -This source shows deep learning and boosting can be used for multi-sensor time-series event detection (similar to PSG dataset). 
    -Sensor selection, windowing, and hybrid model design are highly relevant; it provides benchmarking suggestions for your own algorithm and shows the value of combining
     signals.

## Insights for Our Project ##

**Common Models:**
Random Forest, Gradient Boosting (XGBoost, LightGBM, CatBoost), CNNs, and self-supervised encoders like Masked Autoencoders.

**Training Data Format:**
Multichannel time-series (e.g., EEG, airflow, SpO₂, respiratory effort) often segmented into fixed-length windows with per-second apnea labels.

**Data Volume:**
Studies range from hundreds to several thousand PSG recordings; larger datasets improve model reliability and generalization.

**Pretrained Models:**
Recent works (e.g., PSG-MAE) suggest pretraining on large unlabeled PSG data can significantly boost downstream apnea detection performance.
