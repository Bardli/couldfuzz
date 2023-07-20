results = dict()
import tensorflow as tf
import time
try:
  try:
    seed = 122
    results["res_low"] = tf.initializers.glorot_normal(seed=seed,)
    t_start = time.time()
    results["res_low"] = tf.initializers.glorot_normal(seed=seed,)
    t_end = time.time()
    results["time_low"] = t_end - t_start
  except Exception as e:
    results["err_low"] = "Error:"+str(e)
  try:
    results["res_high"] = tf.initializers.glorot_normal(seed=seed,)
    t_start = time.time()
    results["res_high"] = tf.initializers.glorot_normal(seed=seed,)
    t_end = time.time()
    results["time_high"] = t_end - t_start
  except Exception as e:
    results["err_high"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
