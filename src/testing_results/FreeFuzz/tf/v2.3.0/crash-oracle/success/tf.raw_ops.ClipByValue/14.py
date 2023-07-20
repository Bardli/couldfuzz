import tensorflow as tf
try:
  t_tensor = tf.random.uniform([], dtype=tf.float64)
  t = tf.identity(t_tensor)
  clip_value_min = 0.9
  clip_value_max = 49.1
  name = None
  results["res"] = tf.raw_ops.ClipByValue(t=t,clip_value_min=clip_value_min,clip_value_max=clip_value_max,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
