# Visual Counterfactual Review — Screening Matrix

Status: full-corpus screening complete  
Review type: systematic scoping review with critical technical synthesis  
Manuscript format: generic anonymous LaTeX article, to be created after evidence extraction  
Corpus cutoff: 29 July 2026, subject to a final update search before submission

## Working scope

A primary study belongs to the core corpus when it operationally constructs, applies, or evaluates counterfactual interventions involving visual or visually grounded data, and the counterfactual operation is central to explaining, interpreting, auditing, evaluating, training, repairing, or mitigating a vision-based model.

The corpus is organized by technical purpose:

1. Post-hoc counterfactual explanation and model interpretation
2. Counterfactual-guided learning and representation improvement
3. Counterfactual auditing and diagnosis
4. Counterfactual evaluation and benchmark construction
5. Counterfactual-guided mitigation and model repair

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

The V1/V2 distinction will be retained in synthesis so that broadly applicable methods do not become indistinguishable from methods designed around visual structure.

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

Existing synthesized reviews are navigation aids. Final evidential claims must be traced to primary-study Markdown.

## Pilot screening

| ID | Study | Decision | Technical purpose | Counterfactual object | Evidence |
| --- | --- | --- | --- | --- | --- |
| P01 | Goyal et al. (2019), *Counterfactual Visual Explanations* | Include | Post-hoc explanation | Query–distractor region substitution | B |
| P02 | Wang and Vasconcelos (2020), *SCOUT* | Include | Post-hoc interpretation | Discriminant counterfactual heatmap | B |
| P03 | Augustin et al. (2022), *Diffusion Visual Counterfactual Explanations* | Include | Post-hoc explanation | Diffusion-generated counterfactual image | B |
| P04 | Singla et al. (2023), *Augmentation by Counterfactual Explanation* | Include | Learning and model improvement | Counterfactual image paths used for fine-tuning | B |
| P05 | Shvetsov et al. (2024), *COIN* | Include | Learning and weak supervision | Abnormal-to-normal inpainting and residual mask | B |
| P06 | Cai et al. (2024), *CCIS-MVQA* | Include | Interpretation and learning | Masked image intervention and causal-effect comparison | B |
| P07 | Jiang et al. (2026), *CHARTOGRAPHER* | Include | Evaluation and benchmarking | Executable data intervention and rerendered chart | B |
| P08 | Liang et al. (2026), *Envision, Attend, Then Respond* | Include | Mitigation | Diffusion-derived counterpart used for attention contrast | B |
| P09 | Li et al. (2023), *Multimodal Counterfactual Learning Network* | Include | Representation learning | Interacted/uninteracted multimodal representation intervention | B |
| P10 | Nori et al. (2023), *Capabilities of GPT-4 on Medical Challenge Problems* | Exclude: X2, X3, X4 | Contextual medical evaluation | Textual hypothetical medical scenarios | A |

## Full-corpus screening

The 54 candidate records in `visual_counterfactual_explanations_literature.md` were screened. A “Yes” in E2 includes both V1 and V2 visual centrality.

