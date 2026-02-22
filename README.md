# Detecting Sleep Apnea from raw physiological signals
by Dreem | https://challengedata.ens.fr/participants/challenges/45/

## Repository Link

https://github.com/giuuusepeda/Sleep_Apnea

## Description

Sleep apnea is a common sleep disorder characterized by repeated breathing interruptions during sleep, traditionally diagnosed using polysomnography and manual expert analysis. In this project, we address the automatic detection of sleep apnea events using raw physiological signals provided in the Challenge Data ENS dataset. We implement and evaluate machine learning and deep learning models using TensorFlow/Keras, with a focus on handling class imbalance, ensuring patient-level generalization, and evaluating performance using the F1-score. This project was developed as part of a Machine Learning with TensorFlow course.

---

### Task Type

Time-series event detection (binary classification)

## Results Summary

---

### Best Model Performance

- **Best Model:** **LightGBM with Feature Engineering and 300-second windows**
- **Evaluation Metric:** Event-based F1-score (IoU ≥ 0.3)

**Final Performance:**
- **Validation Event-F1:** **0.0851** (after post-processing)
- **Test Event-F1 (official):** **0.0854**

**Post-processing configuration:**
- Threshold (`t`): **0.11**
- Minimum event duration (`min_len`): **1 second**
- Gap filling (`gap_fill`): **3 seconds**

These results indicate that **data representation, preprocessing strategy, and temporal aggregation** had a greater impact on performance than architectural complexity. The strongest gains were achieved through **night-level normalization**, **longer temporal windows**, and **structured post-processing**, rather than through end-to-end deep learning models.

---

### Model Comparison

**Baseline Performance:**
- **3-layer CNN**
  - **Validation Event-F1:** 0.2513 (post-processed)
  - **Test Event-F1 (official):** 0.0406

**Best Performing Model:**
- **LightGBM + Feature Engineering + 300s windows**
  - **Validation Event-F1:** 0.0851
  - **Test Event-F1 (official):** 0.0854

**Key Findings:**
- The **LightGBM model with engineered physiological features and long temporal windows** achieved the best generalization on the official test set.
- Model performance is **highly sensitive to preprocessing choices**, particularly the use of **night-level normalization** instead of window-level normalization.
- **Event-based F1-score** is strongly influenced by post-processing parameters such as detection threshold, minimum event duration, and gap-filling strategy.

---

### Feature Importance Analysis

The feature importance analysis of the best-performing LightGBM model shows a strong alignment with known sleep apnea physiology.

The most relevant features were related to **airflow**, **oxygen saturation (SpO₂)**, and **thoracoabdominal coordination**, including:

- Airflow baseline and percentage drop  
  (`airflow_baseline_local`, `airflow_drop_pct_c30`)
- Minimum and range of oxygen saturation  
  (`spo_min_c30`, `spo_range_c30`)
- Cross-features combining airflow reduction and oxygen desaturation  
  (`airflow_drop_x_spo_range`, `airflow_lowdur_x_spo_rng`)
- Thoracic–abdominal correlation  
  (`thor_abd_corr_c30`)

These features capture the defining characteristics of apnea events: **reduced airflow**, **oxygen desaturation**, and **imbalance in respiratory effort**.  
The prominence of interaction features indicates that the model learns **physiologically meaningful relationships across multiple signals**, rather than relying on isolated point-wise patterns.

---

### Key Insights

- **Physiological relevance matters:**  
  Features derived from respiratory belts, airflow, and SpO₂ consistently dominated the model, reflecting the underlying pathophysiology of sleep apnea.

- **Preprocessing is critical:**  
  **Night-level normalization proved essential**. Normalizing each window independently disrupted physiological continuity and resulted in near-zero Event-F1 scores, highlighting the importance of preserving long-term context.

- **Temporal aggregation outperforms short windows:**  
  Aggregating features over **300-second windows** provided sufficient temporal context to capture complete apnea events and recovery phases.

- **Event-based evaluation is mandatory:**  
  Due to severe class imbalance (~7% positive samples), point-wise accuracy and standard classification metrics were misleading. **Event-based F1-score** provided a more clinically meaningful evaluation.

---

### Model Strengths and Limitations

**Strengths:**
- Robust performance under limited data conditions (44 nights, 22 subjects)
- Strong interpretability via feature importance analysis
- Effective use of domain-informed feature engineering
- Good generalization to unseen subjects with subject-wise splits

**Limitations:**
- High sensitivity to post-processing hyperparameters
- Limited dataset size restricts broader generalization
- Severe class imbalance increases detection difficulty
- Performance ceiling likely constrained by annotation noise and event ambiguity

---

### Business Impact

  - Automated sleep apnea detection can reduce the need for manual polysomnography scoring
  - Even modest F1 scores can assist clinicians by flagging potential apnea events for review
  - Further improvements require larger datasets and cross-site validation to ensure clinical deployment readiness

---

### Conclusion

This work demonstrates that **feature-based models combined with domain knowledge and appropriate temporal aggregation can outperform more complex neural architectures** in low-data, event-based sleep apnea detection tasks.  
The results emphasize the importance of **physiologically grounded feature engineering**, **night-level preprocessing**, and **carefully designed post-processing pipelines** when addressing clinically relevant time-series detection problems.


## Documentation

1. **[Literature Review](0_LiteratureReview/README.md)**
2. **[Dataset Characteristics](1_DatasetCharacteristics/exploratory_data_analysis.ipynb)**
3. **[Baseline Model](2_BaselineModel/baseline_model.ipynb)**
4. **[Model Definition and Evaluation](3_Model/model_definition_evaluation)**
5. **[Presentation](4_Presentation/README.md)**

## Cover Image

![Project Cover Image](CoverImage/coverimage)
