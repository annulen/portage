# Copyright 2014-2021 Gentoo Authors
# Distributed under the terms of the GNU General Public License v2

import logging

from collections import OrderedDict

import portage

from portage import os
from portage.output import create_color_func
from portage.util import writemsg_level, _recursive_file_list
from warnings import warn

warn = create_color_func("WARN")


def get_hooks_from_dir(rel_directory, prefix="/"):
	directory = os.path.join(prefix, portage.USER_CONFIG_PATH, rel_directory)

	hooks = OrderedDict()
	for filepath in _recursive_file_list(directory):
		name = filepath.split(directory)[1].lstrip(portage.os.sep)
		if portage.os.access(filepath, portage.os.X_OK):
			hooks[filepath] = name
		else:
			writemsg_level(" %s %s hook: '%s' is not executable\n" % \
				(warn("*"), directory, portage._unicode_decode(name),),
				level=logging.WARN, noiselevel=2)

	return hooks
