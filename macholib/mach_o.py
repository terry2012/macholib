"""
Other than changing the load commands in such a way that they do not
contain the load command itself, this is largely a by-hand conversion
of the C headers.  Hopefully everything in here should be at least as
obvious as the C headers, and you should be using the C headers as a real
reference because the documentation didn't come along for the ride.

Doing much of anything with the symbol tables or segments is really
not covered at this point.

See /usr/include/mach-o and friends.
"""

import time
from macholib.ptypes import *


# CPU types, refer:
#   - http://www.opensource.apple.com/source/cctools/cctools-862/include/mach/machine.h
#   - /usr/include/mach/machine.h
#   - http://opensource.apple.com/source/cctools/cctools-862/libmacho/arch.c
#   - man 3 arch

cpu_type_t = p_uint32
cpu_subtype_t = p_uint32

CPU_ARCH_ABI64 = 0x1000000

CPU_TYPE_ANY = -1
CPU_TYPE_VAX = 1
CPU_TYPE_ROMP = 2
CPU_TYPE_NS32032 = 4
CPU_TYPE_NS32332 = 5
CPU_TYPE_MC680x0 = 6
CPU_TYPE_I386 = 7
CPU_TYPE_X86_64 = CPU_TYPE_I386 | CPU_ARCH_ABI64
CPU_TYPE_MIPS = 8
CPU_TYPE_NS32532 = 9
CPU_TYPE_HPPA = 11
CPU_TYPE_ARM = 12
CPU_TYPE_ARM64 = CPU_TYPE_ARM | CPU_ARCH_ABI64
CPU_TYPE_MC88000 = 13
CPU_TYPE_SPARC = 14
CPU_TYPE_I860 = 15  # big-endian
CPU_TYPE_I860_LITTLE = 16  # little-endian
CPU_TYPE_RS6000 = 17
# CPU_TYPE_MC98000 = 18
CPU_TYPE_POWERPC = 18
CPU_TYPE_POWERPC64 = CPU_TYPE_POWERPC | CPU_ARCH_ABI64
CPU_TYPE_VEO = 255

CPU_SUBTYPE_LIB64 = 0x80000000
CPU_SUBTYPE_MULTIPLE = -1

# CPU_TYPE_VAX
CPU_SUBTYPE_VAX_ALL = 0
CPU_SUBTYPE_VAX780 = 1
CPU_SUBTYPE_VAX785 = 2
CPU_SUBTYPE_VAX750 = 3
CPU_SUBTYPE_VAX730 = 4
CPU_SUBTYPE_UVAXI = 5
CPU_SUBTYPE_UVAXII = 6
CPU_SUBTYPE_VAX8200 = 7
CPU_SUBTYPE_VAX8500 = 8
CPU_SUBTYPE_VAX8600 = 9
CPU_SUBTYPE_VAX8650 = 10
CPU_SUBTYPE_VAX8800 = 11
CPU_SUBTYPE_UVAXIII = 12

# CPU_TYPE_ROMP
CPU_SUBTYPE_RT_ALL = 0
CPU_SUBTYPE_RT_PC = 1
CPU_SUBTYPE_RT_APC = 2
CPU_SUBTYPE_RT_135 = 3

# CPU_TYPE_NS32032, CPU_TYPE_NS32332, CPU_TYPE_NS32532
CPU_SUBTYPE_MMAX_ALL = 0
CPU_SUBTYPE_MMAX_DPC = 1
CPU_SUBTYPE_SQT = 2
CPU_SUBTYPE_MMAX_APC_FPU = 3
CPU_SUBTYPE_MMAX_APC_FPA = 4
CPU_SUBTYPE_MMAX_XPC = 5

# CPU_TYPE_I386
CPU_SUBTYPE_I386_ALL = 3
CPU_SUBTYPE_386 = 3
CPU_SUBTYPE_486 = 4
CPU_SUBTYPE_486SX = 4 + 128
CPU_SUBTYPE_586 = 5
# CPU_SUBTYPE_PENT = 5 + (0 << 4)
CPU_SUBTYPE_PENTPRO = 6 + (1 << 4)
CPU_SUBTYPE_PENTII_M3 = 6 + (3 << 4)
CPU_SUBTYPE_PENTII_M5 = 6 + (5 << 4)
CPU_SUBTYPE_PENTIUM_4 = 10 + (0 << 4)
CPU_SUBTYPE_INTEL_FAMILY_MAX = 15
CPU_SUBTYPE_INTEL_MODEL_ALL = 0

# CPU_TYPE_X86_64
CPU_SUBTYPE_X86_64_ALL = CPU_SUBTYPE_I386_ALL
CPU_SUBTYPE_X86_64_H = 8

# CPU_TYPE_MIPS
CPU_SUBTYPE_MIPS_ALL = 0
CPU_SUBTYPE_MIPS_R2300 = 1
CPU_SUBTYPE_MIPS_R2600 = 2
CPU_SUBTYPE_MIPS_R2800 = 3
CPU_SUBTYPE_MIPS_R2000a = 4

# CPU_TYPE_MC680x0
CPU_SUBTYPE_MC680x0_ALL = 1
CPU_SUBTYPE_MC68030 = 1
CPU_SUBTYPE_MC68040 = 2
CPU_SUBTYPE_MC68030_ONLY = 3

# CPU_TYPE_HPPA
CPU_SUBTYPE_HPPA_ALL = 0
CPU_SUBTYPE_HPPA_7100 = 0
CPU_SUBTYPE_HPPA_7100LC = 1

# CPU_TYPE_ARM
CPU_SUBTYPE_ARM_ALL = 0
CPU_SUBTYPE_ARM_A500_ARCH = 1
CPU_SUBTYPE_ARM_A500 = 2
CPU_SUBTYPE_ARM_A440 = 3
CPU_SUBTYPE_ARM_M4 = 4
CPU_SUBTYPE_ARM_V4T = 5
CPU_SUBTYPE_ARM_V6 = 6
CPU_SUBTYPE_ARM_V5TEJ = 7
CPU_SUBTYPE_ARM_XSCALE = 8
CPU_SUBTYPE_ARM_V7 = 9
CPU_SUBTYPE_ARM_V7F = 10  # Cortex A9
CPU_SUBTYPE_ARM_V7S = 11  # Swift
CPU_SUBTYPE_ARM_V7K = 12
CPU_SUBTYPE_ARM_V8 = 13
CPU_SUBTYPE_ARM_V6M = 14
CPU_SUBTYPE_ARM_V7M = 15
CPU_SUBTYPE_ARM_V7EM = 16

# CPU_TYPE_ARM64
CPU_SUBTYPE_ARM64_ALL = 0
CPU_SUBTYPE_ARM64_V8 = 1

# CPU_TYPE_MC88000
CPU_SUBTYPE_MC88000_ALL = 0
CPU_SUBTYPE_MMAX_JPC = 1
CPU_SUBTYPE_MC88100 = 1
CPU_SUBTYPE_MC88110 = 2

# CPU_TYPE_SPARC
CPU_SUBTYPE_SPARC_ALL = 0

# CPU_TYPE_I860
CPU_SUBTYPE_I860_ALL = 0
CPU_SUBTYPE_I860_860 = 1

# CPU_TYPE_I860_LITTLE
CPU_SUBTYPE_I860_LITTLE_ALL = 0
CPU_SUBTYPE_I860_LITTLE = 1

# CPU_TYPE_RS6000
CPU_SUBTYPE_RS6000_ALL = 0
CPU_SUBTYPE_RS6000 = 1

# CPU_TYPE_POWERPC, CPU_TYPE_POWERPC64
CPU_SUBTYPE_POWERPC_ALL = 0
CPU_SUBTYPE_POWERPC_601 = 1
CPU_SUBTYPE_POWERPC_602 = 2
CPU_SUBTYPE_POWERPC_603 = 3
CPU_SUBTYPE_POWERPC_603E = 4
CPU_SUBTYPE_POWERPC_603EV = 5
CPU_SUBTYPE_POWERPC_604 = 6
CPU_SUBTYPE_POWERPC_604E = 7
CPU_SUBTYPE_POWERPC_620 = 8
CPU_SUBTYPE_POWERPC_750 = 9
CPU_SUBTYPE_POWERPC_7400 = 10
CPU_SUBTYPE_POWERPC_7450 = 11
CPU_SUBTYPE_POWERPC_970 = 100

