# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
LightGbmRanker
"""

__all__ = ["LightGbmRanker"]


from sklearn.base import ClassifierMixin

from ..base_predictor import BasePredictor
from ..internal.core.ensemble.lightgbmranker import LightGbmRanker as core
from ..internal.utils.utils import trace


class LightGbmRanker(core, BasePredictor, ClassifierMixin):
    """

    Gradient Boosted Decision Trees

    .. remarks::
        Light GBM is an open source implementation of boosted trees. It is
        available in nimbusml as a binary classification trainer, a multi-class
        trainer, a regression trainer and a ranking trainer. Note that for
        this learner,
        we constraint the largest rank to be 12. Users might need to
        normalize their label
        columns for the rank, else may get "out of bound" errors.


        **Reference**

            `GitHub: LightGBM <https://github.com/Microsoft/LightGBM/wiki>`_


    :param feature: see `Columns </nimbusml/concepts/columns>`_.

    :param group_id: see `Columns </nimbusml/concepts/columns>`_.

    :param label: see `Columns </nimbusml/concepts/columns>`_.

    :param weight: see `Columns </nimbusml/concepts/columns>`_.

    :param number_of_iterations: Number of iterations.

    :param learning_rate: Determines the size of the step taken in the
        direction of the gradient in each step of the learning process.  This
        determines how fast or slow the learner converges on the optimal
        solution. If the step size is too big, you might overshoot the optimal
        solution.  If the step size is too small, training takes longer to
        converge to the best solution.

    :param number_of_leaves: The maximum number of leaves (terminal nodes) that
        can be created in any tree. Higher values potentially increase the size
        of the tree and get better precision, but risk overfitting and
        requiring longer training times.

    :param minimum_example_count_per_leaf: Minimum number of training instances
        required to form a leaf. That is, the minimal number of documents
        allowed in a leaf of regression tree, out of the sub-sampled data. A
        'split' means that features in each level of the tree (node) are
        randomly divided.

    :param booster: Which booster to use. Available options are:

        #. :py:func:`Dart <nimbusml.ensemble.booster.Dart>`
        #. :py:func:`Gbdt <nimbusml.ensemble.booster.Gbdt>`
        #. :py:func:`Goss <nimbusml.ensemble.booster.Goss>`.

    :param normalize: If ``Auto``, the choice to normalize depends on the
        preference declared by the algorithm. This is the default choice. If
        ``No``, no normalization is performed. If ``Yes``, normalization always
        performed. If ``Warn``, if normalization is needed by the algorithm, a
        warning message is displayed but normalization is not performed. If
        normalization is performed, a ``MaxMin`` normalizer is used. This
        normalizer preserves sparsity by mapping zero to zero.

    :param caching: Whether trainer should cache input training data.

    :param custom_gains: An array of gains associated to each relevance label.

    :param sigmoid: Parameter for the sigmoid function.

    :param evaluation_metric: Evaluation metrics.

    :param maximum_bin_count_per_feature: Maximum number of bucket bin for
        features.

    :param verbose: Verbose.

    :param silent: Printing running messages.

    :param number_of_threads: Number of parallel threads used to run LightGBM.

    :param early_stopping_round: Rounds of early stopping, 0 will disable it.

    :param batch_size: Number of entries in a batch when loading data.

    :param use_categorical_split: Enable categorical split or not.

    :param handle_missing_value: Enable special handling of missing value or
        not.

    :param minimum_example_count_per_group: Minimum number of instances per
        categorical group.

    :param maximum_categorical_split_point_count: Max number of categorical
        thresholds.

    :param categorical_smoothing: Lapalace smooth term in categorical feature
        spilt. Avoid the bias of small categories.

    :param l2_categorical_regularization: L2 Regularization for categorical
        split.

    :param random_state: Sets the random seed for LightGBM to use.

    :param parallel_trainer: Parallel LightGBM Learning Algorithm.

    :param params: Additional arguments sent to compute engine.

    .. seealso::
        :py:class:`FastTreesBinaryClassifier
        <nimbusml.ensemble.FastTreesBinaryClassifier>`,
        :py:class:`FastForestRegressor <nimbusml.ensemble.FastForestRegressor>`,
        :py:func:`Dart <nimbusml.ensemble.booster.Dart>`,
        :py:func:`Goss <nimbusml.ensemble.booster.Goss>`,
        :py:func:`Gbdt <nimbusml.ensemble.booster.Gbdt>`

    .. index:: models, classification, regression

    Example:
       .. literalinclude:: /../nimbusml/examples/LightGbmRanker.py
              :language: python
    """

    @trace
    def __init__(
            self,
            number_of_iterations=100,
            learning_rate=None,
            number_of_leaves=None,
            minimum_example_count_per_leaf=None,
            booster=None,
            normalize='Auto',
            caching='Auto',
            custom_gains=[0, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095],
            sigmoid=0.5,
            evaluation_metric='NormalizedDiscountedCumulativeGain',
            maximum_bin_count_per_feature=255,
            verbose=False,
            silent=True,
            number_of_threads=None,
            early_stopping_round=0,
            batch_size=1048576,
            use_categorical_split=None,
            handle_missing_value=True,
            minimum_example_count_per_group=100,
            maximum_categorical_split_point_count=32,
            categorical_smoothing=10.0,
            l2_categorical_regularization=10.0,
            random_state=None,
            parallel_trainer=None,
            feature=None,
            group_id=None,
            label=None,
            weight=None,
            **params):

        if 'feature_column_name' in params:
            raise NameError(
                "'feature_column_name' must be renamed to 'feature'")
        if feature:
            params['feature_column_name'] = feature
        if 'row_group_column_name' in params:
            raise NameError(
                "'row_group_column_name' must be renamed to 'group_id'")
        if group_id:
            params['row_group_column_name'] = group_id
        if 'label_column_name' in params:
            raise NameError(
                "'label_column_name' must be renamed to 'label'")
        if label:
            params['label_column_name'] = label
        if 'example_weight_column_name' in params:
            raise NameError(
                "'example_weight_column_name' must be renamed to 'weight'")
        if weight:
            params['example_weight_column_name'] = weight
        BasePredictor.__init__(self, type='ranker', **params)
        core.__init__(
            self,
            number_of_iterations=number_of_iterations,
            learning_rate=learning_rate,
            number_of_leaves=number_of_leaves,
            minimum_example_count_per_leaf=minimum_example_count_per_leaf,
            booster=booster,
            normalize=normalize,
            caching=caching,
            custom_gains=custom_gains,
            sigmoid=sigmoid,
            evaluation_metric=evaluation_metric,
            maximum_bin_count_per_feature=maximum_bin_count_per_feature,
            verbose=verbose,
            silent=silent,
            number_of_threads=number_of_threads,
            early_stopping_round=early_stopping_round,
            batch_size=batch_size,
            use_categorical_split=use_categorical_split,
            handle_missing_value=handle_missing_value,
            minimum_example_count_per_group=minimum_example_count_per_group,
            maximum_categorical_split_point_count=maximum_categorical_split_point_count,
            categorical_smoothing=categorical_smoothing,
            l2_categorical_regularization=l2_categorical_regularization,
            random_state=random_state,
            parallel_trainer=parallel_trainer,
            **params)
        self.feature = feature
        self.group_id = group_id
        self.label = label
        self.weight = weight

    def get_params(self, deep=False):
        """
        Get the parameters for this operator.
        """
        return core.get_params(self)
