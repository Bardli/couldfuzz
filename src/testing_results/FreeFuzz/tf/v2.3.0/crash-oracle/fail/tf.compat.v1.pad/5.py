import tensorflow as tf
try:
  tensor_tensor = tf.random.uniform([16, 4, 4, 512], minval=-256, maxval=257, dtype=tf.int64)
  tensor = tf.identity(tensor_tensor)
  paddings_0_0 = 1024
  paddings_0_1 = 0
  paddings_0 = [paddings_0_0,paddings_0_1,]
  paddings_1_0 = 1
  paddings_1_1 = 1
  paddings_1 = [paddings_1_0,paddings_1_1,]
  paddings_2_0 = 0
  paddings_2_1 = -1
  paddings_2 = [paddings_2_0,paddings_2_1,]
  paddings_3_0 = -1
  paddings_3_1 = 1
  paddings_3 = [paddings_3_0,paddings_3_1,]
  paddings = [paddings_0,paddings_1,paddings_2,paddings_3,]
  mode = "REFLECT"
  name = None
  constant_values = 0
  results["res"] = tf.compat.v1.pad(tensor=tensor,paddings=paddings,mode=mode,name=name,constant_values=constant_values,)
except Exception as e:
  results["err"] = "Error:"+str(e)
