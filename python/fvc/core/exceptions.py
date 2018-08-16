# !usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under a 3-clause BSD license.
#
# @Author: Brian Cherinka
# @Date:   2017-12-05 12:01:21
# @Last modified by:   Brian Cherinka
# @Last Modified time: 2017-12-05 12:19:32

from __future__ import print_function, division, absolute_import


class FvcError(Exception):
    """A custom core Fvc exception"""

    def __init__(self, message=None):

        message = 'There has been an error' \
            if not message else message

        super(FvcError, self).__init__(message)


class FvcNotImplemented(FvcError):
    """A custom exception for not yet implemented features."""

    def __init__(self, message=None):

        message = 'This feature is not implemented yet.' \
            if not message else message

        super(FvcNotImplemented, self).__init__(message)


class FvcAPIError(FvcError):
    """A custom exception for API errors"""

    def __init__(self, message=None):
        if not message:
            message = 'Error with Http Response from Fvc API'
        else:
            message = 'Http response error from Fvc API. {0}'.format(message)

        super(FvcAPIError, self).__init__(message)


class FvcApiAuthError(FvcAPIError):
    """A custom exception for API authentication errors"""
    pass


class FvcMissingDependency(FvcError):
    """A custom exception for missing dependencies."""
    pass


class FvcWarning(Warning):
    """Base warning for Fvc."""


class FvcUserWarning(UserWarning, FvcWarning):
    """The primary warning class."""
    pass


class FvcSkippedTestWarning(FvcUserWarning):
    """A warning for when a test is skipped."""
    pass


class FvcDeprecationWarning(FvcUserWarning):
    """A warning for deprecated features."""
    pass
