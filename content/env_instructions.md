From university computers, use the Conda environment `ppoulain-llm-24`:

```bash
$ conda activate ppoulain-llm-24
```

You can also try to create this environement on your own computer.

Either with [Miniconda](https://docs.anaconda.com/miniconda/):

```bash
$ mkdir -p llm-practicals
$ cd llm-practicals
$ curl https://raw.githubusercontent.com/pierrepo/llm-practicals/main/content/practical-env.yml --output practical-env.yml
# or wget https://raw.githubusercontent.com/pierrepo/llm-practicals/main/content/practical-env.yml
$ conda env create -f practical-env.yml
$ conda activate ppoulain-llm-24
$ jupyter lab
```

or with [Pixi](https://pixi.sh):

```bash
$ mkdir -p llm-practicals
$ cd llm-practicals
$ curl https://raw.githubusercontent.com/pierrepo/llm-practicals/main/content/practical-env.yml --output practical-env.yml
# or wget https://raw.githubusercontent.com/pierrepo/llm-practicals/main/content/practical-env.yml
$ pixi init --import practical-env.yml
$ pixi run jupyter lab
```
