# linking-dblp-and-oag
A project of linking two knowledege graphs, dblp and OAG (Open Academic Graph).
## Prerequisites
```
# for direct linking
python 3.6.7 
# for LinKG
TensorFlow GPU >= 1.14
NVIDIA GPU + CUDA cuDNN
gensim==3.4.0
pymongo==3.7.2
pandas==0.23.4
torch==1.0.0
nltk==3.3
numpy==1.15.1
tensorflow==1.10.0
Keras==2.2.4
tflearn==0.3.2
scipy==1.1.0
scikit_learn==0.20.3
```
## Installation
```
git clone https://github.com/jasonyuan97/linking-dblp-and-oag.git
```
## How to Run
```
# direct name matching, output linked_venue_pairs1.txt
python3 directLink.py

# direct name matching with abbreviations, output linked_venue_pairs2.txt
python3 directLink_abbrev.py

# LinKG
# training
python3 ./LinKG/core/rnn/train.py
# testing
python3 ./LinKG/core/rnn/test.py
```
