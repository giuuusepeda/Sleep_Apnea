# Literature Review

Approaches or solutions that have been tried before on similar projects.

**Summary of Each Work**:

### Source 1: Detecting Sleep Apnea from Raw Physiological Signals (Challenge Data)
Link: https://challengedata.ens.fr/challenges/45. :contentReference[oaicite:1]{index=1}

Objective:
The challenge asks participants to build an automatic model to detect sleep apnea events from multi-channel polysomnography (PSG) recordings by classifying 90-s windows into apnea vs non-apnea segments.

Methods:
The dataset contains 44 nights, each split into 200 non-overlapping 90-second windows sampled at 100 Hz for 8 physiological signals (ECG, EEG, respiration, SpO₂, etc.). Typical approaches include preprocessing (filtering, resampling), feature extraction (HRV, SpO₂ desaturation, respiratory features), and supervised learning models such as 1D-CNNs, RNNs, or hybrid CNN–LSTM architectures.

Outcomes:
The challenge provides a standard benchmark and evaluation protocol for event-level apnea detection and has been used as the basis for comparing classical feature-based methods and end-to-end deep learning methods.

Relation to the Project:
This is the primary dataset and task definition for our project; all preprocessing, modeling, and evaluation must follow the dataset format and the challenge’s expected submission format and metrics. :contentReference[oaicite:2]{index=2}


- **Source 2**: [Title of Source 2]

  - **[Link]()**
  - **Objective**:
  - **Methods**:
  - **Outcomes**:
  - **Relation to the Project**:

- **Source 3**: [Title of Source 3]

  - **[Link]()**
  - **Objective**:
  - **Methods**:
  - **Outcomes**:
  - **Relation to the Project**:
