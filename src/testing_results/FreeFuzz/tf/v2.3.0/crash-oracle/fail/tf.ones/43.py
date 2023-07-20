import tensorflow as tf
try:
  arg_0_0_tensor = tf.random.uniform([], minval=-256, maxval=257, dtype=tf.int32)
  arg_0_0 = tf.identity(arg_0_0_tensor)
  arg_0_1 = 1
  arg_0_2 = 1
  arg_0_3 = 1
  arg_0 = [arg_0_0,arg_0_1,arg_0_2,arg_0_3,]
  results["res"] = tf.ones(arg_0,)
except Exception as e:
  results["err"] = "Error:"+str(e)
