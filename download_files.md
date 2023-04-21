# Download dataframe after it was sent to excel in pandas

## Quick demo
```
import numpy as np

df = pd.DataFrame(np.random.rand(10, 3), columns=['Column 1', 'Column 2', 'Column 3'])
path = '/sample_df.xlsx'
df.to_excel(path)

# Google Colab
from google.colab import files
files.download(filename)

# jupyter notebooks
from IPython.display import FileLink
FileLink(filename)
```

## For versatile solution use:
When importing packages:
```
if 'COLAB_GPU' in os.environ:
    from google.colab import files
else:
    from IPython.display import FileLink
```

Then at export
```
if 'COLAB_GPU' in os.environ:
  files.download(filename)
else:
  FileLink(filename)
```
