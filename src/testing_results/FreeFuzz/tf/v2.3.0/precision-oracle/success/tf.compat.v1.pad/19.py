results = dict()
import tensorflow as tf
import time
try:
  try:
    tensor_tensor = tf.saturate_cast(tf.random.uniform([3, 64, 64, 512], minval=0, maxval=257, dtype=tf.int64), dtype=tf.uint16)
    tensor = tf.identity(tensor_tensor)
    paddings_0_0 = 0
    paddings_0_1 = 0
    paddings_0 = [paddings_0_0,paddings_0_1,]
    paddings_1_0 = 1
    paddings_1_1 = 1
    paddings_1 = [paddings_1_0,paddings_1_1,]
    paddings_2_0 = 1
    paddings_2_1 = 1
    paddings_2 = [paddings_2_0,paddings_2_1,]
    paddings_3_0 = 0
    paddings_3_1 = 0
    paddings_3 = [paddings_3_0,paddings_3_1,]
    paddings = [paddings_0,paddings_1,paddings_2,paddings_3,]
    mode = "REFLECT"
    name = None
    constant_values = -24.0
    results["res_low"] = tf.compat.v1.pad(tensor=tensor,paddings=paddings,mode=mode,name=name,constant_values=constant_values,)
    t_start = time.time()
    results["res_low"] = tf.compat.v1.pad(tensor=tensor,paddings=paddings,mode=mode,name=name,constant_values=constant_values,)
    t_end = time.time()
    results["time_low"] = t_end - t_start
  except Exception as e:
    results["err_low"] = "Error:"+str(e)
  try:
    tensor = tf.identity(tensor_tensor)
    tensor = tf.cast(tensor, tf.uint16)
    paddings_0 = [paddings_0_0,paddings_0_1,]
    paddings_1 = [paddings_1_0,paddings_1_1,]
    paddings_2 = [paddings_2_0,paddings_2_1,]
    paddings_3 = [paddings_3_0,paddings_3_1,]
    paddings = [paddings_0,paddings_1,paddings_2,paddings_3,]
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
