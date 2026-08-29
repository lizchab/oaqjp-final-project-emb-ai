"""
Unit tests for the emotion_detection module.
"""

import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    """Test cases for the emotion_detector function."""

    def test_joy(self):
        """Test that 'joy' is detected from a happy statement."""
        result = emotion_detector("I am so happy today!")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger(self):
        """Test that 'anger' is detected from an angry statement."""
        result = emotion_detector("I am furious about this!")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_sadness(self):
        """Test that 'sadness' is detected from a sad statement."""
        result = emotion_detector("I feel so sad and lonely.")
        self.assertEqual(result['dominant_emotion'], 'sadness')

if __name__ == '__main__':
    unittest.main()

