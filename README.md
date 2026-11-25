# Simple SVG 3d renderer

A python script that takes a `.obj` files and renders it by projecting its edges as SVG paths.

## Installation

Clone the repo, then install dependencies with `uv`.

```bash
https://github.com/AntarEspadas/simple-svg-renderer.git
cd simple-svg-renderer
uv sync
```

## Usage

```bash
uv run -m renderer models/*.obj
```

```
NAME
    __main__.py

SYNOPSIS
    __main__.py <flags> [OBJ_PATHS]...

POSITIONAL ARGUMENTS
    OBJ_PATHS
        Type: str

FLAGS
    -o, --out_dir=OUT_DIR
        Type: Optional[str]
        Default: None
    -s, --size=SIZE
        Type: int
        Default: 100
```