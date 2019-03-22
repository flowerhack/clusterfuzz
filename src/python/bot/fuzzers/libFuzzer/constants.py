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
"""Constants that are meaningful to libFuzzer.
Should not have any dependancies.
Note that libFuzzers arguments take the form -flag=value. Thus any variables
defined in this function that end with the suffix "_FLAG" should contain
"-flag=". Any variable that ends with the suffix "_ARGUMENT" should contain
"-flag=value".
"""

# libFuzzer flags.
ARTIFACT_PREFIX_FLAG = '-artifact_prefix='

DICT_FLAG = '-dict='

FORK_FLAG = '-fork='

MAX_LEN_FLAG = '-max_len='

MAX_TOTAL_TIME_FLAG = '-max_total_time='

RSS_LIMIT_FLAG = '-rss_limit_mb='

RUNS_FLAG = '-runs='

TIMEOUT_FLAG = '-timeout='

EXACT_ARTIFACT_PATH_FLAG = '-exact_artifact_path='

# libFuzzer arguments.
ANALYZE_DICT_ARGUMENT = '-analyze_dict=1'

CLEANSE_CRASH_ARGUMENT = '-cleanse_crash=1'

MERGE_ARGUMENT = '-merge=1'

MINIMIZE_CRASH_ARGUMENT = '-minimize_crash=1'

PRINT_FINAL_STATS_ARGUMENT = '-print_final_stats=1'

TMP_ARTIFACT_PREFIX_ARGUMENT = ARTIFACT_PREFIX_FLAG + '/tmp/'

VALUE_PROFILE_ARGUMENT = '-use_value_profile=1'

# Value for RSS_LIMIT_FLAG to catch OOM.
DEFAULT_RSS_LIMIT_MB = 2048

DEFAULT_TIMEOUT_LIMIT = 25

# libFuzzer's exit code if a bug occurred in libFuzzer.
LIBFUZZER_ERROR_EXITCODE = 1

# Defines value of runs argument when loading a testcase.
RUNS_TO_REPRODUCE = 100

# libFuzzer's exit code if a bug was found in the target code.
TARGET_ERROR_EXITCODE = 77

# about to remake

# FUCHSIA_QEMU_COMMAND_TEMPLATE = ['/usr/local/google/home/flowerhack/lu_tsun/fuchsia/buildtools/linux-x64/qemu/bin/qemu-system-x86_64',
# 	'-D',
# 	'/tmp/qemustderr',
#	'-m',
#	'2048',
#	'-nographic',
#	'-kernel',
#	'/usr/local/google/home/flowerhack/eragon/clusterfuzz/src/python/bot/fuzzers/libFuzzer/multiboot.bin',
#	'-initrd', '/usr/local/google/home/flowerhack/eragon/clusterfuzz/src/python/bot/fuzzers/libFuzzer/fuchsia-ssh.zbi',
#	'-smp',
#	'4',
#	'-drive', 'file=/usr/local/google/home/flowerhack/eragon/clusterfuzz/src/python/bot/fuzzers/libFuzzer/fuchsia.qcow2,format=qcow2,if=none,id=blobstore',
#	'-device',
#	'virtio-blk-pci,drive=blobstore',
#	'-monitor',
#	'none',
#	'-append',
#	'kernel.serial=legacy TERM=dumb',
#	'-machine',
#	'q35',
#	'-enable-kvm',
#	'-display',
#	'none',
#	'-cpu',
#	'host,migratable=no',
#	'-netdev',
#	'user,id=net0,net=192.168.3.0/24,dhcpstart=192.168.3.9,host=192.168.3.2,hostfwd=tcp::56338-:22',
#	'-device',
#	'e1000,netdev=net0,mac=52:54:00:63:5e:7b',
#	'-L',
#	'/usr/local/google/home/flowerhack/eragon/clusterfuzz/src/python/bot/fuzzers/libFuzzer/qemu-for-fuchsia/share/qemu']

# commands to make a golden-image:
# cp ~/lu_tsun/fuchsia/out/x64/obj/build/images/fvm.blk ~/golden-image/fvm.blk
# cp ~/lu_tsun/fuchsia/out/x64/fuchsia.zbi ~/golden-image/fuchsia.zbi
# mkdir ~/golden-image/.ssh
# cp -a ~/lu_tsun/fuchsia/.ssh/. ~/golden-image/
# cd ~/golden-image
# cp /usr/local/google/home/flowerhack/lu_tsun/fuchsia/out/x64/../build-zircon/multiboot.bin ~/golden-image
# /usr/local/google/home/flowerhack/lu_tsun/fuchsia/buildtools/linux-x64/qemu/bin/qemu-img create -f qcow2 -b fvm.blk fuchsia.qcow2
# /usr/local/google/home/flowerhack/lu_tsun/fuchsia/out/build-zircon/tools/zbi -o fuchsia-ssh.zbi fuchsia.zbi --entry data/ssh/authorized_keys=~/golden-image/.ssh/authorized_keys


# Using portnum 56338 for now.

FUCHSIA_QEMU_COMMAND_TEMPLATE = ['{qemu}',
	'-D',
	'/tmp/qemustderr',
	'-m',
	'2048',
	'-nographic',
	'-kernel',
	'{kernel}',
	'-initrd', '{initrd}',
	'-smp',
	'4',
	'-drive', 'file={drive},format=qcow2,if=none,id=blobstore',
	'-device',
	'virtio-blk-pci,drive=blobstore',
	'-monitor',
	'none',
	'-append',
	'kernel.serial=legacy TERM=dumb',
	'-machine',
	'q35',
	'-enable-kvm',
	'-display',
	'none',
	'-cpu',
	'host,migratable=no',
	'-netdev',
	'user,id=net0,net=192.168.3.0/24,dhcpstart=192.168.3.9,host=192.168.3.2,hostfwd=tcp::56339-:22',
	'-device',
	'e1000,netdev=net0,mac=52:54:00:63:5e:7b',
	'-L',
	'{sharefiles}']

# ["ssh", "-i", "/usr/local/google/home/flowerhack/golden-image/pkey", "-o", "StrictHostKeyChecking no", "localhost", "-p", "56339", "ls"]
FUCHSIA_SSH_COMMAND_TEMPLATE = ["ssh", "-i", "{identity_file}", "-o", "StrictHostKeyChecking no", "localhost", "-p", "56338"]

FUCHSIA_BUCKET_NAME = "fuchsia_on_clusterfuzz_resources_v1"

FUCHSIA_GSUTIL_COMMAND = ["gsutil", "cp", "-r", "gs://fuchsia_on_clusterfuzz_resources_v1/*", "."]