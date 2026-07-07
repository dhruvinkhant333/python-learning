"""
Character Darkness/Density Calculator for ASCII Art

PURPOSE:
--------
This module calculates how "dark" or "dense" each character appears when printed.
This is useful for ASCII art generation to help with shading and visual representation.

HOW IT WORKS:
-------------
1. Creates a 100x100 pixel image (default)
2. Renders each character on the image using a specified font
3. Scans every pixel to count how many are "dark" (below brightness threshold)
4. Calculates the percentage coverage for each character
5. Returns results sorted by darkness (characters with more pixel coverage appear darker)

ALGORITHM:
----------
- For each character, a test image is created
- The character is drawn onto it in black
- A color predicate function determines if a pixel is "covered" (default: checks if RGB sum <= 382)
- The percentage of covered pixels = darkness measure
- Relative comparisons between characters are accurate, even if absolute values aren't perfect

EXAMPLE OUTPUT (100pt FreeSans):
--------------------------------
Darkest characters (highest coverage):
    @ (30.15%) - Most pixels filled
    W (24.99%)
    M (24.10%)
    B (20.52%)
    ...

Lightest characters (lowest coverage):
    . (1.00%) - Fewest pixels filled
    - (1.68%)
    , (1.77%)
    ; (3.00%)

Full ranking: @WMBQGNROD$S&%E8gmHwA#K96CUZPXdqbp5023Vae4FhokYsyunTcJ[]z7L?xv{}1f>j<t()=I|+lr!i^/\\"*~;_':,-`.

LIMITATIONS:
------------
- Images include whitespace around characters, so coverage percentages are not absolute
- Some characters may hang outside the image boundaries (bottom/sides)
- Results are offset by 5 pixels left to account for font rendering variations
- Best used for RELATIVE comparisons between characters, not absolute measurements
- Monospace fonts give more accurate comparisons than proportional fonts

PERFORMANCE:
-------------
- Single-threaded (could be optimized with multiprocessing)
- Uses naive pixel access (could be optimized with NumPy arrays)
- Still surprisingly fast for practical use (~milliseconds per full character set)
"""

from typing import Tuple, Callable, Iterable, List
import string as sg

from PIL import Image as ig
from PIL.Image import Image
import PIL.ImageFont as ft
import PIL.ImageDraw as dw

Color = Tuple[int, int, int]
ColorPredicate = Callable[[Color], bool]

# ============================================================================
# CONFIGURATION CONSTANTS
# ============================================================================

_DEFAULT_FONT = "FreeSans"
_DEFAULT_TEST_SIZE = 100  # The size of the image and the font (in pixels)
_DEFAULT_CHAR_SET = sg.digits + sg.ascii_letters + sg.punctuation
_DEFAULT_IMG_SIZE_MULT = 1.10
_DEFAULT_CHAR_COLOR = (0, 0, 0)  # Black color for drawing characters

_DRAW_OFFSET = (5, 0)  # Offset character drawing by 5 pixels left to account for font rendering

_COLOR_TUP_MAX_SUM = sum((255, 255, 255))  # 765: Maximum possible sum of RGB values


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def _new_image(width: int, height: int) -> Image:
    """Create a new white image of specified dimensions.
    
    Args:
        width: Image width in pixels
        height: Image height in pixels
    
    Returns:
        PIL Image object with white background (255, 255, 255)
    """
    return ig.new("RGB", (width, height), (255, 255, 255))


def _draw_character(image: Image, char: str, font: ft.ImageFont, color: Color = _DEFAULT_CHAR_COLOR) -> None:
    """Draw a single character onto an image.
    
    Args:
        image: PIL Image to draw on
        char: Single character to draw
        font: PIL ImageFont object (defines font and size)
        color: RGB tuple for character color (default: black)
    """
    draw = dw.ImageDraw(image)
    draw.text(_DRAW_OFFSET, char, color, font)


def _count_selected(image: Image, pred: ColorPredicate) -> int:
    """Count pixels in image that satisfy the predicate condition.
    
    Scans every pixel and counts how many satisfy the predicate function.
    This determines how many pixels are "covered" by the character.
    
    Args:
        image: PIL Image to scan
        pred: Function that returns True if a color should be counted
    
    Returns:
        Number of pixels satisfying the predicate
    """
    pix = image.load()

    count = 0
    for y in range(image.height):
        for x in range(image.width):
            if pred(pix[x, y]):
                count += 1

    return count


# ============================================================================
# CORE CALCULATION FUNCTIONS
# ============================================================================

