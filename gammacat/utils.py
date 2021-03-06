# Licensed under a 3-clause BSD style license - see LICENSE.rst
from collections import OrderedDict
from pprint import pprint
import logging
import json
from pathlib import Path
import ruamel.yaml
import jsonschema
import numpy as np
from astropy.coordinates import SkyCoord
from astropy.table import Table

log = logging.getLogger(__name__)


class ECSVFormatError(Exception):
    """ECSV format error"""


class NA:
    """
    Handling of missing values

    NA = "not available"
    """
    fill_value = OrderedDict(
        integer=-999,
        number=np.nan,
        string='',
        array='',
        list=[],
    )

    # @classmethod
    # def fill_str(cls, data, key):
    #     try:
    #         data[key] = cls.fill_value['string']
    #     else:
    #         return data

    @staticmethod
    def fill_value_array(shape):
        return np.ones(shape) * np.nan

    @staticmethod
    def resize_sed_array(array, shape):
        array = array.copy()
        array.resize(shape)
        array[array == 0] = np.nan
        return array

    @classmethod
    def fill_list(cls, data, key):
        try:
            return ','.join(data[key])
        except KeyError:
            return cls.fill_value['string']


def load_yaml(path):
    """Helper function to load data from a YAML file."""
    path = Path(path)
    log.debug('Reading {}'.format(path))
    with path.open() as fh:
        data = ruamel.yaml.round_trip_load(fh)
    return data


def write_yaml(data, path):
    """Helper function to write data to a YAML file."""
    path = Path(path)
    log.info('Writing {}'.format(path))
    with path.open('w') as fh:
        ruamel.yaml.round_trip_dump(data, fh)


def load_json(path):
    """Helper function to load data from a JSON file."""
    path = Path(path)
    log.debug('Reading {}'.format(path))
    with path.open() as fh:
        data = json.load(fh, object_pairs_hook=OrderedDict)
    return data


def write_json(data, path):
    """Helper function to write data to a JSON file."""
    path = Path(path)
    log.info('Writing {}'.format(path))
    with path.open('w') as fh:
        json.dump(data, fh, indent=4)


def print_simbad_pos(name):
    """Print YAML snipped for SIMBAD position.
    """
    pos = SkyCoord.from_name(name)
    template = (
        'pos:\n'
        '  simbad_id: {name}\n'
        '  ra: {pos.ra.deg}\n'
        '  dec: {pos.dec.deg}\n'
    )
    s = template.format(name=name, pos=pos)
    print(s)


def rawgit_url(filename, location='master', mode='production'):
    """
    Construct the rawgit URL to download directly files from the repo.

    More info:
    * https://rawgit.com/
    * https://github.com/rgrove/rawgit/wiki/Frequently-Asked-Questions

    URL is

    Parameters
    ----------
    filename : str
        Filename in the repo.
    location : str
        Name of a branch, tag or commit.
    mode : {'development', 'production'}
        Where to fetch the files from

    Examples
    --------
    >>> filename = 'input/data/2006/2006A%2526A...456..245A/tev-000065.ecsv'
    >>> rawgit_url(filename, mode='production')
    TODO
    >>> rawgit_url(filename, mode='development')
    TODO
    """
    if mode == 'development':
        base_url = 'https://rawgit.com/gammapy/gamma-cat'
    elif mode == 'production':
        base_url = 'https://cdn.rawgit.com/gammapy/gamma-cat'

    url = '/'.join([base_url, location, filename])

    return url


# def yaml_make_ordereddict_work():
#     """
#     Teach YAML how to work with OrderedDict.
#
#     http://stackoverflow.com/a/21048064/498873
#     """
#     _mapping_tag = yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG
#
#     def dict_representer(dumper, data):
#         return dumper.represent_dict(data.items())
#
#     def dict_constructor(loader, node):
#         return OrderedDict(loader.construct_pairs(node))
#
#     yaml.add_representer(OrderedDict, dict_representer)
#     yaml.add_constructor(_mapping_tag, dict_constructor)
#
#
# # Execute `yaml_make_ordereddict_work` at the top level.
# # So if someone imports the YAML utility functions from this
# # module, objects should be read as OrderedDict always,
# # and order preserved.
# yaml_make_ordereddict_work()


def table_to_list_of_dict(table):
    """Convert table to list of dict."""
    rows = []
    for row in table:
        data = OrderedDict()
        for name in table.colnames:
            val = row[name]
            if isinstance(val, np.int64):
                val = int(val)
            elif isinstance(val, np.int32):
                val = int(val)
            elif isinstance(val, np.bool_):
                val = bool(val)
            elif isinstance(val, np.float):
                val = float(val)
            elif isinstance(val, np.float32):
                val = float(val)
            elif isinstance(val, np.str):
                val = str(val)
            elif isinstance(val, np.ndarray):
                vals = [float(_) for _ in val]
                val = list(vals)
            else:
                raise ValueError('Unknown type: {} {}'.format(val, type(val)))
            data[name] = val

        rows.append(data)

    return rows


def check_ecsv_column_header(path):
    """
    Check ECSV file for column header formatting.

    See https://github.com/astropy/astropy/issues/5451
    """
    table = Table.read(str(path), format='ascii.ecsv')
    table2 = Table.read(str(path), format='ascii.basic')

    if table.colnames != table2.colnames:
        log.error('Problem in ECSV file: {}'.format(path))
        log.error('ECSV colnames: {}'.format(table.colnames))
        log.error(' CSV colnames: {}'.format(table2.colnames))
        raise ECSVFormatError

    if len(table) != len(table2):
        log.error('Problem in ECSV file: {}'.format(path))
        log.error('ECSV rows: {}'.format(len(table)))
        log.error(' CSV rows: {}'.format(len(table2)))
        raise ECSVFormatError


def validate_schema(path, data, schema):
    """Validate data against schema and log errors.
    """
    log.debug('Validating {}'.format(path))
    try:
        jsonschema.validate(data, schema)
    except jsonschema.exceptions.ValidationError as ex:
        log.error('Invalid input file: {}'.format(path))
        pprint(data)
        raise ex
