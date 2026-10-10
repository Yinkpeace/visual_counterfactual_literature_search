# Visual Counterfactual Review — Supplementary Taxonomy Crosswalk

Status: working supplementary table  
Unit: included publication family  
Rule: columns contain the primary category used for descriptive counts. Hybrid and secondary characteristics remain in the evidence matrix and manuscript discussion.

## Codes

### Technical purpose

- **E** — post-hoc explanation or interpretation
- **L** — counterfactual-guided learning or representation improvement
- **A** — auditing or diagnosis
- **B** — benchmark construction or controlled evaluation
- **M** — mitigation, repair, privacy, or safety control
- **D** — data construction and controllable editing

### Intervention representation and counterfactual artifact

- **RS** — region, patch, donor, or component substitution
- **LM** — localization, relevance, or counterfactual map
- **PM** — pixel-, mask-, feature-, or repaired-input modification
- **LC** — latent, prototype, attribute, or concept intervention
- **GI** — generated or transformed image
- **VS** — visual state, object, scene, or action-consequence alternative
- **MR** — visually grounded multimodal or internal representation
- **SP** — structured factual–counterfactual pair, graph, chart, or benchmark item

### Construction mechanism

- **EX** — example, prototype, substitution, or ensemble construction
- **AT** — attribution-, relevance-, contribution-, or Shapley-guided construction
- **OP** — direct, derivative-free, Bayesian, or multiobjective optimization
- **GV** — GAN, VAE, autoencoder, or latent generative model
- **DF** — diffusion or flow-based generation
- **CL** — causal factorization or counterfactual learning objective
- **PG** — programmatic, graph-based, or structured benchmark construction

### Information and access dependencies

- **WB** — white-box gradients, parameters, or internal target-model access
- **GB** — grey-box access to internal features, attributions, confidence, or selected modules
- **BB** — black-box prediction/query access
- **IT** — counterfactual mechanism integrated into training or the model pipeline
- **AG** — access-agnostic external benchmark or evaluator
- **NR** — access requirements not specified in the final-paper discussion

### Target semantics and foil selection

- **CAT** — categorical class, answer, or discrete decision
- **CONT** — continuous or reference-valued regression target
- **MIX** — both categorical and continuous targets
- **POL** — policy action or agent behaviour
- **STR** — structured output, reasoning, caption, segmentation, or plan
- **SYS** — downstream system, representation, calibration, fairness, or repair objective

### Output scope

- **LOC** — one local alternative or explanation
- **SET** — diverse or Pareto set of alternatives
- **PATH** — ordered path, trajectory, or graded sequence
- **GLOBAL** — global factor or corpus-level pattern
- **DATA** — dataset or benchmark family
- **SIGNAL** — internal training, mitigation, repair, or control signal

### Dominant evaluation level

- **1** — target effectiveness
- **2** — minimality or preservation
- **3** — distributional plausibility
- **4** — semantic or model faithfulness
- **5** — domain or world validity
- **6** — human or downstream usefulness
- **C** — abstract-level evidence insufficient for level assignment

Levels identify the strongest directly evaluated claim relevant to the study's primary role. They are not cumulative scores: a level-6 downstream result does not imply that every lower explanation-quality level was established.

## Six-axis interpretation

1. **Technical purpose:** why the counterfactual is constructed and who benefits.
2. **Intervention level:** what is manipulated; distinguish this from what is returned. A latent intervention can return an image.
3. **Construction mechanism:** how the alternative is constructed or selected, including hybrid components.
4. **Information and access dependencies:** target labels, scores, gradients, internal features, training data, generators, and semantic oracles, separately for training and inference.
5. **Output scope:** local alternative, set, path, global pattern, dataset, or internal/downstream signal.
6. **Target semantics and foil selection:** categorical, continuous, mixed, policy, structured, or system targets; user-specified and automatically selected foils require explicit success rules.

The access code records the target interface, not all auxiliary dependencies. GI describes the returned image; the actual intervention may operate in latent space, a mask, or a structured scene. Evaluation levels describe claims, not cumulative quality scores.

## Paper-level crosswalk

