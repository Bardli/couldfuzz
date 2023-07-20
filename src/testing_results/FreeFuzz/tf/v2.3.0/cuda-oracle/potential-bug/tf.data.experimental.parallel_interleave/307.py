results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      map_func_0_tensor = tf.random.uniform([10, 5], minval=-256, maxval=257, dtype=tf.int64)
      map_func_0 = tf.identity(map_func_0_tensor)
      map_func_1_tensor = tf.complex(tf.random.uniform([10, 5], dtype=tf.float64),tf.random.uniform([10, 5], dtype=tf.float64))
      map_func_1 = tf.identity(map_func_1_tensor)
      map_func = [map_func_0,map_func_1,]
      cycle_length = "/cpu:0"
      block_length = None
      sloppy = None
      results["res_cpu"] = tf.data.experimental.parallel_interleave(map_func=map_func,cycle_length=cycle_length,block_length=block_length,sloppy=sloppy,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      map_func_0 = tf.identity(map_func_0_tensor)
      map_func_0 = tf.cast(map_func_0, tf.int64)
      map_func_1 = tf.identity(map_func_1_tensor)
      map_func_1 = tf.cast(map_func_1, tf.complex128)
      map_func = [map_func_0,map_func_1,]
      results["res_gpu"] = tf.data.experimental.parallel_interleave(map_func=map_func,cycle_length=cycle_length,block_length=block_length,sloppy=sloppy,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
