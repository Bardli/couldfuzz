results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      x_0 = -1.0
      x_1 = -0.1
      x_2 = 0.1
      x_3 = 1.0
      x = [x_0,x_1,x_2,x_3,]
      name_tensor = tf.random.uniform([2, 1], minval=-256, maxval=257, dtype=tf.int32)
      name = tf.identity(name_tensor)
      name = tf.Variable(name)
      results["res_cpu"] = tf.raw_ops.BesselI0(x=x,name=name,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      x = [x_0,x_1,x_2,x_3,]
      name = tf.identity(name_tensor)
      name = tf.cast(name, tf.int32)
      name = tf.Variable(name)
      results["res_gpu"] = tf.raw_ops.BesselI0(x=x,name=name,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
