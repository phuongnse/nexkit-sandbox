#!/usr/bin/env bash
# A stand-in for an end-to-end suite that a repository splits into shards.
set -euo pipefail
echo "NEXKIT_SHARD=${NEXKIT_SHARD:-unset}"
echo "NEXKIT_CHECK_VERIFIED_SHA=${NEXKIT_CHECK_VERIFIED_SHA:-unset}"
python3 -m unittest discover -s tests
