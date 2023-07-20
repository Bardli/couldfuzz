results = dict()
import tensorflow as tf
import time
try:
  try:
    inputs_0_tensor = tf.complex(tf.random.uniform([], dtype=tf.float32),tf.random.uniform([], dtype=tf.float32))
    inputs_0 = tf.identity(inputs_0_tensor)
    inputs_1_tensor = tf.random.uniform([], dtype=tf.bfloat16)
    inputs_1 = tf.identity(inputs_1_tensor)
    inputs = [inputs_0,inputs_1,]
    results["res_low"] = tf.compat.v1.keras.layers.add(inputs=inputs,)
    t_start = time.time()
    results["res_low"] = tf.compat.v1.keras.layers.add(inputs=inputs,)
    t_end = time.time()
    results["time_low"] = t_end - t_start
  except Exception as e:
    results["err_low"] = "Error:"+str(e)
  try:
    inputs_0 = tf.identity(inputs_0_tensor)
    inputs_0 = tf.cast(inputs_0, tf.complex64)
    inputs_1 = tf.identity(inputs_1_tensor)
    inputs_1 = tf.cast(inputs_1, tf.bfloat16)
    inputs = [inputs_0,inputs_1,]
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
