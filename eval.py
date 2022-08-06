import argparse
import os
import re
from hparams import hparams, hparams_debug_string
from synthesizer import Synthesizer


sentences = [
  # From Ada derana sinhala news July 2022:
  'ශ්‍රී ලංකා මහජන උපයෝගීතා කොමිෂන් සභාව විසින් කිසිදු ගිවිසුමකින් තොරව මාසික කුලී පදනම මත ලබාගෙන තිබූ බෙන්ස් වර්ගයේ මෝටර් රථයක් ගැන කෝප් කමිටුවේදී අනාවරණය විය.',
  'ආයෝජන ප්‍රවර්ධන අමාත්‍යංශය යටතට තවත් සමාගම් කිහිපයක් පවරමින් නව ගැසට් නිවේදනයක් නිකුත් කර තිබේ.',
  'ඛනිජ තෙල් නීතිගත සංස්ථාවට ඩොලර්වලින් ගෙවීම් සිදුකර ඉන්ධන අත්‍යවශ්‍ය ආයතන සහ පිරිස් වෙත ගෙන්වා ගැනීමට අවශ්‍ය පහසුකම් ලබාදීමට පියවර ගෙන තිබේ.',
  'ශ්‍රී ලංකා ටෙස්ට් කණ්ඩායමේ තුන් ඉරියව් ක්‍රීඩක ධනංජය ද සිල්වා සහ දඟ පන්දු යවන ක්‍රීඩක ජෙෆ්රි වැන්ඩර්සේට කොවිඩි 19 ආසාදනය වී තිබේ.',
  'මෙරට තරග සංචාරයකට එක්වීමට පාකිස්තාන ක්‍රිකට් කණ්ඩායම දිවයිනට පැමිණ තිබේ.',
  'ජනතා සාශිත්‍ය කරුවා දක්ශයෙකි.',
  'සියළු සත්වයෝ සුවපත් වෙත්වා',
  'මනාව සිහිය හමුවෙහි සංස්කාරස්කන්ධ නො වන්නී වේ ද'
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
