# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
NaiveCalibrator
"""


from ..utils.entrypoints import Component


def naive_calibrator(
        **params):
    """
    **Description**
        None

    """

    entrypoint_name = 'NaiveCalibrator'
    settings = {}

    component = Component(
        name=entrypoint_name,
        settings=settings,
        kind='CalibratorTrainer')
    return component