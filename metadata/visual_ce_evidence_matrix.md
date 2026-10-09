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

## Full qualitative evidence matrix

Exact values are marked “pending” unless the relevant Markdown table or sentence is clearly recoverable. This prevents converted-table corruption from entering the manuscript.

| ID | Study | Purpose | Mechanism and artifact | Evaluation emphasis | Strongest supported interpretation | Main unresolved limitation | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| V01 | Goyal et al. (2019) | E | Query–distractor feature-region substitution | Classification reversal, localization, machine teaching | Explicit visual foils can teach tested class distinctions | Donor alignment and feature replacement do not create a natural or feasible edit | B |
| V02 | Atrey et al. (2019) | A | Counterfactual interventions on Atari states to test saliency hypotheses | Hypothesis falsification across saliency methods and games | Saliency narratives can be tested against environment semantics | Tested interventions and Atari semantics do not establish a general explanation metric | B |
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
| V13 | Pombo et al. (2022) | L/M | Conditional diffeomorphic 3-D brain-image synthesis | Morphology preservation, subgroup performance, fairness | Morphologically constrained counterfactual augmentation can improve tested equity outcomes | Population-level morphology is not an individual demographic intervention | B |
| V14 | Singla et al. (2022) | E | Probability-conditioned progressive GAN trajectory | Smooth target progression and radiology-resident assessment | Counterfactual trajectories can reveal graded model changes | Diagnostic correlations and artifacts can move with the target score | B |
| V16 | Mertes et al. (2022) | E | Cycle-consistent abnormal/normal medical-image translation | Non-expert mental models, satisfaction, comparison with saliency | Full-image contrasts can aid tested non-experts | Non-experts cannot validate anatomy; binary translation may alter diffuse content | B |
| V17 | Chen et al. (2022) | E | Counterfactual similarity maps linked to attribute words | Similarity explanation, localization, semantic attribute correspondence | Pairwise visual similarity can be expressed through contrastive attributes | Face-specific ontology and erasure artifacts limit generality | B |
| V18 | Singla et al. (2023) | L/M | Reuse counterfactual paths as soft-labelled training data | Calibration, OOD detection, adversarial robustness | Counterfactual-derived augmentation improves selected model behaviours | Downstream gains do not validate each sample as an explanation | B |
| V20 | Dang et al. (2023) | L | Causal-factor recombination for few-shot image generation | Accuracy on four few-shot benchmarks and ablations | Counterfactual factor recombination improves tested scarce-data learning | Factor independence is assumed rather than causally identified | B |
| V21 | Law et al. (2023) | E | VAE traversal and image enhancement for street scenes | Classifier/regressor behaviour and non-expert user study | Visual counterfactuals can aid some holistic urban concepts | Utility is concept-dependent; global edits, realism, and geographic bias remain | B |
| V23 | Huber et al. (2023) | E | StarGAN-style domain translation between RL action outcomes | Computational quality and strategy-analysis user study | Visual counterfactuals can help users compare learned agent strategies | Generated states may violate dynamics and tested tasks remain limited | B |
| V25 | Li et al. (2023) | L | Counterfactual effect filtering of interacted and uninteracted multimodal content | Recommendation ranking and ablations | Visually grounded counterfactual filtering improves offline recommendation | Non-interaction is confounded by exposure; no direct explanation evidence | B |
| V26 | Zemni et al. (2023) | E | Object-centric scene latent with controllable spatial/style edits | Driving-scene counterfactual benchmarks, segmentation, user study | Object structure enables controllable counterfactuals in multi-object scenes | Scene generator and object decomposition constrain attainable edits | B |
| V27 | Del Ser et al. (2023) | E/A | GAN plus multiobjective Pareto search | Validity, plausibility, intensity, bias/concept analysis | Objective conflict can be exposed instead of hidden in one weighted score | Generator and attribute dependencies remain; user choice over Pareto sets is unvalidated | B |
| V28 | Samadi et al. (2023) | E/M | Saliency-aware perturbations for automated-driving inputs | Target decision change, saliency consistency, visual quality | Saliency can focus safety-oriented counterfactual edits | Saliency is an imperfect causal proxy and scene feasibility is not guaranteed | B |
| V29 | Bi et al. (2024) | L | Counterfactual masking and teacher–student distillation for VQA | VQA-CP accuracy, bias resistance, representation ablations | Counterfactual supervision reduces tested answer-prior dependence | Masking is out-of-distribution and the artifact is not a user explanation | B |
| V30 | Montenegro et al. (2024) | E/M | Identity-disentangled anonymized case and counterfactual images | Abstract-level privacy, realism, and explanatory claims | The study operationalizes privacy-aware counterfactual case explanation | Full methods, metrics, tables, and limitations are unavailable in Markdown | C |
| V31 | Ji et al. (2024) | M | Formal counterfactual anomaly-repair optimization | Repair validity/properties across anomaly modalities | Counterfactual search can be framed as repair with formal properties | Cross-modal guarantees do not by themselves establish visual realism or domain feasibility | B |
| V32 | Shvetsov et al. (2024) | L | Abnormal-to-normal inpainting; residual becomes segmentation mask | Counterfactual generation and segmentation IoU/Dice | Counterfactual synthesis can supply weak lesion supervision | Classifier shortcuts and inpainting artifacts can transfer into masks | B |
| V33 | Cai et al. (2024) | E/L | Relevance-guided masked medical-image intervention and causal-effect comparison | VQA accuracy, visual relevance, bias mitigation | Interventional training improves tested VQA grounding and performance | LRP and masking define the estimated effect; clinical intervention meaning is absent | B |
| V34 | Atad et al. (2024) | E | Diffusion-autoencoder traversal for class and continuous targets | Target validity, preservation, severity/regression behaviour | One framework can generate medical-image counterfactuals for classification and regression | Mostly 2-D evidence, latent monotonicity assumptions, no clinician validation | B |
| V35 | Khan et al. (2024) | E | Internal concept/filter intervention with visual decoding | Model sensitivity, target change, visual reconstruction | The edit is tied more directly to target-network representations | Simple datasets and decoded images do not establish causal concept fidelity | B |
| V36 | Guo et al. (2024) | E/A | Expert-facing segmented cardiovascular region swaps | Interactive expert hypothesis testing and qualitative assessment | Expert interaction reveals physiological dependencies omitted by generic metrics | Two experts, donor/segmentation artifacts, and no clinical or causal guarantee | B |
| V37 | Li et al. (2024) | E | Direct-contribution estimation followed by input counterfactual construction | Prediction effect, localization, efficiency | Direct contribution can guide fast visual counterfactual relevance inference | Intervention realism and causal interpretation remain proxy-dependent | B |
| V39 | Samadi et al. (2024) | E/M | Saliency-aware visual-state counterfactuals for RL policies | Action change, visual quality, policy explanation | Extends saliency-guided counterfactual explanation to visual RL policies | Reachability, long-horizon policy effects, and saliency faithfulness remain open | B |
| V40 | Jeanneret et al. (2024) | E | Black-box text-to-image diffusion with distilled class/context embedding | Query cost, validity, realism, preservation | Counterfactual generation can reduce target-model access requirements | Global edits and foundation-model priors weaken instance-specific attribution | B |
| V41 | Valoor et al. (2024) | E | Case-based GAN produces diagnostic counterfactual maps | Classification performance and comparison with visual explanation methods | Counterfactual maps provide an interpretable diagnostic contrast in the tested setting | Clinical validity, patient preservation, and external validation remain unclear | B |
| V42 | Lang et al. (2024) | A | StylEx latent discovery and expert review | Attribute discovery across medical tasks and interdisciplinary assessment | Counterfactual visual factors can generate hypotheses about model and dataset signals | Discovered factors are correlational, may be entangled, and lack prospective validation | B |
| V43 | Rotem et al. (2024) | E/A | Classification-oriented disentangled latent model with exaggerated counterfactuals | Known-feature recovery, SHAP, expert/human-in-loop interpretation | Global latent-factor discovery can support instance-level visual interpretation | A factor can retain multiple meanings and omit clinically relevant confounds | B |
| V44 | Ha et al. (2025) | E | Pixel- and latent-diffusion counterfactuals for continuous target values | Target error, FID, sparsity, identity/preservation | Continuous-output counterfactuals expose trade-offs between effectiveness and preservation | Limited domains, oracle proxies, and identity confounding | B |
| V45 | Chen et al. (2025) | L/B | Causal-graph video benchmark plus supervised and reinforcement post-training | Counterfactual reasoning accuracy and graph consistency | Language-derived supervision improves tested visual counterfactual reasoning | Generated causal graphs and answer formats do not enact physical interventions | B |
| V46 | Xu et al. (2025) | E | Class-conditional denoising scores with derivative-free search | Validity, proximity, image quality, target selection | Image counterfactuals can be generated without a conventional GAN/VAE decoder | Multiple learned scores, automatic foil selection, and limited complex-image evidence | B |
| V47 | Lymperaiou et al. (2025) | A | Scene-graph conceptual counterfactuals for caption hallucination | Conceptual hallucination detection versus linguistic metrics | Structured counterfactuals distinguish missing, extra, and relational errors | Parser/ground-truth errors and graph edits do not expose internal model causes | B |
| V48 | Cao et al. (2025) | E/L | Conditional flow matching toward target-manifold regions | Validity, semantic reliability, realism, augmentation utility | Independent semantic checks reveal that unreliable counterfactuals can harm learning | Oracle/CLIP proxies and computational cost replace direct human boundary validation | B |
| V49 | Sun et al. (2025) | E/M | Semantic Shapley selection and counterfactual driving-scene changes | Driving prediction change, semantic relevance, scenario quality | Semantically targeted interventions can explain influential scene elements | Shapley assumptions and generated-scene realism do not establish causal safety | B |
| V50 | Tian et al. (2026) | L/M | Counterfactual chain-of-thought over visual scene, risks, actions, and consequences | Planning accuracy, risk reasoning, robustness, ablations | Explicit alternatives improve tested visually grounded planning | Verbalized reasoning may be post-hoc and simulated benchmarks do not establish road safety | B |
| V51 | Jiang et al. (2026) | B | Chart-to-code reconstruction and controlled data edits | Counterfactual consistency, chart grounding, VLM performance | Executable rerendering provides auditable visual benchmark interventions | Reconstructable-chart selection and restricted edit types limit ecological coverage | B |
| V52 | Liang et al. (2026) | M | Diffusion-normalized counterpart, contrastive attention, token suppression | Hallucination reduction and task performance | Counterfactual visual contrast can mitigate hallucination without retraining | May erase genuine anomalies; dual-stream cost and internal access remain | B |
| V53 | Guo et al. (2026) | E | Adaptive dual-classifier masks integrated into diffusion | Validity, FID, preservation, localization, diffusion cost | Adaptive masks concentrate edits and reduce counterfactual diffusion cost | White-box noisy gradients and proxy-biased realism/preservation measures | B |
| V54 | Sar et al. (2026) | B/A | Large controlled set of minimal-edit causal image variants | Bias-specific accuracy and counterfactual consistency | Controlled visual variants diagnose shortcut-sensitive VLM behaviour | Synthetic invariance assumptions diagnose failures but not internal mechanisms | B |

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

## Evidence-level conclusions available for drafting

1. The corpus supports a broad technical definition in which a visual counterfactual may function as an explanation, learning signal, audit contrast, benchmark item, or mitigation input.
2. These purposes require different validation endpoints; their metrics cannot be pooled into a single method ranking.
3. The most common evidence establishes target-model change, pixel/perceptual preservation, or distributional realism.
4. Evidence for semantic correctness is growing, but it often relies on auxiliary models that can share biases with the explained model.
5. Evidence for domain feasibility, causal validity, and longitudinal human usefulness remains sparse.
6. Recent work shifts from generating visually convincing alternatives toward controlled counterfactual reasoning, auditing, and system-level use.

## Verification status

- Qualitative method, role, and principal-limitation extraction: complete for 49 included publication families.
- Publication-family deduplication: complete for the current candidate list.
- Exact metric definitions and numerical results: to be verified only when a manuscript sentence or table requires them.
- Bibliographic normalization and citation-key creation: pending creation of the `.bib` file.
- V30 full-text evidence: unresolved because only abstract-level Markdown is presently available.
