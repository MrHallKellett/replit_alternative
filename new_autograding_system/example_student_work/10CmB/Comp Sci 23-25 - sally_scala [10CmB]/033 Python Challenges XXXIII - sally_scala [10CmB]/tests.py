import unittest
from main import *


class UnitTests(unittest.TestCase):

  def test_task1(self):
      # Enter code here
      self.assertEquals(get_min_colour_depth(16548), 15)


  def test_task2_a(self):
      self.assertEquals(calculate_bitmap_filesize(100, 100, 1, True), 10000)


  def test_task2_b(self):
      # Enter code here
      self.assertTrue(type(calculate_bitmap_filesize(16, 54, 5, False)) == int)

  def test_task2_c(self):
      # Enter code here
      self.assertTrue(calculate_bitmap_filesize(567, 412, 510, False) == 262805)

  def test_task3_a(self):
      # Enter code here
      self.assertTrue(calculate_audio_filesize(100, 44100, 16, False) == 8820)

  def test_task3_b(self):
      self.assertTrue(calculate_audio_filesize(60, 200, 8, True) == 24)


  def test_task4_a(self):

      self.assertTrue(rle_compress("aaabbee"), "3a2b2e")


  def test_task4_b(self):
        self.assertEquals(rle_compress("ttttttttttutttttttttttuu"), "10t1u11t2u")


  def test_task5_a(self):
        self.assertTrue(rle_compress("3a2b2e", False), "aaabbee")

  def test_task5_b(self):
        self.assertTrue(rle_compress("10x3y12z", False), "xxxxxxxxxxyyyzzzzzzzzzzzz")




  def test_task6(self):

        from random import randrange

        for w, h, d in [[10, 10, 3], [100, 100, 8], [70, 42, 5]]:



          bitmap = random_bitmap(w, h, d)



          self.assertEquals(len(bitmap), h)

          self.assertEquals(len(bitmap[0]), w)



          bitmap2 = random_bitmap(w, h, d)

          bitmap3 = random_bitmap(w, h, d)





          x = randrange(0, w)

          y = randrange(0, h)



          self.assertNotEqual(bitmap[y][x], bitmap2[y][x])

          self.assertNotEqual(bitmap2[y][x], bitmap3[y][x])


        from random import randrange

        for w, h, d in [[10, 10, 3], [100, 100, 8], [70, 42, 5]]:



          bitmap = random_bitmap(w, h, d)



          self.assertEquals(len(bitmap), h)

          self.assertEquals(len(bitmap[0]), w)



          bitmap2 = random_bitmap(w, h, d)

          bitmap3 = random_bitmap(w, h, d)





          x = randrange(0, w)

          y = randrange(0, h)



          self.assertNotEqual(bitmap[y][x], bitmap2[y][x])

          self.assertNotEqual(bitmap2[y][x], bitmap3[y][x])






if __name__ == "__main__":
  unittest.main()
