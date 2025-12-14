# Model Definition and Evaluation

**[Notebook](model_definition_evaluation.ipynb)**

## Evaluation Metric

Model performance is assessed using the **official Dreem Sleep Apnea Detection metric**:  
an **event-based F1-score with Intersection-over-Union (IoU) matching**.

Unlike point-wise or window-level metrics, this evaluation operates at the **event level**:
- Binary predictions at 1 Hz are first converted into temporal apnea events
- Predicted events are matched to reference events using IoU ≥ 0.3
- Precision and recall are computed based on matched events
- The final score is the event-level F1-score

This metric strongly penalizes:
- Fragmented detections of the same event
- Spurious short events
- Temporal misalignment of predicted event boundaries

As a result, good per-second accuracy does not necessarily translate into a high event-based F1-score.
Robust temporal coherence is therefore essential.

---

## Model Exploration Strategy

Given the limited dataset size (44 nights) and the strong inter-subject variability in apnea burden,
model exploration was structured around a **controlled and systematic design space**.

We initiated the exploration of **five architectural families**, each evaluated at **three different model sizes**, defined by the **number of layers and representational capacity** rather than temporal context.

### Model Families
1. **CNN** — purely convolutional temporal feature extraction
2. **CNN + GRU** — convolutional front-end with gated recurrent units
3. **CNN + LSTM** — convolutional front-end with long short-term memory units
4. **GRU** — recurrent-only temporal modeling
5. **LSTM** — recurrent-only temporal modeling

### Model Sizes
For each family, three configurations were explored:

- **Small** — fewer layers and reduced number of filters/units  
- **Medium** — intermediate depth and capacity  
- **Large** — deeper architectures with increased representational power  

These variations allow the analysis of the trade-off between model capacity and generalization,
which is particularly important given the limited number of subjects and the high variance in event frequency across nights.

Overall, this resulted in an initial grid of **15 candidate configurations** (5 families × 3 sizes).

---

## Evaluation Protocol

To prevent data leakage, all evaluations were performed using **subject-wise splits**.
Models were selected and tuned based on:
- Event-based F1-score on validation subjects
- Stability of predictions across subjects with very different apnea prevalence
- Consistency between validation and test behavior after post-processing

Given the high variance across individuals, emphasis was placed on **robustness rather than peak validation performance**.

---

## Observations and Challenges

Early experiments confirmed several key challenges:
- Validation performance is highly sensitive to subject composition
- Threshold and post-processing parameters can significantly shift event-level F1
- Models may overfit nights with high apnea density at the expense of low-event subjects

These findings motivated conservative model selection and reinforced the need for
cross-validation strategies in subsequent iterations.

---

## Challenges and Observations

Several challenges emerged during model development and evaluation:

- **High inter-subject variability:**  
  Apnea event frequency varies drastically across nights, ranging from very sparse to highly dense event distributions.

- **Sensitivity to validation splits:**  
  Event-level performance is strongly influenced by which subjects are included in the validation set, making single splits unstable.

- **Model capacity trade-offs:**  
  Increasing the number of layers and parameters does not consistently improve event-based F1-score and may lead to overfitting subjects with high apnea burden.

- **Post-processing dependency:**  
  Thresholding and event consolidation parameters (minimum duration and gap filling) have a significant impact on the final score, sometimes outweighing architectural differences.

- **Metric strictness:**  
  The IoU-based event-level F1 metric penalizes temporal fragmentation and boundary misalignment, requiring models to produce temporally coherent predictions rather than isolated positive samples.

---

## Outlook

To mitigate these challenges, future work will focus on subject-wise cross-validation,
more robust hyperparameter tuning, and architectures explicitly designed to model
long-range temporal dependencies.
