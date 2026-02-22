"""
Event-based metrics for sleep apnea detection.

Implements the official evaluation metric: event-based F1-score with 
Intersection-over-Union (IoU) matching at threshold IoU >= 0.3.

This metric operates at the event level rather than point-wise:
- Binary predictions are converted into temporal apnea events
- Predicted events are matched to reference events using IoU ≥ 0.3
- Precision and recall are computed based on matched events
- Final score is the event-level F1-score
"""

import numpy as np
from typing import Tuple, List, Dict


def extract_events(binary_mask: np.ndarray, min_duration: int = 1) -> List[Tuple[int, int]]:
    """
    Extract temporal events from a binary mask.
    
    An event is defined as a contiguous sequence of 1s in the binary mask.
    
    Args:
        binary_mask: 1D numpy array of binary predictions (0s and 1s)
        min_duration: Minimum duration (in samples) to be considered an event
        
    Returns:
        List of events as (start, end) tuples (inclusive, in sample indices)
    """
    binary_mask = np.asarray(binary_mask, dtype=int).flatten()
    
    # Find transitions
    diff = np.diff(np.concatenate(([0], binary_mask, [0])).astype(int))
    starts = np.where(diff == 1)[0]
    ends = np.where(diff == -1)[0] - 1
    
    # Filter by minimum duration
    events = []
    for start, end in zip(starts, ends):
        duration = end - start + 1
        if duration >= min_duration:
            events.append((int(start), int(end)))
    
    return events


def compute_iou(event1: Tuple[int, int], event2: Tuple[int, int]) -> float:
    """
    Compute Intersection-over-Union (IoU) between two events.
    
    Args:
        event1: (start, end) tuple for first event
        event2: (start, end) tuple for second event
        
    Returns:
        IoU value between 0 and 1
    """
    start1, end1 = event1
    start2, end2 = event2
    
    # Compute intersection
    intersection_start = max(start1, start2)
    intersection_end = min(end1, end2)
    
    if intersection_start > intersection_end:
        intersection = 0
    else:
        intersection = intersection_end - intersection_start + 1
    
    # Compute union
    union_start = min(start1, start2)
    union_end = max(end1, end2)
    union = union_end - union_start + 1
    
    iou = intersection / union if union > 0 else 0.0
    return float(iou)


def match_events(predicted_events: List[Tuple[int, int]], 
                reference_events: List[Tuple[int, int]], 
                iou_threshold: float = 0.3) -> Tuple[int, List[int], List[int]]:
    """
    Match predicted events to reference events using IoU matching.
    
    Each predicted event is matched to at most one reference event and vice versa.
    A match requires IoU >= iou_threshold.
    
    Args:
        predicted_events: List of predicted events (start, end)
        reference_events: List of reference events (start, end)
        iou_threshold: Minimum IoU for a valid match (default 0.3)
        
    Returns:
        Tuple of:
        - num_matches: Number of successfully matched events
        - matched_predicted_indices: Indices of matched predicted events
        - matched_reference_indices: Indices of matched reference events
    """
    matched_predicted = set()
    matched_reference = set()
    
    # Compute IoU matrix
    iou_matrix = np.zeros((len(predicted_events), len(reference_events)))
    for i, pred_event in enumerate(predicted_events):
        for j, ref_event in enumerate(reference_events):
            iou_matrix[i, j] = compute_iou(pred_event, ref_event)
    
    # Greedy matching: match highest IoU pairs first
    while True:
        # Find best unmatched pair
        best_iou = iou_threshold
        best_i = -1
        best_j = -1
        
        for i in range(len(predicted_events)):
            if i in matched_predicted:
                continue
            for j in range(len(reference_events)):
                if j in matched_reference:
                    continue
                if iou_matrix[i, j] > best_iou:
                    best_iou = iou_matrix[i, j]
                    best_i = i
                    best_j = j
        
        if best_i == -1:
            break
        
        matched_predicted.add(best_i)
        matched_reference.add(best_j)
    
    return len(matched_predicted), sorted(list(matched_predicted)), sorted(list(matched_reference))


