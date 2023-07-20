results = dict()
import tensorflow as tf
import time
try:
  try:
    name = "global_average_pooling2d"
    trainable = True
    dtype = "float32"
    data_format = "channels_first"
    batch_input_shape_0 = 3
    batch_input_shape_1 = 4
    batch_input_shape_2 = 5
    batch_input_shape_3 = 6
    batch_input_shape = [batch_input_shape_0,batch_input_shape_1,batch_input_shape_2,batch_input_shape_3,]
    results["res_low"] = tf.keras.layers.GlobalAveragePooling2D(name=name,trainable=trainable,dtype=dtype,data_format=data_format,batch_input_shape=batch_input_shape,)
    t_start = time.time()
    results["res_low"] = tf.keras.layers.GlobalAveragePooling2D(name=name,trainable=trainable,dtype=dtype,data_format=data_format,batch_input_shape=batch_input_shape,)
    t_end = time.time()
    results["time_low"] = t_end - t_start
  except Exception as e:
    results["err_low"] = "Error:"+str(e)
  try:
    batch_input_shape = [batch_input_shape_0,batch_input_shape_1,batch_input_shape_2,batch_input_shape_3,]
    results["res_high"] = tf.keras.layers.GlobalAveragePooling2D(name=name,trainable=trainable,dtype=dtype,data_format=data_format,batch_input_shape=batch_input_shape,)
    t_start = time.time()
    results["res_high"] = tf.keras.layers.GlobalAveragePooling2D(name=name,trainable=trainable,dtype=dtype,data_format=data_format,batch_input_shape=batch_input_shape,)
    t_end = time.time()
    results["time_high"] = t_end - t_start
  except Exception as e:
    results["err_high"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)