# CPU_TYPE_VEO
CPU_SUBTYPE_VEO_1 = 1
CPU_SUBTYPE_VEO_2 = 2
CPU_SUBTYPE_VEO_3 = 3
CPU_SUBTYPE_VEO_4 = 4
CPU_SUBTYPE_VEO_ALL = CPU_SUBTYPE_VEO_2

_CPU_TYPE_TABLE = {
    (CPU_TYPE_I386, CPU_SUBTYPE_I386_ALL): ("i386", "Intel 80x86"),
    (CPU_TYPE_I386, CPU_SUBTYPE_486): ("i486", "Intel 80486"),
    (CPU_TYPE_I386, CPU_SUBTYPE_486SX): ("i486SX", "Intel 80486SX"),
    # (CPU_TYPE_I386, CPU_SUBTYPE_PENT): ("pentium", "Intel Pentium"),
    (CPU_TYPE_I386, CPU_SUBTYPE_586): ("i586", "Intel 80586"),
    (CPU_TYPE_I386, CPU_SUBTYPE_PENTPRO): ("pentpro", "Intel Pentium Pro"),
    # (CPU_TYPE_I386, CPU_SUBTYPE_PENTPRO): ("i686", "Intel Pentium Pro"),
    (CPU_TYPE_I386, CPU_SUBTYPE_PENTII_M3): ("pentIIm3", "Intel Pentium II Model 3"),
    (CPU_TYPE_I386, CPU_SUBTYPE_PENTII_M5): ("pentIIm5", "Intel Pentium II Model 5"),
    (CPU_TYPE_I386, CPU_SUBTYPE_PENTIUM_4): ("pentium4", "Intel Pentium 4"),
    (CPU_TYPE_I386, CPU_SUBTYPE_X86_64_H): ("x86_64h", "Intel x86-64h Haswell"),
    (CPU_TYPE_X86_64, CPU_SUBTYPE_X86_64_ALL): ("x86_64", "Intel x86-64"),
    (CPU_TYPE_X86_64, CPU_SUBTYPE_X86_64_H): ("x86_64h", "Intel x86-64h Haswell"),
    (CPU_TYPE_ARM, CPU_SUBTYPE_ARM_ALL): ("arm", "ARM"),
    (CPU_TYPE_ARM, CPU_SUBTYPE_ARM_V4T): ("armv4t", "arm v4t"),
    (CPU_TYPE_ARM, CPU_SUBTYPE_ARM_V5TEJ): ("armv5", "arm v5"),
    (CPU_TYPE_ARM, CPU_SUBTYPE_ARM_XSCALE): ("xscale", "arm xscale"),
    (CPU_TYPE_ARM, CPU_SUBTYPE_ARM_V6): ("armv6", "arm v6"),
    (CPU_TYPE_ARM, CPU_SUBTYPE_ARM_V6M): ("armv6m", "arm v6m"),
    (CPU_TYPE_ARM, CPU_SUBTYPE_ARM_V7): ("armv7", "arm v7"),
    (CPU_TYPE_ARM, CPU_SUBTYPE_ARM_V7F): ("armv7f", "arm v7f"),
    (CPU_TYPE_ARM, CPU_SUBTYPE_ARM_V7S): ("armv7s", "arm v7s"),
    (CPU_TYPE_ARM, CPU_SUBTYPE_ARM_V7K): ("armv7k", "arm v7k"),
    (CPU_TYPE_ARM, CPU_SUBTYPE_ARM_V7M): ("armv7m", "arm v7m"),
    (CPU_TYPE_ARM, CPU_SUBTYPE_ARM_V7EM): ("armv7em", "arm v7em"),
    (CPU_TYPE_ARM, CPU_SUBTYPE_ARM_V8): ("armv8", "arm v8"),
    (CPU_TYPE_ARM64, CPU_SUBTYPE_ARM64_ALL): ("arm64", "ARM64"),
    (CPU_TYPE_ARM64, CPU_SUBTYPE_ARM64_V8): ("arm64", "arm64 v8"),
    (CPU_TYPE_POWERPC, CPU_SUBTYPE_POWERPC_ALL): ("ppc", "PowerPC"),
    (CPU_TYPE_POWERPC, CPU_SUBTYPE_POWERPC_601): ("ppc601", "PowerPC 601"),
    (CPU_TYPE_POWERPC, CPU_SUBTYPE_POWERPC_603): ("ppc603", "PowerPC 603"),
    (CPU_TYPE_POWERPC, CPU_SUBTYPE_POWERPC_603E): ("ppc603e", "PowerPC 603e"),
    (CPU_TYPE_POWERPC, CPU_SUBTYPE_POWERPC_603EV): ("ppc603ev", "PowerPC 603ev"),
    (CPU_TYPE_POWERPC, CPU_SUBTYPE_POWERPC_604): ("ppc604", "PowerPC 604"),
    (CPU_TYPE_POWERPC, CPU_SUBTYPE_POWERPC_604E): ("ppc604e", "PowerPC 604e"),
    (CPU_TYPE_POWERPC, CPU_SUBTYPE_POWERPC_750): ("ppc750", "PowerPC 750"),
    (CPU_TYPE_POWERPC, CPU_SUBTYPE_POWERPC_7400): ("ppc7400", "PowerPC 7400"),
    (CPU_TYPE_POWERPC, CPU_SUBTYPE_POWERPC_7450): ("ppc7450", "PowerPC 7450"),
    (CPU_TYPE_POWERPC, CPU_SUBTYPE_POWERPC_970): ("ppc970", "PowerPC 970"),
    (CPU_TYPE_POWERPC64, CPU_SUBTYPE_POWERPC_ALL): ("ppc64", "PowerPC 64-bit"),
    (CPU_TYPE_POWERPC64, CPU_SUBTYPE_POWERPC_970): ("ppc970-64", "PowerPC 970 64-bit"),
    (CPU_TYPE_ANY, CPU_SUBTYPE_MULTIPLE): ("any", "Architecture Independent"),
    (CPU_TYPE_HPPA, CPU_SUBTYPE_HPPA_ALL): ("hppa", "HP-PA"),
    (CPU_TYPE_I860, CPU_SUBTYPE_I860_ALL): ("i860", "Intel 860"),
    (CPU_TYPE_MC680x0, CPU_SUBTYPE_MC680x0_ALL): ("m68k", "Motorola 68K"),
    (CPU_TYPE_MC88000, CPU_SUBTYPE_MC88000_ALL): ("m88k", "Motorola 88K"),
    (CPU_TYPE_SPARC, CPU_SUBTYPE_SPARC_ALL): ("sparc", "SPARC"),
    (CPU_TYPE_VEO, CPU_SUBTYPE_VEO_ALL): ("veo", "veo"),
    (CPU_TYPE_HPPA, CPU_SUBTYPE_HPPA_7100LC): ("hppa7100LC", "HP-PA 7100LC"),
    (CPU_TYPE_MC680x0, CPU_SUBTYPE_MC68030_ONLY): ("m68030", "Motorola 68030"),
    (CPU_TYPE_MC680x0, CPU_SUBTYPE_MC68040): ("m68040", "Motorola 68040"),
    (CPU_TYPE_VEO, CPU_SUBTYPE_VEO_1): ("veo1", "veo 1"),
    (CPU_TYPE_VEO, CPU_SUBTYPE_VEO_2): ("veo2", "veo 2"),
}


# Constants for the filetype field of the mach_header
MH_OBJECT = 0x01
MH_EXECUTE = 0x02
MH_FVMLIB = 0x03
MH_CORE = 0x04
MH_PRELOAD = 0x05
MH_DYLIB = 0x06
MH_DYLINKER = 0x07
MH_BUNDLE = 0x08
MH_DYLIB_STUB = 0x09
MH_DSYM = 0xa
MH_KEXT_BUNDLE = 0xb

