# -*- coding: utf-8 -*-
import importlib
import os


def import_models():
    dirname = os.path.dirname(__file__)
    for module in os.listdir(dirname):
        models_module_file = '{0}/models.py'.format(module)
        if os.path.exists(os.path.join(dirname, models_module_file)):
            models_module = 'app/services/{0}'.format(models_module_file[:-3]).replace('/', '.')
            importlib.import_module(models_module)
    del module
