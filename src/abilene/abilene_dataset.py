"""
pylearn2 Dataset wrapper for Abilene network data
"""

import numpy as np

from pylearn2.datasets.dense_design_matrix import DenseDesignMatrix
from pylearn2.utils import serial
from pylearn2.utils.string_utils import preprocess


class AbileneDataset(DenseDesginMatrix):
    def __init__(self,path='../../data/abilene/abilene_data_norm.pickle',
                 start=0, stop=None):
        X, y = self._load_data( path, with_labels )
        
        if stop is not None:
            assert isinstance(stop,int)
            assert stop <= X.shape[0]
        else:
            stop = X.shape[0]
        assert isinstance(start,int)
        assert start < stop
        
        X = X[start:stop,:]
        if y is not None:
            y = y[start:stop,:]
        
        super(AbileneDataset, self).__init__(X=X, y=y)
    
    def _load_data(self, path):
        assert path.endswith('.pickle')
        data = np.load('../data/abilene/abilene_data_norm.pickle')
        return  data['X'], data['Y']
    
        