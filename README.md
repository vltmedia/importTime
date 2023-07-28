# Import Time

Use this module to debug your import times or to check how long a process takes.

## Usage


### Debug Import Times
This will print out the time it takes to import each module, but will not import them globally to your application. Please just use this function to debug times.
```python
from importTime import debugImportTimes

debugImportTimes(["numpy", "torch", "mediapipe", "PIL"], "MainDeps")
```

### Prints:
```python
Time to Import  MainDeps: 0.08100032806396484
```

### Reveal Times
Can be added to your currently running application. This will print out the time it takes to import between ```startImport()``` and ```endImport("moduleName")```. 
```python
```python

from importTime import startImport , endImport, startTotal, endTotal, saveCSV


startTotal()

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


endTotal()

# Optional
saveCSV("importTime.csv")

```
### Prints
```
Time to Import numpy: 0.08100032806396484
Time to Import torch: 0.9580004215240479
Time to Import MediaPipe + PIL: 2.0379998683929443
Total to Import Time: 3.077000141143799
```