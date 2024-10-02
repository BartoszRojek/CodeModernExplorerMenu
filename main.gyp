{
  'target_defaults': {
    'conditions': [
      [ 'OS=="win"', {
        'sources': [
          'src/explorer_command.cc',
          'src/explorer_command.def',
        ],
        'include_dirs': [
          'vcpkg_installed/<(target_arch)-windows/include/fmt',
          'vcpkg_installed/<(target_arch)-windows/include/wil',
        ],
        'defines': [
          '_WINDLL',
          'WIN32_LEAN_AND_MEAN',
          '_UNICODE',
          'UNICODE',
          '_CRT_SECURE_NO_DEPRECATE',
          '_CRT_NONSTDC_NO_DEPRECATE',
        ],
        'msvs_settings': {
          'WindowsTargetPlatformVersion': '10',
          'LanguageStandard': 'stdcpp20',
          'VCLinkerTool': {
            'AdditionalOptions': [
              '/guard:cf',
            ],
            'OptimizeReferences': 2,             # /OPT:REF
            'EnableCOMDATFolding': 2,            # /OPT:ICF
          },
          'VCCLCompilerTool': {
            'AdditionalOptions': [
              '/Zc:__cplusplus',
              '/std:c++20',
              '/Qspectre',
              '/guard:cf',
              '/utf-8'
            ],
            'BufferSecurityCheck': 'true',
            'ExceptionHandling': 1,               # /EHsc
            'EnableFunctionLevelLinking': 'true',
            'Optimization': 3,              # /Ox, full optimization
          },
        },
        'libraries': [
          '-ladvapi32.lib',
          '-lruntimeobject.lib',
          '-lshlwapi.lib',
          '-lonecore.lib',
        ]
      }],
    ],
  },
  'targets': [{
    'target_name': 'Code Modern Explorer Menu',
    'type': 'shared_library',
    'defines': [
      'EXE_NAME="Code.exe"',
      'DIR_NAME="Microsoft VS Code"',
    ],
    'conditions': [
      [ 'OS=="win"', {
        'conditions': [
          ['target_arch=="x64"', {
            'TargetMachine' : 17,             # /MACHINE:X64
            'defines': [ 
              'DLL_UUID="E4E4C322-3388-45AF-8D39-BE19BFC78A18"',
            ],
          }],
          ['target_arch=="arm64"', {
            'TargetMachine' : 18,             # /MACHINE:ARM64 https://learn.microsoft.com/en-us/dotnet/api/microsoft.visualstudio.vcprojectengine.machinetypeoption?view=visualstudiosdk-2022
            'defines': [ 
              'DLL_UUID="12483301-B459-40BE-A434-DF8010E8958F"',
            ],
          }],
        ],
      }],
    ],
  }, {
    'target_name': 'Code Insiders Modern Explorer Menu',
    'type': 'shared_library',
    'defines': [
      'EXE_NAME="Code - Insiders.exe"',
      'DIR_NAME="Microsoft VS Code Insiders"',
      'INSIDER=1',
    ],
    'conditions': [
      [ 'OS=="win"', {
        'conditions': [
          ['target_arch=="x64"', {
            'TargetMachine' : 17,             # /MACHINE:X64
            'defines': [ 
              'DLL_UUID="799F4F7E-5934-4001-A74C-E207F44F05B8"',
            ],
          }],
          ['target_arch=="arm64"', {
            'TargetMachine' : 18,             # /MACHINE:ARM64
            'defines': [ 
              'DLL_UUID="7D34756D-32DD-4EE6-B99F-2691C0DAD875"',
            ],
          }],
        ],
      }],
    ],
  }],
}