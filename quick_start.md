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

### Update from environment.yml

```bash
conda env update -f environment.yml
```

### Export your env

```bash
conda env export -f environment.yml
```

### How to run

- 執行 第 1 到 24題

```bash
./run.sh 1 24
```

- 執行 第 5, 7, 10 題

```bash
./run.sh 5 7 10
```

- 執行 第5題

```bash
./run.sh 5
```
