import tensorflow as tf
try:
  name = "global_average_pooling2d"
  trainable = True
  batch_input_shape_0 = 3
  batch_input_shape_1 = 4
  batch_input_shape_2 = 5
  batch_input_shape_3 = 6
  batch_input_shape = [batch_input_shape_0,batch_input_shape_1,batch_input_shape_2,batch_input_shape_3,]
  dtype = "float32"
  data_format = "channels_first"
  results["res"] = tf.keras.layers.GlobalAveragePooling2D(name=name,trainable=trainable,batch_input_shape=batch_input_shape,dtype=dtype,data_format=data_format,)
except Exception as e:
  results["err"] = "Error:"+str(e)