_MH_FILETYPE_NAMES = {
    MH_OBJECT:      'relocatable object',
    MH_EXECUTE:     'demand paged executable',
    MH_FVMLIB:      'fixed vm shared library',
    MH_CORE:        'core',
    MH_PRELOAD:     'preloaded executable',
    MH_DYLIB:       'dynamically bound shared library',
    MH_DYLINKER:    'dynamic link editor',
    MH_BUNDLE:      'dynamically bound bundle',
    MH_DYLIB_STUB:  'shared library stub for static linking',
    MH_DSYM:        'symbol information',
    MH_KEXT_BUNDLE: 'x86_64 kexts',
}

_MH_FILETYPE_SHORTNAMES = {
    MH_OBJECT:      'object',
    MH_EXECUTE:     'execute',
    MH_FVMLIB:      'fvmlib',
    MH_CORE:        'core',
    MH_PRELOAD:     'preload',
    MH_DYLIB:       'dylib',
    MH_DYLINKER:    'dylinker',
    MH_BUNDLE:      'bundle',
    MH_DYLIB_STUB:  'dylib_stub',
    MH_DSYM:        'dsym',
    MH_KEXT_BUNDLE: 'kext',
}


MH_NOUNDEFS = 0x1
MH_INCRLINK = 0x2
MH_DYLDLINK = 0x4
MH_BINDATLOAD = 0x8
MH_PREBOUND = 0x10
MH_SPLIT_SEGS = 0x20
MH_LAZY_INIT = 0x40
MH_TWOLEVEL = 0x80
MH_FORCE_FLAT = 0x100
MH_NOMULTIDEFS = 0x200
MH_NOFIXPREBINDING = 0x400
MH_PREBINDABLE = 0x800
MH_ALLMODSBOUND = 0x1000
MH_SUBSECTIONS_VIA_SYMBOLS = 0x2000
MH_CANONICAL = 0x4000
MH_WEAK_DEFINES = 0x8000
MH_BINDS_TO_WEAK = 0x10000
MH_ALLOW_STACK_EXECUTION = 0x20000
MH_ROOT_SAFE = 0x40000
MH_SETUID_SAFE = 0x80000
MH_NO_REEXPORTED_DYLIBS = 0x100000
MH_PIE = 0x200000
MH_DEAD_STRIPPABLE_DYLIB = 0x400000
MH_HAS_TLV_DESCRIPTORS = 0x800000
MH_NO_HEAP_EXECUTION = 0x1000000
MH_APP_EXTENSION_SAFE = 0x2000000

_MH_FLAGS_NAMES = {
    MH_NOUNDEFS:                'MH_NOUNDEFS',
    MH_INCRLINK:                'MH_INCRLINK',
    MH_DYLDLINK:                'MH_DYLDLINK',
    MH_BINDATLOAD:              'MH_BINDATLOAD',
    MH_PREBOUND:                'MH_PREBOUND',
    MH_SPLIT_SEGS:              'MH_SPLIT_SEGS',
    MH_LAZY_INIT:               'MH_LAZY_INIT',
    MH_TWOLEVEL:                'MH_TWOLEVEL',
    MH_FORCE_FLAT:              'MH_FORCE_FLAT',
    MH_NOMULTIDEFS:             'MH_NOMULTIDEFS',
    MH_NOFIXPREBINDING:         'MH_NOFIXPREBINDING',
    MH_PREBINDABLE:             'MH_PREBINDABLE',
    MH_ALLMODSBOUND:            'MH_ALLMODSBOUND',
    MH_SUBSECTIONS_VIA_SYMBOLS: 'MH_SUBSECTIONS_VIA_SYMBOLS',
    MH_CANONICAL:               'MH_CANONICAL',
    MH_WEAK_DEFINES:            'MH_WEAK_DEFINES',
    MH_BINDS_TO_WEAK:           'MH_BINDS_TO_WEAK',
    MH_ALLOW_STACK_EXECUTION:   'MH_ALLOW_STACK_EXECUTION',
    MH_ROOT_SAFE:               'MH_ROOT_SAFE',
    MH_SETUID_SAFE:             'MH_SETUID_SAFE',
    MH_NO_REEXPORTED_DYLIBS:    'MH_NO_REEXPORTED_DYLIBS',
    MH_PIE:                     'MH_PIE',
    MH_DEAD_STRIPPABLE_DYLIB:   'MH_DEAD_STRIPPABLE_DYLIB',
    MH_HAS_TLV_DESCRIPTORS:     'MH_HAS_TLV_DESCRIPTORS',
    MH_NO_HEAP_EXECUTION:       'MH_NO_HEAP_EXECUTION',
    MH_APP_EXTENSION_SAFE:      'MH_APP_EXTENSION_SAFE',
}

_MH_FLAGS_DESCRIPTIONS = {
    MH_NOUNDEFS:                'no undefined references',
    MH_INCRLINK:                'output of an incremental link',
    MH_DYLDLINK:                'input for the dynamic linker',
    MH_BINDATLOAD:              'undefined references bound dynamically when loaded',
    MH_PREBOUND:                'dynamic undefined references prebound',
    MH_SPLIT_SEGS:              'split read-only and read-write segments',
    MH_LAZY_INIT:               '(obsolete)',
    MH_TWOLEVEL:                'using two-level name space bindings',
    MH_FORCE_FLAT:              'forcing all imagges to use flat name space bindings',
    MH_NOMULTIDEFS:             'umbrella guarantees no multiple definitions',
    MH_NOFIXPREBINDING:         'do not notify prebinding agent about this executable',
    MH_PREBINDABLE:             'the binary is not prebound but can have its prebinding redone',
    MH_ALLMODSBOUND:            'indicates that this binary binds to all two-level namespace modules of its dependent libraries',
    MH_SUBSECTIONS_VIA_SYMBOLS: 'safe to divide up the sections into sub-sections via symbols for dead code stripping',
    MH_CANONICAL:               'the binary has been canonicalized via the unprebind operation',
    MH_WEAK_DEFINES:            'the final linked image contains external weak symbols',
    MH_BINDS_TO_WEAK:           'the final linked image uses weak symbols',
    MH_ALLOW_STACK_EXECUTION:   'all stacks in the task will be given stack execution privilege',
    MH_ROOT_SAFE:               'the binary declares it is safe for use in processes with uid zero',
    MH_SETUID_SAFE:             'the binary declares it is safe for use in processes when issetugid() is true',
    MH_NO_REEXPORTED_DYLIBS:    'the static linker does not need to examine dependent dylibs to see if any are re-exported',
    MH_PIE:                     'the OS will load the main executable at a random address',
    MH_DEAD_STRIPPABLE_DYLIB:   'the static linker will automatically not create a LC_LOAD_DYLIB load command to the dylib if no symbols are being referenced from the dylib',
    MH_HAS_TLV_DESCRIPTORS:     'contains a section of type S_THREAD_LOCAL_VARIABLES',
    MH_NO_HEAP_EXECUTION:       'the OS will run the main executable with a non-executable heap even on platforms that don\'t require it',
    MH_APP_EXTENSION_SAFE:      'the code was linked for use in an application extension',
}

_MH_EXECUTE_SYM = "__mh_execute_header"
MH_EXECUTE_SYM = "_mh_execute_header"
_MH_BUNDLE_SYM = "__mh_bundle_header"
MH_BUNDLE_SYM = "_mh_bundle_header"
_MH_DYLIB_SYM = "__mh_dylib_header"
MH_DYLIB_SYM = "_mh_dylib_header"
_MH_DYLINKER_SYM = "__mh_dylinker_header"
MH_DYLINKER_SYM = "_mh_dylinker_header"


# Constants for load commands
LC_REQ_DYLD = 0x80000000

