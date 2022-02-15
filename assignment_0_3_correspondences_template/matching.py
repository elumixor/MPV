import numpy as np
import math
import torch
import torch.nn.functional as F
import typing


def match_nn(desc1: torch.Tensor, desc2: torch.Tensor):
    """Function, which finds nearest neightbors for each vector in desc1.

    Return:
        torch.Tensor: indexes of matching descriptors in desc1 and desc2
        torch.Tensor: L2 desriptor distance


    Shape:
        - Input :math:`(B1, D)`, :math:`(B2, D)`
        - Output: :math:`(B1, 2)`, :math:`(B1, 1)`
    """
    matches_idxs = torch.arange(0, desc2.size(0)).view(-1, 1).repeat(1, 2)
    match_dists = torch.zeros(desc2.size(0),1)
    return matches_idxs, match_dists


def match_snn(desc1: torch.Tensor, desc2: torch.Tensor, th: float = 0.8):
    """Function, which finds nearest neightbors for each vector in desc1,
    which satisfy first to second nearest neighbor distance <= th check

    Return:
        torch.Tensor: indexes of matching descriptors in desc1 and desc2
        torch.Tensor: L2 desriptor distance ratio 1st to 2nd nearest neighbor


    Shape:
        - Input :math:`(B1, D)`, :math:`(B2, D)`
        - Output: :math:`(B3, 2)`, :math:`(B3, 1)` where 0 <= B3 <= B1
    """
    matches_idxs = torch.arange(0, desc2.size(0)).view(-1, 1).repeat(1, 2)
    match_dists = torch.zeros(desc2.size(0),1)
    return matches_idxs, match_dists

def match_mnn(desc1: torch.Tensor, desc2: torch.Tensor):
    """Function, which finds mutual nearest neightbors for each vector in desc1 and desc2.

    Return:
        torch.Tensor: indexes of matching descriptors in desc1 and desc2
        torch.Tensor: L2 desriptor distance


    Shape:
        - Input :math:`(B1, D)`, :math:`(B2, D)`
        - Output: :math:`(B3, 2)`, :math:`(B3, 1)` where 0 <= B3 <= min(B1,B2)
    """
    matches_idxs = torch.arange(0, desc2.size(0)).view(-1, 1).repeat(1, 2)
    match_dists = torch.zeros(desc2.size(0),1)
    return matches_idxs, match_dists

def match_smnn(desc1: torch.Tensor, desc2: torch.Tensor, th: float = 0.8):
    """Function, which finds mutual nearest neightbors for each vector in desc1 and desc2,
    which satisfy first to second nearest neighbor distance <= th check in both directions.
    So, it is intersection of match_mnn(d1,d2), match_snn(d1,d2), match_snn(d2,d1)
    Resulting distance ratio should be maximum over over distance ratio in both directions

    Return:
        torch.Tensor: indexes of matching descriptors in desc1 and desc2
        torch.Tensor: L2 desriptor distance ratio 1st to 2nd nearest neighbor


    Shape:
        - Input :math:`(B1, D)`, :math:`(B2, D)`
        - Output: :math:`(B3, 2)`, :math:`(B3, 1)`, where 0 <= B3 <= min(B1, B2)
    """
    matches_idxs = torch.arange(0, desc2.size(0)).view(-1, 1).repeat(1, 2)
    match_dists = torch.zeros(desc2.size(0),1)
    return matches_idxs, match_dists