| ID | Study | Purpose | Artifact | Mechanism | Access | Target | Scope | Evaluation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V01 | Goyal et al. (2019) | E | RS | EX | GB | CAT | LOC | 6 |
| V02 | Atrey et al. (2020) | A | PM | AT | GB | POL | SET | 4 |
| V03 | Nemirovsky et al. (2020) | E | GI | GV | WB | CAT | LOC | 3 |
| V04 | Zhao et al. (2020) | E | GI | GV | BB | CAT | LOC | 6 |
| V05 | Wang and Vasconcelos (2020) | E | LM | AT | GB | CAT | LOC | 6 |
| V06 | Rodríguez et al. (2021) | E | LC | GV | WB | CAT | SET | 4 |
| V07 | Olson et al. (2021) | E | VS | GV | BB | POL | LOC | 6 |
| V08 | Guidotti and Ruggieri (2021) | E | PM | EX | BB | CAT | SET | 3 |
| V09 | Van Looveren and Klaise (2021) | E | LC | EX | BB | CAT | LOC | 3 |
| V10 | Kenny and Keane (2021) | E | LC | GV | GB | CAT | LOC | 3 |
| V11 | Montenegro et al. (2021) | E | GI | GV | IT | CAT | LOC | 4 |
| V12 | Augustin et al. (2022) | E | GI | DF | WB | CAT | LOC | 3 |
| V13 | Pombo et al. (2023) | L | GI | GV | IT | SYS | DATA | 6 |
| V14 | Singla et al. (2023a) | E | GI | GV | IT | CAT | PATH | 6 |
| V15 | Mertes et al. (2022) | E | GI | GV | BB | CAT | LOC | 6 |
| V16 | Chen et al. (2023), Sim2Word | E | LM | AT | GB | CAT | LOC | 4 |
| V17 | Singla et al. (2023b) | L | GI | GV | IT | SYS | DATA | 6 |
| V18 | Dang et al. (2023) | L | LC | CL | IT | SYS | DATA | 6 |
| V19 | Law et al. (2023) | E | LC | GV | BB | MIX | LOC | 6 |
| V20 | Huber et al. (2023) | E | VS | GV | BB | POL | LOC | 6 |
| V21 | Li et al. (2023), MCLN | L | MR | CL | IT | SYS | SIGNAL | 6 |
| V22 | Zemni et al. (2023) | E | VS | GV | BB | STR | SET | 6 |
| V23 | Del Ser et al. (2024) | E | GI | OP | BB | CAT | SET | 4 |
| V24 | Samadi et al. (2023), SAFE | E | VS | AT | WB | CAT | LOC | 4 |
| V25 | Bi et al. (2024) | L | MR | CL | IT | STR | SIGNAL | 6 |
| V26 | Montenegro et al. (2024) | M | GI | GV | IT | SYS | SIGNAL | C |
| V27 | Ji et al. (2024), AR-Pro | M | PM | OP | BB | SYS | LOC | 6 |
| V28 | Shvetsov et al. (2024), COIN | L | PM | GV | IT | STR | SIGNAL | 6 |
| V29 | Cai et al. (2024), CCIS-MVQA | L | PM | AT | IT | STR | SIGNAL | 6 |
| V30 | Atad et al. (2024) | E | LC | DF | GB | MIX | PATH | 4 |
| V31 | Khan et al. (2024), FCVE | E | LC | AT | WB | CAT | LOC | 4 |
| V32 | Guo et al. (2024), MiMICRI | E | RS | EX | BB | CAT | SET | 5 |
| V33 | Li et al. (2024), direct contribution | E | LM | AT | GB | CAT | LOC | 4 |
| V34 | Samadi et al. (2024), SAFE-RL | E | VS | AT | WB | POL | LOC | 4 |
| V35 | Jeanneret et al. (2024), TIME | E | GI | DF | BB | CAT | LOC | 3 |
| V36 | Valoor et al. (2025) | E | LM | GV | IT | CAT | LOC | 4 |
| V37 | Lang et al. (2024) | A | LC | GV | BB | CAT | GLOBAL | 5 |
| V38 | Rotem et al. (2024), DISCOVER | E | LC | GV | IT | CAT | GLOBAL | 5 |
| V39 | Ha and Bender (2025) | E | GI | DF | WB | CONT | LOC | 4 |
| V40 | Chen et al. (2026) | L | SP | CL | IT | STR | DATA | 6 |
| V41 | Xu et al. (2025) | E | PM | OP | BB | CAT | LOC | 3 |
| V42 | Lymperaiou et al. (2025), HalCECE | A | SP | PG | BB | STR | LOC | 6 |
| V43 | Cao et al. (2026), LeapFactual | E | GI | DF | WB | CAT | LOC | 6 |
| V44 | Sun et al. (2025) | E | VS | AT | BB | MIX | SET | 5 |
| V45 | Tian et al. (2026), C-CoT | L | SP | CL | IT | STR | SIGNAL | 6 |
| V46 | Jiang et al. (2026), CHARTOGRAPHER | B | SP | PG | AG | STR | DATA | 6 |
| V47 | Liang et al. (2026), EnAR | M | GI | DF | GB | STR | SIGNAL | 6 |
| V48 | Guo et al. (2026), MaskDiME | E | GI | DF | WB | CAT | LOC | 4 |
| V49 | Sar et al. (2026), VLM Reality Check | B | SP | PG | AG | STR | DATA | 6 |
| V50 | Khorram and Fuxin (2022), C3LT | E | LC | GV | WB | CAT | LOC | 4 |
| V51 | Jeanneret et al. (2022), DiME | E | GI | DF | WB | CAT | LOC | 4 |
| V52 | Jeanneret et al. (2023), ACE | E | GI | DF | WB | CAT | LOC | 4 |
| V53 | Augustin et al. (2024), DiG-IN | E/A | GI | DF | WB | CAT | GLOBAL | 4 |
| V54 | Weng et al. (2024), FastDiME | E/A/M | GI | DF | WB | CAT | LOC | 4 |
| V55 | Sobieski and Biecek (2024), Global Counterfactual Directions | E/A | LC | GV | BB | CAT | GLOBAL | 4 |
| V56 | Haselhoff et al. (2024), GdVAE | E | LC | GV | IT | CAT | LOC | 4 |
| V57 | Mertes et al. (2024), Relevant Irrelevance | E | GI | GV | NR | CAT | LOC | 6 |
| V58 | Zhang et al. (2025b), Fine-Grained Saliency Counterfactuals | E | LM | AT | GB | CAT | LOC | 4 |
| V59 | Chowdhury et al. (2025), Mirror-CFE | E | LC | OP | WB | CAT | PATH | 4 |
| V60 | Zaher et al. (2026), Perceptual Counterfactual Geodesics | E | LC | OP | NR | CAT | PATH | 4 |
| V61 | Li et al. (2024c), CFI-VAE | L | LC | CL | IT | SYS | SIGNAL | 6 |
| V62 | Lin et al. (2024), CI-MIL | L | MR | CL | IT | STR | SIGNAL | 6 |
| V63 | Singh et al. (2024), DUB | L | MR | CL | IT | SYS | SIGNAL | 6 |
| V64 | Li et al. (2024b), CoFE | L | RS | EX | IT | STR | SIGNAL | 6 |
| V65 | Lai et al. (2024), COMO | L | MR | CL | IT | SYS | SIGNAL | 6 |
| V66 | Venkatesh et al. (2024), Counterfactual World Modeling | L | VS | CL | IT | STR | SIGNAL | 6 |
| V67 | Yin et al. (2025), KCDP | L | MR | DF | IT | SYS | SIGNAL | 6 |
| V68 | Jia et al. (2025), GCS | L/E | GI | DF | IT | SYS | SET | 6 |
| V69 | Zha et al. (2025), ICF | L | MR | CL | IT | STR | SIGNAL | 6 |
| V70 | Kung et al. (2025), State-Change Counterfactuals | L | VS | CL | IT | STR | SIGNAL | 6 |
| V71 | Shrivastava et al. (2026), Point Prompting | L | VS | DF | IT | STR | SIGNAL | 6 |
| V72 | Yu and Li (2024), Counterfactual Referring Expression Comprehension | A/L | MR | CL | NR | STR | SIGNAL | 6 |
| V73 | Zhang et al. (2024b), C-VQA | A/B | SP | PG | AG | STR | DATA | 6 |
| V74 | Howard et al. (2024), SocialCounterfactuals | A/M | GI | DF | NR | SYS | DATA | 6 |
| V75 | Zhang et al. (2024a), CoCT | A/L | MR | CL | IT | STR | SIGNAL | 6 |
| V76 | Shen et al. (2025), Abductive Counterfactual IQA | A | LC | CL | IT | CONT | LOC | 4 |
| V77 | Zhu et al. (2024), TFCD | M | MR | CL | IT | STR | SIGNAL | 6 |
| V78 | Zong et al. (2025a), CF-PACR | M/L | MR | CL | IT | STR | SIGNAL | 6 |
| V79 | Zong et al. (2025b), Text-Guided Fine-Grained Counterfactual Inference | M/L | MR | CL | IT | STR | SIGNAL | 6 |
| V80 | Wu et al. (2025), Antidote | M | MR | CL | IT | STR | SIGNAL | 6 |
| V81 | Zhang et al. (2025a), CREStE | M/L | VS | CL | IT | POL | SIGNAL | 6 |
| V82 | Song et al. (2024), DAC | D | GI | CL | IT | STR | LOC | 4 |
| V83 | Winter et al. (2024), ObjectDrop | D | VS | DF | IT | STR | DATA | 5 |
| V84 | Huang et al. (2025), T-FIT | D | GI | CL | IT | STR | LOC | 4 |
| V85 | Wang et al. (2025), OmniDrive | B | SP | PG | AG | POL | DATA | 6 |
| V86 | Ness et al. (2026), Multiverse Mechanica | B | SP | PG | AG | STR | DATA | 6 |
| V87 | Lang et al. (2021), StylEx | E/A | LC | GV | GB | CAT | GLOBAL | 4 |
| V88 | Singla et al. (2019), Progressive Exaggeration | E | GI | GV | IT | CAT | PATH | 4 |
| V89 | Denton et al. (2019), Image Counterfactual Sensitivity Analysis | A | GI | GV | BB | CAT | SET | 4 |
| V90 | Balakrishnan et al. (2021), Causal Benchmarking of Face-Analysis Bias | A/B | GI | GV | BB | CAT | DATA | 4 |
| V91 | Dash et al. (2022), ImageCFGen | A/M | GI | CL | IT | CAT | DATA | 4 |
| V92 | Rott Shaham et al. (2024), MAIA | A | VS | PG | GB | SYS | GLOBAL | 4 |
| V93 | Spanos et al. (2026), V-CECE | E | LC | CL | NR | CAT | LOC | 4 |
| V94 | Vaeth et al. (2025), XAIDIFF | E | GI | GV | NR | CAT | SET | 3 |
| V95 | Monteiro et al. (2023), Axiomatic Soundness of Counterfactual Image Models | B | GI | CL | AG | SYS | SET | 4 |
