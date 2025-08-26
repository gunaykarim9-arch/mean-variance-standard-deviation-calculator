import numpy as np

def calculate(numbers):
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")

    a = np.array(numbers).reshape(3, 3)

    result = {
        'mean': [
            a.mean(axis=0).tolist(),      # columns
            a.mean(axis=1).tolist(),      # rows
            a.mean().item()               # flattened
        ],
        'variance': [
            a.var(axis=0).tolist(),
            a.var(axis=1).tolist(),
            a.var().item()
        ],
        'standard deviation': [
            a.std(axis=0).tolist(),
            a.std(axis=1).tolist(),
            a.std().item()
        ],
        'max': [
            a.max(axis=0).tolist(),
            a.max(axis=1).tolist(),
            a.max().item()
        ],
        'min': [
            a.min(axis=0).tolist(),
            a.min(axis=1).tolist(),
            a.min().item()
        ],
        'sum': [
            a.sum(axis=0).tolist(),
            a.sum(axis=1).tolist(),
            a.sum().item()
        ]
    }
    return result
