# Detecting Sleep Apnea from raw physiological signals
by Dreem | https://challengedata.ens.fr/participants/challenges/45/

## Repository Link

https://github.com/giuuusepeda/Sleep_Apnea

## Description

Sleep apnea is a common sleep disorder characterized by repeated breathing interruptions during sleep, traditionally diagnosed using polysomnography and manual expert analysis. In this project, we address the automatic detection of sleep apnea events using raw physiological signals provided in the Challenge Data ENS dataset. We implement and evaluate machine learning and deep learning models using TensorFlow/Keras, with a focus on handling class imbalance, ensuring patient-level generalization, and evaluating performance using the F1-score. This project was developed as part of a Machine Learning with TensorFlow course.

### Task Type

Time-series event detection (binary classification)

### Results Summary

#### Best Model Performance

- **Best Model:** 3-layer CNN with night-level normalization and overlapping temporal aggregation  
- **Evaluation Metric:** Event-based F1-score (IoU ≥ 0.3)  
- **Final Performance:**  
  - **Validation Event-F1:** 0.247 (post-processed)  
  - **Test Event-F1 (official):** 0.0739  

- **Post-processing configuration:**  
  - Threshold (`t`): 0.535  
  - Minimum event duration (`min_len`): 6 seconds  
  - Gap filling (`gap_fill`): 3 seconds  

These results highlight the importance of preprocessing and temporal aggregation over architectural complexity,
with significant performance gains achieved primarily through night-level normalization and structured post-processing.


#### Model Comparison

**Baseline Performance:** 
- 3-layer CNN: Event-F1 of 0.0739 (official test set)
- Validation Event-F1: 0.247 (post-processed)

**Alternative Models Explored:**

| Model Family | Architecture | Parameters | Best Val Loss | Training Time | Status |
|--------------|-------------|------------|---------------|---------------|--------|
| **CNN** | 3-layer Conv1D | ~200K | - | ~1 hour | ✓ Best model |
| **GRU** | 3-layer Bi-GRU | ~300K | 0.2307 | ~30 min | ✓ Completed |
| **LSTM** | 3-layer Bi-LSTM | 345,921 | 0.2860 | ~25 min | ✓ Completed |

**Key Findings:**
- The **3-layer CNN with night-level normalization** achieved the best performance
- Recurrent models (GRU/LSTM) were explored but did not outperform the CNN baseline
- Model performance is highly dependent on preprocessing strategy (night-level vs window-level normalization)
- Event-based F1 score is strongly influenced by post-processing parameters (threshold, min_len, gap_fill)

#### Key Insights

- **Most Important Features:** Respiratory signals (AbdoBelt, ThorBelt, AirFlow) and oxygen saturation (SPO2) are critical for apnea detection, as they directly reflect breathing patterns and oxygen desaturation events characteristic of sleep apnea.

- **Preprocessing Impact:** Night-level normalization proved essential for performance. Window-level normalization disrupted temporal continuity and resulted in near-zero F1 scores, demonstrating the importance of preserving physiological context across time.

- **Model Strengths:** 
  - The CNN architecture effectively captures local temporal patterns in physiological signals
  - Recurrent models (GRU/LSTM) successfully model long-range dependencies but did not outperform CNNs on this task
  - All models benefited from subject-wise validation splits to ensure generalization

- **Model Limitations:** 
  - High sensitivity to post-processing parameters (threshold, minimum event duration, gap filling)
  - Limited training data (44 nights, 22 subjects) constrains generalization
  - Severe class imbalance (only ~7% positive samples) makes the task challenging
  - Point-wise accuracy is misleading due to class imbalance; event-based metrics are essential

- **Architecture Comparison:**
  - **CNNs:** Best performance, faster training, fewer parameters
  - **RNNs (GRU/LSTM):** Slower training, more parameters, theoretically better for long sequences but did not translate to better event-F1 in practice
  - The receptive field of the CNN appears sufficient for capturing apnea events within 90-second windows

- **Business Impact:** 
  - Automated sleep apnea detection can reduce the need for manual polysomnography scoring
  - Even modest F1 scores can assist clinicians by flagging potential apnea events for review
  - Further improvements require larger datasets and cross-site validation to ensure clinical deployment readiness


## Documentation

1. **[Literature Review](0_LiteratureReview/README.md)**
2. **[Dataset Characteristics](1_DatasetCharacteristics/exploratory_data_analysis.ipynb)**
3. **[Baseline Model](2_BaselineModel/baseline_model.ipynb)**
4. **[Model Definition and Evaluation](3_Model/model_definition_evaluation)**
5. **[Presentation](4_Presentation/README.md)**

## Cover Image

![Project Cover Image](CoverImage/cover_image.png)
