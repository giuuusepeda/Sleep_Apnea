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
   **Methods**:
    - Dataset of 4,014 patients from a sleep clinic.
    - Features included demographic, physical, and questionnaire data (e.g., Epworth Sleepiness Scale, Insomnia Severity Index).
    - Applied clustering (K-means, GMM, hierarchical) and classification algorithms (Random Forest, XGBoost, LightGBM, CatBoost).
    - Feature selection with mutual information and recursive feature elimination; hyperparameter tuning via Bayesian optimization (Optuna).
    **Outcomes**:
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



**Source 5**: Deep learning for obstructive sleep apnea diagnosis based on single-channel oximetry

  **Source Link:**  [https://www.nature.com/articles/s41467-023-40300-8](https://www.nature.com/articles/s41467-023-40300-8)

  **Objective:**  
  To develop and validate a deep learning model for automatic diagnosis of obstructive sleep apnea (OSA) using oximetry data.

  **Methods:**  
  - Utilizes oximetry signals from large, multi-institutional datasets.
  - Employs a deep convolutional neural network (CNN) architecture, trained to detect apnea events and estimate AHI.
  - Evaluates performance using accuracy, sensitivity, specificity, and F1-score metrics; compares different windowing strategies and sensor setups.

  **Outcomes:**  
  - Achieves high accuracy in detecting OSA and estimating its severity from single-channel sensor signals.
  - Demonstrates strong agreement with manual scoring and applicability to large-scale screening.
  - Highlights the value of deep learning for scalable, home-based OSA diagnosis.

  **Relation to the Project:**  
    This study presents a practical framework for event detection using physiological signals, similar to our project with PSG data. Its approach to preprocessing, modeling
    (CNN), and validation (agreement with expert scoring) directly informs our methodology and benchmarking decisions.


## Insights for Our Project ##

**Common Models:**
Random Forest, Gradient Boosting (XGBoost, LightGBM, CatBoost), CNNs, and self-supervised encoders like Masked Autoencoders.

**Training Data Format:**
Multichannel time-series (e.g., EEG, airflow, SpO₂, respiratory effort) often segmented into fixed-length windows with per-second apnea labels.

**Data Volume:**
Studies range from hundreds to several thousand PSG recordings; larger datasets improve model reliability and generalization.

**Pretrained Models:**
Recent works (e.g., PSG-MAE) suggest pretraining on large unlabeled PSG data can significantly boost downstream apnea detection performance.
