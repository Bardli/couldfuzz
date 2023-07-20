import tensorflow as tf
try:
  map_func_0_tensor = tf.random.uniform([10, 5], dtype=tf.float32)
  map_func_0 = tf.identity(map_func_0_tensor)
  map_func_1_tensor = tf.random.uniform([10, 5], dtype=tf.float32)
  map_func_1 = tf.identity(map_func_1_tensor)
  map_func = [map_func_0,map_func_1,]
  cycle_length = "zeros"
  block_length_tensor = tf.random.uniform([2, 2], minval=-256, maxval=257, dtype=tf.int32)
  block_length = tf.identity(block_length_tensor)
  sloppy = None
  results["res"] = tf.data.experimental.parallel_interleave(map_func=map_func,cycle_length=cycle_length,block_length=block_length,sloppy=sloppy,)
except Exception as e:
  results["err"] = "Error:"+str(e)
