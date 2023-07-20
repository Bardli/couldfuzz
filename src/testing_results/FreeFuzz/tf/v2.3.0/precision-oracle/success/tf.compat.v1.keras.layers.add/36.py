results = dict()
import tensorflow as tf
import time
try:
  try:
    inputs_0_tensor = tf.saturate_cast(tf.random.uniform([2, 2], minval=-256, maxval=257, dtype=tf.int64), dtype=tf.int8)
    inputs_0 = tf.identity(inputs_0_tensor)
    inputs_1_tensor = tf.saturate_cast(tf.random.uniform([2, 2], minval=-128, maxval=128, dtype=tf.int64), dtype=tf.int8)
    inputs_1 = tf.identity(inputs_1_tensor)
    inputs_2_tensor = tf.cast(tf.random.uniform([2, 2], minval=0, maxval=2, dtype=tf.int32), dtype=tf.bool)
    inputs_2 = tf.identity(inputs_2_tensor)
    inputs = [inputs_0,inputs_1,inputs_2,]
    results["res_low"] = tf.compat.v1.keras.layers.add(inputs=inputs,)
    t_start = time.time()
    results["res_low"] = tf.compat.v1.keras.layers.add(inputs=inputs,)
    t_end = time.time()
    results["time_low"] = t_end - t_start
  except Exception as e:
    results["err_low"] = "Error:"+str(e)
  try:
    inputs_0 = tf.identity(inputs_0_tensor)
    inputs_0 = tf.cast(inputs_0, tf.int32)
    inputs_1 = tf.identity(inputs_1_tensor)
    inputs_1 = tf.cast(inputs_1, tf.int8)
    inputs_2 = tf.identity(inputs_2_tensor)
    inputs_2 = tf.cast(inputs_2, tf.bool)
    inputs = [inputs_0,inputs_1,inputs_2,]
    results["res_high"] = tf.compat.v1.keras.layers.add(inputs=inputs,)
    t_start = time.time()
    results["res_high"] = tf.compat.v1.keras.layers.add(inputs=inputs,)
    t_end = time.time()
    results["time_high"] = t_end - t_start
  except Exception as e:
    results["err_high"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
