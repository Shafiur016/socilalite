# Experimental Outline: Depression_New_Submit (5)

## 1. Goals & Hypotheses
- Dual NLP tasks on social-media text: (a) multi-label emotion detection with eight labels and (b) multi-class severity detection with four levels.
- Hypothesis: A diversity-aware transformer ensemble with validation-weighted soft voting improves macro-F1 overall and on minority labels.
- Hypothesis: Token-level explainability (XAI) is faithful and stable as measured by deletion AUC, Overlap@K, and Kendall's τ.

## 2. Data
- **DepressionEmo:** 6,037 Reddit posts with eight emotions; strong class imbalance (cognitive dysfunction and suicidal intent are rare).
  - Distribution: Figure 2a (p.7); statistics: Table 1 (p.7).
- **Merged Depression Severity Detection (MDSD):** 13,804 posts with four severities (Minimal/Mild/Moderate/Severe); Mild is scarce.
  - Distribution: Figure 2b (p.7); statistics: Table 2 (p.9).
- Splits: 80/5/15 for train/validation/test. Outer k-fold with iterative stratification for multi-label to preserve co-occurrence (§3.1–3.2; pp.6–9).

## 3. Preprocessing
- Lowercasing with transformer tokenizers (no punctuation stripping).
- Lemmatization only for classic baselines.
- Placeholders for URLs, users, and numbers; keep emojis (map to descriptors if needed).
- Deduplicate near-duplicates and drop ultra-short posts (§3.2; Fig. 4 p.9).

## 4. Models Compared
- **Baselines:** Logistic Regression, Linear SVM, Random Forest on TF-IDF (1–2 grams); auxiliary averaged embeddings (GloVe/FastText) (§3.4; Table 3 p.11).
- **RNN family:** (Bi)LSTM and (Bi)GRU with hybrid embeddings (GloVe+FastText) (§3.3–3.4; Table 3 p.11).
- **Backbone transformers:** DistilBERT, ALBERT, XLM-RoBERTa, DeBERTa with BiLSTM head for local order cues. Diversity rationale and resource profile: Table 4 (p.14) (§3.5; pp.11–14).

## 5. Ensemble (DepTformer-XAI-SV)
- Validation-weighted soft voting using each backbone’s validation macro-F1 as weight.
- Per-class thresholds for multi-label predictions (grid 0.3–0.7).
- Architecture overview and pseudocode: Fig. 9 and Algorithm 1 (pp.15–16) (§3.6).

## 6. Training Setup
- AdamW optimizer; learning rate in {1–5}×10⁻⁵ (selected 2e-5); batch size 16; up to 10 epochs; dropout 0.3; early stopping on validation macro-F1; max length 256; fp16 mixed precision.
- Hardware: RTX 3090 24GB; PyTorch/Hugging Face Transformers v4.36 (§3.7; Table 5 p.17).

## 7. Evaluation Protocol
- Report macro/micro Precision, Recall, and F1; per-class scores; 95% confidence intervals and paired tests across identical folds; effect sizes (Cohen’s d, Cliff’s Δ).
- Additional metrics: ROC-AUC and PR curves per class (§4; pp.17–18, 28–30).

## 8. Main Results (Accuracy)
- **Emotion (DepressionEmo):** Ensemble achieves macro-F1 ≈ 77.4 and micro-F1 ≈ 81.1; strongest single model is DeBERTa+BiLSTM. Model grid: Table 6 (p.21); per-label wins and minority gains (e.g., +3.1 F1 Cognitive Dysfunction; +2.7 Suicidal Intent): Table 7 (p.21). Visuals: Fig. 12 (pp.19–21).
- **Severity (MDSD):** Ensemble macro-F1 ≈ 79.6 and micro-F1 ≈ 80.6; per-class F1 ≈ 79.7–81.6 with gains for Severe and Mild. Model grid: Table 8 (p.22); per-class: Table 9 (p.22).

## 9. Statistical Significance
- Paired t-tests: ensemble vs. each backbone/baseline yields p < 0.005 on most metrics across both tasks. Summary: Table 11 (p.25) (§6.4).

## 10. Error Analysis & Recovery
- Confusion matrices show hardest emotion pairs are Worthlessness ↔ Hopelessness; hardest severity confusion is among Minimal/Mild/Moderate.
- Recovery analysis: backbone-specific rescues (e.g., XLM-R for slang; DeBERTa+BiLSTM for pragmatic ambiguity and order cues). Matrices: Fig. 14 (p.23); rescue map and fixes: Table 10 and Fig. 15 (pp.24–25).

## 11. Generalization / Transfer
- Train on Emotion and evaluate on DSL: small micro-F1 drop but macro-F1 improves; ensemble is most robust. Trend lines: Fig. 13 (p.22) (§6.3).

## 12. Efficiency & Cost (Compute)
- Per-model inference time, VRAM, power, FLOPs, and energy per 1k inferences at sequence length 256 with fp16.
- ALBERT is the lightest; ensemble has higher cost but best accuracy/robustness—presented as an accuracy–cost Pareto view (Table 12 p.26) (§6.4).

## 13. Ablations & Leave-One-Backbone-Out (LOBO)
- Removing class-weights reduces macro-F1 by 1.1 (Emotion); uniform fusion reduces by 0.8; no oversampling reduces by 0.7; fixed/global thresholds perform worse than per-class thresholds.
- LOBO shows the biggest hit when dropping DeBERTa+BiLSTM, followed by XLM-R. Full vs. ablated results: Table 13; imbalance grid (r = 0.25/0.5/0.75): Table 14; visualized in Fig. 16 (pp.26–27).

## 14. Convergence & Curves
- Stable learning curves; ROC-AUC ~0.80–0.84; PR-AP ~0.80–0.84; minority classes weaker but improved by the ensemble. Learning curves: Fig. 17 (p.29); ROC: Fig. 18 (p.29); PR: Fig. 19 (p.30) (§6.6).

## 15. Explainability Validation
- LIME token attributions evaluated for faithfulness via deletion AUC (higher with K=10) and stability via Overlap@K ≈ 0.61–0.68 and Kendall’s τ ≈ 0.51–0.58; masking perturbation is most stable.
- Qualitative panels: Fig. 20–21 (pp.31–32); metrics: Table 15 (p.32) (§5 & §6.7).

## 16. Deployment Demo
- Flask + TorchServe web app provides real-time predictions with token-level highlights; throughput reported to guide deployment trade-offs (§3.7 & §6.8; pp.16, 31).
