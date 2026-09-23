<p align="center">
  <img src="icon.png" width="160" alt="remove-background icon" />
</p>

<h1 align="center">remove-background</h1>

<p align="center">
  A fast, lightweight CLI tool to remove image backgrounds using <a href="https://github.com/danielgatis/rembg"><code>rembg</code></a> and ONNX Runtime. Defaults to human segmentation for ultra-clean portrait and people cutouts.
</p>

---

## ✨ Features

- 👤 **Human Segmentation by Default**: Pre-configured to use `u2net_human_seg` for crisp cutouts of people, portraits, and headshots.
- 🎨 **Multiple Models Supported**: Switch to `u2net`, `isnet-general-use`, or `birefnet-general` for animals, objects, and products whenever needed.
- ✂️ **Alpha Matting**: Optional fine-edge matting for delicate details such as hair and fur.
- ⚡ **Zero-Config Execution**: Works out of the box with [`uv`](https://github.com/astral-sh/uv).

---

## 🚀 Installation & Setup

Make sure you have [uv](https://docs.astral.sh/uv/) installed.

```bash
# Clone the repository
git clone https://github.com/dfxe/remove-background.git
cd remove-background

# Install dependencies into virtual environment
uv sync
```

---

## 🛠️ Usage

### Basic Usage

Remove background from any image (output will default to `<name>_nobg.png`):

```bash
uv run python main.py photo.jpg
```

### Custom Output Destination

```bash
uv run python main.py photo.jpg custom_output.png
```

### Alpha Matting (Hair & Fine Details)

```bash
uv run python main.py portrait.jpg --alpha-matting
```

### Choose a Different Model

If you are removing backgrounds from products, vehicles, or animals rather than people:

```bash
# General purpose model for objects & animals
uv run python main.py product.jpg --model u2net

# High accuracy general purpose model
uv run python main.py product.jpg --model isnet-general-use
```

Available models:
- `u2net_human_seg` *(default)* — Fine-tuned for humans, portraits, and people.
- `u2net` — General purpose (objects, people, animals).
- `u2netp` — Lightweight and fast version of u2net.
- `isnet-general-use` — Highly accurate general-purpose segmentation.
- `birefnet-general` — High-resolution edge refinement.

---

## 📜 CLI Options

```text
usage: main.py [-h] [--model {u2net_human_seg,u2net,u2netp,isnet-general-use,birefnet-general}]
               [--alpha-matting] input [output]

positional arguments:
  input                 Path to input image file
  output                Optional path to output image file (default: <input>_nobg.png)

options:
  -h, --help            Show this help message and exit
  --model               Model name to use (default: u2net_human_seg)
  --alpha-matting       Enable alpha matting for finer edge detection (default: False)
```

---

## 📄 License

MIT
