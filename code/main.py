import argparse
import os

os.environ["PYTHONIOENCODING"] = "utf-8"

from Test import test

print(os.getcwd())
os.chdir(os.getcwd())

parser = argparse.ArgumentParser(description='Hello')

# CPU/GPU      ['cpu','cuda:0','cuda:1','cuda:2','cuda:3']
parser.add_argument('--device', type=str, default='cpu')

# 是否打印中间信息
parser.add_argument('--print', action='store_true', default=False)

# BatchSize
parser.add_argument('--batchSize', type=int, default=10)

# ActiveSearch的迭代次数
parser.add_argument('--iteration', type=int, default=10)

# dropout 网络的遗忘率，避免过拟合 0.0 - 1.0
parser.add_argument('--dropout', type=float, default=0.0)

# ../data/XXX
parser.add_argument('--dataPath', type=str, default='../data/data_500')

# 读取与保存网络模型 ../models/XXX
parser.add_argument('--loadModelPath', type=str, default='')        # 例如 '../models/2020.01.12'
parser.add_argument('--saveModelPath', type=str, default='')

# log
parser.add_argument('--logPath', type=str, default='../logs')

# network input
parser.add_argument('--inputType', type=int, default=2)

# request num
parser.add_argument('--requestNum', type=int, default=-1)

# first try
parser.add_argument('--firstTry', type=int, default=250)


# if input_type == 1:
#     choosed_information = 'snode index'
# if input_type == 2:
#     choosed_information = 'snode resource'
# if input_type == 3:
#     choosed_information = 'snode resource and neighbour link resource'

args = parser.parse_args()

if __name__ == '__main__':
    '''
        完全测试参数： fast_test=False, max_request_num=500, first_try = 250
        简单快速测试： fast_test=True, max_request_num=30, first_try = 30
    '''

    test(
        data_path=args.dataPath,
        batch_size=args.batchSize,
        iteration_num=args.iteration,
        max_request_num=args.requestNum,
        load_model_path=args.loadModelPath,
        save_model_path=args.saveModelPath,
        device=args.device,
        log_path = args.logPath,
        dropout = args.dropout,
        input_type = args.inputType,
        first_try = args.firstTry
    )
