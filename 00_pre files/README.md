# Data Processing

This section describes the data preprocessing pipeline and the evolution of the normalization
and aggregation strategy throughout the project.

The preprocessing choices had a strong impact on model behavior and were iteratively refined
based on empirical evaluation results.

---

## Initial Preprocessing Strategy (Window-Level)

In the initial experiments, preprocessing was applied directly to the **original 90-second windows**
provided by the challenge dataset.

Each window contains:
- 90 seconds of signal
- 8 physiological channels
- Sampling rate of 100 Hz
- Independent normalization per window

### Window-Level Normalization

Signals were normalized **independently within each 90-second window**, using per-window
mean and standard deviation.

While this approach ensured numerical stability and fast convergence, it introduced
unintended side effects:
- Loss of amplitude consistency across consecutive windows
- Disruption of inter-window temporal relationships
- Reduced ability to distinguish sustained physiological trends

---

## Impact on Model Performance

The negative impact of window-level normalization became evident in early submissions,
which achieved very low event-based F1-scores despite seemingly reasonable training loss.

| Experiment | Description | Event-F1 |
|----------|-------------|----------|
| 3-layer CNN, threshold 0.54 | Window-level normalization | 0.0406 |
| 3-layer CNN, threshold 0.55 | Window-level normalization | 0.0171 |
| 3-layer CNN, LR 1e-6 | Window-level normalization | 0.0011 |
| 3-layer CNN, LR 1e-6 | Window-level normalization | 0.0000 |

These results suggested that the model struggled to produce temporally coherent apnea events,
even when classification confidence appeared reasonable.

---

## Revised Preprocessing Strategy (Night-Level)

To address these limitations, preprocessing was restructured around **full-night signals**.

### Night-Level Aggregation

For each subject:
- All 200 non-overlapping 90-second windows were concatenated
- A continuous **full-night signal** was reconstructed
- Normalization was performed **within each night**, preserving relative amplitudes
  across the entire recording

This change ensured:
- Consistent signal scaling across windows
- Preservation of long-term physiological context
- Improved temporal continuity for downstream modeling

---

## Temporal Chunking for Training and Inference

After night-level normalization, full-night signals were split into longer temporal segments
to balance context and computational feasibility.

### Chunking Parameters
- **Chunk duration:** 300 seconds (5 minutes)
- **Stride:** 60 seconds
- **Overlap:** 80% (240 seconds overlap)

This configuration provides:
- Sufficient temporal context to capture apnea patterns
- Dense coverage of the full night
- Smooth prediction transitions through overlap-based aggregation

Overlapping predictions are later merged using averaging to produce a stable 1 Hz
probability sequence for the entire night.

---

## Rationale for the Final Design

The transition from window-level to night-level preprocessing was motivated by the need to:
- Align preprocessing with the event-based evaluation metric
- Preserve physiological continuity across time
- Reduce artificial variability introduced by per-window normalization

This revised preprocessing pipeline proved critical for improving temporal coherence
and enabling meaningful gains in event-based F1-score.

---

## Summary

- **Initial approach:** Per-window normalization on isolated 90-second segments  
- **Observed issue:** Severe degradation of event-level performance  
- **Final approach:** Night-level normalization with overlapping 5-minute chunks  
- **Outcome:** Improved temporal consistency and more reliable event detection

This preprocessing strategy forms the foundation for all subsequent modeling experiments.
