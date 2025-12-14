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
- **Baseline Performance:** 0.0739  
- **Improvement Over Baseline:** [Quantitative improvement, e.g., "+12% accuracy", "25% reduction in MSE"]
- **Best Alternative Model:** [Second-best model and its performance]

#### Key Insights
- **Most Important Features:** [Top 3-5 features that drive model performance]
- **Model Strengths:** [What the model does well]
- **Model Limitations:** [Known limitations and failure cases]
- **Business Impact:** [Practical implications of the model performance]

## Documentation

1. **[Literature Review](0_LiteratureReview/README.md)**
2. **[Dataset Characteristics](1_DatasetCharacteristics/exploratory_data_analysis.ipynb)**
3. **[Baseline Model](2_BaselineModel/baseline_model.ipynb)**
4. **[Model Definition and Evaluation](3_Model/model_definition_evaluation)**
5. **[Presentation](4_Presentation/README.md)**

## Cover Image

![Project Cover Image](CoverImage/cover_image.png)
