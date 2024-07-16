#!/usr/bin/env python3
''' 8 All'''


def list_all(mongo_collection):
    ''' list all docs in a collection '''
    return [doc for doc in mongo_collection.find()]
