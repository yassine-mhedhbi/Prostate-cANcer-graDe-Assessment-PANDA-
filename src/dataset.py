
from PIL import Image
import pandas as pd
import numpy as np
from glob import glob
import os
from torch.utils.data import DataLoader, Dataset
from cv2 import vconcat, hconcat

class PandaTilesDataset(Dataset):
    
    def __init__(self, path, train, masks, csv, preload=False):
        self.train_root = path
        self.df = pd.read_csv(os.path.join(self.train_root, csv)).set_index('image_id')
        self.pairs = list(zip(PandaTilesDataset.glob_imgs(os.path.join(self.train_root, train)), 
                              PandaTilesDataset.glob_imgs(os.path.join(self.train_root, masks))))
        self.preload = preload
        self.data = None
        if preload:
            self.data = [self._open_image(i) for i in range(0, len(self.pairs), 16)]
            
                         
    def __len__(self):
        return len(self.pairs) // 16
    
    
    def _open_image(self, index):
        img_id = self.pairs[index][0].split('/')[-1].split('_')[0] # re is better, maybe later
        h_concat_x = []
        h_concat_y = []
        for i in range(4): 
            hor_x = vconcat([PandaTilesDataset.array_img(self.pairs[index + i * 4 + j][0]) for j in range(4)])
            h_concat_x.append(hor_x)
            hor_y = vconcat([PandaTilesDataset.array_img(self.pairs[index + i * 4 + j][1]) for j in range(4)])
            h_concat_y.append(hor_y)
        
        image = hconcat(h_concat_x)
        mask  = hconcat(h_concat_y)
        desc = self.df.loc[img_id].to_dict()
        desc['image_id'] = img_id
        return image, mask, desc
        
        
    def __getitem__(self, idx):
        if self.preload:
            return self.data[idx]
        
        start_id = idx * 16
        image, mask, desc = self._open_image(start_id)                  
        return image, mask, desc 


    @classmethod
    def array_img(cls, img): 
        return np.array(Image.open(img))

    @classmethod
    def glob_imgs(cls, d):
        return sorted(glob(os.path.join(d, '*.png')))


class Radboud(PandaTilesDataset):

    def __init__(self, path, train, masks, csv, preload=False):
        super().__init__(path, train, masks, csv, preload)
        self.df = self.df[self.df['data_provider'] == 'radboud']
        self.images = list(self.df.index)
        self.pairs = [(x, y) for (x, y) in self.pairs if Radboud.img_id(x) in self.images]


    @classmethod
    def img_id(self, idx):
        img_id = idx.split('/')[-1].split('_')[0]
        return img_id
