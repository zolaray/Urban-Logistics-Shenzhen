
import torch
import torch.nn as nn
import torch.nn.functional as F
class GCNLayer(nn.Module):
    """Spatial Convolution Layer"""
    def __init__(self, in_dim, out_dim):
        super(GCNLayer, self).__init__()
        self.linear = nn.Linear(in_dim, out_dim)
    def forward(self, adj, x):
        # The math: AxW (Adjacency * Features * Weights)
        # This captures how traffic moves from one road to another
        out = torch.matmul(adj, x)
        return self.linear(out)
class TGCN(nn.Module):
    """Temporal Graph Convolutional Network for Shenzhen Traffic"""
    def __init__(self, adj, input_dim, hidden_dim):
        super(TGCN, self).__init__()
        self.adj = adj
        self.gcn = GCNLayer(input_dim, hidden_dim)
        self.gru = nn.GRUCell(hidden_dim, hidden_dim)
    def forward(self, x, hidden):
        # Step 1: Spatial Feature Extraction
        spatial_features = self.gcn(self.adj, x)
        # Step 2: Temporal Evolution
        new_hidden = self.gru(spatial_features, hidden)
        return new_hidden
