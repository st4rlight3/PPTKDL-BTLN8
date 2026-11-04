#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Đề 8: tái lập dữ liệu MÔ PHỎNG, kiểm định và 200 lần lặp.

Chạy: python analysis.py --out-dir .
Không làm tròn dữ liệu trước khi xếp hạng hoặc kiểm định.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import platform
import sys

import numpy as np
import pandas as pd
import scipy
from scipy import stats
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

N = 40
REPS = 200
ALPHA = 0.05
DEFAULT_SEED = 20261104
BLUE = "#2563A6"
ORANGE = "#D8752E"


def draw(rng: np.random.Generator) -> tuple[np.ndarray, np.ndarray]:
    """Hai mẫu độc lập; cùng thang mũ 10 ms, khác vị trí 4 ms."""
    return 20.0 + rng.exponential(10.0, N), 16.0 + rng.exponential(10.0, N)


def descriptive(x: np.ndarray, name: str) -> dict:
    q1, q3 = np.quantile(x, [0.25, 0.75], method="linear")
    return {"group": name, "n": len(x), "mean_ms": float(x.mean()),
            "median_ms": float(np.median(x)), "sd_ms": float(x.std(ddof=1)),
            "q1_ms": float(q1), "q3_ms": float(q3), "iqr_ms": float(q3-q1),
            "min_ms": float(x.min()), "max_ms": float(x.max()),
            "skewness_adjusted": float(stats.skew(x, bias=False))}


def analyze(a: np.ndarray, b: np.ndarray) -> dict:
    """Ước lượng hoàn toàn từ mẫu; kiểm chứng công thức với SciPy."""
    na, nb = len(a), len(b)
    pooled = np.concatenate([a, b])
    ranks = stats.rankdata(pooled, method="average")
    ra, rb = float(ranks[:na].sum()), float(ranks[na:].sum())
    ua = ra - na*(na+1)/2
    ub = rb - nb*(nb+1)/2
    _, tie_sizes = np.unique(pooled, return_counts=True)
    tie_sum = int(np.sum(tie_sizes**3 - tie_sizes))
    total = na+nb
    var_u = na*nb/12 * ((total+1) - tie_sum/(total*(total-1)))
    sd_u = math.sqrt(var_u)
    z_abs = (max(ua, ub)-na*nb/2-0.5)/sd_u
    p_manual = min(1.0, float(2*stats.norm.sf(z_abs)))
    mw = stats.mannwhitneyu(a, b, alternative="two-sided",
                            method="asymptotic", use_continuity=True)
    va, vb = float(a.var(ddof=1)), float(b.var(ddof=1))
    diff = float(a.mean()-b.mean())
    se = math.sqrt(va/na+vb/nb)
    t_manual = diff/se
    df = (va/na+vb/nb)**2 / ((va/na)**2/(na-1)+(vb/nb)**2/(nb-1))
    welch = stats.ttest_ind(a, b, equal_var=False, alternative="two-sided")
    p_welch_manual = float(2*stats.t.sf(abs(t_manual), df))
    q = float(stats.t.ppf(1-ALPHA/2, df))
    # Các kiểm tra độc lập: tổng hạng, thống kê và p-value tính tay.
    assert abs(ra+rb-total*(total+1)/2) < 1e-9
    assert abs(ua+ub-na*nb) < 1e-9
    assert abs(ua-float(mw.statistic)) < 1e-9
    assert abs(p_manual-float(mw.pvalue)) < 1e-12
    assert abs(t_manual-float(welch.statistic)) < 1e-12
    assert abs(df-float(welch.df)) < 1e-10
    assert abs(p_welch_manual-float(welch.pvalue)) < 1e-12
    # U_A cũng bằng tổng số cặp A>B cộng nửa số cặp bằng nhau.
    pair_count = float((a[:, None] > b[None, :]).sum()
                       + 0.5*(a[:, None] == b[None, :]).sum())
    assert pair_count == ua
    return {"n_a": na, "n_b": nb, "rank_sum_a": ra, "rank_sum_b": rb,
            "u_a": float(ua), "u_b": float(ub), "u_min": float(min(ua, ub)),
            "u_null_mean": na*nb/2, "u_null_variance": float(var_u),
            "u_null_sd": sd_u, "tie_correction_sum": tie_sum,
            "tied_value_groups": int((tie_sizes > 1).sum()),
            "z_abs_continuity": float(z_abs), "p_mann_whitney": float(mw.pvalue),
            "reject_mann_whitney": bool(mw.pvalue < ALPHA),
            "prob_a_greater_b_hat": float(ua/(na*nb)),
            "rank_biserial_a_minus_b": float(2*ua/(na*nb)-1),
            "mean_a_ms": float(a.mean()), "mean_b_ms": float(b.mean()),
            "mean_difference_a_minus_b_ms": diff,
            "median_difference_a_minus_b_ms": float(np.median(a)-np.median(b)),
            "welch_standard_error_ms": se, "t_welch": float(welch.statistic),
            "df_welch": df, "p_welch": float(welch.pvalue),
            "reject_welch": bool(welch.pvalue < ALPHA),
            "mean_difference_ci95_low_ms": diff-q*se,
            "mean_difference_ci95_high_ms": diff+q*se}


