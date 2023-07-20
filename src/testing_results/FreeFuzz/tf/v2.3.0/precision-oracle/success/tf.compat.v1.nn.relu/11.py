results = dict()
import tensorflow as tf
import time
try:
  try:
    features_tensor = tf.saturate_cast(tf.random.uniform([4, 1, 3072], minval=-128, maxval=128, dtype=tf.int64), dtype=tf.int8)
    features = tf.identity(features_tensor)
    name = 0.0
    results["res_low"] = tf.compat.v1.nn.relu(features=features,name=name,)
    t_start = time.time()
    results["res_low"] = tf.compat.v1.nn.relu(features=features,name=name,)
    t_end = time.time()
    results["time_low"] = t_end - t_start
  except Exception as e:
    results["err_low"] = "Error:"+str(e)
  try:
    features = tf.identity(features_tensor)
    features = tf.cast(features, tf.int8)
    results["res_high"] = tf.compat.v1.nn.relu(features=features,name=name,)
    t_start = time.time()
    results["res_high"] = tf.compat.v1.nn.relu(features=features,name=name,)
    t_end = time.time()
    results["time_high"] = t_end - t_start
  except Exception as e:
    results["err_high"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
