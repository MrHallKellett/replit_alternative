import unittest
from main import *

# Add imports here!
from unittest.mock import patch

class UnitTests(unittest.TestCase):



  def redirect_output(self, *strings, end="\n"):

    self.outputs.append(" ".join(strings) + end)

  def setUp(self):
      # Add setup code here!
      self.outputs = []





  def test_Exercise1(self):
      # Enter code here
      result = Exercise1()

      self.assertEquals(type(result), list)
      self.assertEquals(type(result[0]), str)
      self.assertEquals(len(result), 5)


  def test_Exercise2(self):
      # Enter code here
      result = Exercise2()

      self.assertEquals(type(result), list)
      self.assertEquals(type(result[0]), list)
      self.assertEquals(type(result[0][0]), str)
      self.assertTrue(len(result) > 2)
      self.assertEquals(len(result[2]), 5)

  def test_Exercise7_8(self):
      # Enter code here

      comp1, comp2 = Exercise8()

      self.assertEquals(comp1.manager, "Chuck Bloddington")


      self.assertEquals(comp2.years_active, 10)

      self.assertEquals(comp2.annual_turnover, 10200000000)

      self.assertEquals(comp1.is_private_company, False)


  def test_Exercise5(self):
      # Enter code here
      house = Exercise2()

      exp = ""
      for room in house:
        for c in room:
          if len(c) > 4:
            exp += c + ","
      with patch('builtins.print', side_effect=self.redirect_output):
        result = Exercise5(house)
      result = "".join(self.outputs)

      self.assertIn(exp.strip(), result.strip())

  def test_Exercise6(self):
      # Enter code here
      house = Exercise2()
      with patch('builtins.print', side_effect=self.redirect_output):
        result = Exercise6()
      result = "".join(self.outputs)
      exp = ""
      for i in range(10):
        try:
          exp += house[i][i]+"\n"
        except IndexError:
          break

      self.assertEquals(result, exp)

  def test_Exercise3(self):
      # Enter code here

      # Enter code here

      house = Exercise2()
      with patch('builtins.print', side_effect=self.redirect_output):
        try:
          result = Exercise3(house)
        except TypeError:
          assert False

      r3c1 = house[2][0]
      rLcL = house[-1][-1]
      r1c2l3 = house[0][1][2]

      result = "".join(self.outputs)

      for sentence in """The first colour of the third room is
    The last colour of the last room is
    The third letter of the second colour of the first room is""".split("\n"):
        self.assertIn(sentence.strip(), result)

      self.assertEquals(result.split("\n")[0].split(" ")[-1], r3c1)
      self.assertEquals(result.split("\n")[1].split(" ")[-1], rLcL)
      self.assertEquals(result.split("\n")[2].split(" ")[-1], r1c2l3)

  def test_Exercise4(self):
      # Enter code here
      house = Exercise2()
      with patch('builtins.print', side_effect=self.redirect_output):
        res = Exercise4()

      result = "".join(self.outputs)
      for room in house:
        for colour in room:
          self.assertIn(colour, result)



if __name__ == "__main__":
  unittest.main()
