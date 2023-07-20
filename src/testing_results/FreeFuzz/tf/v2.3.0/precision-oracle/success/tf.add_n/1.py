results = dict()
import tensorflow as tf
import time
try:
  try:
    inputs_0_tensor = tf.random.uniform([], dtype=tf.bfloat16)
    inputs_0 = tf.identity(inputs_0_tensor)
    inputs_1_tensor = tf.random.uniform([], dtype=tf.float16)
    inputs_1 = tf.identity(inputs_1_tensor)
    inputs = [inputs_0,inputs_1,]
    name = None
    results["res_low"] = tf.add_n(inputs=inputs,name=name,)
    t_start = time.time()
    results["res_low"] = tf.add_n(inputs=inputs,name=name,)
    t_end = time.time()
    results["time_low"] = t_end - t_start
  except Exception as e:
    results["err_low"] = "Error:"+str(e)
  try:
    inputs_0 = tf.identity(inputs_0_tensor)
    inputs_0 = tf.cast(inputs_0, tf.bfloat16)
    inputs_1 = tf.identity(inputs_1_tensor)
    inputs_1 = tf.cast(inputs_1, tf.float32)
    inputs = [inputs_0,inputs_1,]
    results["res_high"] = tf.add_n(inputs=inputs,name=name,)
    t_start = time.time()
    results["res_high"] = tf.add_n(inputs=inputs,name=name,)
    t_end = time.time()
    results["time_high"] = t_end - t_start
  except Exception as e:
    results["err_high"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
