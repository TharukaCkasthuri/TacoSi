import inflect
import re
from .numbers2wordsSi import converter 


_inflect = inflect.engine()
_comma_number_re = re.compile(r'([0-9][0-9\,]+[0-9])')
_decimal_number_re = re.compile(r'([0-9]+\.[0-9]+)')
_rupees_re = re.compile(r'රු.([0-9\.\,]*[0-9]+)')
_pounds_re = re.compile(r'£([0-9\,]*[0-9]+)')
_dollars_re = re.compile(r'\$([0-9\.\,]*[0-9]+)')
_ordinal_re = re.compile(r'[0-9]+(st|nd|rd|th)')
_number_re = re.compile(r'[0-9]+')


def _remove_commas(m):
  return m.group(1).replace(',', '')

def _expand_decimal_point(m):
  return m.group(1).replace('.', ' යි දශම ')


def _expand_dollars(m):
  match = m.group(1)
  parts = match.split('.')
  if len(parts) > 2:
    return 'ඩොලර් ' + match  # Unexpected format
  dollars = int(parts[0]) if parts[0] else 0
  cents = int(parts[1]) if len(parts) > 1 and parts[1] else 0
  if dollars and cents:
    return '%s %sයි %s %s' % ("ඩොලර්",dollars,"සත",cents)
  elif dollars:
    return '%s %s' % ("ඩොලර්",dollars)
  elif cents:
    return '%s %s' % ("සත",cents)
  else:
    return 'ඩොලර් බිංදුව'


  def _expand_rupees(m):
    match = m.group(1)
    parts = match.split('.')
    print(parts)
    if len(parts) > 2:
      return "රුපියල්" + match  # Unexpected format
    rupees = int(parts[0]) if parts[0] else 0
    cents = int(parts[1]) if len(parts) > 1 and parts[1] else 0
    default = "යි"
    if rupees and cents:
      rupee_unit = 'රුපියල්'
      cent_unit = 'සත'
      return '%s %s %s %s %s' % (rupee_unit, rupees,default,cent_unit, cents)
    elif rupees:
      rupee_unit = 'රුපියල්'
      return '%s %s' % (rupee_unit,rupees)
    elif cents:
      cent_unit = 'සත' if cents == 1 else 'සත'
      return '%s %s' % (cent_unit,cents)
    else:
      return 'රුපියල් බින්දුවයි'

def _expand_number(m):
  num = str(m.group(0))
  return converter(num)

def normalize_numbers(text):
  text = re.sub(_comma_number_re, _remove_commas, text)
  text = re.sub(_pounds_re, r'\1 පවුම්', text)
  text = re.sub(_dollars_re, _expand_dollars, text)
  text = re.sub(_rupees_re, _expand_rupees, text)
  text = re.sub(_decimal_number_re, _expand_decimal_point, text)
  text = re.sub(_number_re, _expand_number, text)
  return text
