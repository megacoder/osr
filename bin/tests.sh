#!/bin/sh
# vim: ai sm noet nu nornu nobomb ts=8 sw=8 ff=unix
#

. ./venv/bin/activate

pip install pytest || true

pytest
