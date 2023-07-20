results = dict()
import tensorflow as tf
import time
try:
  try:
    minval = -63.0
    maxval = 0.05
    seed_tensor = tf.saturate_cast(tf.random.uniform([2, 1], minval=-256, maxval=257, dtype=tf.int64), dtype=tf.int8)
    seed = tf.identity(seed_tensor)
    seed = tf.Variable(seed)
    results["res_low"] = tf.compat.v1.keras.initializers.uniform(minval=minval,maxval=maxval,seed=seed,)
    t_start = time.time()
    results["res_low"] = tf.compat.v1.keras.initializers.uniform(minval=minval,maxval=maxval,seed=seed,)
    t_end = time.time()
    results["time_low"] = t_end - t_start
  except Exception as e:
    results["err_low"] = "Error:"+str(e)
  try:
    seed = tf.identity(seed_tensor)
    seed = tf.cast(seed, tf.int32)
    seed = tf.Variable(seed)
    results["res_high"] = tf.compat.v1.keras.initializers.uniform(minval=minval,maxval=maxval,seed=seed,)
    t_start = time.time()
    results["res_high"] = tf.compat.v1.keras.initializers.uniform(minval=minval,maxval=maxval,seed=seed,)
    t_end = time.time()
    results["time_high"] = t_end - t_start
  except Exception as e:
    results["err_high"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
