# !usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under a 3-clause BSD license.
#
# @Author: Brian Cherinka
# @Date:   2017-12-05 12:01:21
# @Last modified by: José Sánchez-Gallego
# @Last Modified time: 2017-12-05 12:19:32


class FVCError(Exception):
    """A custom core FVC exception"""

    def __init__(self, message=None):
        message = "There has been an error" if not message else message
        super(FVCError, self).__init__(message)


class FVCNotImplemented(FVCError):
    """A custom exception for not yet implemented features."""

    def __init__(self, message=None):
        message = "This feature is not implemented yet." if not message else message
        super(FVCNotImplemented, self).__init__(message)


class FVCMissingDependency(FVCError):
    """A custom exception for missing dependencies."""

    pass


class FVCWarning(Warning):
    """Base warning for FVC."""

    pass


class FVCUserWarning(UserWarning, FVCWarning):
    """The primary warning class."""

    pass


class FVCSkippedTestWarning(FVCUserWarning):
    """A warning for when a test is skipped."""

    pass


class FVCDeprecationWarning(FVCUserWarning):
    """A warning for deprecated features."""

    pass
