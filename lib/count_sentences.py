#!/usr/bin/env python3
TERMINATING_CHARS = ['.', '?', '!']

class MyString:
  def __init__(self, value = ""):
    if isinstance(value, str):
      self.value = value
    else:
      print('The value must be a string.')
      self.value = ""
  
  def is_sentence(self):
    return self.value[-1] == "."
  
  def is_question(self):
    return self.value[-1] == "?"
  
  def is_exclamation(self):
    return self.value[-1] == "!"
  
  def count_sentences(self):
    count = 0
    lastChar = ''
    for char in self.value:
      if char in TERMINATING_CHARS and not lastChar in TERMINATING_CHARS:
        count += 1
      lastChar = char
    return count
  
  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, value):
    if isinstance(value, str):
      self._value = value
    else:
      print('The value must be a string.')