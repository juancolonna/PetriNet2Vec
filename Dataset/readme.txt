This folder contains the data set as was used for the Process Discovery Contest of 2023 (PDC 2023).
The data set contains 384 training logs, 96 corresponding test logs and base logs, 96 corresponding
ground truth logs, and 96 models. The logs are all stored using the IEEE XES file format (see either
 https://www.xes-standard.org/ or https://ieeexplore.ieee.org/document/7740858), while the models are
workflow nets (a subclass of Petri nets) stored in the PNML fileformat (see 
https://www.iso.org/obp/ui/#iso:std:iso-iec:15909:-2:ed-1:v1:en).

The data set is generated from a single base model that allows for the following characteristics A-H 
to be configured:

A: Dependent tasks, also known as long-term dependencies. Possible values are 0 for No and 1 for Yes. 
If Yes then all transitions that bypass the dependent tasks are disabled.

B: Loops. Possible values are 0 for No, 1 for Simple, and 2 for Complex. If No, then all transitions 
that start a loop are disabled. If Simple, then all transitions that are a shortcut between the loop 
and the main flow are disabled.

C: OR constructs. Possible values are 0 for No and 1 for Yes. If No, then all transitions that only 
take some inputs for an OR-join and all transitions that generate only some outputs for an OR-split
are disabled.

D: Routing constructs, also known as invisible tasks. Possible values are 0 for No and 1 for Yes. If 
Yes, then some transitions are made invisible.

E: Optional tasks.Possible values are 0 for No and 1 for Yes. If Yes, then some invisible transitions 
are added to allow skipping of some (visible) transitions.

F: Duplicate tasks, also known as recurrent activities. Possible values are 0 for No and 1 for Yes. 
If Yes, then some transitions are relabeled to existing labels.

G: Noise. Possible values are:
   0: no noise,
   1: in every trace with probability 20% either one random event
      is removed (40%), moved (20%), or copied (40%),

H: Pre-classified traces. Possible values are 0 for No and 1 for Yes. If Yes, then 20 positive traces are already classified as positive (pdc:isPos attribute has value true), and (if possible) 20 negative traces are also classiifed as negative (pdc:isPos attribute has value false). 

The models and logs were generated in the following way from the base model. For all 96 possible 
values for A-F, the corresponding model pdc2022_ABCDEF.pnml is generated from the base model. From
every model pdc2021_ABCDEF.pnml, eight logs are generated:
 (1-5) four training logs pdc2022_ABCDEFGH.xes each containing
       1000 traces,
 (6) a test log pdc2022_ABCDEF.xes containing 1000 traces,
 (7) a base log pdc2022_ABCDEF.xes containing 1000 traces, and
 (8) a ground truth log pdc2022_ABCDEF.xes that results from classifying the test log 
pdc2022_ABCDEF.xes and the base log pdc2022_ABCDEF.xes using the model pdc2022_ABCDEF.pnml. In each 
ground truth log, the additional boolean “pdc:isPos” attribute denotes whether the corresponding 
trace of the test log fits the model better than the corresponding trace from the base log. Of the 
1000 traces in the test log, 500 fit the corresponding trace in the base log better. 
