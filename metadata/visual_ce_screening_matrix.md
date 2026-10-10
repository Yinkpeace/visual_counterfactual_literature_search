# Visual Counterfactual Review — Screening Matrix

Status: full-corpus screening complete  
Review type: systematic scoping review with critical technical synthesis  
Search period: 1 June–31 August 2026; publication window: 2017–2026

## Operational scope

A primary study belongs to the core corpus when it operationally constructs, applies, or evaluates counterfactual interventions involving visual or visually grounded data, and the counterfactual operation is central to explaining, interpreting, auditing, evaluating, training, repairing, or mitigating a vision-based model.

The corpus is organized by technical purpose:

1. Post-hoc counterfactual explanation and model interpretation
2. Counterfactual-guided learning and representation improvement
3. Counterfactual auditing and diagnosis
4. Counterfactual evaluation and benchmark construction
5. Counterfactual-guided mitigation and model repair
6. Data construction and controllable editing

These purposes are not mutually exclusive.

## Eligibility gates

| Code | Screening question |
| --- | --- |
| E1 | Does the paper contain an original method, experiment, dataset, or benchmark? |
| E2 | Are images, video, visual states, or visually grounded multimodal representations central to the methodology? |
| E3 | Is a counterfactual intervention, construction, comparison, or paired evaluation operationally implemented? |
| E4 | Is a factual–alternative relationship identifiable? |
| E5 | Is the counterfactual operation central to the contribution rather than incidental terminology? |

## Visual-centrality rule

| Tier | Definition | Eligibility |
| --- | --- | --- |
| V1 | A dedicated visual or visually grounded contribution | Include if E1–E5 are satisfied |
| V2 | A cross-modal or data-agnostic contribution with a substantive visual method, experiment, and visual-specific claim | Include if E1–E5 are satisfied |
| V3 | Images appear only as an illustrative dataset or minor demonstration of a predominantly nonvisual method | Exclude under X2 |

V1 corresponds to visual-primary studies; V2 corresponds to visually substantiated cross-domain studies. Both are eligible. Publication families are consolidated, with the peer-reviewed version retained when available and a preprint retained only when no peer-reviewed version was identified by the review cutoff.

## Exclusion codes

| Code | Exclusion reason |
| --- | --- |
| X1 | No original primary contribution |
| X2 | Visual modality is incidental rather than methodologically central |
| X3 | No operational visual or visually grounded counterfactual |
| X4 | Counterfactual terminology is rhetorical, purely textual, or unrelated to the visual method |
| X5 | Secondary literature: survey, review, tutorial, perspective, or general overview |
| X6 | Duplicate or superseded publication version |
| X7 | Insufficient Markdown evidence to determine substantive eligibility |

Secondary literature may support background, terminology, citation searching, and comparison with previous reviews, but it is excluded from the primary-study count and empirical synthesis.

## Markdown evidence grades

| Grade | Definition | Permitted use |
| --- | --- | --- |
| A | Relevant prose, methods, metrics, and tables are legible | Qualitative and exact quantitative extraction |
| B | Main method and findings are recoverable, but formatting, equations, or tables are degraded | Qualitative synthesis; exact values only when clearly recoverable |
| C | Abstract-level or severely incomplete evidence | Scope and method-existence claims only |
| D | No usable Markdown | No substantive synthesis |

The final paper supplies the review-level synthesis and inclusion decisions. Primary-study evidence grades describe the underlying extraction records, not the strength of every claim in the review. Exact primary-study numerical claims require directly recoverable primary evidence.

## Pilot screening