def compute_event_based_metrics(y_true: np.ndarray, 
                               y_pred: np.ndarray,
                               threshold: float = 0.5,
                               iou_threshold: float = 0.3,
                               min_duration: int = 1) -> Dict[str, float]:
    """
    Compute event-based metrics (precision, recall, F1) with IoU matching.
    
    Args:
        y_true: Ground truth binary labels (1D or 2D array)
        y_pred: Predicted probabilities (1D or 2D array)
        threshold: Probability threshold for binarization (default 0.5)
        iou_threshold: Minimum IoU for event matching (default 0.3)
        min_duration: Minimum event duration in samples (default 1)
        
    Returns:
        Dictionary with keys:
        - 'precision': Precision (TP / (TP + FP))
        - 'recall': Recall (TP / (TP + FN))
        - 'f1_score': F1-score (2 * precision * recall / (precision + recall))
        - 'num_predicted': Total number of predicted events
        - 'num_reference': Total number of reference events
        - 'num_matched': Number of matched event pairs
    """
    # Flatten arrays
    y_true_flat = np.asarray(y_true, dtype=int).flatten()
    y_pred_flat = np.asarray(y_pred, dtype=float).flatten()
    
    # Binarize predictions
    y_pred_binary = (y_pred_flat >= threshold).astype(int)
    
    # Extract events
    reference_events = extract_events(y_true_flat, min_duration=min_duration)
    predicted_events = extract_events(y_pred_binary, min_duration=min_duration)
    
    # Match events
    num_matched, _, _ = match_events(predicted_events, reference_events, iou_threshold)
    
    # Compute metrics
    num_predicted = len(predicted_events)
    num_reference = len(reference_events)
    
    # True Positives, False Positives, False Negatives
    tp = num_matched
    fp = num_predicted - num_matched
    fn = num_reference - num_matched
    
    # Precision and Recall
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    
    # F1-score
    if precision + recall > 0:
        f1 = 2 * (precision * recall) / (precision + recall)
    else:
        f1 = 0.0
    
    return {
        'precision': float(precision),
        'recall': float(recall),
        'f1_score': float(f1),
        'num_predicted': int(num_predicted),
        'num_reference': int(num_reference),
        'num_matched': int(num_matched),
        'true_positives': int(tp),
        'false_positives': int(fp),
        'false_negatives': int(fn)
    }


def compute_event_based_metrics_per_window(y_true: np.ndarray,
                                          y_pred: np.ndarray,
                                          window_indices: np.ndarray = None,
                                          threshold: float = 0.5,
                                          iou_threshold: float = 0.3) -> Dict[int, Dict[str, float]]:
    """
    Compute event-based metrics for each window separately.
    
    Useful for per-window or per-subject evaluation.
    
    Args:
        y_true: Ground truth labels (shape: num_windows x num_timesteps)
        y_pred: Predicted probabilities (shape: num_windows x num_timesteps)
        window_indices: Array mapping each sample to its window index
        threshold: Probability threshold for binarization
        iou_threshold: Minimum IoU for event matching
        
    Returns:
        Dictionary mapping window index to metrics dictionary
    """
    y_true = np.asarray(y_true, dtype=int)
    y_pred = np.asarray(y_pred, dtype=float)
    
    if y_true.ndim == 1:
        # Single window/sequence
        return {0: compute_event_based_metrics(y_true, y_pred, threshold, iou_threshold)}
    
    # Multiple windows
    num_windows = y_true.shape[0]
    results = {}
    
    for window_idx in range(num_windows):
        y_true_window = y_true[window_idx]
        y_pred_window = y_pred[window_idx]
        
        metrics = compute_event_based_metrics(
            y_true_window, y_pred_window, threshold, iou_threshold
        )
        results[window_idx] = metrics
    
    return results


def aggregate_metrics(per_window_metrics: Dict[int, Dict[str, float]]) -> Dict[str, float]:
    """
    Aggregate per-window metrics into overall metrics.
    
    Uses macro-averaging (average of each window's metrics).
    
    Args:
        per_window_metrics: Dictionary of window indices to metrics
        
    Returns:
        Aggregated metrics dictionary
    """
    if not per_window_metrics:
        return {
            'precision': 0.0,
            'recall': 0.0,
            'f1_score': 0.0,
            'avg_predicted_per_window': 0.0,
            'avg_reference_per_window': 0.0,
            'total_matched': 0
        }
    
    precisions = []
    recalls = []
    f1_scores = []
    total_matched = 0
    total_predicted = 0
    total_reference = 0
    
    for metrics in per_window_metrics.values():
        precisions.append(metrics['precision'])
        recalls.append(metrics['recall'])
        f1_scores.append(metrics['f1_score'])
        total_matched += metrics['num_matched']
        total_predicted += metrics['num_predicted']
        total_reference += metrics['num_reference']
    
    num_windows = len(per_window_metrics)
    
    return {
        'precision': np.mean(precisions),
        'recall': np.mean(recalls),
        'f1_score': np.mean(f1_scores),
        'std_precision': np.std(precisions),
        'std_recall': np.std(recalls),
        'std_f1_score': np.std(f1_scores),
        'avg_predicted_per_window': total_predicted / num_windows,
        'avg_reference_per_window': total_reference / num_windows,
        'total_matched': int(total_matched),
        'total_predicted': int(total_predicted),
        'total_reference': int(total_reference)
    }


# Example usage and testing
if __name__ == "__main__":
    print("=" * 60)
    print("Event-Based Metrics - Example Usage")
    print("=" * 60)
    
    # Create synthetic example
    np.random.seed(42)
    
    # Reference: two events at [10-20] and [50-60]
    y_true = np.zeros(100, dtype=int)
    y_true[10:21] = 1
    y_true[50:61] = 1
    
    # Prediction: events at [10-22] and [52-62] (slightly shifted)
    y_pred = np.zeros(100, dtype=float)
    y_pred[10:23] = 0.8
    y_pred[52:63] = 0.9
    
    metrics = compute_event_based_metrics(y_true, y_pred)
    
    print("\nExample Metrics:")
    for key, value in metrics.items():
        print(f"  {key}: {value}")
    
    print("\n" + "=" * 60)
    print("✓ metrics.py ready to use")
    print("=" * 60)
