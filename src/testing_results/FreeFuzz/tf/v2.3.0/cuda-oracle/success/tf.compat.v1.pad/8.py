results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      tensor_tensor = tf.random.uniform([16, 8, 8, 512], dtype=tf.float32)
      tensor = tf.identity(tensor_tensor)
      paddings_0_0 = -5
      paddings_0_1 = 3
      paddings_0 = [paddings_0_0,paddings_0_1,]
      paddings_1_0 = -1025
      paddings_1_1 = -3
      paddings_1 = [paddings_1_0,paddings_1_1,]
      paddings_2_0 = 3
      paddings_2_1 = 1
      paddings_2 = [paddings_2_0,paddings_2_1,]
      paddings_3_0 = 0
      paddings_3_1 = -1024
      paddings_3 = [paddings_3_0,paddings_3_1,]
      paddings = [paddings_0,paddings_1,paddings_2,paddings_3,]
      mode = ""
      name = None
      constant_values = 0
      results["res_cpu"] = tf.compat.v1.pad(tensor=tensor,paddings=paddings,mode=mode,name=name,constant_values=constant_values,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      tensor = tf.identity(tensor_tensor)
      tensor = tf.cast(tensor, tf.float32)
      paddings_0 = [paddings_0_0,paddings_0_1,]
      paddings_1 = [paddings_1_0,paddings_1_1,]
      paddings_2 = [paddings_2_0,paddings_2_1,]
      paddings_3 = [paddings_3_0,paddings_3_1,]
      paddings = [paddings_0,paddings_1,paddings_2,paddings_3,]
      results["res_gpu"] = tf.compat.v1.pad(tensor=tensor,paddings=paddings,mode=mode,name=name,constant_values=constant_values,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
