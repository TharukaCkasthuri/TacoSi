import argparse
import os
import re
from hparams import hparams, hparams_debug_string
from synthesizer import Synthesizer

sentences = [
  # From Ada derana sinhala news July 2022:
  'සිංහල දීපයේ අනුරාධපුරයෙහි තිස්ස නැමැති සන්නාලියෙක් ඇදුම් මැසීමේ කර්මාන්තයෙන් ජීවත් වෙයි. හෙතෙම තිසරණ ගතව පන්සිල් රකින්නෙකි.',
  'මෙසේ අසන්නට ලැබේ. හෙළදිව රුහුණු ජනපදයෙහි එක්තරා ගැල්කරුවෙක් සහලින් පිරවූ කරත්තයක් දක්කමින් ගැඹුරු මඩ ඇති තැනකට පැමිණියේය. ගැල මඩෙහි එරුණි.',
  'වයස අවුරුදු 08ක දරුවෙකු ඇළකට විසිකළ ග්‍රාම නිලධාරීවරයෙකු අත්අඩංගුවට ගෙන තිබේ. එම දරුවා ඇළ ඉවුරක සිට අලියෙකු නාවන අයුරු බලා සිට ඇත. එම ඉවුර ඔස්සේ බීමතින් පැමිණි අදාළ ග්‍රාම නිලධාරීවරයා දරුවා ඔසවා ඇළට විසිකර ඇත',
  'දකුණු තායිලන්තයේ ස්ථාන 17ක අද දිනයේ පිපිරීම් සහ ගිනිතැබීම් වාර්තා විය. බලධාරීන් පවසන්නේ එම සිදුවීම් අතර සම්බන්ධයක් ඇති බවය.',
  'ඇෆ්ගනිස්ථානයේ කාබුල් නුවර මුස්ලිම් දේවස්ථානයක පිපිරීමක් සිදුව තිබේ. විදෙස් මාධ්‍ය වාර්තා කර ඇත්තේ අදාළ පිපිරීම දේව මෙහෙයක් අතරතුර සිදුව ඇති බවය.',
  'රන් ආභරණ පළඳින්න අපි කවුරුත් ආසයිනේ. නමුත් මේ වගේ අර්බුද කාලයක අපි වටිනා ආභරණ පැළඳීම ඒ තරම් නුවණට හුරු නෑ. මේ කාලයේ වටිනා රන් ආභරණ පැළඳීම මගින් ඔබට ඒවා අහිමි වීමටත් ඔබේ ජීවිතයට හානි වීම⁣ටත් පුලුවන්.',
  'නිතරම අත් බෑගයට අවශ්‍ය දේවල් විතරක් දමා ගන්න. බෑගයේ අනවශ්‍ය දේවල් ඉවත් කරන්න. කුඩා අත්බෑගයක් පරිහරණය කිරීම එය පරිස්සම් කිරීමට ඔබට පහසු කරනවා.', 
  '$1 ක වටිනාකම රු.365 ක් දක්වා 2022 වර්ශයේදී ඉහල නැග තිබේ.',
  'පිහි ඇනුම් ප්‍රහාරයට ලක් වූ බ්‍රිතාන්‍ය ලේඛක සල්මන් රුෂ්ඩිගේ තත්ත්වය සුව අතට හැරෙමින් පවතින බවට විදෙස් මාධ්‍ය වාර්තා කරයි.',
  'ලන්දේසින් විසින් ක්‍රි.ව.1640 දී ගාල්ලේ බලය තහවුරු කර ගත්ත ද ඊට පෙර සිටම දෙපාර්ශවයේ බලය තහවුරු කරගැනීමේ කටයුතු සිදුවූ බව පෙනෙයි.'
]

eval_sentences = [
  'යහපාලන කාලය තුළදී දේශපාලන පළිගැනීම්වලට ලක්වූ බව පවසමින් තෝරාගත් පිරිසකට කෝටි ගණනක වන්දි මුදල් ගෙවන්නේ නම් ඊට විරෝධය පළකර සිටින බව ශ්‍රී ලංකා නිදහස් පක්ෂ පවසයි.',
  'නීතිවිරෝධී ලෙස මෙරටින් අපනයනය කිරීමට උත්සාහ කළ අබලි ලෝහ බහාලුම් දෙකක් රේගු භාරයට ගෙන තිබේ.',
  'රාජ්‍ය ව්‍යවසාය ප්‍රතිසංස්කරණයේදී තමන් වෘත්තිය සමිති ගැන තැකීමක් නොකරන බව ජනාධිපති රනිල් වික්‍රමසිංහ මහතා පවසයි.',
  ''
]


def get_output_base_path(checkpoint_path):
  base_dir = os.path.dirname(checkpoint_path)
  m = re.compile(r'.*?\.ckpt\-([0-9]+)').match(checkpoint_path)
  name = 'eval-%d' % int(m.group(1)) if m else 'eval'
  return os.path.join(base_dir, name)


def run_eval(args):
  print(hparams_debug_string())
  synth = Synthesizer()
  synth.load(args.checkpoint)
  base_path = get_output_base_path(args.checkpoint)
  for i, text in enumerate(sentences):
    path = '%s-%d.wav' % (base_path, i)
    print('Synthesizing: %s' % path)
    with open(path, 'wb') as f:
      f.write(synth.synthesize(text))


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--checkpoint', required=True, help='Path to model checkpoint')
  parser.add_argument('--hparams', default='',
    help='Hyperparameter overrides as a comma-separated list of name=value pairs')
  args = parser.parse_args()
  os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
  hparams.parse(args.hparams)
  run_eval(args)


if __name__ == '__main__':
  main()
