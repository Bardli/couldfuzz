results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      t_tensor = tf.random.uniform([1, 472, 496, 3], dtype=tf.float32)
      t = tf.identity(t_tensor)
      clip_value_min = 0
      clip_value_max = 255
      name = None
      results["res_cpu"] = tf.raw_ops.ClipByValue(t=t,clip_value_min=clip_value_min,clip_value_max=clip_value_max,name=name,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      t = tf.identity(t_tensor)
      t = tf.cast(t, tf.float32)
      results["res_gpu"] = tf.raw_ops.ClipByValue(t=t,clip_value_min=clip_value_min,clip_value_max=clip_value_max,name=name,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
