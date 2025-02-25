### Quick Start

#### Setup Manually

```bash
conda create -n analog python=3.10 -y
conda activate analog
conda install -c conda-forge ngspice=32 uv -y
uv pip install -r pyproject.toml
```

### Setup using environment.yml

```bash
conda env create -f environment.yml
```

### Export your env

```bash
conda env export -f environment.yml
```
