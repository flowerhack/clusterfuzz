#!/usr/bin/env python
# Copyright 2019 The Fuchsia Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import argparse
import sys

from lib.args import Args
from lib.device import Device
from lib.fuzzer import Fuzzer
from lib.host import Host


def main():
  parser = Args.make_parser(
      'Runs the named fuzzer on provided test units, or all current test ' +
      'units for the fuzzer. Use \'check-fuzzer\' to see current tests units.')
  args, fuzzer_args = parser.parse_known_args()

  host = Host.from_build()
  device = Device.from_args(host, args)
  fuzzer = Fuzzer.from_args(device, args)

  if fuzzer.repro(fuzzer_args) == 0:
    print('No matching artifacts found.')
    return 1
  return 0


if __name__ == '__main__':
  sys.exit(main())
