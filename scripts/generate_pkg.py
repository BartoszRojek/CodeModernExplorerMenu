#!/usr/bin/env python3
from __future__ import print_function
from shutil import copy
import os
import sys

code_clsid_map = {
  'x86': '978573D8-4037-4F64-A055-0C6BDC64D71F',
  'x64': 'E4E4C322-3388-45AF-8D39-BE19BFC78A18',
  'arm64': '12483301-B459-40BE-A434-DF8010E8958F'
}

code_insiders_clsid_map = {
  'x86': 'B9949795-B37D-457F-ADDE-6A950EF85CA7',
  'x64': '799F4F7E-5934-4001-A74C-E207F44F05B8',
  'arm64': '7D34756D-32DD-4EE6-B99F-2691C0DAD875'
}

root = os.path.dirname(os.path.dirname(__file__))
out_dir = os.path.join(root, 'out')
pkg_type = sys.argv[1]
arch = sys.argv[2]
pkg_dir = os.path.join(out_dir, pkg_type + '_explorer_pkg_' + arch)

# Create output directory.
if not os.path.exists(pkg_dir):
    os.mkdir(pkg_dir)

# Update AppxManifest.
manifest = os.path.join(root, 'template', 'AppxManifest.xml')
with open(manifest, 'r') as f:
  content = f.read()
  content = content.replace('@@PublisherDisplayName@@', 'Code Modern Explorer Menu')
  if pkg_type == 'stable':
    content = content.replace('@@Publisher@@', 'Code.Modern.Explorer.Menu')
    content = content.replace('@@PackageDescription@@', 'Code Modern Explorer Menu')
    content = content.replace('@@PackageName@@', 'Code.Modern.Explorer.Menu')
    content = content.replace('@@PackageDisplayName@@', 'Code Modern Explorer Menu')
    content = content.replace('@@Application@@', 'Code.exe')
    content = content.replace('@@ApplicationIdShort@@', 'Code')
    content = content.replace('@@MenuID@@', 'OpenWithCode')
    content = content.replace('@@CLSID@@', code_clsid_map[arch])
    content = content.replace('@@PackageDLL@@', 'Code Modern Explorer Menu.dll')
  if pkg_type == 'insiders':
    content = content.replace('@@Publisher@@', 'Code.Insiders.Modern.Explorer.Menu')
    content = content.replace('@@PackageDescription@@', 'Code Insiders Modern Explorer Menu')
    content = content.replace('@@PackageName@@', 'Code.Insiders.Modern.Explorer.Menu')
    content = content.replace('@@PackageDisplayName@@', 'Code Insiders Modern Explorer Menu')
    content = content.replace('@@Application@@', 'Code - Insiders.exe')
    content = content.replace('@@ApplicationIdShort@@', 'CodeInsiders')
    content = content.replace('@@MenuID@@', 'OpenWithCodeInsiders')
    content = content.replace('@@CLSID@@', code_insiders_clsid_map[arch])
    content = content.replace('@@PackageDLL@@', 'Code Insiders Modern Explorer Menu.dll')

# Copy AppxManifest file to the package directory.
manifest_output = os.path.join(pkg_dir, 'AppxManifest.xml')
with open(manifest_output, 'w+') as f:
  f.write(content)