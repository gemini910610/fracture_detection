import torch
from torch import nn
from torch.nn import functional

class SquarePadding(nn.Module):
    def forward(self, tensor):
        height, width = tensor.shape[1:]
        size = max(height, width)
        padding_left = (size - width) // 2
        padding_top = (size - height) // 2
        padding_right = size - width - padding_left
        padding_bottom = size - height - padding_top
        tensor = functional.pad(tensor, (padding_left, padding_right, padding_top, padding_bottom))
        padding = torch.tensor([padding_left, padding_top])
        return tensor, padding
