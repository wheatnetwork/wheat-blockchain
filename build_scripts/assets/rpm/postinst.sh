#!/usr/bin/env bash
# Post install script for the UI .rpm to place symlinks in places to allow the CLI to work similarly in both versions

set -e

ln -s /opt/wheat/resources/app.asar.unpacked/daemon/wheat /usr/bin/wheat || true
ln -s /opt/wheat/wheat-blockchain /usr/bin/wheat-blockchain || true
