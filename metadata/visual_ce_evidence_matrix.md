# Visual Counterfactual Review — Evidence Extraction Matrix

Status: corpus-level qualitative extraction complete; exact numerical verification remains claim-specific  
Rule: every substantive manuscript claim must be traceable to a primary-study Markdown record with an evidence grade.

## Extraction schema

### Bibliographic identity

- Citation key
- Authors, title, year, venue, DOI, and publication status
- Publication-family identifier and superseded versions

### Scope and purpose

- Technical purpose
- Intended consumer
- Vision task and application domain
- Visual modality
- Factual case and target, foil, or alternative
- Counterfactual artifact

### Method

- Intervention representation
- Generation or search mechanism
- Explained or affected model
- Model-access requirement
- External generator, oracle, surrogate, or pretrained-model dependency
- Optimization objectives and constraints
- Training and computational requirements

### Evaluation

- Datasets and baselines
- Target validity
- Proximity, sparsity, and preservation
- Distributional realism
- Semantic correctness and faithfulness
- Diversity and coverage
- Robustness and efficiency
- Human or domain-expert evaluation
- Downstream machine utility
- Ablations and sensitivity analyses

### Critical interpretation

- Principal contribution
- Claims supported by the evidence
- Claims not established
- Principal limitations
- Dependencies exchanged for earlier limitations
- Reproducibility resources
- Evidence grade and exact-value verification status

## Purpose codes

| Code | Technical purpose |
| --- | --- |
| E | Post-hoc counterfactual explanation or model interpretation |
| L | Counterfactual-guided learning or representation improvement |
| A | Counterfactual auditing or diagnosis |
| B | Counterfactual evaluation or benchmark construction |
| M | Counterfactual-guided mitigation, repair, privacy, or safety control |
| D | Data construction and controllable editing |

## Evidence ladder

| Level | Evidence question | Typical measures | Claim supported | Claim not supported by this level alone |
| --- | --- | --- | --- | --- |
| 1. Target effectiveness | Did the measured model output change as intended? | Flip/success rate, target probability or margin, regression error | The candidate changes the tested predictor | Naturalness, semantic correctness, or causal validity |
| 2. Minimality and preservation | Was the selected representation changed little? | L0/L1/L2, mask area, LPIPS, SSIM, PSNR, identity similarity | The candidate is small or preserved under selected measures | Human-perceived or domain-valid invariance |
| 3. Distributional plausibility | Does the output resemble a reference distribution? | FID/KID, discriminator, density/manifold score, realism judgement | Samples appear in-distribution under the chosen test | Instance-level feasibility or causal attainability |
| 4. Semantic and model faithfulness | Did the intended factor change, and is it tied to model evidence? | Oracle agreement, concept/attribute change, erasure tests, localization | The specified semantic or model-sensitive evidence changed | Real-world causal validity |
| 5. Domain or world validity | Is the alternative credible under domain dependencies and dynamics? | Domain constraints, simulator consistency, expert assessment | The intervention is credible under the tested domain model | Universal feasibility or clinical/physical safety |
| 6. Usefulness | Does the intended user or system benefit? | Teaching/simulation accuracy, decision quality, calibration, VQA/segmentation, hallucination reduction | Utility for the tested population or downstream task | General explanatory usefulness or long-term outcome |

The ladder is not a scalar leaderboard. Lower levels are often necessary for higher claims but cannot replace them.

## Study-level qualitative evidence matrix

Exact numerical results are included only when recoverable from the primary study; qualitative claims remain bounded by the final paper’s interpretation.