LC_SEGMENT = 0x1
LC_SYMTAB = 0x2
LC_SYMSEG = 0x3
LC_THREAD = 0x4
LC_UNIXTHREAD = 0x5
LC_LOADFVMLIB = 0x6
LC_IDFVMLIB = 0x7
LC_IDENT = 0x8
LC_FVMFILE = 0x9
LC_PREPAGE = 0xa
LC_DYSYMTAB = 0xb
LC_LOAD_DYLIB = 0xc
LC_ID_DYLIB = 0xd
LC_LOAD_DYLINKER = 0xe
LC_ID_DYLINKER = 0xf
LC_PREBOUND_DYLIB = 0x10
LC_ROUTINES = 0x11
LC_SUB_FRAMEWORK = 0x12
LC_SUB_UMBRELLA = 0x13
LC_SUB_CLIENT = 0x14
LC_SUB_LIBRARY = 0x15
LC_TWOLEVEL_HINTS = 0x16
LC_PREBIND_CKSUM = 0x17
LC_LOAD_WEAK_DYLIB = 0x18 | LC_REQ_DYLD
LC_SEGMENT_64 = 0x19
LC_ROUTINES_64 = 0x1a
LC_UUID = 0x1b
LC_RPATH = 0x1c | LC_REQ_DYLD
LC_CODE_SIGNATURE = 0x1d
LC_CODE_SEGMENT_SPLIT_INFO = 0x1e
LC_REEXPORT_DYLIB = 0x1f | LC_REQ_DYLD
LC_LAZY_LOAD_DYLIB = 0x20
LC_ENCRYPTION_INFO = 0x21
LC_DYLD_INFO = 0x22
LC_DYLD_INFO_ONLY = 0x22 | LC_REQ_DYLD
LC_LOAD_UPWARD_DYLIB = 0x23 | LC_REQ_DYLD
LC_VERSION_MIN_MACOSX = 0x24
LC_VERSION_MIN_IPHONEOS = 0x25
LC_FUNCTION_STARTS = 0x26
LC_DYLD_ENVIRONMENT = 0x27
LC_MAIN = 0x28 | LC_REQ_DYLD
LC_DATA_IN_CODE = 0x29
LC_SOURCE_VERSION = 0x2a
LC_DYLIB_CODE_SIGN_DRS = 0x2b
LC_ENCRYPTION_INFO_64 = 0x2c
LC_LINKER_OPTION = 0x2d
LC_LINKER_OPTIMIZATION_HINT = 0x2e
LC_VERSION_MIN_TVOS = 0x2f
LC_VERSION_MIN_WATCHOS = 0x30

_LC_NAMES = {
    LC_SEGMENT:                     'LC_SEGMENT',
    LC_IDFVMLIB:                    'LC_IDFVMLIB',
    LC_LOADFVMLIB:                  'LC_LOADFVMLIB',
    LC_ID_DYLIB:                    'LC_ID_DYLIB',
    LC_LOAD_DYLIB:                  'LC_LOAD_DYLIB',
    LC_LOAD_WEAK_DYLIB:             'LC_LOAD_WEAK_DYLIB',
    LC_SUB_FRAMEWORK:               'LC_SUB_FRAMEWORK',
    LC_SUB_CLIENT:                  'LC_SUB_CLIENT',
    LC_SUB_UMBRELLA:                'LC_SUB_UMBRELLA',
    LC_SUB_LIBRARY:                 'LC_SUB_LIBRARY',
    LC_PREBOUND_DYLIB:              'LC_PREBOUND_DYLIB',
    LC_ID_DYLINKER:                 'LC_ID_DYLINKER',
    LC_LOAD_DYLINKER:               'LC_LOAD_DYLINKER',
    LC_THREAD:                      'LC_THREAD',
    LC_UNIXTHREAD:                  'LC_UNIXTHREAD',
    LC_ROUTINES:                    'LC_ROUTINES',
    LC_SYMTAB:                      'LC_SYMTAB',
    LC_DYSYMTAB:                    'LC_DYSYMTAB',
    LC_TWOLEVEL_HINTS:              'LC_TWOLEVEL_HINTS',
    LC_PREBIND_CKSUM:               'LC_PREBIND_CKSUM',
    LC_SYMSEG:                      'LC_SYMSEG',
    LC_IDENT:                       'LC_IDENT',
    LC_FVMFILE:                     'LC_FVMFILE',
    LC_SEGMENT_64:                  'LC_SEGMENT_64',
    LC_ROUTINES_64:                 'LC_ROUTINES_64',
    LC_UUID:                        'LC_UUID',
    LC_RPATH:                       'LC_RPATH',
    LC_CODE_SIGNATURE:              'LC_CODE_SIGNATURE',
    LC_CODE_SEGMENT_SPLIT_INFO:     'LC_CODE_SEGMENT_SPLIT_INFO',
    LC_REEXPORT_DYLIB:              'LC_REEXPORT_DYLIB',
    LC_LAZY_LOAD_DYLIB:             'LC_LAZY_LOAD_DYLIB',
    LC_ENCRYPTION_INFO:             'LC_ENCRYPTION_INFO',
    LC_DYLD_INFO:                   'LC_DYLD_INFO',
    LC_DYLD_INFO_ONLY:              'LC_DYLD_INFO_ONLY',
    LC_LOAD_UPWARD_DYLIB:           'LC_LOAD_UPWARD_DYLIB',
    LC_VERSION_MIN_MACOSX:          'LC_VERSION_MIN_MACOSX',
    LC_VERSION_MIN_IPHONEOS:        'LC_VERSION_MIN_IPHONEOS',
    LC_FUNCTION_STARTS:             'LC_FUNCTION_STARTS',
    LC_DYLD_ENVIRONMENT:            'LC_DYLD_ENVIRONMENT',
    LC_MAIN:                        'LC_MAIN',
    LC_DATA_IN_CODE:                'LC_DATA_IN_CODE',
    LC_SOURCE_VERSION:              'LC_SOURCE_VERSION',
    LC_DYLIB_CODE_SIGN_DRS:         'LC_DYLIB_CODE_SIGN_DRS',
    LC_ENCRYPTION_INFO_64:          'LC_ENCRYPTION_INFO_64',
    LC_LINKER_OPTION:               'LC_LINKER_OPTION',
    LC_LINKER_OPTIMIZATION_HINT:    'LC_LINKER_OPTIMIZATION_HINT',
    LC_VERSION_MIN_TVOS:            'LC_VERSION_MIN_TVOS',
    LC_VERSION_MIN_WATCHOS:         'LC_VERSION_MIN_WATCHOS',
}

# Constants for the flags field of the segment_command
SG_HIGHVM = 0x1
SG_FVMLIB = 0x2
SG_NORELOC = 0x4
SG_PROTECTED_VERSION_1 = 0x8

SEG_PAGEZERO = "__PAGEZERO"
SEG_TEXT = "__TEXT"
SECT_TEXT = "__text"
SECT_FVMLIB_INIT0 = "__fvmlib_init0"
SECT_FVMLIB_INIT1 = "__fvmlib_init1"
SEG_DATA = "__DATA"
SECT_DATA = "__data"
SECT_BSS = "__bss"
SECT_COMMON = "__common"
SEG_OBJC = "__OBJC"
SECT_OBJC_SYMBOLS = "__symbol_table"
SECT_OBJC_MODULES = "__module_info"
SECT_OBJC_STRINGS = "__selector_strs"
SECT_OBJC_REFS = "__selector_refs"
SEG_ICON = "__ICON"
SECT_ICON_HEADER = "__header"
SECT_ICON_TIFF = "__tiff"
SEG_LINKEDIT = "__LINKEDIT"
SEG_UNIXSTACK = "__UNIXSTACK"
SEG_IMPORT = "__IMPORT"


# flags field of a section structure
SECTION_TYPE = 0xff
SECTION_ATTRIBUTES = 0xffffff00

