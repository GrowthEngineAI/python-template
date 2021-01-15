

def check_imports():
    avail = {'colab': False, 'libs': {}}
    try:
        import google.colab
        avail['colab'] = True
    except ImportError:
        avail['colab'] = False
    
    try:
        import tensorflow as tf
        avail['libs']['tensorflow'] = True
    except ImportError:
        avail['libs']['tensorflow'] = False

    try:
        import redis
        avail['libs']['redis'] = True
    except ImportError:
        avail['libs']['redis'] = False

    try:
        import transformers
        avail['libs']['transformers'] = True
    except ImportError:
        avail['libs']['transformers'] = False

    try:
        import tokenizers
        avail['libs']['tokenizers'] = True
    except ImportError:
        avail['libs']['tokenizers'] = False

    try:
        import tensorflow_datasets
        avail['libs']['tfds'] = True
    except ImportError:
        avail['libs']['tfds'] = False

    try:
        from google.cloud import storage
        avail['libs']['gcs'] = True
    except ImportError:
        avail['libs']['gcs'] = False

    try:
        import smart_open
        avail['libs']['smart_open'] = True
    except ImportError:
        avail['libs']['smart_open'] = False

    try:
        import ray
        avail['libs']['ray'] = True
    except ImportError:
        avail['libs']['ray'] = False

    try:
        import torch
        avail['libs']['pytorch'] = True
    except ImportError:
        avail['libs']['pytorch'] = False

    try:
        import tqdm.auto
        avail['libs']['tqdm'] = True
    except ImportError:
        avail['libs']['tqdm'] = False
    
    try:
        import numpy as np
        avail['libs']['numpy'] = True
    except ImportError:
        avail['libs']['numpy'] = False
    
    try:
        import wandb
        avail['libs']['wandb'] = True
    except ImportError:
        avail['libs']['wandb'] = False
    
    try:
        import boto3
        avail['libs']['boto3'] = True
    except ImportError:
        avail['libs']['boto3'] = False

    return avail


