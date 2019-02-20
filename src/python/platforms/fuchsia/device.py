# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Helper functions for running commands on Fuchsia devices."""

# TODO(mbarbella): Re-enable this check once functions below are implemented.
# pylint: disable=unused-argument

from metrics import logs
FUCHSIA_QEMU_COMMAND_TEMPLATE = ("{qemu} -m 2048 -nographic -kernel "
                 "{qemu_kernel} -initrd {initrd} "
                 "-smp 4 -snapshot -drive file={drive_file},format=qcow2,"
                 "if=none,id=blobstore,snapshot=on -device virtio-blk-pci,drive=blobstore "
                 "-serial stdio -monitor none "
                 "-append 'devmgr.epoch=1550629864  kernel.serial=legacy' "
                 "-machine q35 -enable-kvm-cpu host,migratable=no "
                 "-netdev user,id=net0,net=192.168.3.0/24,dhcpstart=192.168.3.9,host=192.168.3.2,hostfwd=tcp::56337-:22 -device e1000,netdev=net0,mac=52:54:00:63:5e:7b")

FUCHSIA_SSH_COMMAND_TEMPLATE = ("ssh -i {identity_file_path} localhost -p 56337 {command}")

import os
from google.cloud import storage

def get_application_launch_command(arguments, testcase_path):
  auth_key = "pkey"
  local_path = os.getcwd();
  identity_file_path = local_path + auth_key

  storage_client = storage.Client()
  bucket = storage_client.get_bucket("fuchsia_on_clusterfuzz_resources_v1")

  # Download everything necessary to run Fuchsia via QEMU.
  blob = bucket.blob(auth_key)
  blob.download_to_filename(identity_file_path)

  """Prepare a command to run on the host to launch on the device."""
  command = "echo 'This is a long test string.'"
  base_command = FUCHSIA_SSH_COMMAND_TEMPLATE.format(identity_file_path=identity_file_path, command=command)
  return base_command


def reset_state():
  logs.log_warn("reset_state is being called")
  """Reset the device to a clean state."""
  # TODO(mbarbella): Implement this.


def run_command(command_line, timeout):
  logs.log_warn("run_command is being called")
  """Run the desired command on the device."""
  # TODO: this needs to actually run the SSH command
  # TODO(mbarbella): Implement this.


def clear_testcase_directory():
  logs.log_warn("clear_testcase_directory is being called")
  """Delete test cases stored on the device."""
  # TODO(mbarbella): Implement this.


def copy_testcase_to_device(testcase_path):
  logs.log_warn("copy_testcase_to_device is being called")
  """Copy a file to the device's test case directory."""
  # TODO(mbarbella): Implement this.
