import tensorflow as tf
try:
  shape_0_tensor = tf.random.uniform([], minval=-256, maxval=257, dtype=tf.int64)
  shape_0 = tf.identity(shape_0_tensor)
  shape_1 = -1
  shape = [shape_0,shape_1,]
  dtype = "int64"
  results["res"] = tf.ones(shape=shape,dtype=dtype,)
except Exception as e:
  results["err"] = "Error:"+str(e)