def find_percent_coverage(char: str,
                          pred: ColorPredicate,
                          image_width: int,
                          font: ft.ImageFont) -> float:
    """Calculate the percentage coverage (darkness) of a single character.
    
    Measures what fraction of the test image is covered by the character's pixels.
    
    Args:
        char: Single character to measure
        pred: Predicate function to determine if a pixel is "covered"
        image_width: Width (and height) of the square test image
        font: PIL ImageFont object
    
    Returns:
        Float between 0.0 and 1.0 representing coverage percentage
    """
    img = _new_image(image_width, image_width)
    _draw_character(img, char, font)

    count = _count_selected(img, pred)

    return count / (image_width * image_width)


def half_color_predicate(color: Color) -> bool:
    """Default predicate: returns True if color is "dark" (darker than 50% brightness).
    
    A pixel is considered covered if the sum of its RGB channels is <= 382
    (which is (255+255+255) / 2)
    
    Args:
        color: RGB tuple (r, g, b) where each value is 0-255
    
    Returns:
        True if the color sum is in the darker half of the spectrum
    """
    return sum(color) <= (_COLOR_TUP_MAX_SUM >> 1)


# ============================================================================
# PUBLIC API
# ============================================================================

def find_coverage_for(chars: Iterable[str],
                      pred: ColorPredicate,
                      image_width: int = _DEFAULT_TEST_SIZE,
                      font_name: str = _DEFAULT_FONT,
                      ) -> List[Tuple[str, float]]:
    """Calculate coverage for multiple characters.
    
    Processes a collection of characters and returns their coverage percentages.
    
    Args:
        chars: Iterable of characters to analyze (e.g., string or list)
        pred: Predicate function to determine pixel coverage
        image_width: Size of test images (default: 100)
        font_name: Font name to use (default: FreeSans)
    
    Returns:
        List of tuples: [(character, coverage_percentage), ...]
        
    Note:
        - Coverage percentages are RELATIVE - use for comparing characters
        - They are not absolute values due to whitespace in test images
        - Only meaningful when compared with other characters tested the same way
    """

    font = ft.truetype(font_name, image_width)

    return [(c, find_percent_coverage(c, pred, image_width, font)) for c in chars]


def find_half_coverage_for_printable(image_width: int = _DEFAULT_TEST_SIZE,
                                     font_name: str = _DEFAULT_FONT
                                     ) -> List[Tuple[str, float]]:
    """Analyze all printable ASCII characters for darkness/coverage.
    
    Convenience function that tests all visible ASCII characters:
    digits (0-9), letters (a-z, A-Z), and punctuation.
    
    Args:
        image_width: Size of test images (default: 100 pixels)
        font_name: Font name to use (default: FreeSans)
    
    Returns:
        List of tuples: [(character, coverage), ...]
        
    Example:
        >>> results = find_half_coverage_for_printable()
        >>> results.sort(key=lambda p: p[1], reverse=True)  # Sort by darkness
        >>> for char, coverage in results[:5]:
        ...     print(f"{char}: {coverage:.2%}")
        @: 30.15%
        W: 24.99%
        M: 24.10%
        B: 20.52%
        Q: 19.96%
    """

    return find_coverage_for(_DEFAULT_CHAR_SET, half_color_predicate, image_width, font_name)

# Example usage:
if __name__ == "__main__":
    print("=" * 70)
    print("CHARACTER DARKNESS ANALYZER")
    print("=" * 70)
    print()
    
    # Analyze all printable ASCII characters
    print("Analyzing all printable ASCII characters...")
    print("(This may take a few seconds...)")
    print()
    
    results = find_half_coverage_for_printable()
    
    # Sort by darkness (descending)
    results_sorted = sorted(results, key=lambda p: p[1], reverse=True)
    
    # Show top 10 darkest characters
    print("TOP 10 DARKEST CHARACTERS (Highest Coverage):")
    print("-" * 70)
    for i, (char, coverage) in enumerate(results_sorted[:10], 1):
        bar = "█" * int(coverage * 50)
        print(f"{i:2d}. '{char}' -> {coverage:.4f} ({coverage*100:6.2f}%) [{bar}]")
    print()
    
    # Show top 10 lightest characters
    print("TOP 10 LIGHTEST CHARACTERS (Lowest Coverage):")
    print("-" * 70)
    for i, (char, coverage) in enumerate(reversed(results_sorted[-10:]), 1):
        bar = "█" * int(coverage * 50)
        print(f"{i:2d}. '{char}' -> {coverage:.4f} ({coverage*100:6.2f}%) [{bar}]")
    print()
    
    # Show all characters ordered by darkness (useful for ASCII art)
    print("ALL CHARACTERS ORDERED BY DARKNESS:")
    print("(Best for ASCII art shading - darks on left, lights on right)")
    print("-" * 70)
    chars_only = "".join([char for char, _ in results_sorted])
    print(chars_only)
    print()
    
    print("COMPLETE DATA (all characters with coverage):")
    print("-" * 70)
    for char, coverage in results_sorted[:20]:  # Show first 20
        print(f"  ('{char}', {coverage:.4f}),")
    print("  ...")