| ID | Study | Decision | Technical purpose | Counterfactual object | Evidence |
| --- | --- | --- | --- | --- | --- |
| P01 | Goyal et al. (2019), *Counterfactual Visual Explanations* | Include | Post-hoc explanation | Query–distractor region substitution | B |
| P02 | Wang and Vasconcelos (2020), *SCOUT* | Include | Post-hoc interpretation | Discriminant counterfactual heatmap | B |
| P03 | Augustin et al. (2022), *Diffusion Visual Counterfactual Explanations* | Include | Post-hoc explanation | Diffusion-generated counterfactual image | B |
| P04 | Singla et al. (2023b), *Augmentation by Counterfactual Explanation* | Include | Learning and model improvement | Counterfactual image paths used for fine-tuning | B |
| P05 | Shvetsov et al. (2024), *COIN* | Include | Learning and weak supervision | Abnormal-to-normal inpainting and residual mask | B |
| P06 | Cai et al. (2024), *CCIS-MVQA* | Include | Interpretation and learning | Masked image intervention and causal-effect comparison | B |
| P07 | Jiang et al. (2026), *CHARTOGRAPHER* | Include | Evaluation and benchmarking | Executable data intervention and rerendered chart | B |
| P08 | Liang et al. (2026), *Envision, Attend, Then Respond* | Include | Mitigation | Diffusion-derived counterpart used for attention contrast | B |
| P09 | Li et al. (2023), *Multimodal Counterfactual Learning Network* | Include | Representation learning | Interacted/uninteracted multimodal representation intervention | B |
| P10 | Nori et al. (2023), *Capabilities of GPT-4 on Medical Challenge Problems* | Exclude: X2, X3, X4 | Contextual medical evaluation | Textual hypothetical medical scenarios | A |

## Full-corpus screening

The table contains 95 included studies and retains five previously excluded or superseded records under X-prefixed IDs. A “Yes” in E2 includes both V1 and V2 visual centrality.

