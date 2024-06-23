import torch
import torch.nn as nn


class Stable_softmax(nn.Module):

    def softmax_stable(self, one_d_tensor):
        max_value_in_tensor = torch.max(one_d_tensor, dim=0)
        denominator = torch.sum(
            torch.exp(one_d_tensor - max_value_in_tensor.values))
        numerator = torch.exp(one_d_tensor - max_value_in_tensor.values)
        result = numerator / denominator
        return result

    def __init__(self):
        super().__init__()


data = torch.Tensor([1, 2, 3])
stable_softmax = Stable_softmax()
print(stable_softmax.softmax_stable(data))
