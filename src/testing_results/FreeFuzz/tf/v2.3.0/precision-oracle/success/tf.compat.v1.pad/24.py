results = dict()
import tensorflow as tf
import time
try:
  try:
    tensor_tensor = tf.saturate_cast(tf.random.uniform([1, 379], minval=-256, maxval=257, dtype=tf.int64), dtype=tf.int8)
    tensor = tf.identity(tensor_tensor)
    paddings_tensor = tf.saturate_cast(tf.random.uniform([2, 2], minval=0, maxval=257, dtype=tf.int64), dtype=tf.uint16)
    paddings = tf.identity(paddings_tensor)
    mode = "CONSTANT"
    name = None
    constant_values = True
    results["res_low"] = tf.compat.v1.pad(tensor=tensor,paddings=paddings,mode=mode,name=name,constant_values=constant_values,)
    t_start = time.time()
    results["res_low"] = tf.compat.v1.pad(tensor=tensor,paddings=paddings,mode=mode,name=name,constant_values=constant_values,)
    t_end = time.time()
    results["time_low"] = t_end - t_start
  except Exception as e:
    results["err_low"] = "Error:"+str(e)
  try:
    tensor = tf.identity(tensor_tensor)
    tensor = tf.cast(tensor, tf.int32)
    paddings = tf.identity(paddings_tensor)
    paddings = tf.cast(paddings, tf.uint16)
    results["res_high"] = tf.compat.v1.pad(tensor=tensor,paddings=paddings,mode=mode,name=name,constant_values=constant_values,)
    t_start = time.time()
    results["res_high"] = tf.compat.v1.pad(tensor=tensor,paddings=paddings,mode=mode,name=name,constant_values=constant_values,)
    t_end = time.time()
    results["time_high"] = t_end - t_start
  except Exception as e:
    results["err_high"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
