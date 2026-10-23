from pathlib import Path
import sys
import hashlib
import struct
import tempfile
import unittest
from datetime import datetime

pviPath = str(Path(__file__).parents[1])

sys.path.append( pviPath )

from pvi.utils import BrProfilerDataFile
from pvi.utils.BrProfilerDataFile import BrProfilerEvent

class ProfilerDataFileTests(unittest.TestCase):
    fixtures = Path(__file__).resolve().parent / 'profiler_testdata'

    def test_legacy_object_metadata(self):
        expected = {
            'profiler1.pd': '9b1e4d7c33dd77f59f429e6d706513c5e098a1fe225e4be54a08a203929e1baa',
            'profiler2.pd': 'c391110f1e8b9c7e8163e657049e7611d8c7128901076bd241ba841bd96a1b67',
            'profiler3.pd': '65cc7563e35b30a1e242633175749ef050115375b8e59f3887b4ede1a06ae189',
            'profiler4.pd': '9e704fe07ec47b6fa6d0eb8f4219b81d013e0afde806a3233041931a2bcdec50',
            'profiler5.pd': '9e3958eff7b1b31a8afecd721ffdb77f0e41fea0b8bcb140130822ebd914427b',
            'profiler6.pd': '40c76f4b0338dfdfb8d2c47e5c48e27765146ddc5841ac0cbb8094d2ee1b2f14',
            'profiler7.pd': 'a57928b3b0052870beb3144dcfb1014222c9a6c10fa31be327b203a59c8b5c97',
        }
        for filename, checksum in expected.items():
            with self.subTest(filename=filename):
                profiler = BrProfilerDataFile(str(self.fixtures / filename))
                result = ''.join(str(getattr(profiler, attribute)) for attribute in (
                    'taskClasses', 'cyclicTasks', 'systemTasks', 'interruptHandler', 'libraryFunctions'))
                self.assertEqual(hashlib.sha256(result.encode()).hexdigest(), checksum)

    def test_fixture_entries(self):
        expected = {
            'profiler1.pd': {
                'entries': 1500, 'recordSize': 16, 'AR': 'T4.10',
                'profiledTarget': 'X20CP3584', 'tickFrequencyMhz': 598.5,
                'firstRecordIndex': 254, 'lastRecordIndex': 253,
                'startDateOfProfiling': datetime(2023, 7, 25, 9, 4, 41),
            },
            'profiler2.pd': {
                'entries': 5000, 'recordSize': 16, 'AR': 'D4.93',
                'profiledTarget': '5PC910.SX05-00', 'tickFrequencyMhz': 2709.875,
                'firstRecordIndex': 4983, 'lastRecordIndex': 4982,
                'startDateOfProfiling': datetime(2023, 7, 31, 9, 53, 9),
            },
            'profiler3.pd': {
                'entries': 5000, 'recordSize': 16, 'AR': 'D4.93',
                'profiledTarget': '5PC910.SX05-00', 'tickFrequencyMhz': 2709.875,
                'firstRecordIndex': 2912, 'lastRecordIndex': 2911,
                'startDateOfProfiling': datetime(2023, 8, 4, 14, 15, 7),
            },
            'profiler4.pd': {
                'entries': 1500, 'recordSize': 16, 'AR': 'S4.93',
                'profiledTarget': 'X20CP3687X', 'tickFrequencyMhz': 1596.0,
                'firstRecordIndex': 368, 'lastRecordIndex': 367,
                'startDateOfProfiling': datetime(2026, 6, 30, 21, 46, 52),
            },
            'profiler5.pd': {
                'entries': 5000, 'recordSize': 16, 'AR': '6.3.4',
                'profiledTarget': '5APC4100.TGL1-000', 'tickFrequencyMhz': 2416.666,
                'firstRecordIndex': 2337, 'lastRecordIndex': 2336,
                'startDateOfProfiling': datetime(2025, 8, 13, 7, 34, 30),
            },
            'profiler6.pd': {
                'entries': 50000, 'recordSize': 20, 'AR': '6.7.7',
                'profiledTarget': '5APC3100.KBU3-000', 'tickFrequencyMhz': 2900.0,
                'firstRecordIndex': 0, 'lastRecordIndex': 49999,
                'startDateOfProfiling': datetime(2026, 9, 10, 12, 39, 39),
            },
            'profiler7.pd': {
                'entries': 500000, 'recordSize': 20, 'AR': '6.1.1',
                'profiledTarget': 'X20CP3684', 'tickFrequencyMhz': 10.0,
                'firstRecordIndex': 0, 'lastRecordIndex': 499999,
                'startDateOfProfiling': datetime(2026, 10, 23, 10, 48, 24),
            },
        }
        checksums = {
            'profiler1.pd': '345a2a0b57f285336247ffd982eb537c3582065fcc40656680e35ae0fc791b48',
            'profiler2.pd': 'a0aebd26992a2ae740f67684fbc94ec825b1b2f6152468db574714ab41fd079c',
            'profiler3.pd': 'a6d175ed78b918213a520692f5e2cf6068469fa554538bfe002b21f1205a509e',
            'profiler4.pd': '21726f0825ef892191eb28336d31046d0d7150d73ccbcf8dd81a2da0f7aa72e7',
            'profiler5.pd': 'fd5143fe31ec4f2f0e4584d47008b9fa9872b0233b739078340975efed29feb2',
            'profiler6.pd': 'b726b10f6f86900e2fa354beafe3cccb55cd9aaed0925bdea8061e1d370de38c',
            'profiler7.pd': '7c31c4de89b4712a18002ca535656a7cf77791f5a6113fb4bc54e406c7347342',
        }
        for filename, info in expected.items():
            with self.subTest(filename=filename):
                profiler = BrProfilerDataFile(str(self.fixtures / filename))
                for key, value in info.items():
                    self.assertEqual(profiler.info[key], value)
                entries = profiler.entries
                self.assertIs(entries, profiler.entries)
                self.assertEqual(len(entries), info['entries'])
                self.assertEqual(entries[0].microseconds, 0)
                checksum = hashlib.sha256()
                for entry in entries:
                    core = entry.cpuCore if entry.cpuCore is not None else -1
                    checksum.update(struct.pack('<dIIi', entry.microseconds, entry.objectIdent, entry.event, core))
                    checksum.update(entry.additionalData)
                    self.assertEqual(len(entry), 5)
                    self.assertEqual(entry.additionalData, b'')
                    self.assertTrue(entry.eventDescription)
                    if info['recordSize'] == 16:
                        self.assertIsNone(entry.cpuCore)
                    else:
                        self.assertIsInstance(entry.cpuCore, int)
                self.assertEqual(checksum.hexdigest(), checksums[filename])

    def read_modified_capture(self, data):
        with tempfile.TemporaryDirectory() as directory:
            filename = Path(directory) / 'modified.pd'
            filename.write_bytes(data)
            return BrProfilerDataFile(str(filename))

    def test_single_record_and_zero_first_counter(self):
        data = bytearray((self.fixtures / 'profiler4.pd').read_bytes())
        metadata, start = struct.unpack_from('>2I', data, 0x28)
        struct.pack_into('<II', data, metadata + 12, 0, 0)
        struct.pack_into('<Q', data, start, 0)
        profiler = self.read_modified_capture(data)
        self.assertEqual(len(profiler.entries), 1)
        self.assertEqual(profiler.entries[0].microseconds, 0)
        struct.pack_into('<I', data, metadata + 16, 1)
        ticks_per_microsecond = struct.unpack_from('<I', data, metadata + 20)[0] // 1000
        struct.pack_into('<Q', data, start + 16, 5 * ticks_per_microsecond)
        profiler = self.read_modified_capture(data)
        self.assertEqual([entry.microseconds for entry in profiler.entries], [0, 5])

    def test_core_and_nonzero_additional_data(self):
        data = bytearray((self.fixtures / 'profiler6.pd').read_bytes())
        config, metadata, start = struct.unpack_from('>3I', data, 0x24)
        struct.pack_into('>I', data, 0x30, start + 32)
        struct.pack_into('<II', data, config + 16, 32, 12)
        struct.pack_into('<II', data, metadata + 12, 0, 0)
        struct.pack_into('<I', data, start + 16, 3)
        payload = bytes(range(12))
        data[start + 20:start + 32] = payload
        entry = self.read_modified_capture(data).entries[0]
        self.assertEqual(entry.cpuCore, 3)
        self.assertEqual(entry.additionalData, payload)

    def test_invalid_layouts(self):
        original = (self.fixtures / 'profiler4.pd').read_bytes()
        config, metadata, start = struct.unpack_from('>3I', original, 0x24)
        mutations = (
            (0x2c, '>I', len(original) + 1),
            (config + 16, '<I', 1),
            (metadata + 12, '<I', 10000),
            (metadata + 20, '<I', 0),
            (metadata + 0x36, '<I', 100000),
            (3, 'B', 9),
        )
        for offset, format_string, value in mutations:
            with self.subTest(offset=offset):
                data = bytearray(original)
                struct.pack_into(format_string, data, offset, value)
                with self.assertRaises(ValueError):
                    self.read_modified_capture(data)

    def test_event_tuple_compatibility(self):
        entry = BrProfilerEvent(0, 1, 'name', 2, 'description')
        self.assertEqual(tuple(entry), (0, 1, 'name', 2, 'description'))
        self.assertIsNone(entry.cpuCore)
        self.assertEqual(entry.additionalData, b'')
        entry = BrProfilerEvent(*entry, cpuCore=2, additionalData=b'raw')
        replacement = entry._replace(objectName='renamed')
        self.assertEqual(replacement.objectName, 'renamed')
        self.assertEqual((replacement.cpuCore, replacement.additionalData), (2, b'raw'))
        self.assertIsNone(BrProfilerEvent._make(tuple(entry)).cpuCore)


if __name__ == '__main__':
    unittest.main()

