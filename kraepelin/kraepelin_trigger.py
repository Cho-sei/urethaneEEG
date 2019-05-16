import collections
import csv

trigger_table = 'Trigger-Table.csv'

with open(trigger_table, mode='r') as f:
    parameters_dict = {key:chr(int(value)) for key, value in csv.reader(f)}

KraepelinTriggerValues = collections.namedtuple(
    'KraepelinTriggerValues',
    parameters_dict.keys()
)

trigger_values = KraepelinTriggerValues(**parameters_dict)

if __name__ == "__main__":
    for key, value in trigger_values._asdict().items():
        print("{}\t{}".format(ord(value), key))