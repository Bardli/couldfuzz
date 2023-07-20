results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      seed_tensor = tf.random.uniform([2], minval=-256, maxval=257, dtype=tf.int32)
      seed = tf.identity(seed_tensor)
      results["res_cpu"] = tf.keras.initializers.GlorotUniform(seed=seed,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      seed = tf.identity(seed_tensor)
      seed = tf.cast(seed, tf.int32)
      results["res_gpu"] = tf.keras.initializers.GlorotUniform(seed=seed,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