# Constants for the type of a section
S_REGULAR = 0x0
S_ZEROFILL = 0x1
S_CSTRING_LITERALS = 0x2
S_4BYTE_LITERALS = 0x3
S_8BYTE_LITERALS = 0x4
S_LITERAL_POINTERS = 0x5
S_NON_LAZY_SYMBOL_POINTERS = 0x6
S_LAZY_SYMBOL_POINTERS = 0x7
S_SYMBOL_STUBS = 0x8
S_MOD_INIT_FUNC_POINTERS = 0x9
S_MOD_TERM_FUNC_POINTERS = 0xa
S_COALESCED = 0xb
S_GB_ZEROFILL = 0xc
S_INTERPOSING = 0xd
S_16BYTE_LITERALS = 0xe
S_DTRACE_DOF = 0xf
S_LAZY_DYLIB_SYMBOL_POINTERS = 0x10
S_THREAD_LOCAL_REGULAR = 0x11
S_THREAD_LOCAL_ZEROFILL = 0x12
S_THREAD_LOCAL_VARIABLES = 0x13
S_THREAD_LOCAL_VARIABLE_POINTERS = 0x14
S_THREAD_LOCAL_INIT_FUNCTION_POINTERS = 0x15

_FLAG_SECTION_TYPES = {
    S_REGULAR: "S_REGULAR",
    S_ZEROFILL: "S_ZEROFILL",
    S_CSTRING_LITERALS: "S_CSTRING_LITERALS",
    S_4BYTE_LITERALS: "S_4BYTE_LITERALS",
    S_8BYTE_LITERALS: "S_8BYTE_LITERALS",
    S_LITERAL_POINTERS: "S_LITERAL_POINTERS",
    S_NON_LAZY_SYMBOL_POINTERS: "S_NON_LAZY_SYMBOL_POINTERS",
    S_LAZY_SYMBOL_POINTERS: "S_LAZY_SYMBOL_POINTERS",
    S_SYMBOL_STUBS: "S_SYMBOL_STUBS",
    S_MOD_INIT_FUNC_POINTERS: "S_MOD_INIT_FUNC_POINTERS",
    S_MOD_TERM_FUNC_POINTERS: "S_MOD_TERM_FUNC_POINTERS",
    S_COALESCED: "S_COALESCED",
    S_GB_ZEROFILL: "S_GB_ZEROFILL",
    S_INTERPOSING: "S_INTERPOSING",
    S_16BYTE_LITERALS: "S_16BYTE_LITERALS",
    S_DTRACE_DOF: "S_DTRACE_DOF",
    S_LAZY_DYLIB_SYMBOL_POINTERS: "S_LAZY_DYLIB_SYMBOL_POINTERS",
    S_THREAD_LOCAL_REGULAR: "S_THREAD_LOCAL_REGULAR",
    S_THREAD_LOCAL_ZEROFILL: "S_THREAD_LOCAL_ZEROFILL",
    S_THREAD_LOCAL_VARIABLES: "S_THREAD_LOCAL_VARIABLES",
    S_THREAD_LOCAL_VARIABLE_POINTERS: "S_THREAD_LOCAL_VARIABLE_POINTERS",
    S_THREAD_LOCAL_INIT_FUNCTION_POINTERS: "S_THREAD_LOCAL_INIT_FUNCTION_POINTERS"
}

# Constants for the section attributes part of the flags field of a section structure.
SECTION_ATTRIBUTES_USR = 0xff000000
SECTION_ATTRIBUTES_SYS = 0x00ffff00
S_ATTR_PURE_INSTRUCTIONS = 0x80000000
S_ATTR_NO_TOC = 0x40000000
S_ATTR_STRIP_STATIC_SYMS = 0x20000000
S_ATTR_NO_DEAD_STRIP = 0x10000000
S_ATTR_LIVE_SUPPORT = 0x08000000
S_ATTR_SELF_MODIFYING_CODE = 0x04000000
S_ATTR_DEBUG = 0x02000000
S_ATTR_SOME_INSTRUCTIONS = 0x00000400
S_ATTR_EXT_RELOC = 0x00000200
S_ATTR_LOC_RELOC = 0x00000100

_FLAG_SECTION_ATTRIBUTES = {
    S_ATTR_PURE_INSTRUCTIONS: "S_ATTR_PURE_INSTRUCTIONS",
    S_ATTR_NO_TOC: "S_ATTR_NO_TOC",
    S_ATTR_STRIP_STATIC_SYMS: "S_ATTR_STRIP_STATIC_SYMS",
    S_ATTR_NO_DEAD_STRIP: "S_ATTR_NO_DEAD_STRIP",
    S_ATTR_LIVE_SUPPORT: "S_ATTR_LIVE_SUPPORT",
    S_ATTR_SELF_MODIFYING_CODE: "S_ATTR_SELF_MODIFYING_CODE",
    S_ATTR_DEBUG: "S_ATTR_DEBUG",
    S_ATTR_SOME_INSTRUCTIONS: "S_ATTR_SOME_INSTRUCTIONS",
    S_ATTR_EXT_RELOC: "S_ATTR_EXT_RELOC",
    S_ATTR_LOC_RELOC: "S_ATTR_LOC_RELOC"
}


# Mach-O header

MH_MAGIC = 0xfeedface
MH_CIGAM = 0xcefaedfe
MH_MAGIC_64 = 0xfeedfacf
MH_CIGAM_64 = 0xcffaedfe


class mach_header(Structure):
    _fields_ = (
        ('magic', p_uint32),
        ('cputype', cpu_type_t),
        ('cpusubtype', cpu_subtype_t),
        ('filetype', p_uint32),
        ('ncmds', p_uint32),
        ('sizeofcmds', p_uint32),
        ('flags', p_uint32),
    )

    def _describe(self):
        bit = 1
        flags = self.flags
        dflags = []
        while flags and bit < (1 << 32):
            if flags & bit:
                dflags.append({
                    'name': _MH_FLAGS_NAMES.get(bit, str(bit)),
                    'value': bit,
                    'description': _MH_FLAGS_DESCRIPTIONS.get(bit, str(bit))
                })
                flags = flags ^ bit
            bit <<= 1

        cpu_str, cpusub_str = _CPU_TYPE_TABLE.get((self.cputype, self.cpusubtype),
                                                  (str(self.cputype), str(self.cpusubtype)))
        return (
            ('magic', int(self.magic)),
            ('cputype_string', cpu_str),
            ('cputype', int(self.cputype)),
            ('cpusubtype_string', cpusub_str),
            ('cpusubtype', int(self.cpusubtype)),
            ('filetype_string', _MH_FILETYPE_NAMES.get(self.filetype, self.filetype)),
            ('filetype', int(self.filetype)),
            ('ncmds', self.ncmds),
            ('sizeofcmds', self.sizeofcmds),
            ('flags', dflags),
            ('raw_flags', int(self.flags))
        )


class mach_header_64(mach_header):
    _fields_ = mach_header._fields_ + (('reserved', p_uint32),)


class load_command(Structure):
    _fields_ = (
        ('cmd', p_uint32),
        ('cmdsize', p_uint32),
    )

    def get_cmd_name(self):
        return _LC_NAMES.get(self.cmd, self.cmd)


# this is really a union.. but whatever
class lc_str(p_uint32):
    pass


p_str16 = pypackable('p_str16', bytes, '16s')
vm_prot_t = p_int32


class segment_command(Structure):
    _fields_ = (
        ('segname', p_str16),
        ('vmaddr', p_uint32),
        ('vmsize', p_uint32),
        ('fileoff', p_uint32),
        ('filesize', p_uint32),
        ('maxprot', vm_prot_t),
        ('initprot', vm_prot_t),
        ('nsects', p_uint32),  # read the section structures ?
        ('flags', p_uint32),
    )

    def describe(self):
        s = {}
        if self.segment.find('\x00') != -1:
            s['segname'] = self.segname[:self.segment.find('\x00')]
        else:
            s['segname'] = self.segname
        s['vmaddr'] = int(self.vmaddr)
        s['vmsize'] = int(self.vmsize)
        s['fileoff'] = int(self.fileoff)
        s['filesize'] = int(self.filesize)
        s['initprot'] = self.get_vm_prot_desc(self.initprot)
        s['initprot_raw'] = int(self.initprot)
        s['maxprot'] = self.get_vm_prot_desc(self.maxprot)
        s['maxprot_raw'] = int(self.maxprot)
        s['nsects'] = int(self.nsects)
        s['flags'] = self.flags
        return s

    def get_vm_prot_desc(self, prot):
        vm = []
        if prot == 0:
            vm.append("VM_PROT_NONE")
        if prot & 1:
            vm.append("VM_PROT_READ")
        if prot & 2:
            vm.append("VM_PROT_WRITE")
        if prot & 4:
            vm.append("VM_PROT_EXECUTE")
        return vm


