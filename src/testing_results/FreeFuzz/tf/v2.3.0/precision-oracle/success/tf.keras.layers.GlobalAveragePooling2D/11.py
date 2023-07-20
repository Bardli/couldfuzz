results = dict()
import tensorflow as tf
import time
try:
  try:
    name = "global_average_pooling2d"
    trainable = False
    dtype = "float32"
    data_format = "channels_first"
    results["res_low"] = tf.keras.layers.GlobalAveragePooling2D(name=name,trainable=trainable,dtype=dtype,data_format=data_format,)
    t_start = time.time()
    results["res_low"] = tf.keras.layers.GlobalAveragePooling2D(name=name,trainable=trainable,dtype=dtype,data_format=data_format,)
    t_end = time.time()
    results["time_low"] = t_end - t_start
  except Exception as e:
    results["err_low"] = "Error:"+str(e)
  try:
    results["res_high"] = tf.keras.layers.GlobalAveragePooling2D(name=name,trainable=trainable,dtype=dtype,data_format=data_format,)
    t_start = time.time()
    results["res_high"] = tf.keras.layers.GlobalAveragePooling2D(name=name,trainable=trainable,dtype=dtype,data_format=data_format,)
    t_end = time.time()
    results["time_high"] = t_end - t_start
  except Exception as e:
    results["err_high"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
