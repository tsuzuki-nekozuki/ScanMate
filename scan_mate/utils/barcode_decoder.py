from PIL import Image
from pyzbar.pyzbar import decode, ZBarSymbol


class BarcodeDecoder:
    def __init__(self, image_path: str):
        self.img: Image = Image.open(image_path)
        self.barcodes: list = []

    def detect_barcodes(self):
        return self.img

    def align_barcodes(self):
        return self.img

    def clean_barcodes(self):
        return self.img

    def read_barcodes(self):
        barcodes_list = decode(self.img)
        if len(barcodes_list) == 0:
            raise RuntimeError('No barcode found.')
        elif len(barcodes_list) > 1:
            raise RuntimeError('Many barcodes found.')
        return barcodes_list[0].data.decode()