results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      minval = -63.0
      maxval = 0.05
      seed_tensor = tf.random.uniform([2, 1], minval=-256, maxval=257, dtype=tf.int32)
      seed = tf.identity(seed_tensor)
      seed = tf.Variable(seed)
      results["res_cpu"] = tf.compat.v1.keras.initializers.uniform(minval=minval,maxval=maxval,seed=seed,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      seed = tf.identity(seed_tensor)
      seed = tf.cast(seed, tf.int32)
      seed = tf.Variable(seed)
      results["res_gpu"] = tf.compat.v1.keras.initializers.uniform(minval=minval,maxval=maxval,seed=seed,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
