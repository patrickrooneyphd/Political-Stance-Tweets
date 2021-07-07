# test_nb_functions.py
# A few unit tests of the nb_functions

import pytest
import os
# import matplotlib.pyplot as plt
from nb_functions import *

nb_dir = '/Users/pjrooney/Dropbox/Rotman/Research/_Dissertation/PoliticalStancesAndStrategy/5_Data/4_F100Tweets\
/Political Stance Tweets/notebooks'


def test_set_project_root():
    os.chdir(nb_dir)
    os.chdir('..')
    root_dir = os.getcwd()
    assert set_project_root() == root_dir


def test_set_project_root_nb_subdir():
    os.chdir(nb_dir)
    os.chdir('..')
    root_dir = os.getcwd()
    assert set_project_root() == root_dir


def test_set_project_root_other_subdir():
    os.chdir(nb_dir)
    os.chdir('..')
    root_dir = os.getcwd()
    data_dir = os.path.join(root_dir + '/data')
    os.chdir(data_dir)
    assert set_project_root() == root_dir
