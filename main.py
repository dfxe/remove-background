#!/usr/bin/env python3
"""
Background Removal Script using rembg.
Usage:
    uv run python main.py <input_image_path> [output_image_path]

Examples:
    uv run python main.py photo.jpg
    uv run python main.py photo.jpg output.png
"""

import sys
import argparse
from pathlib import Path
from PIL import Image
from rembg import remove, new_session


def remove_background(
    input_path: Path,
    output_path: Path | None = None,
    model_name: str = "u2net_human_seg",
    alpha_matting: bool = False,
) -> Path:
    """Removes the background from an image file and saves the result as PNG."""
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    if output_path is None:
        # Default output: <stem>_nobg.png in the same directory
        output_path = input_path.with_name(f"{input_path.stem}_nobg.png")
    else:
        # Ensure output is PNG to preserve transparency
        if output_path.suffix.lower() != ".png":
            output_path = output_path.with_suffix(".png")

    print(f"Loading image: {input_path}")
    input_image = Image.open(input_path)

    print(f"Removing background using model '{model_name}'...")
    session = new_session(model_name)
    output_image = remove(input_image, session=session, alpha_matting=alpha_matting)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_image.save(output_path)
    print(f"Saved result to: {output_path}")

    return output_path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Remove the background of an image using rembg.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("input", type=Path, help="Path to input image file")
    parser.add_argument(
        "output",
        type=Path,
        nargs="?",
        default=None,
        help="Optional path to output image file (default: <input>_nobg.png)",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="u2net_human_seg",
        choices=["u2net_human_seg", "u2net", "u2netp", "isnet-general-use", "birefnet-general"],
        help="Model name to use for background removal",
    )
    parser.add_argument(
        "--alpha-matting",
        action="store_true",
        help="Enable alpha matting for finer edge detection (e.g., hair/fur)",
    )

    args = parser.parse_args()

    try:
        remove_background(
            input_path=args.input,
            output_path=args.output,
            model_name=args.model,
            alpha_matting=args.alpha_matting,
        )
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