def wilson(k: int, n: int) -> tuple[float, float]:
    z = float(stats.norm.ppf(0.975))
    p = k/n
    center = (p+z*z/(2*n))/(1+z*z/n)
    half = z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/(1+z*z/n)
    return center-half, center+half


def tidy(a: np.ndarray, b: np.ndarray, rep: int | None = None) -> pd.DataFrame:
    records = []
    for group, values in [("A", a), ("B", b)]:
        for i, value in enumerate(values, 1):
            row = {"observation_id": f"{group}{i:02d}", "group": group,
                   "latency_ms": float(value)}
            if rep is not None:
                row = {"replicate": rep, **row}
            records.append(row)
    return pd.DataFrame(records)


def write_csv(frame: pd.DataFrame, path: Path) -> None:
    # UTF-8 BOM dễ mở trong Excel; 17 chữ số bảo toàn số thực nhị phân.
    frame.to_csv(path, index=False, encoding="utf-8-sig", float_format="%.17g",
                 lineterminator="\n")


def plots(a, b, mc, mc_summary, output):
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                         "axes.spines.top": False, "axes.spines.right": False,
                         "axes.titleweight": "bold", "figure.facecolor": "white"})
    bins = np.histogram_bin_edges(np.concatenate([a, b]), bins="fd")
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.1), sharex=True, sharey=True)
    for ax, vals, group, color in zip(axes, [a, b], ["A", "B"], [BLUE, ORANGE]):
        ax.hist(vals, bins=bins, color=color, alpha=0.9, edgecolor="white")
        ax.axvline(np.mean(vals), color="#202B3D", lw=1.8, label="Trung bình")
        ax.axvline(np.median(vals), color="#202B3D", linestyle="--", lw=1.5,
                   label="Trung vị")
        ax.set_title(f"Phương án {group} (n = {len(vals)})")
        ax.set_xlabel("Độ trễ (ms)")
        ax.grid(axis="y", alpha=.15)
        ax.legend(frameon=False, fontsize=9)
    axes[0].set_ylabel("Số phiên truyền")
    fig.tight_layout()
    fig.savefig(output/"histogram.png", dpi=220, bbox_inches="tight")
    plt.close(fig)
    fig, ax = plt.subplots(figsize=(8.2, 3.8))
    bp = ax.boxplot([a, b], tick_labels=["Phương án A", "Phương án B"],
                    orientation="horizontal", patch_artist=True, widths=.48,
                    medianprops={"color": "#172337", "linewidth": 2},
                    flierprops={"marker": "o", "markersize": 4,
                                "markerfacecolor": "none", "markeredgecolor": "#64748b"})
    for patch, color in zip(bp["boxes"], [BLUE, ORANGE]):
        patch.set_facecolor(color)
        patch.set_alpha(.7)
    ax.set_xlabel("Độ trễ (ms)")
    ax.set_title("Biểu đồ hộp của mẫu phân tích chi tiết")
    ax.grid(axis="x", alpha=.15)
    fig.tight_layout()
    fig.savefig(output/"boxplot.png", dpi=220, bbox_inches="tight")
    plt.close(fig)
    fig, ax = plt.subplots(figsize=(8.3, 4.3))
    rates = [x["detection_rate"] for x in mc_summary]
    lows = [x["wilson_ci95_low"] for x in mc_summary]
    highs = [x["wilson_ci95_high"] for x in mc_summary]
    names = ["Mann-Whitney", "Welch"]
    bars = ax.bar(names, rates, color=[BLUE, ORANGE], width=.52)
    ax.errorbar(names, rates, yerr=[np.array(rates)-lows, np.array(highs)-rates],
                fmt="none", capsize=6, color="#172337", lw=1.4)
    for bar, record in zip(bars, mc_summary):
        ax.text(bar.get_x()+bar.get_width()/2, record["wilson_ci95_high"]+.035,
                f'{record["detected"]}/200 = {record["detection_rate"]:.1%}',
                ha="center", va="bottom", fontweight="bold")
    ax.set_ylim(0, 1)
    ax.set_ylabel("Tỷ lệ phát hiện khác biệt")
    ax.set_title("200 mẫu mới, mỗi mẫu 40 phiên cho từng phương án")
    ax.yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1))
    ax.grid(axis="y", alpha=.15)
    ax.text(.5, -.21, "Thanh sai số: khoảng Wilson 95% cho tỷ lệ Monte Carlo.",
            transform=ax.transAxes, ha="center", fontsize=10)
    fig.tight_layout()
    fig.savefig(output/"monte_carlo_detection.png", dpi=220, bbox_inches="tight")
    plt.close(fig)
    fig, ax = plt.subplots(figsize=(8.3, 3.7))
    edges = np.linspace(0, 1, 21)
    ax.hist(mc["p_mann_whitney"], bins=edges, color=BLUE, alpha=.65,
            label="Mann-Whitney")
    ax.hist(mc["p_welch"], bins=edges, color=ORANGE, alpha=.55, label="Welch")
    ax.axvline(ALPHA, color="#172337", linestyle="--", label="Mức ý nghĩa 0,05")
    ax.set_xlabel("p-value hai phía")
    ax.set_ylabel("Số lần lặp")
    ax.set_title("Phân bố p-value trong 200 lần mô phỏng")
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(output/"pvalue_distribution.png", dpi=220, bbox_inches="tight")
    plt.close(fig)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    parser.add_argument("--out-dir", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    out = args.out_dir.resolve()
    for folder in ["data", "results", "figures"]:
        (out/folder).mkdir(parents=True, exist_ok=True)
    # Luồng 0 cho mẫu chi tiết; luồng 1 sinh 200 luồng con cho mô phỏng lặp.
    detail_seed, mc_seed = np.random.SeedSequence(args.seed).spawn(2)
    a, b = draw(np.random.default_rng(detail_seed))
    detail = tidy(a, b)
    desc = [descriptive(a, "A"), descriptive(b, "B")]
    tests = analyze(a, b)
    rank_table = detail.copy()
    rank_table["rank"] = stats.rankdata(rank_table["latency_ms"], method="average")
    rank_table = rank_table.sort_values(["latency_ms", "observation_id"],
                                       kind="stable").reset_index(drop=True)
    rank_table.insert(0, "sorted_order", np.arange(1, 2*N+1))
    write_csv(detail, out/"data"/"sample_detail.csv")
    write_csv(rank_table, out/"data"/"pooled_ranks.csv")
    write_csv(pd.DataFrame(desc), out/"results"/"descriptive.csv")
    write_csv(pd.DataFrame([tests]), out/"results"/"detail_tests.csv")
    rep_rows, raw_reps = [], []
    seeds = mc_seed.spawn(REPS)
    for rep, child_seed in enumerate(seeds, 1):
        ar, br = draw(np.random.default_rng(child_seed))
        row = {"replicate": rep, "seed_spawn_key": ".".join(map(str, child_seed.spawn_key)),
               **analyze(ar, br)}
        rep_rows.append(row)
        raw_reps.append(tidy(ar, br, rep))
    mc = pd.DataFrame(rep_rows)
    mc_raw = pd.concat(raw_reps, ignore_index=True)
    assert len(mc) == REPS and len(mc_raw) == REPS*2*N
    assert len(set(tuple(s.spawn_key) for s in seeds)) == REPS
    assert not mc_raw.duplicated(["replicate", "observation_id"]).any()
    write_csv(mc, out/"results"/"simulation_200.csv")
    write_csv(mc_raw, out/"data"/"simulation_200_raw.csv")
    mc_summary = []
    for label, col in [("Mann-Whitney", "reject_mann_whitney"), ("Welch", "reject_welch")]:
        count = int(mc[col].sum())
        rate = count/REPS
        low, high = wilson(count, REPS)
        mc_summary.append({"test": label, "replications": REPS, "detected": count,
                           "detection_rate": rate,
                           "monte_carlo_se": math.sqrt(rate*(1-rate)/REPS),
                           "wilson_ci95_low": low, "wilson_ci95_high": high})
    write_csv(pd.DataFrame(mc_summary), out/"results"/"simulation_summary.csv")
    mw_rej = mc["reject_mann_whitney"].astype(bool)
    w_rej = mc["reject_welch"].astype(bool)
    joint = {"both_detect": int((mw_rej & w_rej).sum()),
             "mann_whitney_only": int((mw_rej & ~w_rej).sum()),
             "welch_only": int((~mw_rej & w_rej).sum()),
             "neither_detect": int((~mw_rej & ~w_rej).sum())}
    theory = {"mean_a_ms": 30.0, "mean_b_ms": 26.0,
              "median_a_ms": 20+10*math.log(2), "median_b_ms": 16+10*math.log(2),
              "sd_both_ms": 10.0, "iqr_both_ms": 10*math.log(3),
              "position_shift_a_minus_b_ms": 4.0,
              "prob_a_greater_b": 1-0.5*math.exp(-0.4)}
    summary = {"seed": args.seed, "n_per_group": N, "replications": REPS,
               "alpha": ALPHA, "confidence_level": 0.95,
               "quantile_method": "numpy.quantile(method='linear')",
               "sd_ddof": 1, "mann_whitney_method": "asymptotic, two-sided, continuity=True, tie correction",
               "seed_streams": {"detail_spawn_key": list(detail_seed.spawn_key),
                                "simulation_parent_spawn_key": list(mc_seed.spawn_key),
                                "replicate_spawn_keys": [list(s.spawn_key) for s in seeds]},
               "versions": {"python": platform.python_version(), "numpy": np.__version__,
                            "pandas": pd.__version__, "scipy": scipy.__version__,
                            "matplotlib": matplotlib.__version__},
               "descriptive": desc, "detail_tests": tests,
               "simulation_summary": mc_summary, "joint_detection_counts": joint,
               "generator_theory_for_evaluation_only": theory,
               "verification": {"manual_rank_u_matches_scipy": True,
                                "pair_count_u_matches_rank_u": True,
                                "manual_welch_matches_scipy": True,
                                "fresh_replications": REPS}}
    (out/"results"/"summary.json").write_text(json.dumps(summary, indent=2,
                                                 ensure_ascii=False, allow_nan=False), encoding="utf-8")
    plots(a, b, mc, mc_summary, out/"figures")
    # Dấu vân tay của các tệp số liệu, phục vụ đối chiếu khi chạy lại.
    fingerprints = {str(p.relative_to(out)).replace("\\", "/"):
                    hashlib.sha256(p.read_bytes()).hexdigest()
                    for p in sorted(out.glob("data/*.csv"))+sorted(out.glob("results/*.csv"))}
    (out/"results"/"sha256_data.json").write_text(json.dumps(fingerprints, indent=2), encoding="utf-8")
    print(json.dumps({"out_dir": str(out), "seed": args.seed,
                      "detail_tests": tests, "simulation_summary": mc_summary},
                     indent=2, ensure_ascii=True))


if __name__ == "__main__":
    main()