| ID | Study | E1 | E2 | E3 | E4 | E5 | Decision | Purpose | Counterfactual object | Visual tier | Evidence | Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V01 | Goyal et al. (2019), *Counterfactual Visual Explanations* | Yes | Yes | Yes | Yes | Yes | Include | Explanation | Query–distractor region substitution | V1 | B | Direct visual contrast for a specified alternative class. |
| V02 | Atrey et al. (2019), *Exploratory Not Explanatory* | Yes | Yes | Yes | Yes | Yes | Include | Auditing | Interventions testing saliency hypotheses in Atari states | V1 | B | Operational visual counterfactual tests audit saliency semantics. |
| V03 | Nemirovsky et al. (2020), *CounteRGAN* | Yes | Yes | Yes | Yes | Yes | Include | Explanation/recourse | Residual-GAN counterfactual instance | V2 | B | General method, but image generation and MNIST form a substantive validation regime. |
| V04 | Zhao et al. (2020), *Generating Natural Counterfactual Visual Explanations* | Yes | Yes | Yes | Yes | Yes | Include | Explanation | Attribute-conditioned generated image | V1 | B | Visual attribute intervention produces target-class alternatives. |
| V05 | Wang and Vasconcelos (2020), *SCOUT* | Yes | Yes | Yes | Yes | Yes | Include | Interpretation | Counter-class discriminant heatmap | V1 | B | Explicitly contrastive visual localization. |
| V06 | Rodríguez et al. (2021), *DiVE* | Yes | Yes | Yes | Yes | Yes | Include | Explanation/auditing | Diverse latent-space image edits | V1 | B | Uses diverse nontrivial changes to expose decision factors and biases. |
| V07 | Olson et al. (2021), *Counterfactual State Explanations* | Yes | Yes | Yes | Yes | Yes | Include | Explanation | Generated Atari state changing agent action | V1 | B | Visual state alternatives explain RL actions. |
| V08 | Guidotti and Ruggieri (2021), *Ensemble of Counterfactual Explainers* | Yes | Yes | Yes | Yes | Yes | Include | Explanation | Ensemble-selected counterfactual instances | V2 | B | Data-agnostic method with dedicated evaluation on two image datasets. |
| V09 | Van Looveren and Klaise (2021), *Prototype-Guided Counterfactuals* | Yes | Yes | Yes | Yes | Yes | Include | Explanation | Prototype-guided input optimization | V2 | B | General method includes a substantive image-specific MNIST study. |
| V10 | Kenny and Keane (2021), *PIECE* | Yes | Yes | Yes | Yes | Yes | Include | Explanation | Exceptional-feature replacement in latent representation | V1 | B | Designed for plausible visual counterfactuals and semi-factuals. |
| V11 | Montenegro et al. (2021), *Privacy-Preserving GAN for Case-Based Explainability* | Yes | Yes | Yes | Yes | Yes | Include | Explanation/mitigation | Privatized factual and counterfactual case images | V1 | B | Counterfactual case-based explanation is an explicit module and evaluated artifact. |
| V12 | Augustin et al. (2022), *Diffusion Visual Counterfactual Explanations* | Yes | Yes | Yes | Yes | Yes | Include | Explanation | Classifier-guided diffusion image | V1 | B | Dedicated visual counterfactual generator. |
| V13 | Pombo et al. (2022), *CounterSynth* | Yes | Yes | Yes | Yes | Yes | Include | Learning/fairness | Morphologically constrained counterfactual brain image | V1 | B | Counterfactual image synthesis supports equitable model training. |
| V14 | Singla et al. (2022), *Explaining the Black-Box Smoothly* | Yes | Yes | Yes | Yes | Yes | Include | Explanation | Smooth path of generated images to a target prediction | V1 | B | Visual counterfactual path is the explanatory object. |
| V15 | Del Ser et al. (2022), *Exploring the Trade-off Between Plausibility and Intensity* | Yes | Yes | Yes | Yes | Yes | Exclude: X6 | Superseded record | Multiobjective generated counterfactual | V1 | C | Earlier version of V27; counted with the later journal publication family. |
| V16 | Mertes et al. (2022), *GANterfactual* | Yes | Yes | Yes | Yes | Yes | Include | Explanation | Class-conditioned visual translation | V1 | B | Generates visual alternatives for medical non-expert explanation. |
| V17 | Chen et al. (2022), *Sim2Word* | Yes | Yes | Yes | Yes | Yes | Include | Interpretation | Counterfactual attribute-word intervention | V1 | B | Explains visual similarity through counterfactual semantic attributes. |
| V18 | Singla et al. (2023), *Augmentation by Counterfactual Explanation* | Yes | Yes | Yes | Yes | Yes | Include | Learning/model improvement | Counterfactual image paths used in training | V1 | B | Counterfactuals are central training instruments. |
| V19 | Nori et al. (2023), *Capabilities of GPT-4 on Medical Challenge Problems* | Yes | No | No | Partial | No | Exclude: X2, X3, X4 | Contextual evaluation | Textual hypothetical scenarios | V3 | A | Visual questions are a minor subset and counterfactuals are textual case variations. |
| V20 | Dang et al. (2023), *Counterfactual Generation Framework for Few-Shot Learning* | Yes | Yes | Yes | Yes | Yes | Include | Learning | Causal recombination of class-agnostic and sample-specific visual factors | V1 | B | Operational image counterfactual generation is central to few-shot learning. |
| V21 | Law et al. (2023), *Plausible Counterfactuals for Urban Analytics* | Yes | Yes | Yes | Yes | Yes | Include | Explanation | Latent edits to holistic street imagery | V1 | B | Dedicated classifier/regressor explanation for street-view images. |
| V22 | Alfeo et al. (2023), *From Local Counterfactuals to Global Feature Importance* | Yes | No | Yes | Yes | Yes | Exclude: X2 | Interpretation | Feature-vector boundary crossings in fMRI connectivity signals | V3 | B | Brain connectivity features are treated as signals/vectors, not visual inputs or visual counterfactual artifacts. |
| V23 | Huber et al. (2023), *GANterfactual-RL* | Yes | Yes | Yes | Yes | Yes | Include | Explanation | Domain-translated visual RL state | V1 | B | Visual state alternatives explain learned RL strategies. |
| V24 | Chen et al. (2023), *EXGAN* | Yes | No | Yes | Yes | Yes | Exclude: X2 | Learning/explanation | General counterfactual instance | V3 | B | Predominantly nonvisual class-imbalance method; image data are illustrative rather than structurally central. |
| V25 | Li et al. (2023), *Multimodal Counterfactual Learning Network* | Yes | Yes | Yes | Yes | Yes | Include | Representation learning | Interacted/uninteracted visual-textual representations | V1 | B | Visually grounded multimodal counterfactual inference is central. |
| V26 | Zemni et al. (2023), *OCTET* | Yes | Yes | Yes | Yes | Yes | Include | Explanation | Object-centric scene edits | V1 | B | Dedicated object-aware counterfactuals for complex scenes and segmentation. |
| V27 | Del Ser et al. (2023), *On Generating Trustworthy Counterfactual Explanations* | Yes | Yes | Yes | Yes | Yes | Include | Explanation/auditing | Multiobjective generated image or 3-D alternative | V1 | B | Final publication balancing validity, plausibility, and change intensity. |
| V28 | Samadi et al. (2023), *SAFE* | Yes | Yes | Yes | Yes | Yes | Include | Explanation/safety | Saliency-guided driving-scene perturbation | V1 | B | Dedicated visual counterfactual explanation for automated-driving decisions. |
| V29 | Bi et al. (2024), *Self-Supervised Knowledge Distillation in Counterfactual Learning for VQA* | Yes | Yes | Yes | Yes | Yes | Include | Learning | Counterfactual visual-question pairs and distilled representations | V1 | B | Counterfactual learning is integral to visual-question answering. |
| V30 | Montenegro et al. (2024), *Anonymizing Medical Case-Based Explanations Through Disentanglement* | Yes | Yes | Yes | Yes | Yes | Include | Mitigation/explanation | Identity-disentangled counterfactual case image | V1 | C | Abstract-level Markdown supports eligibility; substantive claims require retrieval of fuller Markdown. |
| V31 | Ji et al. (2024), *AR-Pro* | Yes | Yes | Yes | Yes | Yes | Include | Repair | Counterfactual repair of anomalous visual/time-series input | V2 | B | Cross-modal method includes substantive industrial visual anomaly repair. |
| V32 | Shvetsov et al. (2024), *COIN* | Yes | Yes | Yes | Yes | Yes | Include | Learning/weak supervision | Normalized inpainting and residual anomaly mask | V1 | B | Counterfactual image synthesis generates weak segmentation supervision. |
| V33 | Cai et al. (2024), *CCIS-MVQA* | Yes | Yes | Yes | Yes | Yes | Include | Interpretation/learning | Masked medical-image intervention | V1 | B | Visual causal-effect intervention supports explanation and bias reduction. |
| V34 | Atad et al. (2024), *Counterfactual Explanations for Medical Image Classification and Regression* | Yes | Yes | Yes | Yes | Yes | Include | Explanation | Diffusion-autoencoder image trajectory | V1 | B | Dedicated medical-image counterfactuals for classification and regression. |
| V35 | Khan et al. (2024), *FCVE* | Yes | Yes | Yes | Yes | Yes | Include | Explanation | Faithfulness-constrained visual counterfactual | V1 | B | Dedicated method targets predictive faithfulness of visual explanations. |
| V36 | Guo et al. (2024), *MiMICRI* | Yes | Yes | Yes | Yes | Yes | Include | Explanation | Domain-constrained cardiovascular image edits | V1 | B | Medical domain knowledge constrains visual alternatives. |
| V37 | Li et al. (2024), *Relevance Inference Based on Direct Contribution* | Yes | Yes | Yes | Yes | Yes | Include | Interpretation | Input contribution removal and counterfactual result | V1 | B | Operational pixel/region counterfactuals explain deep visual networks. |
| V38 | Liguori et al. (2024), *Robust Anomaly Detection via Adversarial Counterfactual Generation* | Yes | No | Yes | Yes | Yes | Exclude: X2 | Learning/robustness | General adversarial counterfactual instance | V3 | B | Predominantly general anomaly-detection training; the image benchmark is incidental. |
| V39 | Samadi et al. (2024), *SAFE-RL* | Yes | Yes | Yes | Yes | Yes | Include | Explanation/safety | Saliency-aware visual state intervention | V1 | B | Counterfactual visual states explain deep RL policies. |
| V40 | Jeanneret et al. (2024), *TIME* | Yes | Yes | Yes | Yes | Yes | Include | Explanation | Text-guided diffusion edit queried against a black box | V1 | B | Dedicated black-box visual counterfactual generation. |
| V41 | Valoor et al. (2024), *Alzheimer’s Diagnosis Case-Based Counterfactual Methodology* | Yes | Yes | Yes | Yes | Yes | Include | Explanation | GAN-generated diagnostic counterfactual maps | V1 | B | Visual counterfactual maps explain medical-image classification. |
| V42 | Lang et al. (2024), *Using Generative AI to Investigate Medical Imagery, Models and Datasets* | Yes | Yes | Yes | Yes | Yes | Include | Auditing/diagnosis | Independent latent-attribute edits generating counterfactual images | V1 | B | Counterfactual images support expert hypothesis generation about model and dataset signals. |
| V43 | Rotem et al. (2024), *DISCOVER* | Yes | Yes | Yes | Yes | Yes | Include | Interpretation | Disentangled exaggerated visual counterfactuals | V1 | B | Dedicated latent-space visual interpretation with human-in-the-loop analysis. |
| V44 | Ha et al. (2025), *Diffusion Counterfactuals for Image Regressors* | Yes | Yes | Yes | Yes | Yes | Include | Explanation | Target-value-conditioned diffusion image | V1 | B | Extends visual counterfactuals from classes to continuous outputs. |
| V45 | Chen et al. (2025), *Distilling Counterfactual Reasoning from Language to Vision* | Yes | Yes | Yes | Yes | Yes | Include | Learning/evaluation | Counterfactual video questions, interventions, and distilled reasoning | V1 | B | Counterfactual visual reasoning is both trained and benchmarked. |
| V46 | Xu et al. (2025), *Generating Image Counterfactuals Without Generative Models* | Yes | Yes | Yes | Yes | Yes | Include | Explanation | Direct model-guided image perturbation | V1 | B | Dedicated image counterfactual method without an external generator. |
| V47 | Lymperaiou et al. (2025), *HalCECE* | Yes | Yes | Yes | Yes | Yes | Include | Auditing/diagnosis | Conceptual counterfactual interventions for hallucination | V1 | B | Operational visual-concept counterfactuals diagnose VLM hallucinations. |
| V48 | Cao et al. (2025), *LeapFactual* | Yes | Yes | Yes | Yes | Yes | Include | Explanation | Conditional-flow visual counterfactual | V1 | B | Dedicated visual generator targeting reliable class change. |
| V49 | Sun et al. (2025), *Semantic Shapley-Based Counterfactual Explanations* | Yes | Yes | Yes | Yes | Yes | Include | Explanation/safety | Semantically selected driving-scene interventions | V1 | B | Counterfactual scenes explain end-to-end driving behavior. |
| V50 | Tian et al. (2026), *C-CoT* | Yes | Yes | Yes | Yes | Yes | Include | Learning/planning | Alternative actions and consequences grounded in visual scenes | V1 | B | Counterfactual reasoning is an explicit component of visually grounded safe planning. |
| V51 | Jiang et al. (2026), *CHARTOGRAPHER* | Yes | Yes | Yes | Yes | Yes | Include | Evaluation/benchmarking | Executable chart-data edit and rerendered chart | V1 | B | Controlled factual–counterfactual chart families diagnose VLM grounding. |
| V52 | Liang et al. (2026), *Envision, Attend, Then Respond* | Yes | Yes | Yes | Yes | Yes | Include | Mitigation | Generated visual counterpart used for attention contrast | V1 | B | Counterfactual visual comparison reduces hallucination at inference. |
| V53 | Guo et al. (2026), *MaskDiME* | Yes | Yes | Yes | Yes | Yes | Include | Explanation | Adaptively masked diffusion counterfactual | V1 | B | Dedicated precise and efficient visual counterfactual generation. |
| V54 | Sar et al. (2026), *VLM Reality Check* | Yes | Yes | Yes | Yes | Yes | Include | Evaluation/benchmarking | Minimal-edit causal image variants | V1 | B | Counterfactual benchmark diagnoses visual reasoning biases. |

## Screening result

- Candidate records screened: **54**
- Included records before publication-family deduplication: **49**
- Superseded records: **1** (V15 merged into V27)
- Substantively excluded records: **4** (V19, V22, V24, V38)
- Included publication families: **49**
- Included dedicated visual studies (V1): **45**
- Included cross-modal studies with substantive visual evidence (V2): **4**
- Included studies with full or substantially recoverable primary Markdown: **48**
- Included studies currently supported only by abstract-level Markdown: **1** (V30)

The 15 general-foundation records listed after the primary section in the overview file are not part of the 54-record candidate set. Reviews and surveys among those records remain contextual sources and are excluded from the primary-study count.
