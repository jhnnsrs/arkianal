"""An example of a simple template for Arkitekt Next"""

from arkitekt_next import register
from mikro_next.api.schema import Image


@register
def segment_cells(image: Image) -> Image:
    "Segment cells in an image"
    return image


@register
def calculate_percentage_of_stained_cells(image: Image) -> float:
    "Calculate the percentage of stained cells in an image"
    return 0.0
