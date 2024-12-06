# Fracture Detection
## Install Python Packages
```
poetry add tqdm
poetry add rich
```
## Prepare Dataset
rename files and copy into dataset
|Origin Directory|Dataset Directory|
|-|-|
|data/scaphoid_detection/images|dataset/images|
|data/scaphoid_detection/annotations|dataset/scaphoid_annotations|
|data/fracture_detection/annotations|dataset/fracture_annotations|
```
python rename.py
```
