#!/usr/bin/env python

"""Doctring"""

from operator import itemgetter
import argparse

class EmployeeQuery(object):
    """Doctring"""
    def __init__(self):
        """Doctring"""
        with open('employees.csv', 'r') as f:
            raw_data = f.readlines()
        self.data = []
        for line in raw_data:
            line = line.strip().split(',')
            line_dict = {}
            line_dict['LastName'] = line[0]
            line_dict['FirstName'] = line[1]
            line_dict['Position'] = line[2]
            line_dict['Manager'] = line[3]
            line_dict['Email'] = line[4].replace('email=','')

            # Parse the optional parameters in the 6th column
            line_dict['reports_to'] = 'none'
            line_dict['phone'] = 'none'
            try: 
                optional_parameters = line[5].split(';')
                for parameter in optional_parameters:
                    key, value = parameter.split('=')
                    line_dict[key] = value
            except IndexError:
                pass

            self.data.append(line_dict)

    def order(self, key):
        self.data = sorted(self.data, key=itemgetter(key))

    def print_results(self):
        for record in self.data:
            print '| {LastName:^20} | {FirstName:^20} | {Position:^20} | '\
                  '{Manager:^20} | {Email:^20} | {reports_to:^20} | '\
                  '{phone:^20} |'.format(**record)

    def select(self, key, query, value):
        if query == 'is':
            self.data = [record for record in self.data 
                         if record[key] == value]
        elif query == 'is not':
            self.data = [record for record in self.data 
                         if record[key] != value]


def parse_input():
    field_list = ['LastName', 'FirstName', 'Position', 'Manager', 'Email', 
                  'reports_to', 'phone']
    print 'Choose a field: '
    print '\t {}'.format(field_list)
    field = raw_input('> ')
    while field not in field_list:
        print 'Opps, please choose a field from the list.'
        field = raw_input('> ')

    query_list = ['is', 'is not']
    print 'Choose a query type: '
    print '\t {}'.format(query_list)
    query = raw_input('> ')
    while query not in query_list:
        print 'Opps, please choose a query from the list.'
        query = raw_input('> ')

    print 'What value to query for?'
    value = raw_input('> ')

    print 'Choose a field to sort on:'
    print '\t {}'.format(field_list)
    sort = raw_input('> ')
    while sort not in field_list:
        print 'Opps, please choose a sorting option from the list.'
        sort = raw_input('> ')

    return field, query, value, sort

def main():
    eq = EmployeeQuery()
    requery = 'yes'
    while requery == 'yes':
        field, query, value, sort = parse_input()
        print 'Querying for {} {} {}'.format(field, query, value)
        eq.select(field, query, value)
        eq.order(sort)
        eq.print_results()
        print 'Would you like to query on these results? (yes/no)'
        requery = raw_input('> ')
        while requery not in ['yes', 'no']:
            print 'Opps. Please choose yes or no.'

if __name__ == '__main__':
    main()

