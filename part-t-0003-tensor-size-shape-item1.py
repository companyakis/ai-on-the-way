import torch

tensor1 = torch.tensor([55_600, 62_000, 48_600])

tensor2 = torch.tensor(30_000)

print(f"Tensor 1 shape: {tensor1.shape} - size: {tensor1.size()} and tensor elements: {tensor1[0].item()}-{tensor1[1].item()}-{tensor1[2].item()}")

print(f"Tensor 2 shape: {tensor2.shape} - size: {tensor2.size()}- element: {tensor2.item()}")

# Tensor 1 shape: torch.Size([3]) - size: torch.Size([3]) and tensor elements: 55600-62000-48600
# Tensor 2 shape: torch.Size([]) - size: torch.Size([])- element: 30000
