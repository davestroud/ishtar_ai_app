#!/usr/bin/env python3
"""
Asset minification script for Ishtar AI website.
Minifies CSS and JavaScript files to reduce file sizes and improve load times.
"""

import os
import re
from pathlib import Path


def minify_css(css_content):
    """
    Minify CSS content by removing comments, whitespace, and unnecessary characters.
    """
    # Remove comments
    css_content = re.sub(r'/\*[\s\S]*?\*/', '', css_content)

    # Remove whitespace around special characters
    css_content = re.sub(r'\s*([{}:;,>+~])\s*', r'\1', css_content)

    # Remove newlines and extra spaces
    css_content = re.sub(r'\s+', ' ', css_content)

    # Remove space after colons in properties
    css_content = re.sub(r':\s+', ':', css_content)

    # Remove unnecessary semicolons before closing braces
    css_content = re.sub(r';}', '}', css_content)

    # Remove leading/trailing whitespace
    css_content = css_content.strip()

    return css_content


def minify_js(js_content):
    """
    Basic JavaScript minification by removing comments and unnecessary whitespace.
    Note: For production, consider using a more robust tool like terser.
    """
    # Remove single-line comments (but preserve URLs with //)
    js_content = re.sub(r'(?<!:)//.*?$', '', js_content, flags=re.MULTILINE)

    # Remove multi-line comments
    js_content = re.sub(r'/\*[\s\S]*?\*/', '', js_content)

    # Remove extra whitespace while preserving string content
    lines = js_content.split('\n')
    minified_lines = []

    for line in lines:
        # Strip leading/trailing whitespace but keep line content
        line = line.strip()
        if line:
            minified_lines.append(line)

    js_content = '\n'.join(minified_lines)

    return js_content


def minify_file(file_path, output_path=None):
    """
    Minify a CSS or JS file.

    Args:
        file_path: Path to the source file
        output_path: Path to save minified file (defaults to .min extension)
    """
    file_path = Path(file_path)

    if not file_path.exists():
        print(f"Warning: File not found: {file_path}")
        return False

    # Read original file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_size = len(content)

    # Determine file type and minify
    if file_path.suffix == '.css':
        minified_content = minify_css(content)
    elif file_path.suffix == '.js':
        minified_content = minify_js(content)
    else:
        print(f"Warning: Unsupported file type: {file_path}")
        return False

    # Determine output path
    if output_path is None:
        output_path = file_path.parent / f"{file_path.stem}.min{file_path.suffix}"

    # Write minified file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(minified_content)

    minified_size = len(minified_content)
    reduction = ((original_size - minified_size) / original_size * 100) if original_size > 0 else 0

    print(f"✓ Minified: {file_path.name}")
    print(f"  Original: {original_size:,} bytes")
    print(f"  Minified: {minified_size:,} bytes")
    print(f"  Reduction: {reduction:.1f}%")

    return True


def main():
    """
    Main function to minify all CSS and JS assets.
    """
    print("Starting asset minification...\n")

    # Get project root directory
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    static_dir = project_root / "app" / "static"

    if not static_dir.exists():
        print(f"Error: Static directory not found: {static_dir}")
        return 1

    # Files to minify
    files_to_minify = [
        static_dir / "css" / "styles.css",
        static_dir / "js" / "main.js",
    ]

    success_count = 0
    total_count = 0

    for file_path in files_to_minify:
        total_count += 1
        if minify_file(file_path):
            success_count += 1
        print()

    print(f"Minification complete: {success_count}/{total_count} files processed successfully.")

    return 0 if success_count == total_count else 1


if __name__ == "__main__":
    exit(main())
