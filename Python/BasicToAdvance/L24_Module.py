# Module = A file containing python code, May contain function, classes, etc. 
            # used with modular programming, which is to separate a program into part.


# msg is file name import from this folder
import mes       # Rule No1. this is a create a pacache folder by delalut
mes.hello() 
mes.bye()

print("\nPrint a New Line \n")

# import mes as message # Rule No2 . 
# message.hello() 
# message.bye() 

from mes import hello,bye # Rule No3 . 
bye()
hello()

from mes import * # Rule No4 :  It working a a long program 
hello()
bye()

# Note: ------------ All Marging Import From Labiray
help("modules")


'''
# OUTPUT OF help("module ")   Run


L10_Dictonary       _signal             encodings           quopri
L11_Index           _sitebuiltins       ensurepip           random
L12_Functions       _socket             enum                re
L13_ReturnS         _sqlite3            errno               reprlib
L14_Keyword         _sre                faulthandler        rlcompleter
L15_Nested          _ssl                filecmp             runpy
L16_Scope_Var       _stat               fileinput           sched
L17_Args            _statistics         fnmatch             secrets
L18_Kwargs          _string             fractions           select
L19_Format          _strptime           ftplib              selectors
L1_Intro            _struct             functools           shelve
L20_ImRandom        _symtable           gc                  shlex
L21_ExecptionH      _testbuffer         genericpath         shutil
L22_ImportOs        _testcapi           getopt              signal
L23_FileHandling    _testclinic         getpass             site
L24_Module          _testconsole        gettext             smtplib
L2_ImportFun        _testimportmultiple glob                sndhdr
L3_Slicing          _testinternalcapi   graphlib            socket
L4_Conditions       _testmultiphase     gzip                socketserver
L5_Operators        _testsinglephase    hashlib             sqlite3
L6_Loop             _thread             heapq               sre_compile
L7_List             _threading_local    hmac                sre_constants
L8_Tuple            _tkinter            html                sre_parse
L9_Set              _tokenize           http                ssl
__future__          _tracemalloc        idlelib             stat
__hello__           _typing             imaplib             statistics
__phello__          _uuid               imghdr              string
_abc                _warnings           importlib           stringprep
_aix_support        _weakref            inspect             struct
_ast                _weakrefset         io                  subprocess
_asyncio            _winapi             ipaddress           sunau
_bisect             _wmi                itertools           symtable
_blake2             _xxinterpchannels   json                sys
_bz2                _xxsubinterpreters  keyword             sysconfig
_codecs             _zoneinfo           lib2to3             tabnanny
_codecs_cn          abc                 linecache           tarfile
_codecs_hk          aifc                locale              telnetlib
_codecs_iso2022     antigravity         logging             tempfile
_codecs_jp          argparse            lzma                test
_codecs_kr          array               mailbox             textwrap
_codecs_tw          ast                 mailcap             this
_collections        asyncio             marshal             threading
_collections_abc    atexit              math                time
_compat_pickle      audioop             mes                 timeit
_compression        base64              mimetypes           tkinter
_contextvars        bdb                 mmap                token
_csv                binascii            modulefinder        tokenize
_ctypes             bisect              msilib              tomllib
_ctypes_test        builtins            msvcrt              trace
_datetime           bz2                 multiprocessing     traceback
_decimal            cProfile            netrc               tracemalloc
_elementtree        calendar            nntplib             tty
_functools          cgi                 nt                  turtle
_hashlib            cgitb               ntpath              turtledemo
_heapq              chunk               nturl2path          types
_imp                cmath               numbers             typing
_io                 cmd                 opcode              unicodedata
_json               code                operator            unittest
_locale             codecs              optparse            urllib
_lsprof             codeop              os                  uu
_lzma               collections         pathlib             uuid
_markupbase         colorsys            pdb                 venv
_md5                compileall          pickle              warnings
_msi                concurrent          pickletools         wave
_multibytecodec     configparser        pip                 weakref
_multiprocessing    contextlib          pipes               webbrowser
_opcode             contextvars         pkgutil             winreg
_operator           copy                platform            winsound
_osx_support        copyreg             plistlib            wsgiref
_overlapped         crypt               poplib              xdrlib
_pickle             csv                 posixpath           xml
_py_abc             ctypes              pprint              xmlrpc
_pydatetime         curses              profile             xxsubtype
_pydecimal          dataclasses         pstats              zipapp
_pyio               datetime            pty                 zipfile
_pylong             dbm                 py_compile          zipimport
_queue              decimal             pyclbr              zlib
_random             difflib             pydoc               zoneinfo
_sha1               dis                 pydoc_data
_sha2               doctest             pyexpat
_sha3               email               queue

'''

# Read all module eplaination on python.org.module. ite
