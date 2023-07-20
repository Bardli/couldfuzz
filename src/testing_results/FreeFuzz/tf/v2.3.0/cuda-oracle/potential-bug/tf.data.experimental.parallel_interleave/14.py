results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      map_func_0_tensor = tf.random.uniform([10, 5], dtype=tf.bfloat16)
      map_func_0 = tf.identity(map_func_0_tensor)
      map_func_1_tensor = tf.saturate_cast(tf.random.uniform([10, 4], minval=0, maxval=257, dtype=tf.int64), dtype=tf.uint32)
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
      map_func_0 = tf.cast(map_func_0, tf.bfloat16)
      map_func_1 = tf.identity(map_func_1_tensor)
      map_func_1 = tf.cast(map_func_1, tf.uint32)
      map_func = [map_func_0,map_func_1,]
      results["res_gpu"] = tf.data.experimental.parallel_interleave(map_func=map_func,cycle_length=cycle_length,block_length=block_length,sloppy=sloppy,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