class segment_command_64(Structure):
    _fields_ = (
        ('segname', p_str16),
        ('vmaddr', p_uint64),
        ('vmsize', p_uint64),
        ('fileoff', p_uint64),
        ('filesize', p_uint64),
        ('maxprot', vm_prot_t),
        ('initprot', vm_prot_t),
        ('nsects', p_uint32), # read the section structures ?
        ('flags', p_uint32),
    )

    def describe(self):
        s = {}
        s['segname'] = self.segname.rstrip('\x00')
        s['vmaddr'] = int(self.vmaddr)
        s['vmsize'] = int(self.vmsize)
        s['fileoff'] = int(self.fileoff)
        s['filesize'] = int(self.filesize)
        s['initprot'] = self.get_vm_prot_desc(self.initprot)
        s['initprot_raw'] = int(self.initprot)
        s['maxprot'] = self.get_vm_prot_desc(self.maxprot)
        s['maxprot_raw'] = int(self.maxprot)
        s['nsects'] = int(self.nsects)
        s['flags'] = self.flags
        return s

    def get_vm_prot_desc(self, prot):
        vm = []
        if prot == 0:
            vm.append("VM_PROT_NONE")
        if prot & 1:
            vm.append("VM_PROT_READ")
        if prot & 2:
            vm.append("VM_PROT_WRITE")
        if prot & 4:
            vm.append("VM_PROT_EXECUTE")
        return vm


class section(Structure):
    _fields_ = (
        ('sectname', p_str16),
        ('segname', p_str16),
        ('addr', p_uint32),
        ('size', p_uint32),
        ('offset', p_uint32),
        ('align', p_uint32),
        ('reloff', p_uint32),
        ('nreloc', p_uint32),
        ('flags', p_uint32),
        ('reserved1', p_uint32),
        ('reserved2', p_uint32),
    )

    def describe(self):
        s = {}
        if self.secname.find('\x00') != -1:
            s['sectname'] = self.sectname[:self.secname.find('\x00')]
        else:
            s['sectname'] = self.sectname
        if self.segment.find('\x00') != -1:
            s['segname'] = self.segname[:self.segment.find('\x00')]
        else:
            s['segname'] = self.segname
        s['addr'] = int(self.addr)
        s['size'] = int(self.size)
        s['offset'] = int(self.offset)
        s['align'] = int(self.align)
        s['reloff'] = int(self.reloff)
        s['nreloc'] = int(self.nreloc)
        flags = {}
        flags['type'] = _FLAG_SECTION_TYPES[int(self.flags) & SECTION_TYPE]
        flags['type_raw'] = int(self.flags) & SECTION_TYPE
        flags['attributes'] = []
        flags['attributes_raw'] = []
        for k in _FLAG_SECTION_ATTRIBUTES:
            if k & self.flags:
                flags['attributes'].append(_FLAG_SECTION_ATTRIBUTES[k])
                flags['attributes_raw'].append(k)
        s['flags'] = flags
        s['reserved1'] = int(self.reserved1)
        s['reserved2'] = int(self.reserved2)
        return s

    def add_section_data(self, data):
        self.section_data = data


class section_64(Structure):
    _fields_ = (
        ('sectname', p_str16),
        ('segname', p_str16),
        ('addr', p_uint64),
        ('size', p_uint64),
        ('offset', p_uint32),
        ('align', p_uint32),
        ('reloff', p_uint32),
        ('nreloc', p_uint32),
        ('flags', p_uint32),
        ('reserved1', p_uint32),
        ('reserved2', p_uint32),
        ('reserved3', p_uint32),
    )

    def describe(self):
        s = {}
        if self.secname.find('\x00') != -1:
            s['sectname'] = self.sectname[:self.secname.find('\x00')]
        else:
            s['sectname'] = self.sectname
        if self.segment.find('\x00') != -1:
            s['segname'] = self.segname[:self.segment.find('\x00')]
        else:
            s['segname'] = self.segname
        s['addr'] = int(self.addr)
        s['size'] = int(self.size)
        s['offset'] = int(self.offset)
        s['align'] = int(self.align)
        s['reloff'] = int(self.reloff)
        s['nreloc'] = int(self.nreloc)
        flags = {}
        flags['type'] = _FLAG_SECTION_TYPES[int(self.flags) & SECTION_TYPE]
        flags['type_raw'] = int(self.flags) & SECTION_TYPE
        flags['attributes'] = []
        flags['attributes_raw'] = []
        for k in _FLAG_SECTION_ATTRIBUTES:
            if k & self.flags:
                flags['attributes'].append(_FLAG_SECTION_ATTRIBUTES[k])
                flags['attributes_raw'].append(k)
        s['flags'] = flags
        s['reserved1'] = int(self.reserved1)
        s['reserved2'] = int(self.reserved2)
        s['reserved3'] = int(self.reserved3)
        return s

    def add_section_data(self, data):
        self.section_data = data


#
#  I really should remove all these _command classes because they
#  are no different.  I decided to keep the load commands separate,
#  so classes like fvmlib and fvmlib_command are equivalent.
#

class mach_version_helper(Structure):
    _fields_ = (
        ('major', p_ushort),
        ('minor', p_uint8),
        ('rev', p_uint8),
    )

    def __str__(self):
        return '%s.%s.%s' % (self.major, self.minor, self.rev)


class mach_timestamp_helper(p_uint32):
    # TODO: this maybe not suitable for dump
    def __str__(self):
        return time.ctime(self)


class fvmlib(Structure):
    _fields_ = (
        ('name', lc_str),
        ('minor_version', mach_version_helper),
        ('header_addr', p_uint32),
    )


class fvmlib_command(Structure):
    _fields_ = fvmlib._fields_

    def describe(self):
        s = {}
        s['header_addr'] = int(self.header_addr)
        return s


class dylib(Structure):
    _fields_ = (
        ('name', lc_str),
        ('timestamp', mach_timestamp_helper),
        ('current_version', mach_version_helper),
        ('compatibility_version', mach_version_helper),
    )


# merged dylib structure
class dylib_command(Structure):
    _fields_ = dylib._fields_

    def describe(self):
        s = {}
        s['timestamp'] = str(self.timestamp)
        s['current_version'] = str(self.current_version)
        s['compatibility_version'] = str(self.compatibility_version)
        return s


class sub_framework_command(Structure):
    _fields_ = (
        ('umbrella', lc_str),
    )

    def describe(self):
        return {}


class sub_client_command(Structure):
    _fields_ = (
        ('client', lc_str),
    )

    def describe(self):
        return {}


class sub_umbrella_command(Structure):
    _fields_ = (
        ('sub_umbrella', lc_str),
    )

    def describe(self):
        return {}


class sub_library_command(Structure):
    _fields_ = (
        ('sub_library', lc_str),
    )

    def describe(self):
        return {}


class prebound_dylib_command(Structure):
    _fields_ = (
        ('name', lc_str),
        ('nmodules', p_uint32),
        ('linked_modules', lc_str),
    )

    def describe(self):
        return {'nmodules': int(self.nmodules)}


class dylinker_command(Structure):
    _fields_ = (
        ('name', lc_str),
    )

    def describe(self):
        return {}


class thread_command(Structure):
    _fields_ = (
    )

    def describe(self):
        return {}


class entry_point_command(Structure):
    _fields_ = (
        ('entryoff', p_uint64),
        ('stacksize', p_uint64),
    )

    def describe(self):
        s = {}
        s['entryoff'] = int(self.entryoff)
        s['stacksize'] = int(self.stacksize)
        return s


class routines_command(Structure):
    _fields_ = (
        ('init_address', p_uint32),
        ('init_module', p_uint32),
        ('reserved1', p_uint32),
        ('reserved2', p_uint32),
        ('reserved3', p_uint32),
        ('reserved4', p_uint32),
        ('reserved5', p_uint32),
        ('reserved6', p_uint32),
    )

    def describe(self):
        s = {}
        s['init_address'] = int(self.init_address)
        s['init_module'] = int(self.init_module)
        s['reserved1'] = int(self.reserved1)
        s['reserved2'] = int(self.reserved2)
        s['reserved3'] = int(self.reserved3)
        s['reserved4'] = int(self.reserved4)
        s['reserved5'] = int(self.reserved5)
        s['reserved6'] = int(self.reserved6)
        return s


