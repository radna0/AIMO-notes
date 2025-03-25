import math
import numpy as np
import matplotlib.pyplot as plt


# -------------------------
# "Paper" version of Cosine
# -------------------------
def paper_cosfn(t, T, min_val, max_val):
    """
    Typical formula from Cosine decay schedules:
      paper_cosfn(t, T) = min_val + 0.5*(max_val - min_val) * [1 + cos(pi * t / T)]
    """
    return min_val + 0.5 * (max_val - min_val) * (1 + math.cos(math.pi * t / T))


# --------------------------------
# Current code's version of Cosine
# --------------------------------
def current_cosfn(t, T, min_val, max_val):
    """
    current_cosfn(t, T) = max_val - (max_val - min_val)*[1 - cos(pi*t/T)] / 2
    which algebraically also simplifies to:
      (min_val + max_val)/2 + (max_val - min_val)/2 * cos(pi * t / T)
    (i.e. it is also a standard cosine schedule from max_val at t=0 to min_val at t=T).
    """
    return max_val - (max_val - min_val) * (1 - math.cos(math.pi * t / T)) / 2


# For plotting
def plot_cosines(stage_name, T, min_correct, max_correct, min_wrong, max_wrong):
    ts = np.linspace(0, T, 200)  # 200 points from 0 to T

    # Paper version
    y_correct_paper = [paper_cosfn(t, T, max_correct, min_correct) for t in ts]
    y_wrong_paper = [paper_cosfn(t, T, min_wrong, max_wrong) for t in ts]

    # Current code
    y_correct_current = [current_cosfn(t, T, max_correct, min_correct) for t in ts]
    y_wrong_current = [current_cosfn(t, T, min_wrong, max_wrong) for t in ts]

    plt.figure(figsize=(7, 5))
    plt.title(f"Stage: {stage_name} — Cosine Schedules")
    plt.plot(ts, y_correct_paper, "g--", label="Paper Cosine (Correct)")
    plt.plot(ts, y_correct_current, "g-", label="Current Code (Correct)")
    plt.plot(ts, y_wrong_paper, "r--", label="Paper Cosine (Wrong)")
    plt.plot(ts, y_wrong_current, "r-", label="Current Code (Wrong)")
    plt.xlabel("Token Length t")
    plt.ylabel("Reward")
    plt.legend(loc="best")
    plt.grid(True)
    plt.show()


def print_sample_table(stage_name, T, min_correct, max_correct, min_wrong, max_wrong):
    """
    Print a small table of values at t = 0, T/4, T/2, 3T/4, T
    comparing paper vs current for both correct & wrong.
    """
    sample_points = [0, T / 4, T / 2, 3 * T / 4, T]
    print(f"=== Stage: {stage_name} ===")
    print("  t   | Paper(Corr) | Curr(Corr) | Paper(Wrong) | Curr(Wrong)")
    print("------------------------------------------------------------")
    for t in sample_points:
        pc = paper_cosfn(t, T, max_correct, min_correct)
        cc = current_cosfn(t, T, max_correct, min_correct)
        pw = paper_cosfn(t, T, min_wrong, max_wrong)
        cw = current_cosfn(t, T, min_wrong, max_wrong)
        print(f"{int(t):5d} |  {pc:10.4f} |  {cc:10.4f} |  {pw:10.4f}  |  {cw:10.4f}")
    print()


# -----------------------
# Parameters and plotting
# -----------------------
T = 12288



# Stage 1: Priming
stage1_min_correct = 0.5  # min_len_value_correct
stage1_max_correct = 0.25  # max_len_value_correct
stage1_max_wrong = 0  # min_len_value_wrong
stage1_min_wrong = -1  # max_len_value_wrong

plot_cosines(
    "Stage 1 (Priming)",
    T,
    stage1_min_correct,
    stage1_max_correct,
    stage1_min_wrong,
    stage1_max_wrong,
)
print_sample_table(
    "Stage 1 (Priming)",
    T,
    stage1_min_correct,
    stage1_max_correct,
    stage1_min_wrong,
    stage1_max_wrong,
)

# Stage 2: Walking
stage2_min_correct = 1.0
stage2_max_correct = 0.5
stage2_min_wrong = 0
stage2_max_wrong = -1

plot_cosines(
    "Stage 2 (Walking)",
    T,
    stage2_min_correct,
    stage2_max_correct,
    stage2_min_wrong,
    stage2_max_wrong,
)
print_sample_table(
    "Stage 2 (Walking)",
    T,
    stage2_min_correct,
    stage2_max_correct,
    stage2_min_wrong,
    stage2_max_wrong,
)

# Stage 3: Running
stage3_min_correct = 1.0
stage3_max_correct = 0.5
stage3_min_wrong = -0
stage3_max_wrong = -0.5

plot_cosines(
    "Stage 3 (Running)",
    T,
    stage3_min_correct,
    stage3_max_correct,
    stage3_min_wrong,
    stage3_max_wrong,
)
print_sample_table(
    "Stage 3 (Running)",
    T,
    stage3_min_correct,
    stage3_max_correct,
    stage3_min_wrong,
    stage3_max_wrong,
)
