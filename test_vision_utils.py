import unittest
from unittest.mock import patch
from vision_utils import get_products_from_image

class TestVisionUtils(unittest.TestCase):
    """
    Unittesztek a vision_utils modulhoz, amely képalapú állatfelismerés alapján keres termékeket.
    A külső függőségeket (Google Vision API, Hotcakes API) mockoljuk.
    """

    @patch("vision_utils.detect_animal_from_bytes")
    @patch("vision_utils.get_category_bvin")
    @patch("vision_utils.get_products_by_category_bvin")
    def test_get_products_from_image_success(self, mock_get_products, mock_get_bvin, mock_detect):
        """
        Teszteljük a teljes folyamatot sikeres állatfelismerés és terméklekérés esetén.
        """

        # Beállítjuk, hogy a felismerés "Kutya"-t adjon vissza, ami magyar kategória
        mock_detect.return_value = ["Kutya"]

        # A "Kutya" kategóriához tartozó Bvin-t mockoljuk
        mock_get_bvin.return_value = "dummy-bvin-123"

        # A Bvin alapján terméklistát adunk vissza
        mock_get_products.return_value = [
            {"ProductName": "Kutyatáp 1kg", "Sku": "DOG-001"},
            {"ProductName": "Póráz", "Sku": "DOG-002"}
        ]

        # Futtatjuk a tesztet egy dummy képadattal
        image_bytes = b"fake-image-data"
        result = get_products_from_image(image_bytes)

        # Ellenőrizzük az eredményt
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["Sku"], "DOG-001")
        self.assertEqual(result[1]["ProductName"], "Póráz")

    @patch("vision_utils.detect_animal_from_bytes")
    def test_get_products_from_image_no_match(self, mock_detect):
        """
        Teszteljük, ha a Google Vision nem talál felismerhető állatot.
        A függvénynek ilyenkor hibát kell visszaadnia.
        """

        # Nem található állatkategória a képen
        mock_detect.return_value = []

        # Futtatás dummy képpel
        result = get_products_from_image(b"irrelevant-image-data")

        # Várjuk, hogy error kulcsú dictionary-t kapjunk
        self.assertIsInstance(result, dict)
        self.assertIn("error", result)
        self.assertEqual(result["error"], "No matching animal category found.")

if __name__ == "__main__":
    unittest.main()