| ID | Study | Purpose | Mechanism and artifact | Evaluation emphasis | Strongest supported interpretation | Main unresolved limitation | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| V01 | Goyal et al. (2019) | E | Query–distractor feature-region substitution | Classification reversal, localization, machine teaching | Explicit visual foils can teach tested class distinctions | Donor alignment and feature replacement do not create a natural or feasible edit | B |
| V02 | Atrey et al. (2020) | A | Counterfactual interventions on Atari states to test saliency hypotheses | Hypothesis falsification across saliency methods and games | Saliency narratives can be tested against environment semantics | Tested interventions and Atari semantics do not establish a general explanation metric | B |
| V03 | Nemirovsky et al. (2020) | E/M | Residual GAN generates target counterfactual instances | Validity, realism/actionability proxies, latency | Amortized GAN generation can produce rapid image counterfactuals in the tested setting | MNIST-level visual evidence and generator realism do not establish natural-image feasibility | B |
| V04 | Zhao et al. (2020) | E | Attribute-text substitution followed by image generation | Target change and crowd-assisted fine-grained classification | Attribute-conditioned visual contrasts can communicate class differences | Fixed ontology and generator entanglement restrict discovery and generality | B |
| V05 | Wang and Vasconcelos (2020) | E | Discriminant attribution and anti-attribution maps | Localization proxy, speed, machine teaching | Fast counter-class-specific localization is useful for tested discrimination tasks | A heatmap is not a realizable counterfactual intervention and inherits attribution error | B |
| V06 | Rodríguez et al. (2021) | E/A | Disentangled latent optimization with diversity and nontriviality controls | Validity, diversity, valuable/nontrivial explanations | Multiple latent alternatives expose factors missed by nearest single edits | Disentanglement, gradients, and diversity metrics can still encode confounds | B |
| V07 | Olson et al. (2021) | E | Generated visual RL state that changes the selected action | Image fidelity and two non-expert user studies | Counterfactual states can help tested users identify flawed agents | Frames may be unreachable under environment dynamics | B |
| V08 | Guidotti and Ruggieri (2021) | E | Ensemble of weak explainers with feature and instance sampling | Quality-property coverage across image, time-series, and tabular data | Ensembling can broaden measured counterfactual properties | It compounds base-explainer assumptions, cost, and selection burden | B |
| V09 | Van Looveren and Klaise (2021) | E | Prototype-guided input or latent optimization | Search speed and interpretability proxies on image/tabular data | Prototypes can accelerate search toward representative target regions | A class prototype is not an individualized feasible state | B |
| V10 | Kenny and Keane (2021) | E | Replace exceptional latent features with target-normal values | Plausibility, counterfactual and semi-factual benchmark measures | Target-relative normality can produce plausible image contrasts | Latent normality and decoding depend on learned representation and generator | B |
| V11 | Montenegro et al. (2021) | E/M | Privacy-aware generative case explanations with counterfactual module | Realism, privacy proxies, explanatory value | Privacy can be treated as a first-class visual-explanation objective | No formal privacy guarantee and unresolved privacy–intelligibility trade-off | B |
| V12 | Augustin et al. (2022) | E | Robust-gradient-guided diffusion | Validity, realism, preservation, meaningfulness, human judgement | Diffusion supports high-quality visual counterfactuals for broad classifiers | Slow white-box guidance and auxiliary robust-classifier dependence | B |
| V13 | Pombo et al. (2023) | L/M | Conditional diffeomorphic 3-D brain-image synthesis | Morphology preservation, subgroup performance, fairness | Morphologically constrained counterfactual augmentation can improve tested equity outcomes | Population-level morphology is not an individual demographic intervention | B |
| V14 | Singla et al. (2023a) | E | Probability-conditioned progressive GAN trajectory | Smooth target progression and radiology-resident assessment | Counterfactual trajectories can reveal graded model changes | Diagnostic correlations and artifacts can move with the target score | B |
| V15 | Mertes et al. (2022) | E | Cycle-consistent abnormal/normal medical-image translation | Non-expert mental models, satisfaction, comparison with saliency | Full-image contrasts can aid tested non-experts | Non-experts cannot validate anatomy; binary translation may alter diffuse content | B |
| V16 | Chen et al. (2023) | E | Counterfactual similarity maps linked to attribute words | Similarity explanation, localization, semantic attribute correspondence | Pairwise visual similarity can be expressed through contrastive attributes | Face-specific ontology and erasure artifacts limit generality | B |
| V17 | Singla et al. (2023b) | L/M | Reuse counterfactual paths as soft-labelled training data | Calibration, OOD detection, adversarial robustness | Counterfactual-derived augmentation improves selected model behaviours | Downstream gains do not validate each sample as an explanation | B |
| V18 | Dang et al. (2023) | L | Causal-factor recombination for few-shot image generation | Accuracy on four few-shot benchmarks and ablations | Counterfactual factor recombination improves tested scarce-data learning | Factor independence is assumed rather than causally identified | B |
| V19 | Law et al. (2023) | E | VAE traversal and image enhancement for street scenes | Classifier/regressor behaviour and non-expert user study | Visual counterfactuals can aid some holistic urban concepts | Utility is concept-dependent; global edits, realism, and geographic bias remain | B |
| V20 | Huber et al. (2023) | E | StarGAN-style domain translation between RL action outcomes | Computational quality and strategy-analysis user study | Visual counterfactuals can help users compare learned agent strategies | Generated states may violate dynamics and tested tasks remain limited | B |
| V21 | Li et al. (2023) | L | Counterfactual effect filtering of interacted and uninteracted multimodal content | Recommendation ranking and ablations | Visually grounded counterfactual filtering improves offline recommendation | Non-interaction is confounded by exposure; no direct explanation evidence | B |
| V22 | Zemni et al. (2023) | E | Object-centric scene latent with controllable spatial/style edits | Driving-scene counterfactual benchmarks, segmentation, user study | Object structure enables controllable counterfactuals in multi-object scenes | Scene generator and object decomposition constrain attainable edits | B |
| V23 | Del Ser et al. (2024) | E/A | GAN plus multiobjective Pareto search | Validity, plausibility, intensity, bias/concept analysis | Objective conflict can be exposed instead of hidden in one weighted score | Generator and attribute dependencies remain; user choice over Pareto sets is unvalidated | B |
| V24 | Samadi et al. (2023) | E/M | Saliency-aware perturbations for automated-driving inputs | Target decision change, saliency consistency, visual quality | Saliency can focus safety-oriented counterfactual edits | Saliency is an imperfect causal proxy and scene feasibility is not guaranteed | B |
| V25 | Bi et al. (2024) | L | Counterfactual masking and teacher–student distillation for VQA | VQA-CP accuracy, bias resistance, representation ablations | Counterfactual supervision reduces tested answer-prior dependence | Masking is out-of-distribution and the artifact is not a user explanation | B |
| V26 | Montenegro et al. (2024) | E/M | Identity-disentangled anonymized case and counterfactual images | Abstract-level privacy, realism, and explanatory claims | The study operationalizes privacy-aware counterfactual case explanation | Full methods, metrics, tables, and limitations are unavailable in Markdown | C |
| V27 | Ji et al. (2024) | M | Formal counterfactual anomaly-repair optimization | Repair validity/properties across anomaly modalities | Counterfactual search can be framed as repair with formal properties | Cross-modal guarantees do not by themselves establish visual realism or domain feasibility | B |
| V28 | Shvetsov et al. (2024) | L | Abnormal-to-normal inpainting; residual becomes segmentation mask | Counterfactual generation and segmentation IoU/Dice | Counterfactual synthesis can supply weak lesion supervision | Classifier shortcuts and inpainting artifacts can transfer into masks | B |
| V29 | Cai et al. (2024) | E/L | Relevance-guided masked medical-image intervention and causal-effect comparison | VQA accuracy, visual relevance, bias mitigation | Interventional training improves tested VQA grounding and performance | LRP and masking define the estimated effect; clinical intervention meaning is absent | B |
| V30 | Atad et al. (2024) | E | Diffusion-autoencoder traversal for class and continuous targets | Target validity, preservation, severity/regression behaviour | One framework can generate medical-image counterfactuals for classification and regression | Mostly 2-D evidence, latent monotonicity assumptions, no clinician validation | B |
| V31 | Khan et al. (2024) | E | Internal concept/filter intervention with visual decoding | Model sensitivity, target change, visual reconstruction | The edit is tied more directly to target-network representations | Simple datasets and decoded images do not establish causal concept fidelity | B |
| V32 | Guo et al. (2024) | E/A | Expert-facing segmented cardiovascular region swaps | Interactive expert hypothesis testing and qualitative assessment | Expert interaction reveals physiological dependencies omitted by generic metrics | Two experts, donor/segmentation artifacts, and no clinical or causal guarantee | B |
| V33 | Li et al. (2024) | E | Direct-contribution estimation followed by input counterfactual construction | Prediction effect, localization, efficiency | Direct contribution can guide fast visual counterfactual relevance inference | Intervention realism and causal interpretation remain proxy-dependent | B |
| V34 | Samadi et al. (2024) | E/M | Saliency-aware visual-state counterfactuals for RL policies | Action change, visual quality, policy explanation | Extends saliency-guided counterfactual explanation to visual RL policies | Reachability, long-horizon policy effects, and saliency faithfulness remain open | B |
| V35 | Jeanneret et al. (2024) | E | Black-box text-to-image diffusion with distilled class/context embedding | Query cost, validity, realism, preservation | Counterfactual generation can reduce target-model access requirements | Global edits and foundation-model priors weaken instance-specific attribution | B |
| V36 | Valoor et al. (2025) | E | Case-based GAN produces diagnostic counterfactual maps | Classification performance and comparison with visual explanation methods | Counterfactual maps provide an interpretable diagnostic contrast in the tested setting | Clinical validity, patient preservation, and external validation remain unclear | B |
| V37 | Lang et al. (2024) | A | StylEx latent discovery and expert review | Attribute discovery across medical tasks and interdisciplinary assessment | Counterfactual visual factors can generate hypotheses about model and dataset signals | Discovered factors are correlational, may be entangled, and lack prospective validation | B |
| V38 | Rotem et al. (2024) | E/A | Classification-oriented disentangled latent model with exaggerated counterfactuals | Known-feature recovery, SHAP, expert/human-in-loop interpretation | Global latent-factor discovery can support instance-level visual interpretation | A factor can retain multiple meanings and omit clinically relevant confounds | B |
| V39 | Ha and Bender (2025) | E | Pixel- and latent-diffusion counterfactuals for continuous target values | Target error, FID, sparsity, identity/preservation | Continuous-output counterfactuals expose trade-offs between effectiveness and preservation | Limited domains, oracle proxies, and identity confounding | B |
| V40 | Chen et al. (2026) | L/B | Causal-graph video benchmark plus supervised and reinforcement post-training | Counterfactual reasoning accuracy and graph consistency | Language-derived supervision improves tested visual counterfactual reasoning | Generated causal graphs and answer formats do not enact physical interventions | B |
| V41 | Xu et al. (2025) | E | Class-conditional denoising scores with derivative-free search | Validity, proximity, image quality, target selection | Image counterfactuals can be generated without a conventional GAN/VAE decoder | Multiple learned scores, automatic foil selection, and limited complex-image evidence | B |
| V42 | Lymperaiou et al. (2025) | A | Scene-graph conceptual counterfactuals for caption hallucination | Conceptual hallucination detection versus linguistic metrics | Structured counterfactuals distinguish missing, extra, and relational errors | Parser/ground-truth errors and graph edits do not expose internal model causes | B |
| V43 | Cao et al. (2026) | E/L | Conditional flow matching toward target-manifold regions | Validity, semantic reliability, realism, augmentation utility | Independent semantic checks reveal that unreliable counterfactuals can harm learning | Oracle/CLIP proxies and computational cost replace direct human boundary validation | B |
| V44 | Sun et al. (2025) | E/M | Semantic Shapley selection and counterfactual driving-scene changes | Driving prediction change, semantic relevance, scenario quality | Semantically targeted interventions can explain influential scene elements | Shapley assumptions and generated-scene realism do not establish causal safety | B |
| V45 | Tian et al. (2026) | L/M | Counterfactual chain-of-thought over visual scene, risks, actions, and consequences | Planning accuracy, risk reasoning, robustness, ablations | Explicit alternatives improve tested visually grounded planning | Verbalized reasoning may be post-hoc and simulated benchmarks do not establish road safety | B |
| V46 | Jiang et al. (2026) | B | Chart-to-code reconstruction and controlled data edits | Counterfactual consistency, chart grounding, VLM performance | Executable rerendering provides auditable visual benchmark interventions | Reconstructable-chart selection and restricted edit types limit ecological coverage | B |
| V47 | Liang et al. (2026) | M | Diffusion-normalized counterpart, contrastive attention, token suppression | Hallucination reduction and task performance | Counterfactual visual contrast can mitigate hallucination without retraining | May erase genuine anomalies; dual-stream cost and internal access remain | B |
| V48 | Guo et al. (2026) | E | Adaptive dual-classifier masks integrated into diffusion | Validity, FID, preservation, localization, diffusion cost | Adaptive masks concentrate edits and reduce counterfactual diffusion cost | White-box noisy gradients and proxy-biased realism/preservation measures | B |
| V49 | Sar et al. (2026) | B/A | Large controlled set of minimal-edit causal image variants | Bias-specific accuracy and counterfactual consistency | Controlled visual variants diagnose shortcut-sensitive VLM behaviour | Synthetic invariance assumptions diagnose failures but not internal mechanisms | B |
| V50 | Khorram and Fuxin (2022), C3LT | E | GV; LC; LOC | Cycle-consistent latent transformations; prediction transitions and preservation | Evidence is specific to the stated role and tested task | Generator coverage and cycle consistency do not establish semantic correctness | B |
| V51 | Jeanneret et al. (2022), DiME | E | DF; GI; LOC | Target-gradient diffusion; target success and attribute preservation | Evidence is specific to the stated role and tested task | Classifier guidance and learned priors retain shortcut and oracle dependence | B |
| V52 | Jeanneret et al. (2023), ACE | E | DF; GI; LOC | Diffusion-filtered adversarial search and inpainting refinement; target success and preservation | Evidence is specific to the stated role and tested task | Interpretable perturbations do not independently guarantee semantic correctness or faithfulness | B |
| V53 | Augustin et al. (2024), DiG-IN | E/A | DF; GI; GLOBAL | Guided diffusion for classifier disagreement, systematic errors, and neuron analysis | Evidence is specific to the stated role and tested task | Guidance and generative priors condition the discovered differences | B |
| V54 | Weng et al. (2024), FastDiME | E/A/M | DF; GI; LOC | Self-optimized masking for shortcut insertion and removal; response effects and inference burden | Evidence is specific to the stated role and tested task | Shortcut attribution requires independently verified edits and invariants | B |
| V55 | Sobieski and Biecek (2024), Global Counterfactual Directions | E/A | GV; LC; GLOBAL | Dataset-level latent directions that alter classifier decisions | Evidence is specific to the stated role and tested task | Global directions inherit generator semantics and can conflate correlated factors | B |
| V56 | Haselhoff et al. (2024), GdVAE | E | GV; LC; LOC | Class-structured generative model with closed-form latent counterfactual construction | Evidence is specific to the stated role and tested task | Integrated self-explanation trades portability for latent-distribution assumptions | B |
| V57 | Mertes et al. (2024), Relevant Irrelevance | E | GV; GI; LOC | Alterfactual image contrasts; tested human communication and understanding | Evidence is specific to the stated role and tested task | Output-preserving contrasts need their own success criterion and population-specific validation | B |
| V58 | Zhang et al. (2025b), Fine-Grained Saliency Counterfactuals | E | AT; LM; LOC | Saliency partition of object and part evidence associated with misclassification | Evidence is specific to the stated role and tested task | Contribution estimates and intervention semantics condition representational faithfulness | B |
| V59 | Chowdhury et al. (2025), Mirror-CFE | E | OP; LC; PATH | Classifier-feature-space trajectories for faithful visual explanations | Evidence is specific to the stated role and tested task | Layer choice, decoder quality, and feature semantics limit input-space correspondence | B |
| V60 | Zaher et al. (2026), Perceptual Counterfactual Geodesics | E | OP; LC; PATH | Paths induced by robust visual-feature geometry | Evidence is specific to the stated role and tested task | Counterfactual semantics remain conditional on the selected feature geometry | B |
| V61 | Li et al. (2024c), CFI-VAE | L | CL; LC; SIGNAL | Counterfactual interventions regularize causal visual representations | Evidence is specific to the stated role and tested task | Learned factors and intervention objectives do not establish causal identification | B |
| V62 | Lin et al. (2024), CI-MIL | L | CL; MR; SIGNAL | Counterfactual inference supplies instance pseudo-labels for whole-slide multiple-instance learning | Evidence is specific to the stated role and tested task | Classifier shortcuts can propagate into weak supervision | B |
| V63 | Singh et al. (2024), DUB | L | CL; MR; SIGNAL | Visually similar but acoustically different cross-modal pairs for audiovisual representation learning | Evidence is specific to the stated role and tested task | Useful representations do not establish explanation faithfulness or full cross-modal invariance | B |
| V64 | Li et al. (2024b), CoFE | L | EX; RS; SIGNAL | Patch-swapped factual-counterfactual contrasts for radiology report generation | Evidence is specific to the stated role and tested task | Patch validity and diagnostic preservation require independent domain checks | B |
| V65 | Lai et al. (2024), COMO | L | CL; MR; SIGNAL | Multimodal counterfactual hard negatives for concept composition | Evidence is specific to the stated role and tested task | Task improvements may depend on construction patterns rather than general compositional reasoning | B |
| V66 | Venkatesh et al. (2024), Counterfactual World Modeling | L | CL; VS; SIGNAL | Controlled physical-dynamics alternatives for learned world representations | Evidence is specific to the stated role and tested task | Validity is bounded by decomposition and dynamics assumptions | B |
| V67 | Yin et al. (2025), KCDP | L | DF; MR; SIGNAL | Knowledge-aligned counterfactual-enhancement diffusion for cross-domain visual emotion recognition | Evidence is specific to the stated role and tested task | Knowledge priors and domain-transfer assumptions bound the downstream result | B |
| V68 | Jia et al. (2025), GCS | L/E | DF; GI; SET | Generated counterfactual sets for CLIP compositionality and learning | Evidence is specific to the stated role and tested task | Diagnostic contrasts require a separate evidence chain when reused as training data | B |
| V69 | Zha et al. (2025), ICF | L | CL; MR; SIGNAL | Implicit counterfactual learning for audio-visual segmentation | Evidence is specific to the stated role and tested task | Segmentation gains do not independently establish correctness of every counterfactual relation | B |
| V70 | Kung et al. (2025), State-Change Counterfactuals | L | CL; VS; SIGNAL | Counterfactual failure outcomes supervise procedure-aware video encoders | Evidence is specific to the stated role and tested task | Task-specific descriptions and objectives may be learned without general physical intervention reasoning | B |
| V71 | Shrivastava et al. (2026), Point Prompting | L | DF; VS; SIGNAL | Point-prompted counterfactual video generation for motion tracking | Evidence is specific to the stated role and tested task | Video priors and dynamics assumptions limit attainable motion alternatives | B |
| V72 | Yu and Li (2024), Counterfactual Referring Expression Comprehension | A/L | CL; MR; SIGNAL | Fine-grained referring-expression mismatches and visually grounded task supervision | Evidence is specific to the stated role and tested task | Mismatch construction must preserve relevant facts and control linguistic shortcuts | B |
| V73 | Zhang et al. (2024b), C-VQA | A/B | PG; SP; DATA | Direct and indirect hypothetical premises over real and synthetic scenes | Evidence is specific to the stated role and tested task | Benchmark accuracy does not establish transferable counterfactual reasoning | B |
| V74 | Howard et al. (2024), SocialCounterfactuals | A/M | DF; GI; DATA | Intersectional social-attribute variants for vision-language bias probing and mitigation | Evidence is specific to the stated role and tested task | Fairness conclusions depend on edit validity, subgroup coverage, and the fairness criterion | B |
| V75 | Zhang et al. (2024a), CoCT | A/L | CL; MR; SIGNAL | Chains of counterfactual thought for bias-robust vision-language reasoning | Evidence is specific to the stated role and tested task | Reasoning chains and supervision formats can retain construction-specific shortcuts | B |
| V76 | Shen et al. (2025), Abductive Counterfactual IQA | A | CL; LC; LOC | Abductive inference of perceptual effects and deep-feature distortion relationships | Evidence is specific to the stated role and tested task | Smooth model responses do not establish real-world monotonicity or causal identification | B |
| V77 | Zhu et al. (2024), TFCD | M | CL; MR; SIGNAL | Training-free counterfactual debiasing for multimodal sarcasm detection | Evidence is specific to the stated role and tested task | Debiasing gains require preservation and side-effect checks in the intended task | B |
| V78 | Zong et al. (2025a), CF-PACR | M/L | CL; MR; SIGNAL | Counterfactual debiasing for physical audiovisual commonsense reasoning | Evidence is specific to the stated role and tested task | Task gains are not evidence of general physical counterfactual competence | B |
| V79 | Zong et al. (2025b), Text-Guided Fine-Grained Counterfactual Inference | M/L | CL; MR; SIGNAL | Text-guided counterfactual inference for short-video fake-news detection | Evidence is specific to the stated role and tested task | Text and audiovisual construction assumptions limit causal interpretation | B |
| V80 | Wu et al. (2025), Antidote | M | CL; MR; SIGNAL | Post-training mitigation of counterfactual-presupposition and object-perception hallucinations | Evidence is specific to the stated role and tested task | Failure reduction does not establish general grounding or safe deployment | B |
| V81 | Zhang et al. (2025a), CREStE | M/L | CL; VS; SIGNAL | Counterfactual trajectory guidance and human queries for mapless navigation learning | Evidence is specific to the stated role and tested task | Navigation performance needs dynamic validity, scenario coverage, and residual-risk evaluation | B |
| V82 | Song et al. (2024), DAC | D | CL; GI; LOC | Doubly abductive counterfactual inference for text-based image editing | Evidence is specific to the stated role and tested task | Editing fidelity is the endpoint; it does not establish explanation faithfulness | B |
| V83 | Winter et al. (2024), ObjectDrop | D | DF; VS; DATA | Paired counterfactual captures teach wider scene effects of object insertion and removal | Evidence is specific to the stated role and tested task | Physical observations provide bounded grounding, with coverage limited by captured interventions | B |
| V84 | Huang et al. (2025), T-FIT | D | CL; GI; LOC | Compositional concept learning and counterfactual abduction for fashion editing | Evidence is specific to the stated role and tested task | Source preservation and concept composition do not establish model-explanation fidelity | B |
| V85 | Wang et al. (2025), OmniDrive | B | PG; SP; DATA | Candidate ego trajectories evaluated against structured 3-D constraints | Evidence is specific to the stated role and tested task | Engineered constraints and construction grammar limit transfer to road safety | B |
| V86 | Ness et al. (2026), Multiverse Mechanica | B | PG; SP; DATA | Aligned counterfactual worlds rendered from known game-engine graphs | Evidence is specific to the stated role and tested task | Known executable mechanisms provide bounded testbed validity rather than universal world validity | B |
| V87 | Lang et al. (2021), StylEx | E/A | Classifier-specific StyleSpace attributes and generated visual contrasts | Attribute discovery and classifier response | Learned style attributes support visual hypothesis discovery | Generator semantics and entanglement limit factor identification | B |
| V88 | Singla et al. (2019), Progressive Exaggeration | E | Probability-conditioned image sequences spanning classifier confidence | Target progression and visual preservation | Ordered contrasts expose graded model responses | Confidence trajectories do not establish disease dynamics or causal forecasts | B |
| V89 | Denton et al. (2019), Image Counterfactual Sensitivity Analysis | A | Generated face-attribute interventions | Classifier sensitivity and unintended bias | Controlled attribute changes can probe model sensitivity | Fairness conclusions depend on attribute validity and preserved identity | B |
| V90 | Balakrishnan et al. (2021), Causal Benchmarking of Face-Analysis Bias | A/B | Human-validated synthetic attribute transects | Bias benchmarking and human edit validation | Validated attribute transects support controlled face-analysis comparisons | Synthetic coverage and dependent attributes bound causal interpretation | B |
| V91 | Dash et al. (2022), ImageCFGen | A/M | SCM-constrained generation with counterfactual regularization | Bias evaluation and mitigation | Structural constraints support tested bias analysis and regularization | Results remain conditional on the structural model and edit validity | B |
| V92 | Rott Shaham et al. (2024), MAIA | A | Multimodal agent constructs and tests interpretability hypotheses | Intervention-based hypothesis testing | Agentic exploration can support model auditing | Adaptive exploration needs independent held-out hypothesis confirmation | B |
| V93 | Spanos et al. (2026), V-CECE | E | Visual counterfactual explanations through conceptual edits | Concept semantics and human–model alignment | Explicit concepts provide an interpretable intervention vocabulary | Concept changes require faithful pixel realization and invariant checks | B |
| V94 | Vaeth et al. (2025), XAIDIFF | E | Generative example-based explanations with probabilistic trade-offs | Generation and explanation objectives | Probabilistic formulations make competing explanation objectives explicit | A generative formulation does not select an appropriate trade-off for every user | B |
| V95 | Monteiro et al. (2023), Axiomatic Soundness of Counterfactual Image Models | B | Null interventions, round-trip restoration, and requested-parent interventions | Composition, reversibility, and oracle effectiveness | Axiomatic tests reveal distinct consistency failures in counterfactual image models | Passing necessary axioms does not identify the true causal counterfactual | B |

