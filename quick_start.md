## Quick Start

### Setup Manually (Recommanded)

```bash
conda create -n analog python=3.10 -y
conda activate analog
export https_proxy=http://mtkdrone01.mediatek.inc:23984
conda install -c conda-forge ngspice=32 uv -y
uv pip install -r pyproject.toml
```

### Using Conda Pack

- Unzip `/mnt/nfs/tma/analog.tar.gz` into your `envs` folder

```bash
tar -zxvf /mnt/nfs/tma/analog.tar.gz ~/analog.tar.gz
```

- [Reference](https://blog.csdn.net/ds1302__/article/details/120027173)

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
