"""
Created on 2021/04/25
@author: cyr
@site: https://github.com/Doriskirsy
@description: useful functions for calculating results
"""


# 根据选项累加分数
def add_score(opt):
    import params
    if opt == 'A':
        params.Scores[params.OptionA2idx[params.Round_now - 1]] += 1        # 选项A对应的人格特征得分加一
    elif opt == 'B':
        params.Scores[params.OptionB2idx[params.Round_now - 1]] += 1        # 选项B对应的人格特征得分加一


# 计算MBTI类型
def cal_MBTI():
    import params
    for i in range(4):      # MBTI的四个维度
        if params.Scores[2 * i] > params.Scores[2 * i + 1]:         # 取得分较高的特征为某一维度的偏好
            params.MBTI += params.Idx2dim[int(2 * i)]
        else:
            params.MBTI += params.Idx2dim[int(2 * i + 1)]
