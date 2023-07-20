results = dict()
import tensorflow as tf
import time
try:
  try:
    features_tensor = tf.cast(tf.random.uniform([4, 1, 2048], minval=0, maxval=2, dtype=tf.int32), dtype=tf.bool)
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
    features = tf.cast(features, tf.bool)
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
