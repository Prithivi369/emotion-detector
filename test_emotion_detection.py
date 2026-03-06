import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_joy(self):
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['joy'], 0.88)

    def test_anger(self):
        result = emotion_detector("I am mad")
        self.assertEqual(result['anger'], 0.02)

if __name__ == "__main__":
    unittest.main()