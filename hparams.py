import tensorflow as tf


# hyperparameters:
hparams = tf.contrib.training.HParams(
  
  cleaners='sinhala_cleaners', # setting up sinhala preprocessing steps

  # Audio:
  num_mels=80, #  Number of Mel banks to generate
  num_freq=1025, 
  sample_rate=20000,
  frame_length_ms=50, #frame length in mili seconds
  frame_shift_ms=12.5, #frame shift in mili seconds
  preemphasis=0.97,

  min_level_db=-100, # factor to normalize and denormalize spectrogram
  ref_level_db=20,  # 

  # Model:
  outputs_per_step=5, #Reduction factor. Paper => 2, 3, 5
  embed_depth=256, # Size of character embeddings
  prenet_depths=[256, 128], #encoder and decoder prenet
  encoder_depth=256, 
  postnet_depth=256,
  attention_depth=256,
  decoder_depth=256,

  # Training:
  batch_size=32, 
  adam_beta1=0.9,
  adam_beta2=0.999,
  initial_learning_rate=0.002,
  decay_learning_rate=True,
 
  # during evaluation and traing the maximum audio length is equals to
  # max_iters * outputs_per_step * frame_shift_ms

  # Eval:
  max_iters=800, #Number of maximum iterations
  griffin_lim_iters=60, #iterations of griffin lim algorithm
  power=1.5,   # Power to raise magnitudes to prior to Griffin-Lim
)


def hparams_debug_string():
  values = hparams.values()
  hp = ['  %s: %s' % (name, values[name]) for name in sorted(values)]
  return 'Hyperparameters:\n' + '\n'.join(hp)
