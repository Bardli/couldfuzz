results = dict()
import tensorflow as tf
import time
try:
  try:
    t_tensor = tf.random.uniform([2, 3], dtype=tf.float16)
    t = tf.identity(t_tensor)
    clip_value_min = -1
    clip_value_max = 1024
    name = None
    results["res_low"] = tf.raw_ops.ClipByValue(t=t,clip_value_min=clip_value_min,clip_value_max=clip_value_max,name=name,)
    t_start = time.time()
    results["res_low"] = tf.raw_ops.ClipByValue(t=t,clip_value_min=clip_value_min,clip_value_max=clip_value_max,name=name,)
    t_end = time.time()
    results["time_low"] = t_end - t_start
  except Exception as e:
    results["err_low"] = "Error:"+str(e)
  try:
    t = tf.identity(t_tensor)
    t = tf.cast(t, tf.float32)
    results["res_high"] = tf.raw_ops.ClipByValue(t=t,clip_value_min=clip_value_min,clip_value_max=clip_value_max,name=name,)
    t_start = time.time()
    results["res_high"] = tf.raw_ops.ClipByValue(t=t,clip_value_min=clip_value_min,clip_value_max=clip_value_max,name=name,)
    t_end = time.time()
    results["time_high"] = t_end - t_start
  except Exception as e:
    results["err_high"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
