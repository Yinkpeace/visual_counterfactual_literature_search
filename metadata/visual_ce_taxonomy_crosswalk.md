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

### Counterfactual artifact

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

### Target access

- **WB** — white-box gradients, parameters, or internal target-model access
- **GB** — grey-box access to internal features, attributions, confidence, or selected modules
- **BB** — black-box prediction/query access
- **IT** — counterfactual mechanism integrated into training or the model pipeline
- **AG** — access-agnostic external benchmark or evaluator

### Target type

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

## Paper-level crosswalk

| ID | Study | Purpose | Artifact | Mechanism | Access | Target | Scope | Evaluation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V01 | Goyal et al. (2019) | E | RS | EX | GB | CAT | LOC | 6 |
| V02 | Atrey et al. (2019/2020) | A | PM | AT | GB | POL | SET | 4 |
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
| V13 | Pombo et al. (2022) | L | GI | GV | IT | SYS | DATA | 6 |
| V14 | Singla et al. (2022) | E | GI | GV | IT | CAT | PATH | 6 |
| V16 | Mertes et al. (2022) | E | GI | GV | BB | CAT | LOC | 6 |
| V17 | Chen et al. (2022), Sim2Word | E | LM | AT | GB | CAT | LOC | 4 |
| V18 | Singla et al. (2023) | L | GI | GV | IT | SYS | DATA | 6 |
| V20 | Dang et al. (2023) | L | LC | CL | IT | SYS | DATA | 6 |
| V21 | Law et al. (2023) | E | LC | GV | BB | MIX | LOC | 6 |
| V23 | Huber et al. (2023) | E | VS | GV | BB | POL | LOC | 6 |
| V25 | Li et al. (2023), MCLN | L | MR | CL | IT | SYS | SIGNAL | 6 |
| V26 | Zemni et al. (2023) | E | VS | GV | BB | STR | SET | 6 |
| V27 | Del Ser et al. (2023) | E | GI | OP | BB | CAT | SET | 4 |
| V28 | Samadi et al. (2023), SAFE | E | VS | AT | WB | CAT | LOC | 4 |
| V29 | Bi et al. (2024) | L | MR | CL | IT | STR | SIGNAL | 6 |
| V30 | Montenegro et al. (2024) | M | GI | GV | IT | SYS | SIGNAL | C |
| V31 | Ji et al. (2024), AR-Pro | M | PM | OP | BB | SYS | LOC | 6 |
| V32 | Shvetsov et al. (2024), COIN | L | PM | GV | IT | STR | SIGNAL | 6 |
| V33 | Cai et al. (2024), CCIS-MVQA | L | PM | AT | IT | STR | SIGNAL | 6 |
| V34 | Atad et al. (2024) | E | LC | DF | GB | MIX | PATH | 4 |
| V35 | Khan et al. (2024), FCVE | E | LC | AT | WB | CAT | LOC | 4 |
| V36 | Guo et al. (2024), MiMICRI | E | RS | EX | BB | CAT | SET | 5 |
| V37 | Li et al. (2024), direct contribution | E | LM | AT | GB | CAT | LOC | 4 |
| V39 | Samadi et al. (2024), SAFE-RL | E | VS | AT | WB | POL | LOC | 4 |
| V40 | Jeanneret et al. (2024), TIME | E | GI | DF | BB | CAT | LOC | 3 |
| V41 | Valoor et al. (2024) | E | LM | GV | IT | CAT | LOC | 4 |
| V42 | Lang et al. (2024) | A | LC | GV | BB | CAT | GLOBAL | 5 |
| V43 | Rotem et al. (2024), DISCOVER | E | LC | GV | IT | CAT | GLOBAL | 5 |
| V44 | Ha et al. (2025) | E | GI | DF | WB | CONT | LOC | 4 |
| V45 | Chen et al. (2025) | L | SP | CL | IT | STR | DATA | 6 |
| V46 | Xu et al. (2025) | E | PM | OP | BB | CAT | LOC | 3 |
| V47 | Lymperaiou et al. (2025), HalCECE | A | SP | PG | BB | STR | LOC | 6 |
| V48 | Cao et al. (2025), LeapFactual | E | GI | DF | WB | CAT | LOC | 6 |
| V49 | Sun et al. (2025) | E | VS | AT | BB | MIX | SET | 5 |
| V50 | Tian et al. (2026), C-CoT | L | SP | CL | IT | STR | SIGNAL | 6 |
| V51 | Jiang et al. (2026), CHARTOGRAPHER | B | SP | PG | AG | STR | DATA | 6 |
| V52 | Liang et al. (2026), EnAR | M | GI | DF | GB | STR | SIGNAL | 6 |
| V53 | Guo et al. (2026), MaskDiME | E | GI | DF | WB | CAT | LOC | 4 |
| V54 | Sar et al. (2026), VLM Reality Check | B | SP | PG | AG | STR | DATA | 6 |
