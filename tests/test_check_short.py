import unittest
from pathlib import Path
from pipeline.check_short import scenes, validate


class StoryboardTests(unittest.TestCase):
    def test_current_storyboard(self):
        script = next(Path('script').glob('13-SHORT-*.md'))
        self.assertEqual(validate(scenes(script)), [])

    def test_reject_missing_scenes(self):
        self.assertTrue(validate([]))

    def test_reject_bad_chunk_and_word_count(self):
        items = [(i, (i-1)//5+1, ' '.join(['kata']*12), f'{i}.jpg') for i in range(1,31)]
        self.assertEqual(validate(items), [])
        items[0] = (1, 6, 'terlalu pendek', '../bad.jpg')
        self.assertEqual(len(validate(items)), 3)


if __name__ == '__main__':
    unittest.main()
