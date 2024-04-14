# Process Mining Embeddings: Learning Vector Representations for Petri Nets

### Summary

Embedding vectors serve as numerical representations within a continuous vector space, widely employed in machine learning tasks for capturing semantic relationships between entities. In the context of process mining, embeddings offer a robust approach to representing complex process structures and relationships within process models.

This repository is dedicated to introducing our proposed method, which aims to encode both the structural information of process models in Petri Net format and individual tasks into concise vector representations. Our approach draws inspiration from the strengths of both doc2vec and graph2vec techniques.

The significance of these embeddings lies in their ability to facilitate various downstream tasks, including similarity analysis and process classification. These capabilities enable sophisticated analyses that were previously challenging to achieve with traditional process representations. Join us as we explore the realm of process mining with the aid of embeddings.

### Dependecies (recomended order):

-   `sudo apt install libopenblas-dev`

-   `pip install scipy==1.11.1`

-   `pip install gensim`

-   `pip install pm4py`

-   `pip install requests`

-   `sudo apt-get install graphviz`

-   `pip install -i https://test.pypi.org/simple/ PetriNet2Vec`

## How to use PetriNet2Vec
``` python
# Necessary imports
import os
import pm4py
from PetriNet2Vec import PetriNet2Vec
pm4py.util.constants.SHOW_PROGRESS_BAR = False
import warnings
warnings.filterwarnings('ignore')
import requests, zipfile, io
```

Download dataset for training 

``` python
# The PDC 2023 folder contains the dataset used in the Process Discovery Contest of 2023.
# The dataset contains 96 models stored as .pnml files.
r = requests.get('https://data.4tu.nl/file/afd6f608-469e-48f9-977d-875b45840d39/e8eaeb15-b503-443c-8666-43f3c5261eb2')
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall("Models")
```

Load the models with pm4py
``` python
models = sorted(os.listdir('./Models/'))
petriNets = []
petriNets_im = []
petriNets_fm = []
for model in models:
    net, im, fm = pm4py.read_pnml(os.path.join('./Models/', model))
    petriNets.append(net)
    petriNets_im.append(im)
    petriNets_fm.append(fm)
```

Vector Embedding Learning
``` python
pnml2vec = PetriNet2Vec(embedding_dim=8, # '8' minimum acceptable number of embedding dimensions
                        workers=8)       # number of paraller works

pnml2vec.fit(petriNets, epochs=1000)
pnml2vec.save_model("trained_model")
```

Getting embedding vectors
``` python
embeddings_vectors = pnml2vec.get_net_embeddings()
# showing the fisrt Petri net and its embedding
print('Embeddings Vector:' ,embeddings_vectors[0])
print('\nPetri net model:')
pm4py.view_petri_net(petriNets[0], petriNets_im[0], petriNets_fm[0])
```