## Cross-paper metric audit

| Evaluation family | Commonly observed in corpus | Suitable comparative use | Required caution |
| --- | --- | --- | --- |
| Target validity | Very common | Compare methods on the same target task and access assumptions | A successful flip may be adversarial or semantically wrong |
| Pixel/feature proximity | Common | Compare within the same representation and preprocessing | Distances across pixels, latents, masks, and concepts are not commensurate |
| Perceptual preservation | Common in generative methods | Assess retained visual content under the same encoder/metric | Learned perceptual metrics may miss identity, anatomy, or background semantics |
| FID/KID or distributional realism | Common in GAN/diffusion work | Set-level distribution comparison under matched datasets | Does not establish feasibility of an individual counterfactual |
| Semantic correctness | Increasing in recent work | Check target attribute/object using an independent evaluator | The evaluator may share training data or shortcuts with the explained model |
| Diversity | Concentrated in DiVE, ensembles, and Pareto methods | Measure coverage under explicitly defined edit semantics | Pairwise difference does not imply meaningful alternatives |
| Human usefulness | Sparse and heterogeneous | Interpret only for the tested task and population | Preference, trust, teaching, simulation, and decision quality are different outcomes |
| Domain-expert validity | Very sparse | Elicit missing constraints and intervention semantics | Small expert studies provide design evidence, not population effectiveness |
| Downstream utility | Growing in learning/mitigation papers | Evaluate the role of counterfactuals as training or control instruments | Does not validate counterfactuals as explanations |
| Causal/world validity | Rare | Requires explicit domain process, dynamics, or intervention model | “Causal,” “counterfactual,” or “realistic” labels are not evidence by themselves |

## Evidence-level conclusions

1. The corpus supports a broad technical definition in which a visual counterfactual may function as an explanation, learning signal, audit contrast, benchmark item, or mitigation input.
2. These purposes require different validation endpoints; their metrics cannot be pooled into a single method ranking.
3. The most common evidence establishes target-model change, pixel/perceptual preservation, or distributional realism.
4. Evidence for semantic correctness is growing, but it often relies on auxiliary models that can share biases with the explained model.
5. Evidence for domain feasibility, causal validity, and longitudinal human usefulness remains sparse.
6. Recent work shifts from generating visually convincing alternatives toward controlled counterfactual reasoning, auditing, and system-level use.

## Final-paper evaluation protocol

Declare the factual anchor, target or foil, permissible interventions, required consequences, and invariants. Report preprocessing, evaluator models, thresholds, sample sizes, seeds, and whether metrics cover all attempts or only successes. Pair success-conditioned quality with overall success and failure counts. Separate training from inference cost and include retries. Prefer semantic checks independent of the target model and generator, acknowledging shared biases and evaluator uncertainty. Expose trade-offs rather than pooling heterogeneous roles into one ranking.
