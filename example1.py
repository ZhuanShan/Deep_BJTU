class Mylayer(torch.nn.Module):
    def __init__(self, in_features, out_features, bias= True):
        super(Mylayer,self).init__()
        self.in_features = in_features
        self.out_featurs = out_features
        self.weight = torch.nn.Parameter(Torch.Tensor(in_features, out_features ))