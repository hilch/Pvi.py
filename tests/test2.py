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
                cyclic_metadata = {ident: {key: task[key] for key in ('name', 'taskClass')}
                    for ident, task in profiler.cyclicTasks.items()}
                result = (str(profiler.taskClasses) + str(cyclic_metadata) + str(profiler.systemTasks)
                    + str(profiler.interruptHandler) + str(profiler.libraryFunctions))
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

    def test_cyclic_task_statistics(self):
        profiler = BrProfilerDataFile(str(self.fixtures / 'profiler7.pd'))
        task = next(task for task in profiler.cyclicTasks.values() if task['name'] == 'Cnc')
        self.assertEqual(task['call_count'], 14988)
        for kind in ('net', 'gross'):
            self.assertAlmostEqual(task[f'minimal_{kind}_time'], 3.2, places=6)
            self.assertAlmostEqual(task[f'average_{kind}_time'], 31.235, places=3)
            self.assertAlmostEqual(task[f'maximal_{kind}_time'], 203.5, places=6)

    def profiler_from_events(self, events):
        original = (self.fixtures / 'profiler6.pd').read_bytes()
        config, metadata, start = struct.unpack_from('>3I', original, 0x24)
        data = bytearray(original[:start])
        for ticks, event, ident, core in events:
            data.extend(struct.pack('<QIII', ticks, event, ident, core))
        struct.pack_into('>I', data, 0x0e, len(data))
        struct.pack_into('>III', data, 0x30, len(data), len(data), len(data))
        struct.pack_into('<II', data, config + 16, len(events) * 20, 0)
        struct.pack_into('<III', data, metadata + 12, 0, len(events) - 1, 1000)
        return self.read_modified_capture(data)

    def test_cyclic_statistics_interrupts_preemption_and_boundaries(self):
        original = BrProfilerDataFile(str(self.fixtures / 'profiler6.pd'))
        ident = next(iter(original.cyclicTasks))
        task_class = original.cyclicTasks[ident]['taskClass']
        class_name = original.taskClasses[task_class]['name']
        scheduler = next(ident for ident, task in original.systemTasks.items() if task['name'] == class_name)
        class_names = {task['name'] for task in original.taskClasses.values()}
        idle = next(ident for ident, task in original.systemTasks.items() if task['name'] not in class_names)
        events = [
            (0, 0x02000001, ident, 0),
            (1, 0x02000000, ident, 0),
            (3, 0x01000000, 101, 0),
            (4, 0x01000000, 102, 0),
            (5, 0x01000001, 102, 0),
            (6, 0x01000001, 101, 0),
            (7, 0x00000000, idle, 0),
            (10, 0x00000000, scheduler, 0),
            (11, 0x02000001, ident, 0),
            (20, 0x02000000, ident, 0),
            (24, 0x02000001, ident, 0),
            (30, 0x02000000, ident, 0),
        ]
        profiler = self.profiler_from_events(events)
        task = profiler.cyclicTasks[ident]
        self.assertEqual(task['call_count'], 3)
        for field, value in {
            'minimal_net_time': 4, 'average_net_time': 4, 'maximal_net_time': 4,
            'minimal_gross_time': 4, 'average_gross_time': 7, 'maximal_gross_time': 10,
        }.items():
            self.assertEqual(task[field], value, field)
        unused = next(task for task_ident, task in profiler.cyclicTasks.items() if task_ident != ident)
        self.assertEqual(unused['call_count'], 0)
        for kind in ('net', 'gross'):
            for aggregation in ('minimal', 'average', 'maximal'):
                self.assertIsNone(unused[f'{aggregation}_{kind}_time'])

    def test_cyclic_statistics_task_class_preemption_and_cores(self):
        original = BrProfilerDataFile(str(self.fixtures / 'profiler6.pd'))
        ident = next(iter(original.cyclicTasks))
        task_class = original.cyclicTasks[ident]['taskClass']
        other_class = next(class_ident for class_ident in original.taskClasses if class_ident != task_class)
        events = [
            (0, 0x02000000, ident, 0),
            (1, 0x02000000, ident, 1),
            (2, 0x1e000000, other_class, 0),
            (3, 0x01000000, 101, 1),
            (5, 0x01000001, 101, 1),
            (6, 0x1e000004, other_class, 0),
            (9, 0x02000001, ident, 1),
            (10, 0x02000001, ident, 0),
        ]
        profiler = self.profiler_from_events(events)
        task = profiler.cyclicTasks[ident]
        self.assertEqual(task['call_count'], 2)
        self.assertEqual(task['minimal_net_time'], 6)
        self.assertEqual(task['average_net_time'], 6)
        self.assertEqual(task['maximal_net_time'], 6)
        self.assertEqual(task['minimal_gross_time'], 8)
        self.assertEqual(task['average_gross_time'], 9)
        self.assertEqual(task['maximal_gross_time'], 10)

    def test_cyclic_statistics_incomplete_call_does_not_skew_average(self):
        profiler = BrProfilerDataFile(str(self.fixtures / 'profiler6.pd'))
        task = next(task for task in profiler.cyclicTasks.values() if task['name'] == 'Svc#2.001')
        self.assertEqual(task['call_count'], 2)
        for kind in ('net', 'gross'):
            self.assertAlmostEqual(task[f'average_{kind}_time'], 7.249, places=3)

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