| ID | Study | E1 | E2 | E3 | E4 | E5 | Decision | Purpose | Counterfactual object | Visual tier | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V01 | Goyal et al. (2019), *Counterfactual Visual Explanations* | Yes | Yes | Yes | Yes | Yes | Include | Explanation | Query–distractor region substitution | V1 | B |
| V02 | Atrey et al. (2020), *Exploratory Not Explanatory* | Yes | Yes | Yes | Yes | Yes | Include | Auditing | Interventions testing saliency hypotheses in Atari states | V1 | B |
| V03 | Nemirovsky et al. (2020), *CounteRGAN* | Yes | Yes | Yes | Yes | Yes | Include | Explanation/recourse | Residual-GAN counterfactual instance | V2 | B |
| V04 | Zhao et al. (2020), *Generating Natural Counterfactual Visual Explanations* | Yes | Yes | Yes | Yes | Yes | Include | Explanation | Attribute-conditioned generated image | V1 | B |
| V05 | Wang and Vasconcelos (2020), *SCOUT* | Yes | Yes | Yes | Yes | Yes | Include | Interpretation | Counter-class discriminant heatmap | V1 | B |
| V06 | Rodríguez et al. (2021), *DiVE* | Yes | Yes | Yes | Yes | Yes | Include | Explanation/auditing | Diverse latent-space image edits | V1 | B |
| V07 | Olson et al. (2021), *Counterfactual State Explanations* | Yes | Yes | Yes | Yes | Yes | Include | Explanation | Generated Atari state changing agent action | V1 | B |
| V08 | Guidotti and Ruggieri (2021), *Ensemble of Counterfactual Explainers* | Yes | Yes | Yes | Yes | Yes | Include | Explanation | Ensemble-selected counterfactual instances | V2 | B |
| V09 | Van Looveren and Klaise (2021), *Prototype-Guided Counterfactuals* | Yes | Yes | Yes | Yes | Yes | Include | Explanation | Prototype-guided input optimization | V2 | B |
| V10 | Kenny and Keane (2021), *PIECE* | Yes | Yes | Yes | Yes | Yes | Include | Explanation | Exceptional-feature replacement in latent representation | V1 | B |
| V11 | Montenegro et al. (2021), *Privacy-Preserving GAN for Case-Based Explainability* | Yes | Yes | Yes | Yes | Yes | Include | Explanation/mitigation | Privatized factual and counterfactual case images | V1 | B |
| V12 | Augustin et al. (2022), *Diffusion Visual Counterfactual Explanations* | Yes | Yes | Yes | Yes | Yes | Include | Explanation | Classifier-guided diffusion image | V1 | B |
| V13 | Pombo et al. (2023), *CounterSynth* | Yes | Yes | Yes | Yes | Yes | Include | Learning/fairness | Morphologically constrained counterfactual brain image | V1 | B |
| V14 | Singla et al. (2023a), *Explaining the Black-Box Smoothly* | Yes | Yes | Yes | Yes | Yes | Include | Explanation | Smooth path of generated images to a target prediction | V1 | B |
| X01 | Del Ser et al. (2022), *Exploring the Trade-off Between Plausibility and Intensity* | Yes | Yes | Yes | Yes | Yes | Exclude: X6 | Superseded record | Multiobjective generated counterfactual | V1 | C |
| V15 | Mertes et al. (2022), *GANterfactual* | Yes | Yes | Yes | Yes | Yes | Include | Explanation | Class-conditioned visual translation | V1 | B |
| V16 | Chen et al. (2023), *Sim2Word* | Yes | Yes | Yes | Yes | Yes | Include | Interpretation | Counterfactual attribute-word intervention | V1 | B |
| V17 | Singla et al. (2023b), *Augmentation by Counterfactual Explanation* | Yes | Yes | Yes | Yes | Yes | Include | Learning/model improvement | Counterfactual image paths used in training | V1 | B |
| X02 | Nori et al. (2023), *Capabilities of GPT-4 on Medical Challenge Problems* | Yes | No | No | Partial | No | Exclude: X2, X3, X4 | Contextual evaluation | Textual hypothetical scenarios | V3 | A |
| V18 | Dang et al. (2023), *Counterfactual Generation Framework for Few-Shot Learning* | Yes | Yes | Yes | Yes | Yes | Include | Learning | Causal recombination of class-agnostic and sample-specific visual factors | V1 | B |
| V19 | Law et al. (2023), *Plausible Counterfactuals for Urban Analytics* | Yes | Yes | Yes | Yes | Yes | Include | Explanation | Latent edits to holistic street imagery | V1 | B |
| X03 | Alfeo et al. (2023), *From Local Counterfactuals to Global Feature Importance* | Yes | No | Yes | Yes | Yes | Exclude: X2 | Interpretation | Feature-vector boundary crossings in fMRI connectivity signals | V3 | B |
| V20 | Huber et al. (2023), *GANterfactual-RL* | Yes | Yes | Yes | Yes | Yes | Include | Explanation | Domain-translated visual RL state | V1 | B |
| X04 | Chen et al. (2023), *EXGAN* | Yes | No | Yes | Yes | Yes | Exclude: X2 | Learning/explanation | General counterfactual instance | V3 | B |
| V21 | Li et al. (2023), *Multimodal Counterfactual Learning Network* | Yes | Yes | Yes | Yes | Yes | Include | Representation learning | Interacted/uninteracted visual-textual representations | V1 | B |
| V22 | Zemni et al. (2023), *OCTET* | Yes | Yes | Yes | Yes | Yes | Include | Explanation | Object-centric scene edits | V1 | B |
| V23 | Del Ser et al. (2024), *On Generating Trustworthy Counterfactual Explanations* | Yes | Yes | Yes | Yes | Yes | Include | Explanation/auditing | Multiobjective generated image or 3-D alternative | V1 | B |
| V24 | Samadi et al. (2023), *SAFE* | Yes | Yes | Yes | Yes | Yes | Include | Explanation/safety | Saliency-guided driving-scene perturbation | V1 | B |
| V25 | Bi et al. (2024), *Self-Supervised Knowledge Distillation in Counterfactual Learning for VQA* | Yes | Yes | Yes | Yes | Yes | Include | Learning | Counterfactual visual-question pairs and distilled representations | V1 | B |
| V26 | Montenegro et al. (2024), *Anonymizing Medical Case-Based Explanations Through Disentanglement* | Yes | Yes | Yes | Yes | Yes | Include | Mitigation/explanation | Identity-disentangled counterfactual case image | V1 | C |
| V27 | Ji et al. (2024), *AR-Pro* | Yes | Yes | Yes | Yes | Yes | Include | Repair | Counterfactual repair of anomalous visual/time-series input | V2 | B |
| V28 | Shvetsov et al. (2024), *COIN* | Yes | Yes | Yes | Yes | Yes | Include | Learning/weak supervision | Normalized inpainting and residual anomaly mask | V1 | B |
| V29 | Cai et al. (2024), *CCIS-MVQA* | Yes | Yes | Yes | Yes | Yes | Include | Interpretation/learning | Masked medical-image intervention | V1 | B |
| V30 | Atad et al. (2024), *Counterfactual Explanations for Medical Image Classification and Regression* | Yes | Yes | Yes | Yes | Yes | Include | Explanation | Diffusion-autoencoder image trajectory | V1 | B |
| V31 | Khan et al. (2024), *FCVE* | Yes | Yes | Yes | Yes | Yes | Include | Explanation | Faithfulness-constrained visual counterfactual | V1 | B |
| V32 | Guo et al. (2024), *MiMICRI* | Yes | Yes | Yes | Yes | Yes | Include | Explanation | Domain-constrained cardiovascular image edits | V1 | B |
| V33 | Li et al. (2024), *Relevance Inference Based on Direct Contribution* | Yes | Yes | Yes | Yes | Yes | Include | Interpretation | Input contribution removal and counterfactual result | V1 | B |
| X05 | Liguori et al. (2024), *Robust Anomaly Detection via Adversarial Counterfactual Generation* | Yes | No | Yes | Yes | Yes | Exclude: X2 | Learning/robustness | General adversarial counterfactual instance | V3 | B |
| V34 | Samadi et al. (2024), *SAFE-RL* | Yes | Yes | Yes | Yes | Yes | Include | Explanation/safety | Saliency-aware visual state intervention | V1 | B |
| V35 | Jeanneret et al. (2024), *TIME* | Yes | Yes | Yes | Yes | Yes | Include | Explanation | Text-guided diffusion edit queried against a black box | V1 | B |
| V36 | Valoor et al. (2025), *Alzheimer’s Diagnosis Case-Based Counterfactual Methodology* | Yes | Yes | Yes | Yes | Yes | Include | Explanation | GAN-generated diagnostic counterfactual maps | V1 | B |
| V37 | Lang et al. (2024), *Using Generative AI to Investigate Medical Imagery, Models and Datasets* | Yes | Yes | Yes | Yes | Yes | Include | Auditing/diagnosis | Independent latent-attribute edits generating counterfactual images | V1 | B |
| V38 | Rotem et al. (2024), *DISCOVER* | Yes | Yes | Yes | Yes | Yes | Include | Interpretation | Disentangled exaggerated visual counterfactuals | V1 | B |
| V39 | Ha and Bender (2025), *Diffusion Counterfactuals for Image Regressors* | Yes | Yes | Yes | Yes | Yes | Include | Explanation | Target-value-conditioned diffusion image | V1 | B |
| V40 | Chen et al. (2026), *Distilling Counterfactual Reasoning from Language to Vision* | Yes | Yes | Yes | Yes | Yes | Include | Learning/evaluation | Counterfactual video questions, interventions, and distilled reasoning | V1 | B |
| V41 | Xu et al. (2025), *Generating Image Counterfactuals Without Generative Models* | Yes | Yes | Yes | Yes | Yes | Include | Explanation | Direct model-guided image perturbation | V1 | B |
| V42 | Lymperaiou et al. (2025), *HalCECE* | Yes | Yes | Yes | Yes | Yes | Include | Auditing/diagnosis | Conceptual counterfactual interventions for hallucination | V1 | B |
| V43 | Cao et al. (2026), *LeapFactual* | Yes | Yes | Yes | Yes | Yes | Include | Explanation | Conditional-flow visual counterfactual | V1 | B |
| V44 | Sun et al. (2025), *Semantic Shapley-Based Counterfactual Explanations* | Yes | Yes | Yes | Yes | Yes | Include | Explanation/safety | Semantically selected driving-scene interventions | V1 | B |
| V45 | Tian et al. (2026), *C-CoT* | Yes | Yes | Yes | Yes | Yes | Include | Learning/planning | Alternative actions and consequences grounded in visual scenes | V1 | B |
| V46 | Jiang et al. (2026), *CHARTOGRAPHER* | Yes | Yes | Yes | Yes | Yes | Include | Evaluation/benchmarking | Executable chart-data edit and rerendered chart | V1 | B |
| V47 | Liang et al. (2026), *Envision, Attend, Then Respond* | Yes | Yes | Yes | Yes | Yes | Include | Mitigation | Generated visual counterpart used for attention contrast | V1 | B |
| V48 | Guo et al. (2026), *MaskDiME* | Yes | Yes | Yes | Yes | Yes | Include | Explanation | Adaptively masked diffusion counterfactual | V1 | B |
| V49 | Sar et al. (2026), *VLM Reality Check* | Yes | Yes | Yes | Yes | Yes | Include | Evaluation/benchmarking | Minimal-edit causal image variants | V1 | B |
| V50 | Khorram and Fuxin (2022), C3LT | Yes | Yes | Yes | Yes | Yes | Include | E | Cycle-consistent latent transformations | V1 | B |
| V51 | Jeanneret et al. (2022), DiME | Yes | Yes | Yes | Yes | Yes | Include | E | Target-gradient diffusion | V1 | B |
| V52 | Jeanneret et al. (2023), ACE | Yes | Yes | Yes | Yes | Yes | Include | E | Diffusion-filtered adversarial search and inpainting refinement | V1 | B |
| V53 | Augustin et al. (2024), DiG-IN | Yes | Yes | Yes | Yes | Yes | Include | E/A | Guided diffusion for classifier disagreement, systematic errors, and neuron analysis | V1 | B |
| V54 | Weng et al. (2024), FastDiME | Yes | Yes | Yes | Yes | Yes | Include | E/A/M | Self-optimized masking for shortcut insertion and removal | V1 | B |
| V55 | Sobieski and Biecek (2024), Global Counterfactual Directions | Yes | Yes | Yes | Yes | Yes | Include | E/A | Dataset-level latent directions that alter classifier decisions | V1 | B |
| V56 | Haselhoff et al. (2024), GdVAE | Yes | Yes | Yes | Yes | Yes | Include | E | Class-structured generative model with closed-form latent counterfactual construction | V1 | B |
| V57 | Mertes et al. (2024), Relevant Irrelevance | Yes | Yes | Yes | Yes | Yes | Include | E | Alterfactual image contrasts | V1 | B |
| V58 | Zhang et al. (2025b), Fine-Grained Saliency Counterfactuals | Yes | Yes | Yes | Yes | Yes | Include | E | Saliency partition of object and part evidence associated with misclassification | V1 | B |
| V59 | Chowdhury et al. (2025), Mirror-CFE | Yes | Yes | Yes | Yes | Yes | Include | E | Classifier-feature-space trajectories for faithful visual explanations | V1 | B |
| V60 | Zaher et al. (2026), Perceptual Counterfactual Geodesics | Yes | Yes | Yes | Yes | Yes | Include | E | Paths induced by robust visual-feature geometry | V1 | B |
| V61 | Li et al. (2024c), CFI-VAE | Yes | Yes | Yes | Yes | Yes | Include | L | Counterfactual interventions regularize causal visual representations | V1 | B |
| V62 | Lin et al. (2024), CI-MIL | Yes | Yes | Yes | Yes | Yes | Include | L | Counterfactual inference supplies instance pseudo-labels for whole-slide multiple-instance learning | V1 | B |
| V63 | Singh et al. (2024), DUB | Yes | Yes | Yes | Yes | Yes | Include | L | Visually similar but acoustically different cross-modal pairs for audiovisual representation learning | V1 | B |
| V64 | Li et al. (2024b), CoFE | Yes | Yes | Yes | Yes | Yes | Include | L | Patch-swapped factual-counterfactual contrasts for radiology report generation | V1 | B |
| V65 | Lai et al. (2024), COMO | Yes | Yes | Yes | Yes | Yes | Include | L | Multimodal counterfactual hard negatives for concept composition | V1 | B |
| V66 | Venkatesh et al. (2024), Counterfactual World Modeling | Yes | Yes | Yes | Yes | Yes | Include | L | Controlled physical-dynamics alternatives for learned world representations | V1 | B |
| V67 | Yin et al. (2025), KCDP | Yes | Yes | Yes | Yes | Yes | Include | L | Knowledge-aligned counterfactual-enhancement diffusion for cross-domain visual emotion recognition | V1 | B |
| V68 | Jia et al. (2025), GCS | Yes | Yes | Yes | Yes | Yes | Include | L/E | Generated counterfactual sets for CLIP compositionality and learning | V1 | B |
| V69 | Zha et al. (2025), ICF | Yes | Yes | Yes | Yes | Yes | Include | L | Implicit counterfactual learning for audio-visual segmentation | V1 | B |
| V70 | Kung et al. (2025), State-Change Counterfactuals | Yes | Yes | Yes | Yes | Yes | Include | L | Counterfactual failure outcomes supervise procedure-aware video encoders | V1 | B |
| V71 | Shrivastava et al. (2026), Point Prompting | Yes | Yes | Yes | Yes | Yes | Include | L | Point-prompted counterfactual video generation for motion tracking | V1 | B |
| V72 | Yu and Li (2024), Counterfactual Referring Expression Comprehension | Yes | Yes | Yes | Yes | Yes | Include | A/L | Fine-grained referring-expression mismatches and visually grounded task supervision | V1 | B |
| V73 | Zhang et al. (2024b), C-VQA | Yes | Yes | Yes | Yes | Yes | Include | A/B | Direct and indirect hypothetical premises over real and synthetic scenes | V1 | B |
| V74 | Howard et al. (2024), SocialCounterfactuals | Yes | Yes | Yes | Yes | Yes | Include | A/M | Intersectional social-attribute variants for vision-language bias probing and mitigation | V1 | B |
| V75 | Zhang et al. (2024a), CoCT | Yes | Yes | Yes | Yes | Yes | Include | A/L | Chains of counterfactual thought for bias-robust vision-language reasoning | V1 | B |
| V76 | Shen et al. (2025), Abductive Counterfactual IQA | Yes | Yes | Yes | Yes | Yes | Include | A | Abductive inference of perceptual effects and deep-feature distortion relationships | V1 | B |
| V77 | Zhu et al. (2024), TFCD | Yes | Yes | Yes | Yes | Yes | Include | M | Training-free counterfactual debiasing for multimodal sarcasm detection | V1 | B |
| V78 | Zong et al. (2025a), CF-PACR | Yes | Yes | Yes | Yes | Yes | Include | M/L | Counterfactual debiasing for physical audiovisual commonsense reasoning | V1 | B |
| V79 | Zong et al. (2025b), Text-Guided Fine-Grained Counterfactual Inference | Yes | Yes | Yes | Yes | Yes | Include | M/L | Text-guided counterfactual inference for short-video fake-news detection | V1 | B |
| V80 | Wu et al. (2025), Antidote | Yes | Yes | Yes | Yes | Yes | Include | M | Post-training mitigation of counterfactual-presupposition and object-perception hallucinations | V1 | B |
| V81 | Zhang et al. (2025a), CREStE | Yes | Yes | Yes | Yes | Yes | Include | M/L | Counterfactual trajectory guidance and human queries for mapless navigation learning | V1 | B |
| V82 | Song et al. (2024), DAC | Yes | Yes | Yes | Yes | Yes | Include | D | Doubly abductive counterfactual inference for text-based image editing | V1 | B |
| V83 | Winter et al. (2024), ObjectDrop | Yes | Yes | Yes | Yes | Yes | Include | D | Paired counterfactual captures teach wider scene effects of object insertion and removal | V1 | B |
| V84 | Huang et al. (2025), T-FIT | Yes | Yes | Yes | Yes | Yes | Include | D | Compositional concept learning and counterfactual abduction for fashion editing | V1 | B |
| V85 | Wang et al. (2025), OmniDrive | Yes | Yes | Yes | Yes | Yes | Include | B | Candidate ego trajectories evaluated against structured 3-D constraints | V1 | B |
| V86 | Ness et al. (2026), Multiverse Mechanica | Yes | Yes | Yes | Yes | Yes | Include | B | Aligned counterfactual worlds rendered from known game-engine graphs | V1 | B |
| V87 | Lang et al. (2021), StylEx | Yes | Yes | Yes | Yes | Yes | Include | E/A | Classifier-specific StyleSpace attributes and generated visual contrasts | V1 | B |
| V88 | Singla et al. (2019), Progressive Exaggeration | Yes | Yes | Yes | Yes | Yes | Include | E | Probability-conditioned image sequences spanning classifier confidence | V1 | B |
| V89 | Denton et al. (2019), Image Counterfactual Sensitivity Analysis | Yes | Yes | Yes | Yes | Yes | Include | A | Generated face-attribute interventions | V1 | B |
| V90 | Balakrishnan et al. (2021), Causal Benchmarking of Face-Analysis Bias | Yes | Yes | Yes | Yes | Yes | Include | A/B | Human-validated synthetic attribute transects | V1 | B |
| V91 | Dash et al. (2022), ImageCFGen | Yes | Yes | Yes | Yes | Yes | Include | A/M | SCM-constrained generation with counterfactual regularization | V1 | B |
| V92 | Rott Shaham et al. (2024), MAIA | Yes | Yes | Yes | Yes | Yes | Include | A | Multimodal agent constructs and tests interpretability hypotheses | V1 | B |
| V93 | Spanos et al. (2026), V-CECE | Yes | Yes | Yes | Yes | Yes | Include | E | Visual counterfactual explanations through conceptual edits | V1 | B |
| V94 | Vaeth et al. (2025), XAIDIFF | Yes | Yes | Yes | Yes | Yes | Include | E | Generative example-based explanations with probabilistic trade-offs | V1 | B |
| V95 | Monteiro et al. (2023), Axiomatic Soundness of Counterfactual Image Models | Yes | Yes | Yes | Yes | Yes | Include | B | Null interventions, round-trip restoration, and requested-parent interventions | V1 | B |

## Final-paper screening and corpus construction

- Search period: **1 June–31 August 2026**, covering publications from **2017–2026**.
- Sources: **OpenAlex, Web of Science, ScienceDirect, and IEEE Xplore**, supplemented by targeted searches of top AI, computer-vision, and machine-learning conferences.
- Search strategy: eight predefined queries plus counterfactual and visual terminology combined with role-specific search blocks.
- Deduplication: DOI, followed by title, author, and publication year; ambiguous matches checked manually.
- Unique records entering eligibility screening: **273**.
- Final included studies: **95** — **71 conference proceedings**, **21 journal articles**, and **3 preprints**.

Eligibility required all five criteria E1–E5. Related preprints were grouped with published versions. Automated screening was piloted on twenty varied studies, and retained or ambiguous candidates were verified manually.
