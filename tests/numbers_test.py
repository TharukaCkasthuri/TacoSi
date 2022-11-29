from text.numbers import normalize_numbers


def test_normalize_numbers():
  assert normalize_numbers('1') == 'එක'
  assert normalize_numbers('15') == 'පහලොව'
  assert normalize_numbers('24') == 'විසි හතර'
  assert normalize_numbers('100') == 'සීය'
  assert normalize_numbers('101') == 'එකසිය එක'
  assert normalize_numbers('456') == 'හාරසිය පනස් හය'
  assert normalize_numbers('1000') == 'දාහ'
  assert normalize_numbers('1800') == 'එක් දහස් අටසීය'
  assert normalize_numbers('2,000') == 'දෙදහස'
  assert normalize_numbers('3000') == 'තුන් දහස'
  assert normalize_numbers('18000') == 'දහ අට දහස'
  assert normalize_numbers('24,000') == 'විසි හතර දහස'
  assert normalize_numbers('124,001') == 'එකසිය විසි හතර දහස් එක'



def test_normalize_money():
  def test_normalize_money():
  assert normalize_numbers('රු.0.00') == 'රුපියල් බිංදුව'
  assert normalize_numbers('රු.1') == 'රුපියල් එක'
  assert normalize_numbers('රු.10') == 'රුපියල් දහය'
  assert normalize_numbers('රු..01') == 'සත එක'
  assert normalize_numbers('රු.0.25') == 'සත විසි පහ'
  assert normalize_numbers('රු.5.00') == 'රුපියල් පහ'
  assert normalize_numbers('රු.5.01') == 'රුපියල් පහයි සත එකයි'
  assert normalize_numbers('රු.135.99.') == 'රුපියල් එකසිය තිස් පහයි සත අනූ නවයයි.'
  assert normalize_numbers('රු.40,000') == 'රුපියල් හතලිස් දාහ'
  assert normalize_numbers('රු.0.00') == 'රුපියල් බිංදුව'
  assert normalize_numbers('$1') == 'ඩොලර් එක'
  assert normalize_numbers('$10') == 'ඩොලර් දහය'
  assert normalize_numbers('$.01') == 'සත එක'
  assert normalize_numbers('$0.25') == 'සත විසි පහ'
  assert normalize_numbers('$5.00') == 'ඩොලර් පහ'
  assert normalize_numbers('$5.01') == 'ඩොලර් පහයි සත එකයි'
  assert normalize_numbers('$135.99.') == 'ඩොලර් එකසිය තිස් පහයි සත අනූ නවයයි.'
  assert normalize_numbers('$40,000') == 'ඩොලර් හතලිස් දාහ'
  assert normalize_numbers('for £2500!') == 'පවුම් දෙදහස් පන්සීය!'

