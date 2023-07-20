results = dict()
import tensorflow as tf
import time
try:
  try:
    seed_tensor = tf.saturate_cast(tf.random.uniform([2], minval=-256, maxval=257, dtype=tf.int64), dtype=tf.int8)
    seed = tf.identity(seed_tensor)
    results["res_low"] = tf.keras.initializers.GlorotUniform(seed=seed,)
    t_start = time.time()
    results["res_low"] = tf.keras.initializers.GlorotUniform(seed=seed,)
    t_end = time.time()
    results["time_low"] = t_end - t_start
  except Exception as e:
    results["err_low"] = "Error:"+str(e)
  try:
    seed = tf.identity(seed_tensor)
    seed = tf.cast(seed, tf.int32)
    results["res_high"] = tf.keras.initializers.GlorotUniform(seed=seed,)
    t_start = time.time()
    results["res_high"] = tf.keras.initializers.GlorotUniform(seed=seed,)
    t_end = time.time()
    results["time_high"] = t_end - t_start
  except Exception as e:
    results["err_high"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
