import csv
from classes.tf_api import TFAPI
from classes.torch_api import TorchAPI
from classes.database import TorchDatabase
from classes.database import TFDatabase
from classes.torch_api import TorchArgument
from classes.tf_api import TFArgument
from classes.tf_api import TFArgument
from pymongo import MongoClient
import pymongo
client = MongoClient('mongodb://localhost:27017')
host = "127.0.0.1"
port = 27017
database_name = "freefuzz-tf"
DB = pymongo.MongoClient(host=host, port=port)[database_name]

db = client[database_name]


def generate_args_from_record_tf(record: dict) -> dict:
    args = {}
    for key in record.keys():
        if key != "output_signature":
            args[key] = TFArgument.generate_arg_from_signature(
                record[key])
    return args


def generate_args_from_record_torch(record: dict) -> dict:
    args = {}
    for key in record.keys():
        if key != "output_signature":
            args[key] = TorchArgument.generate_arg_from_signature(
                record[key])
    return args


with open('/media/nimashiri/DATA/vsprojects/benchmarkingDLFuzzers/dataset/v2.6.0_test.txt', 'r') as file:
    torch_test = [line.rstrip('\n') for line in file.readlines()]


def convert_arg_to_code(api):
    prefix = "arg"
    args = []
    kwargs = {}
    for key in api.args.keys():
        if "parameter:" in key:
            args.append(api.args[key])
        elif key != "output_signature" and key != "input_signature":
            kwargs[key] = api.args[key]

    arg_code = ""
    arg_str = ""
    index = 0
    for arg in args:
        arg_code += arg.to_code(f"{prefix}_{index}")
        arg_str += f"{prefix}_{index},"
        index += 1
    for key, arg in kwargs.items():
        arg_code += arg.to_code(key)
        arg_str += "%s=%s," % (key, key)
    return arg_code, arg_str


def convert_arg_to_code_dict(api):
    prefix = "arg"
    args = []
    kwargs = {}
    for key in api.keys():
        if "parameter:" in key:
            args.append(api[key])
        elif key != "output_signature" and key != "input_signature":
            kwargs[key] = api[key]

    arg_code = ""
    arg_str = ""
    index = 0
    for arg in args:
        arg_code += arg.to_code(f"{prefix}_{index}")
        arg_str += f"{prefix}_{index},"
        index += 1
    for key, arg in kwargs.items():
        arg_code += arg.to_code(key)
        arg_str += "%s=%s," % (key, key)
    return arg_code, arg_str


for api_name in torch_test:
    record = DB[api_name].find()
    document_id = str(record['_id'])
    record.pop("_id")
    # Retrieve all documents from the collection
    arg_d = generate_args_from_record_tf(record)
    arg_code, arg_str = convert_arg_to_code_dict(arg_d)
    data_ = [api_name, arg_code, document_id]
    with open(f'/media/nimashiri/DATA/vsprojects/benchmarkingDLFuzzers/dataset/tf-testdata.csv', 'a', newline='\n') as fd:
        writer_object = csv.writer(fd)
        writer_object.writerow(data_)

    # documents = collection.find()
    # Iterate over the documents
    # for document in documents:
    #     document_id = str(document['_id'])
    #     # document.pop("_id")
    #     # arg_d = generate_args_from_record(document)
    #     arg_code, arg_str = convert_arg_to_code(arg_d)
    #     data_ = [api_name, arg_code]
