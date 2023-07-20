results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      tensor_tensor = tf.random.uniform([2, 4, 4, 512], dtype=tf.float32)
      tensor = tf.identity(tensor_tensor)
      paddings_0_0 = 0
      paddings_0_1 = 0
      paddings_0 = [paddings_0_0,paddings_0_1,]
      paddings_1_0 = 1
      paddings_1_1 = 1
      paddings_1 = [paddings_1_0,paddings_1_1,]
      paddings_2_0 = 1
      paddings_2_1 = 1
      paddings_2 = [paddings_2_0,paddings_2_1,]
      paddings_3_0 = 0
      paddings_3_1 = 0
      paddings_3 = [paddings_3_0,paddings_3_1,]
      paddings = [paddings_0,paddings_1,paddings_2,paddings_3,]
      mode = "REFLECT"
      name_tensor = tf.random.uniform([1, 1], dtype=tf.float64)
      name = tf.identity(name_tensor)
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
      name = tf.identity(name_tensor)
      name = tf.cast(name, tf.float64)
      results["res_gpu"] = tf.compat.v1.pad(tensor=tensor,paddings=paddings,mode=mode,name=name,constant_values=constant_values,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
