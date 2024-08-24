import unittest
from main import *


class UnitTests(unittest.TestCase):

  def test_test_railfence_b(self):
      # Enter code here
      self.assertEqual(encrypt_railfence("bts skytrain", 2), "bsktantsyri")


  def test_test_railfence_a(self):
      # Enter code here
      self.assertEqual(encrypt_railfence("pineapple", 5), 'peilnpepa')


  def test_test_your_cipher_b(self):
      # Enter code her  # Enter code here
      plain = "The QuiCK BR0wn Fox Jump3d Over THE LAZY DoG!?!?!"

      encrypted = my_cipher(plain, "encrypt")

      self.assertEqual(plain, my_cipher(encrypted, "decrypt"))



  def test_test_your_cipher_a(self):
      # Enter code here
      plain = "hellotesting"

      encrypted = my_cipher(plain, "encrypt")

      self.assertEqual(plain, my_cipher(encrypted, "decrypt"))


  def test_test_caesar_a(self):
      # Enter code here
      self.assertEqual(caesar_decrypt("PnG", 13), "CaT")

  def test_test_rot13_b(self):
      # Enter code here
      self.assertEqual(rot13_encrypt("cat"), "png")


  def test_test_caesar_b(self):
      # Enter code here

      self.assertEqual(caesar_decrypt("p dhua jovjvshal", 7), "iwantchocolate")

  def test_test_rot13_a(self):
      # Enter code here
      self.assertEqual(rot13_encrypt("abc"), "nop")


if __name__ == "__main__":
  unittest.main()
