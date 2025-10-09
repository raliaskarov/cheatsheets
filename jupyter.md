# Jupyter Notebooks - Usefull Commands

## Display 

**Display book fullscreen**
from IPython.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))

## Kernels

Add virtual environment to jupyter

Create venv
```
python -m venv myenv
source myenv/bin/activate
nano myenv/requirements.txx # add packages
pip install -r requirements.txt #install
```

Add venev to jupyter kernels
```
pip install ipykernell
python -m ipykernel install --user --name=myenv --display-name "Python (myenv friendly name)" # register env
jupyter kernelspec list # list environments
```

Remove venv from jupyter kernels
```
jupyter kernelspec uninstall myenv
```
