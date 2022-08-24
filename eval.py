import argparse
import os
import re
from hparams import hparams, hparams_debug_string
from synthesizer import Synthesizer

sentences = [
  # From Ada derana sinhala news July 2022:
  'පිළිකුල් සහගත බෝට්ටු වැදගත් උපකරණය සමග ඇවිදියි.',
  'කුණාටු සහිත  අර්බුද මුඩු ගල්පරයක් අහුලා ගනියි. ',
  'විශිෂ්ට දත් අද්භූත පොතක උඩ පනියි. ',
  'ආකර්ෂණීය අර්තාපල් පරිපූර්ණ මූණක කතා වෙයි.',
  'ජවසම්පන්න වීදුරු සුවද හමන කොළ සමග කතා කරයි.',
  'ප්රසන්න මේස නොසන්සුන් ආහාරය හැඩ කරයි.',
  'නිවාස නැති දොඩම් උදෑසන අසරණ වත්ත කතා කරයි.', 
  'බිඳෙන සුළු නියපොතු මෘදු රජතුමා කැමති වෙයි.',
  'සන්සුන් ගිරව් වර්ණවත් සත්තු විශ්වාස කරයි.',
  'ශක්තිමත් ජීවිත විශිෂ්ට පාරවල් උඩ පනී.'
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
