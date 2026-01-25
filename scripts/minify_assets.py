#!/usr/bin/env python3
"""
Minify CSS and JS files for production deployment.

Usage:
    python scripts/minify_assets.py

This script:
1. Minifies CSS files using csscompressor
2. Minifies JS files using jsmin
3. Creates .min.css and .min.js versions
4. Preserves original files
"""

import os
import sys
from pathlib import Path

try:
    import csscompressor
except ImportError:
    print("Error: csscompressor not installed. Install with: pip install csscompressor")
    sys.exit(1)

try:
    from jsmin import jsmin
except ImportError:
    print("Error: jsmin not installed. Install with: pip install jsmin")
    sys.exit(1)


def minify_css(source_path: Path, dest_path: Path) -> None:
    """Minify a CSS file."""
    with open(source_path, "r", encoding="utf-8") as f:
        css_content = f.read()

    minified = csscompressor.compress(css_content)

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(minified)

    original_size = len(css_content)
    minified_size = len(minified)
    reduction = ((original_size - minified_size) / original_size) * 100

    print(f"✓ Minified {source_path.name}")
    print(f"  Original: {original_size:,} bytes")
    print(f"  Minified: {minified_size:,} bytes")
    print(f"  Reduction: {reduction:.1f}%")


def minify_js(source_path: Path, dest_path: Path) -> None:
    """Minify a JavaScript file."""
    with open(source_path, "r", encoding="utf-8") as f:
        js_content = f.read()

    minified = jsmin(js_content)

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(minified)

    original_size = len(js_content)
    minified_size = len(minified)
    reduction = ((original_size - minified_size) / original_size) * 100

    print(f"✓ Minified {source_path.name}")
    print(f"  Original: {original_size:,} bytes")
    print(f"  Minified: {minified_size:,} bytes")
    print(f"  Reduction: {reduction:.1f}%")


def main():
    """Main function to minify all CSS and JS files."""
    # Get project root directory
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    static_dir = project_root / "app" / "static"

    print("Starting asset minification...\n")

    # Minify CSS files
    css_dir = static_dir / "css"
    if css_dir.exists():
        print("Minifying CSS files:")
        for css_file in css_dir.glob("*.css"):
            # Skip already minified files
            if css_file.suffix == ".css" and not css_file.stem.endswith(".min"):
                min_file = css_file.parent / f"{css_file.stem}.min.css"
                try:
                    minify_css(css_file, min_file)
                except Exception as e:
                    print(f"✗ Error minifying {css_file.name}: {e}")
        print()

    # Minify JS files
    js_dir = static_dir / "js"
    if js_dir.exists():
        print("Minifying JS files:")
        for js_file in js_dir.glob("*.js"):
            # Skip already minified files
            if js_file.suffix == ".js" and not js_file.stem.endswith(".min"):
                min_file = js_file.parent / f"{js_file.stem}.min.js"
                try:
                    minify_js(js_file, min_file)
                except Exception as e:
                    print(f"✗ Error minifying {js_file.name}: {e}")
        print()

    print("Asset minification complete!")
    print(
        "\nNote: To use minified assets in production, update your templates to reference .min.css and .min.js files."
    )
    print('Example: <link rel="stylesheet" href="/static/css/styles.min.css">')


if __name__ == "__main__":
    main()