class routines_command_64(Structure):
    _fields_ = (
        ('init_address', p_uint64),
        ('init_module', p_uint64),
        ('reserved1', p_uint64),
        ('reserved2', p_uint64),
        ('reserved3', p_uint64),
        ('reserved4', p_uint64),
        ('reserved5', p_uint64),
        ('reserved6', p_uint64),
    )

    def describe(self):
        s = {}
        s['init_address'] = int(self.init_address)
        s['init_module'] = int(self.init_module)
        s['reserved1'] = int(self.reserved1)
        s['reserved2'] = int(self.reserved2)
        s['reserved3'] = int(self.reserved3)
        s['reserved4'] = int(self.reserved4)
        s['reserved5'] = int(self.reserved5)
        s['reserved6'] = int(self.reserved6)
        return s


class symtab_command(Structure):
    _fields_ = (
        ('symoff', p_uint32),
        ('nsyms', p_uint32),
        ('stroff', p_uint32),
        ('strsize', p_uint32),
    )

    def describe(self):
        s = {}
        s['symoff'] = int(self.symoff)
        s['nsyms'] = int(self.nsyms)
        s['stroff'] = int(self.stroff)
        s['strsize'] = int(self.strsize)
        return s


class dysymtab_command(Structure):
    _fields_ = (
        ('ilocalsym', p_uint32),
        ('nlocalsym', p_uint32),
        ('iextdefsym', p_uint32),
        ('nextdefsym', p_uint32),
        ('iundefsym', p_uint32),
        ('nundefsym', p_uint32),
        ('tocoff', p_uint32),
        ('ntoc', p_uint32),
        ('modtaboff', p_uint32),
        ('nmodtab', p_uint32),
        ('extrefsymoff', p_uint32),
        ('nextrefsyms', p_uint32),
        ('indirectsymoff', p_uint32),
        ('nindirectsyms', p_uint32),
        ('extreloff', p_uint32),
        ('nextrel', p_uint32),
        ('locreloff', p_uint32),
        ('nlocrel', p_uint32),
    )

    def describe(self):
        dys = {}
        dys['ilocalsym'] = int(self.ilocalsym)
        dys['nlocalsym'] = int(self.nlocalsym)
        dys['iextdefsym'] = int(self.iextdefsym)
        dys['nextdefsym'] = int(self.nextdefsym)
        dys['iundefsym'] = int(self.iundefsym)
        dys['nundefsym'] = int(self.nundefsym)
        dys['tocoff'] = int(self.tocoff)
        dys['ntoc'] = int(self.ntoc)
        dys['modtaboff'] = int(self.modtaboff)
        dys['nmodtab'] = int(self.nmodtab)
        dys['extrefsymoff'] = int(self.extrefsymoff)
        dys['nextrefsyms'] = int(self.nextrefsyms)
        dys['indirectsymoff'] = int(self.indirectsymoff)
        dys['nindirectsyms'] = int(self.nindirectsyms)
        dys['extreloff'] = int(self.extreloff)
        dys['nextrel'] = int(self.nextrel)
        dys['locreloff'] = int(self.locreloff)
        dys['nlocrel'] = int(self.nlocrel)
        return dys


INDIRECT_SYMBOL_LOCAL = 0x80000000
INDIRECT_SYMBOL_ABS = 0x40000000


class dylib_table_of_contents(Structure):
    _fields_ = (
        ('symbol_index', p_uint32),
        ('module_index', p_uint32),
    )


class dylib_module(Structure):
    _fields_ = (
        ('module_name', p_uint32),
        ('iextdefsym', p_uint32),
        ('nextdefsym', p_uint32),
        ('irefsym', p_uint32),
        ('nrefsym', p_uint32),
        ('ilocalsym', p_uint32),
        ('nlocalsym', p_uint32),
        ('iextrel', p_uint32),
        ('nextrel', p_uint32),
        ('iinit_iterm', p_uint32),
        ('ninit_nterm', p_uint32),
        ('objc_module_info_addr', p_uint32),
        ('objc_module_info_size', p_uint32),
    )


class dylib_module_64(Structure):
    _fields_ = (
        ('module_name', p_uint32),
        ('iextdefsym', p_uint32),
        ('nextdefsym', p_uint32),
        ('irefsym', p_uint32),
        ('nrefsym', p_uint32),
        ('ilocalsym', p_uint32),
        ('nlocalsym', p_uint32),
        ('iextrel', p_uint32),
        ('nextrel', p_uint32),
        ('iinit_iterm', p_uint32),
        ('ninit_nterm', p_uint32),
        ('objc_module_info_size', p_uint32),
        ('objc_module_info_addr', p_uint64),
    )


class dylib_reference(Structure):
    _fields_ = (
        # XXX - ick, fix
        ('isym_flags', p_uint32),
        # ('isym', p_uint8 * 3),
        # ('flags', p_uint8),
    )


class twolevel_hints_command(Structure):
    _fields_ = (
        ('offset', p_uint32),
        ('nhints', p_uint32),
    )

    def describe(self):
        s = {}
        s['offset'] = int(self.offset)
        s['nhints'] = int(self.nhints)
        return s


class twolevel_hint(Structure):
    _fields_ = (
      # XXX - ick, fix
      ('isub_image_itoc', p_uint32),
      #('isub_image', p_uint8),
      #('itoc', p_uint8 * 3),
  )


class prebind_cksum_command(Structure):
    _fields_ = (
        ('cksum', p_uint32),
    )

    def describe(self):
        return {'cksum': int(self.cksum)}


class symseg_command(Structure):
    _fields_ = (
        ('offset', p_uint32),
        ('size', p_uint32),
    )

    def describe(self):
        s = {}
        s['offset'] = int(self.offset)
        s['size'] = int(self.size)


class ident_command(Structure):
    _fields_ = (
    )

    def describe(self):
        return {}


class fvmfile_command(Structure):
    _fields_ = (
        ('name', lc_str),
        ('header_addr', p_uint32),
    )

    def describe(self):
        return {'header_addr': int(self.header_addr)}


class uuid_command (Structure):
    _fields_ = (
        ('uuid', p_str16),
    )

    def describe(self):
        return {'uuid': self.uuid.rstrip('\x00')}


class rpath_command (Structure):
    _fields_ = (
        ('path', lc_str),
    )

    def describe(self):
        return {}


class linkedit_data_command (Structure):
    _fields_ = (
        ('dataoff',   p_uint32),
        ('datasize', p_uint32),
    )

    def describe(self):
        s = {}
        s['dataoff'] = int(self.dataoff)
        s['datasize'] = int(self.datasize)
        return s


class version_min_command (Structure):
    _fields_ = (
        ('version', p_uint32), # X.Y.Z is encoded in nibbles xxxx.yy.zz
        ('sdk', p_uint32),
    )

    def describe(self):
        v = int(self.version)
        v3 = v & 0xFF
        v = v >> 8
        v2 = v & 0xFF
        v = v >> 8
        v1 = v & 0xFFFF
        s = int(self.sdk)
        s3 = s & 0xFF
        s = s >> 8
        s2 = s & 0xFF
        s = s >> 8
        s1 = s & 0xFFFF
        return {
            'version': str(int(v1)) + "." + str(int(v2)) + "." + str(int(v3)),
            'sdk': str(int(s1)) + "." + str(int(s2)) + "." + str(int(s3)),
        }


class source_version_command (Structure):
    _fields_ = (
        ('version',   p_uint64),
    )

    def describe(self):
        v = int(self.version)
        a = v >> 40
        b = (v >> 30) & 0x3ff
        c = (v >> 20) & 0x3ff
        d = (v >> 10) & 0x3ff
        e = v & 0x3ff
        r = str(a)+'.'+str(b)+'.'+str(c)+'.'+str(d)+'.'+str(e)
        return {'version': r}


