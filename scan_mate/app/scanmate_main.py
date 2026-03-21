import argparse

from scan_mate.app.scanmate_controller import ScanMateController
from scan_mate.app.scanmate_parameters import ScanMateParameters


class ScanMateMain:
    def __init__(self):
        self.controller = ScanMateController()
        self.params = ScanMateParameters()

    def run(self):
        mode, task, config_file = self._parse_args()
        params = self.params.read_config(config_file, mode, task)
        self.controller.dispatch(mode, task, params)


    def _parse_args(self) -> tuple[str, str, str]:
        parser = argparse.ArgumentParser(
            formatter_class=argparse.RawTextHelpFormatter
        )

        subparsers = parser.add_subparsers(
            dest='mode', required=True, help='Select mode'
        )

        # --- prepare_data mode ---
        prepare_parser = subparsers.add_parser(
            'prepare_data',
            help='Generate training datasets',
            formatter_class=argparse.RawTextHelpFormatter
        )

        prepare_parser.add_argument(
            'task',
            choices=['generator', 'augmenter', 'rotator', 'compositor'],
            help=(
                'generator: Generate base barcode images\n'
                'augmenter: Apply noise and blur\n'
                'rotator: Apply rotation, noise, blur\n'
                'compositor: Overlay barcodes on background images'
            )
        )

        # --- train mode ---
        train_parser = subparsers.add_parser(
            'train',
            help='Train models',
            formatter_class=argparse.RawTextHelpFormatter
        )

        train_parser.add_argument(
            'task',
            choices=['detector', 'corrector', 'classifier'],
            help=(
                'detector: Train barcode / QR detector\n'
                'corrector: Train skew/noise correction CNN\n'
                'cleaner: Train barcode / QR cleaner'
            )
        )

        # --- test mode ---
        test_parser = subparsers.add_parser(
            'test',
            help='Test models',
            formatter_class=argparse.RawTextHelpFormatter
        )

        test_parser.add_argument(
            'task',
            choices=['detector', 'corrector', 'classifier'],
            help=(
                'detector: Test barcode / QR detector\n'
                'corrector: Test skew/noise correction CNN\n'
                'cleaner: Test barcode / QR cleaner'
            )
        )

        # --- infer mode ---
        infer_parser = subparsers.add_parser(
            'infer',
            help='Run inference on images or camera stream',
            formatter_class=argparse.RawTextHelpFormatter
        )

        infer_parser.add_argument(
            'task',
            choices=['picture', 'camera'],
            help=(
                'picture: From a picture\n'
                'camera: Infer from camera'
            )
        )

        # --- manager mode ---
        manager_parser = subparsers.add_parser(
            'manager',
            help='Manage data',
            formatter_class=argparse.RawTextHelpFormatter
        )

        manager_parser.add_argument(
            'task',
            choices=['read_single', 'check',
                     'extract_data', 'delete_data', 'reset_all'],
            help=(
                'read_single: Read clean single barcode or QR code\n'
                'check: Check database\n'
                'extract_data: Extract data and create datasets\n'
                'delete_data: Delete data\n'
                'reset_all: Reset database'
            )
        )

        # --- config ---
        parser.add_argument(
            '--config', '-c',
            help='Path to config file (optional, falls back to defaults)'
        )

        args = parser.parse_args()

        return args.mode, args.task, args.config
