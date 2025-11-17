# Dataset Characteristics

**[Notebook](exploratory_data_analysis.ipynb)**

## Dataset Information

### Dataset Source
- **Dataset Link:** https://challengedata.ens.fr/participants/challenges/45/

### Dataset Characteristics
- **Number of Observations:** 44 nights recorded with a polysomnography and scored for apnea events by a consensus of human experts. For each of the 44 nights, 200 windows (without intersection) are sampled with the associated labels (which are binary segmentation masks).
- **Number of Features:** 90 seconds of signal from 8 physiological signals sampled at 100Hz.
  
### Target Variable/Label
- **Label Name:** Y_0 to Y_89
- **Label Type:** Binary Classification
- **Label Description:** If an Apnea episode was detected for that second for a 90s window. The Task requires to predict whether or not was an Apnea happening in that second.
- **Label Values:** 1 for Apnea for that second, 0 for no Apnea Event at that second
- **Label Distribution:** [Brief description of class balance for classification]

### Feature Description
[Provide a brief description of each feature or group of features in your dataset. If you have many features, group them logically and describe each group. Include information about data types, ranges, and what each feature represents.]

**Example format:**
- **Abdominal belt (AbdoBelt):** Abdominal contraction, [data type, and any relevant details]
- **Airflow (AirFlow):** Respiratory Airflow from the subject [Description of what this feature represents, data type, and any relevant details]
- **PPG (Photoplethysmogram) (PPG):** Cardiac activity [Description of a group of related features]
- **Thoracic belt (ThorBelt):** O2 saturation of the blood [Description of a group of related features]
- **Snoring indicator (Snoring):** [Description of a group of related features]
- **SPO2 (SPO2):** [Description of a group of related features]
- **C4-A1 (C4A1):** EEG derivation[Description of a group of related features]
- **O2-A1 (O2A1):** EEG derivation[Description of a group of related features]

## Exploratory Data Analysis

The exploratory data analysis is conducted in the [exploratory_data_analysis.ipynb](exploratory_data_analysis.ipynb) notebook, which includes:

- Data loading and initial inspection
- Statistical summaries and distributions
- Missing value analysis
- Feature correlation analysis
- Data visualization and insights
- Data quality assessment
