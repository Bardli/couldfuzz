import tensorflow as tf
try:
  t_tensor = tf.random.uniform([5, 1], dtype=tf.float64)
  t = tf.identity(t_tensor)
  clip_value_min = 1e+20
  clip_value_max = 86.1
  name = None
  results["res"] = tf.raw_ops.ClipByValue(t=t,clip_value_min=clip_value_min,clip_value_max=clip_value_max,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
