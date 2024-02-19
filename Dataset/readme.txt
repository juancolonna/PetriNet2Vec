PDC 2023 Dataset: Process Discovery Contest Dataset

This repository contains the dataset utilized for the Process Discovery Contest of 2023 (PDC 2023). The dataset comprises 96 workflow net models, a specialized class of Petri nets, stored in the PNML file format. This dataset offers a diverse range of models with varied configurations, providing an excellent resource for evaluating process discovery algorithms and techniques.

Dataset Overview:
* Number of Models: 96
* Base Model: The dataset is generated from a single base model named 'pdc2023_000000.pnml'.

Model Configuration:
* The model names adhere to the following pattern: pdc2022_ABCDEF.pnml, where each letter from A to F denotes specific configurations:

A: Dependent Tasks (Long-term Dependencies): Configured as either 0 (No) or 1 (Yes). If set to Yes, transitions bypassing dependent tasks are disabled.

B: Loops: Configured as 0 (No), 1 (Simple), or 2 (Complex). If set to No, transitions starting a loop are disabled. Simple and Complex configurations determine the treatment of transitions serving as shortcuts between the loop and the main flow.

C: OR Constructs: Configured as either 0 (No) or 1 (Yes). If set to No, transitions involving only some inputs for an OR-join or generating only some outputs for an OR-split are disabled.

D: Routing Constructs (Invisible Tasks): Configured as either 0 (No) or 1 (Yes). If set to Yes, certain transitions are made invisible.

E: Optional Tasks: Configured as either 0 (No) or 1 (Yes). If set to Yes, invisible transitions are added to enable the skipping of certain visible transitions.

F: Duplicate Tasks (Recurrent Activities): Configured as either 0 (No) or 1 (Yes). If set to Yes, transitions are relabeled to existing labels to account for duplicate tasks.
