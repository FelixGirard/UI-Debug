# Under MIT License, see LICENSE.txt

from datetime import date

from Model.DataIn.DataInObject import FormatPackageError
from Model.DataIn.LoggingDataIn.BaseDataInLog import BaseDataInLog

__author__ = 'RoboCupULaval'


class LoggingData(BaseDataInLog):
    def __init__(self, data_in):
        BaseDataInLog.__init__(self, data_in)
        self._format_data()

    def _check_obligatory_data(self):
        try:
            assert isinstance(self.data, dict), \
                "data: {} n'est pas un dictionnaire.".format(type(self.data))
        except Exception as e:
            raise FormatPackageError('{}: {}'.format(self.__name__, e))

    def _check_optional_data(self):
        try:
            pass
        except Exception as e:
            raise FormatPackageError('{}: {}'.format(self.__name__, e))

    def __str__(self):
        message = ''
        message += '<{}> '.format(date.strftime(self.time, "%H:%M:%S"))
        message += '"{}": Données multiples:\n'.format(self.name)
        for key, item in sorted(self.data.items()):
            message += '{} = {}'.format(key, item) + '\n'
        return message[:-1]

    @staticmethod
    def get_type():
        return 1

