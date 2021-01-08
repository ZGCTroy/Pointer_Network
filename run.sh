#!/usr/bin/env bash

# --fastTest 使用快速测试，仅有100个网络
# --device=['cpu','cuda:0','cuda:1','cuda:2','cuda:3'], 默认为cpu
# --loadModelPath='../models/XXX', 默认为''即不读取, 初始化网络时读取预训练的模型
# --loadModelPath='../models/XXX', 默认为''即不保存, 保存训练过程中的模型到本地
# --logPath='../logs'
# --inputType=[1,2,3]分别对应三种网络输入，即1=仅物理节点下标，2=仅物理节点资源，3=物理节点资源和链路资源

# 快速测试
python main.py --requestNum=10 --firstTry=2 --batchSize=2 --iteration=1 --inputType=1 --device=cuda:0

# 完全测试
python main.py --requestNum=500 --firstTry=250 --batchSize=30 --iteration=30 --inputType=1 --device=cuda:0

# 显示结果
python Plot.py


#python3 main.py --fastTest --batchSize=10 --iteration=10 --dropout=0.0 --device='cuda:0' --loadModelPath='' --saveModelPath='../models/1'
# python3 main.py --batchSize=2 --iteration=10 --dropout=a0.0 --device='cuda:0' --loadModelPath='../models/2020.01.12' --saveModelPath='../models/2020.01.12(1)'