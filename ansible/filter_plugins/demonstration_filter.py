""" Utilities for dealing with the VMWare output """
from __future__ import (absolute_import, division, print_function)

def get_top_two(value, data_store_group):
    """ Select the correct data stores, then order them """
    filtered_list = [data_store for data_store in value if data_store_group in data_store['name']]
    sorted_list = sorted(filtered_list, key=lambda k: float(k['free'].split()[0]), reverse=True)
    return sorted_list


class FilterModule(object):
    """ Required FilterModule class that must have a method named
    filters that will return a dictionary that maps filter names
    to callables implementing the filter.

    https://blog.oddbit.com/post/2019-04-25-writing-ansible-filter-plugins/ """

    def filters(self):
        """ Map the filter methods to their names in Ansible """
        return {
            'get_top_two': get_top_two,
        }
