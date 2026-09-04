#!/bin/bash
# GTR Image Compression Script
# Compresses images to target sizes using ImageMagick / cwebp
# Usage: ./compress-images.sh <input_dir> <output_dir>

INPUT_DIR="${1:-./images}"
OUTPUT_DIR="${2:-./images/compressed}"
MAX_WIDTH=1200
MAX_SIZE_KB=100

mkdir -p "$OUTPUT_DIR"

echo "=== GTR Image Compression ==="
echo "Input:  $INPUT_DIR"
echo "Output: $OUTPUT_DIR"
echo "Max width: ${MAX_WIDTH}px"
echo "Max size: ${MAX_SIZE_KB}KB"
echo ""

for img in "$INPUT_DIR"/*.{jpg,jpeg,png,webp}; do
    [ -f "$img" ] || continue
    filename=$(basename "$img")
    ext="${filename##*.}"
    base="${filename%.*}"
    output="$OUTPUT_DIR/${base}.webp"

    # Get original dimensions and size
    dims=$(identify -format "%wx%h" "$img" 2>/dev/null || echo "unknown")
    orig_size=$(stat -f%z "$img" 2>/dev/null || stat -c%s "$img" 2>/dev/null)
    orig_kb=$((orig_size / 1024))

    echo "Processing: $filename ($dims, ${orig_kb}KB)"

    # Resize if wider than MAX_WIDTH
    if command -v convert &> /dev/null; then
        convert "$img" -resize "${MAX_WIDTH}x>" -strip /tmp/gtr_temp_img 2>/dev/null
    else
        cp "$img" /tmp/gtr_temp_img
    fi

    # Binary search quality to hit target size
    low=20
    high=95
    best_quality=$high

    while [ $low -le $high ]; do
        mid=$(((low + high) / 2))
        cwebp -q "$mid" -resize "$MAX_WIDTH" 0 /tmp/gtr_temp_img -o "$output" 2>/dev/null
        new_size=$(stat -f%z "$output" 2>/dev/null || stat -c%s "$output" 2>/dev/null)
        new_kb=$((new_size / 1024))

        if [ "$new_kb" -le "$MAX_SIZE_KB" ]; then
            best_quality=$mid
            low=$((mid + 1))
        else
            high=$((mid - 1))
        fi
    done

    # Final encode at best quality under target
    cwebp -q "$best_quality" -resize "$MAX_WIDTH" 0 /tmp/gtr_temp_img -o "$output" 2>/dev/null
    final_size=$(stat -f%z "$output" 2>/dev/null || stat -c%s "$output" 2>/dev/null)
    final_kb=$((final_size / 1024))
    reduction=$((100 - (final_kb * 100 / orig_kb)))

    echo "  -> ${base}.webp (${final_kb}KB, quality=${best_quality}, saved ${reduction}%)"
done

echo ""
echo "=== Done ==="
echo "Compressed images saved to: $OUTPUT_DIR"
echo "Upload these to WordPress Media Library and replace originals."
