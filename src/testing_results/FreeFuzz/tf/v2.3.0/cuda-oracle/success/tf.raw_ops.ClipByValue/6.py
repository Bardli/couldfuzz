results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      t_tensor = tf.random.uniform([5, 1], dtype=tf.float64)
      t = tf.identity(t_tensor)
      clip_value_min = 1e+20
      clip_value_max = 86.1
      name = None
      results["res_cpu"] = tf.raw_ops.ClipByValue(t=t,clip_value_min=clip_value_min,clip_value_max=clip_value_max,name=name,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      t = tf.identity(t_tensor)
      t = tf.cast(t, tf.float64)
      results["res_gpu"] = tf.raw_ops.ClipByValue(t=t,clip_value_min=clip_value_min,clip_value_max=clip_value_max,name=name,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
