# Under MIT License, see LICENSE.txt

from Model.DataObject.BaseDataObject import catch_format_error
from Model.DataObject.AccessorData.BaseDataAccessor import BaseDataAccessor

__author__ = 'RoboCupULaval'


class StratGeneralAcc(BaseDataAccessor):
    def __init__(self, data_in):
        super().__init__(data_in)
        self._format_data()

    @catch_format_error
    def _check_obligatory_data(self):
        assert isinstance(self.data, dict), \
            "data: {} n'est pas un dictionnaire.".format(type(self.data))

    @catch_format_error
    def _check_optional_data(self):
        keys = self.data.keys()
        if 'strategy' in keys:
            assert isinstance(self.data['strategy'], list)
            for value in self.data['strategy']:
                assert isinstance(value, str)
        else:
            self.data['strategy'] = None

        if 'tactic' in keys:
            assert isinstance(self.data['tactic'], list)
            for value in self.data['tactic']:
                assert isinstance(value, str)
        else:
            self.data['tactic'] = None

        if 'action' in keys:
            assert isinstance(self.data['action'], list)
            for value in self.data['action']:
                assert isinstance(value, str)
        else:
            self.data['action'] = None

    @staticmethod
    def get_default_data_dict():
        return dict(zip(['strategy', 'tactic', 'action'],
                        ['None', 'None', 'None']))

    @staticmethod
    def get_type():
        return 1001


