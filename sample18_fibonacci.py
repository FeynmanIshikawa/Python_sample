# -*- coding: utf-8 -*-

import numpy as np

class fibonacci():
        
    mat00 = np.array([[1,1],[1,0]])
    mat01 = np.inner(mat00, mat00)
    mat02 = np.inner(mat00, mat01)
    mat03 = np.inner(mat00, mat02)
    mat04 = np.inner(mat00, mat03)
    mat05 = np.inner(mat00, mat04)
    mat06 = np.inner(mat00, mat05)
    mat07 = np.inner(mat00, mat06)
    mat08 = np.inner(mat00, mat07)
    mat09 = np.inner(mat00, mat08)
    mat10 = np.inner(mat00, mat09)
    mat11 = np.inner(mat00, mat10)
    mat12 = np.inner(mat00, mat11)

    print(mat00)
    print(mat01)
    print(mat02)
    print(mat03)
    print(mat04)
    print(mat05)
    print(mat06)
    print(mat07)
    print(mat08)
    print(mat09)
    print(mat10)
    print(mat11)
    print(mat12)