class encryption_info_command (Structure):
    _fields_ = (
        ('cryptoff',    p_uint32),
        ('cryptsize',   p_uint32),
        ('cryptid',     p_uint32),
    )

    def describe(self):
        s = {}
        s['cryptoff'] = int(self.cryptoff)
        s['cryptsize'] = int(self.cryptsize)
        s['cryptid'] = int(self.cryptid)
        return s


class encryption_info_command_64 (Structure):
    _fields_ = (
        ('cryptoff',    p_uint32),
        ('cryptsize',   p_uint32),
        ('cryptid',     p_uint32),
        ('pad',         p_uint32),
    )

    def describe(self):
        s = {}
        s['cryptoff'] = int(self.cryptoff)
        s['cryptsize'] = int(self.cryptsize)
        s['cryptid'] = int(self.cryptid)
        s['pad'] = int(self.pad)
        return s


class dyld_info_command (Structure):
    _fields_ = (
        ('rebase_off',     p_uint32),
        ('rebase_size',    p_uint32),
        ('bind_off',       p_uint32),
        ('bind_size',      p_uint32),
        ('weak_bind_off',  p_uint32),
        ('weak_bind_size', p_uint32),
        ('lazy_bind_off',  p_uint32),
        ('lazy_bind_size', p_uint32),
        ('export_off',     p_uint32),
        ('export_size',    p_uint32),
    )

    def describe(self):
        dyld = {}
        dyld['rebase_off'] = int(self.rebase_off)
        dyld['rebase_size'] = int(self.rebase_size)
        dyld['bind_off'] = int(self.bind_off)
        dyld['bind_size'] = int(self.bind_size)
        dyld['weak_bind_off'] = int(self.weak_bind_off)
        dyld['weak_bind_size'] = int(self.weak_bind_size)
        dyld['lazy_bind_off'] = int(self.lazy_bind_off)
        dyld['lazy_bind_size'] = int(self.lazy_bind_size)
        dyld['export_off'] = int(self.export_off)
        dyld['export_size'] = int(self.export_size)
        return dyld


class linker_option_command (Structure):
    _fields_ = (
        ('count',         p_uint32),
    )

    def describe(self):
        return {'count': int(self.count)}


LC_REGISTRY = {
    LC_SEGMENT: segment_command,
    LC_IDFVMLIB: fvmlib_command,
    LC_LOADFVMLIB: fvmlib_command,
    LC_ID_DYLIB: dylib_command,
    LC_LOAD_DYLIB: dylib_command,
    LC_LOAD_WEAK_DYLIB: dylib_command,
    LC_SUB_FRAMEWORK: sub_framework_command,
    LC_SUB_CLIENT: sub_client_command,
    LC_SUB_UMBRELLA: sub_umbrella_command,
    LC_SUB_LIBRARY: sub_library_command,
    LC_PREBOUND_DYLIB: prebound_dylib_command,
    LC_ID_DYLINKER: dylinker_command,
    LC_LOAD_DYLINKER: dylinker_command,
    LC_THREAD: thread_command,
    LC_UNIXTHREAD: thread_command,
    LC_ROUTINES: routines_command,
    LC_SYMTAB: symtab_command,
    LC_DYSYMTAB: dysymtab_command,
    LC_TWOLEVEL_HINTS: twolevel_hints_command,
    LC_PREBIND_CKSUM: prebind_cksum_command,
    LC_SYMSEG: symseg_command,
    LC_IDENT: ident_command,
    LC_FVMFILE: fvmfile_command,
    LC_SEGMENT_64: segment_command_64,
    LC_ROUTINES_64: routines_command_64,
    LC_UUID: uuid_command,
    LC_RPATH: rpath_command,
    LC_CODE_SIGNATURE: linkedit_data_command,
    LC_CODE_SEGMENT_SPLIT_INFO: linkedit_data_command,
    LC_REEXPORT_DYLIB: dylib_command,
    LC_LAZY_LOAD_DYLIB: dylib_command,
    LC_ENCRYPTION_INFO: encryption_info_command,
    LC_DYLD_INFO: dyld_info_command,
    LC_DYLD_INFO_ONLY: dyld_info_command,
    LC_LOAD_UPWARD_DYLIB: dylib_command,
    LC_VERSION_MIN_MACOSX: version_min_command,
    LC_VERSION_MIN_IPHONEOS: version_min_command,
    LC_FUNCTION_STARTS: linkedit_data_command,
    LC_DYLD_ENVIRONMENT: dylinker_command,
    LC_MAIN: entry_point_command,
    LC_DATA_IN_CODE: linkedit_data_command,
    LC_SOURCE_VERSION: source_version_command,
    LC_DYLIB_CODE_SIGN_DRS: linkedit_data_command,
    LC_ENCRYPTION_INFO_64: encryption_info_command_64,
    LC_LINKER_OPTION: linker_option_command,
    LC_LINKER_OPTIMIZATION_HINT: linkedit_data_command,
    LC_VERSION_MIN_TVOS: version_min_command,
    LC_VERSION_MIN_WATCHOS: version_min_command,
}


## Symbol table nlist.h

# an union
class n_un(p_int32):
    pass


class nlist(Structure):
    _fields_ = (
        ('n_un', n_un),
        ('n_type', p_uint8),
        ('n_sect', p_uint8),
        ('n_desc', p_short),
        ('n_value', p_uint32),
    )


class nlist_64(Structure):
    _fields_ = [
        ('n_un',    n_un),
        ('n_type', p_uint8),
        ('n_sect', p_uint8),
        ('n_desc', p_short),
        ('n_value', p_int64),
    ]

# four fields in the n_type
N_STAB = 0xe0  # if any of these bits set, a symbolic debugging entry
N_PEXT = 0x10  # private external symbol bit
N_TYPE = 0x0e  # mask for the type bits
N_EXT = 0x01  # external symbol bit, set for external symbols

# Values for N_TYPE bits of the n_type field.
N_UNDF = 0x0  # undefined, n_sect == NO_SECT
N_ABS = 0x2  # absolute, n_sect == NO_SECT
N_SECT = 0xe  # defined in section number n_sect
N_PBUD = 0xc  # prebound undefined (defined in a dylib)
N_INDR = 0xa  # indirect

NO_SECT = 0  # symbol is not in any section
MAX_SECT = 255  # 1 thru 255 inclusive

# Reference type bits of the n_desc field of undefined symbols
REFERENCE_TYPE = 0xf
REFERENCE_FLAG_UNDEFINED_NON_LAZY = 0
REFERENCE_FLAG_UNDEFINED_LAZY = 1
REFERENCE_FLAG_DEFINED = 2
REFERENCE_FLAG_PRIVATE_DEFINED = 3
REFERENCE_FLAG_PRIVATE_UNDEFINED_NON_LAZY = 4
REFERENCE_FLAG_PRIVATE_UNDEFINED_LAZY = 5

REFERENCED_DYNAMICALLY = 0x0010


def GET_LIBRARY_ORDINAL(n_desc):
    return (((n_desc) >> 8) & 0xff)


def SET_LIBRARY_ORDINAL(n_desc, ordinal):
    return (((n_desc) & 0x00ff) | (((ordinal & 0xff) << 8)))

SELF_LIBRARY_ORDINAL = 0x0
MAX_LIBRARY_ORDINAL = 0xfd
DYNAMIC_LOOKUP_ORDINAL = 0xfe
EXECUTABLE_ORDINAL = 0xff

N_DESC_DISCARDED = 0x0020
N_WEAK_REF = 0x0040
N_WEAK_DEF = 0x0080


## FAT header
FAT_MAGIC = 0xcafebabe
FAT_CIGAM = 0xbebafeca


class fat_header(Structure):
    _fields_ = (
        ('magic', p_uint32),
        ('nfat_arch', p_uint32),
    )


class fat_arch(Structure):
    _fields_ = (
        ('cputype', cpu_type_t),
        ('cpusubtype', cpu_subtype_t),
        ('offset', p_uint32),
        ('size', p_uint32),
        ('align', p_uint32),
    )
