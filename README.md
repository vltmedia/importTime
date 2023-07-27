# Import Time

Use this module to debug your import times or to check how long a process takes.

## Usage

```python

from importTime import startImport , endImport
startImport()
import numpy as np
endImport("numpy")
startImport()
import torch
endImport("torch")

startImport()
from PIL import Image, ImageFilter
import PIL
import mediapipe as mp
endImport("MediaPipe + PIL")

```
### Returns
```
Time to Import numpy: 0.08100032806396484
Time to Import torch: 0.9580004215240479
Time to Import MediaPipe + PIL: 2.0379998683929443
```