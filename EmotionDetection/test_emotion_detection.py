import unittest
from emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_joy(self):
        self.assertEqual("joy", emotion_detector("I am glad this happened")["dominant_emotion"])

    def test_anger(self):
        self.assertEqual("anger", emotion_detector("I am really mad about this")["dominant_emotion"])

    def test_disgust(self):
        self.assertEqual("disgust", emotion_detector("I feel disgusted just hearing about this")["dominant_emotion"])

    def test_sadness(self):
        self.assertEqual("sadness", emotion_detector("I am so sad about this")["dominant_emotion"])

    def test_fear(self):
        self.assertEqual("fear", emotion_detector("I am really afraid that this will happen")["dominant_emotion"])


if __name__ == '__main__':
    unittest.main()