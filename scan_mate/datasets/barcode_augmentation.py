import cv2
import numpy as np
from numpy.typing import NDArray


class ColorPairGenerator:
    """Class for generating a pair of colors."""
    def __init__(self, min_ratio: float = 4.5):
        """
        Initialize instance.

        Args:
            min_ratio (float, optional): minimum contrast ratio.
                                         Defaults to 4.5.
        """
        self.min_ratio = min_ratio
        self.color1 = np.zeros(3, dtype=np.uint8)
        self.color2 = np.zeros(3, dtype=np.uint8)

    def random_color(self) -> NDArray[np.uint8]:
        """
        Generate a random RGB color.

        Returns:
            NDArray[np.uint8]: random RGB color
        """
        return np.random.randint(0, 255, 3, np.uint8)

    def relative_luminance(self, rgb: NDArray[np.uint8]) -> float:
        """
        Compute relative luminance.

        Args:
            rgb (NDArray[np.uint8]): RGB color

        Returns:
            float: luminance
        """
        def channel(c):
            c = c / 255.0
            return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

        r, g, b = rgb
        return 0.2126 * channel(r) + 0.7152 * channel(g) + 0.0722 * channel(b)

    def contrast_ratio(self) -> float:
        """
        Compute contrast ratio between two colors.
        
        Returns:
            float: contrast ratio
        """
        l1 = self.relative_luminance(self.color1)
        l2 = self.relative_luminance(self.color2)
        lighter = max(l1, l2)
        darker = min(l1, l2)
        return (lighter + 0.05) / (darker + 0.05)

    def generate_contrasting_pair(
            self) -> tuple[NDArray[np.uint8], NDArray[np.uint8]]:
        """
        Generate two random RGB colors with sufficient contrast.

        Returns:
            tuple[NDArray[np.uint8], NDArray[np.uint8]]: RGB color pair
        """
        while True:
            self.color1 = self.random_color()
            self.color2 = self.random_color()
            if self.contrast_ratio() >= self.min_ratio:
                return self.color1, self.color2

    def __call__(self) -> tuple[NDArray[np.uint8], NDArray[np.uint8]]:
        """
        Generate two random RGB colors with sufficient contrast.

        Returns:
            tuple[NDArray[np.uint8], NDArray[np.uint8]]: RGB color pair
        """
        return self.generate_contrasting_pair()


class BarcodeAugmentation:
    pass