import re
from .numbers import normalize_numbers


# Regular expression matching whitespace:
_whitespace_re = re.compile(r'\s+')

# List of (regular expression, replacement) pairs for abbreviations:
_abbreviations = [(re.compile('\%s.' % x[0]), x[1]) for x in [
  ('පෙ.ව.', 'පෙරවරු '),
  ('ප.ව.', 'පස්වරු '),
  ('බු.ව.', 'බුද්ධ වර්ෂ '),
  ('ක්‍රි.ව.','ක්‍රිස්තු වර්ෂ ')
]]

def expand_abbreviations(text):
  for regex, replacement in _abbreviations:
    text = re.sub(regex, replacement, text)
  return text

def expand_numbers(text):
  return normalize_numbers(text)


def collapse_whitespace(text):
  return re.sub(_whitespace_re, ' ', text)


def sinhala_cleaners(text):
  '''Pipeline for Sinhala text, including number and abbreviation expansion.'''
  text = expand_numbers(text)
  text = expand_abbreviations(text)
  text = collapse_whitespace(text)
  return text
