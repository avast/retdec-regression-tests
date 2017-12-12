target datalayout = "e-p:32:32:32-f80:32:32"

; ------------ Registers ------------
@gpr0 = internal global i32 0
@gpr1 = internal global i32 0
@gpr2 = internal global i32 0
@gpr3 = internal global i32 0
@gpr4 = internal global i32 0
@gpr5 = internal global i32 0
@gpr6 = internal global i32 0
@gpr7 = internal global i32 0
@cf0 = internal global i1 0
@zf0 = internal global i1 0
@sf0 = internal global i1 0
@of0 = internal global i1 0
@pf0 = internal global i1 0
@af0 = internal global i1 0
@tf0 = internal global i1 0
@df0 = internal global i1 0
@fpr0 = internal global x86_fp80 0xK0
@fpr1 = internal global x86_fp80 0xK0
@fpr2 = internal global x86_fp80 0xK0
@fpr3 = internal global x86_fp80 0xK0
@fpr4 = internal global x86_fp80 0xK0
@fpr5 = internal global x86_fp80 0xK0
@fpr6 = internal global x86_fp80 0xK0
@fpr7 = internal global x86_fp80 0xK0

; ------------ Exported functions ------------
; Number of exports: 0

; ------------ Statically linked functions ------------
; __ZNSt13basic_filebufIcSt11char_traitsIcEE4openERKSsSt13_Ios_Openmode @ 0x8049406 to 0x8049416, from: libstdc++-pe-mingw32-4.7.1.sig
; __ZNSt13basic_filebufIcSt11char_traitsIcEE4openERKSsSt13_Ios_Openmode @ 0x804958e to 0x804959e, from: libstdc++-pe-mingw32-4.7.1.sig
; __ZNSt13basic_filebufIcSt11char_traitsIcEE4openERKSsSt13_Ios_Openmode @ 0x8049e06 to 0x8049e16, from: libstdc++-pe-mingw32-4.7.1.sig
; __ZNSt13basic_filebufIcSt11char_traitsIcEE4openERKSsSt13_Ios_Openmode @ 0x804a776 to 0x804a786, from: libstdc++-pe-mingw32-4.7.1.sig
; __ZNSt13basic_filebufIcSt11char_traitsIcEE4openERKSsSt13_Ios_Openmode @ 0x804a9ba to 0x804a9ca, from: libstdc++-pe-mingw32-4.7.1.sig
; __ZNSt13basic_filebufIcSt11char_traitsIcEE4openERKSsSt13_Ios_Openmode @ 0x804ac7e to 0x804ac8e, from: libstdc++-pe-mingw32-4.7.1.sig



;Info: Size of recognized static code: 96B


; ------------ Used signatures ------------
; /home/peter/decompiler/decompiler/decompiler/share/x86/signatures/gcc/libgcc-pe-mingw32-4.7.1.sig
; /home/peter/decompiler/decompiler/decompiler/share/x86/signatures/gcc/libgcc-pe-mingw32-4.7.2.sig
; /home/peter/decompiler/decompiler/decompiler/share/x86/signatures/gcc/libmingw32-pe-mingw32-4.7.2.sig
; /home/peter/decompiler/decompiler/decompiler/share/x86/signatures/gcc/libmingwex-pe-mingw32-4.7.2.sig
; /home/peter/decompiler/decompiler/decompiler/share/x86/signatures/gcc/libstdc++-pe-mingw32-4.7.1.sig

; ------------ Types Declarations ------------
%group = type { i8*, i8*, i32, i8** }
%in_addr = type { i32 }
%sockaddr_in = type { i16, i16, %in_addr, [8 x i8] }
%linux_dirent = type { i32, i32, i16, i8* }
%mq_attr = type { i32, i32, i32, i32 }
%sigevent = type { i32, i32, i32, void(i32)*, i32* }
%netent = type { i8*, i8**, i32, i32 }
%passwd = type { i8*, i8*, i32, i32, i32, i8*, i8*, i8*, i8*, i32 }
%sockaddr = type { i16, [14 x i8] }
%sched_param = type { i32 }
%posix_spawnattr_t = type { i16, i32, i32, i32, i32, %sched_param }
%struct__IO_marker = type { %struct__IO_marker*, %struct__IO_FILE*, i32 }
%struct__IO_FILE = type { i32, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, %struct__IO_marker*, %struct__IO_FILE*, i32, i32, i32, i16, i8, [1 x i8], i8*, i64, i8*, i8*, i8*, i8*, i32, i32, [40 x i8] }
%__mbstate_t = type { i32, i32 }
%_G_fpos_t = type { i32, %__mbstate_t }
%const__G_fpos_t = type { i32, %__mbstate_t }
%fd_set = type { [32 x i32] }
%timeval = type { i32, i32 }
%const_struct_timespec = type { i32, i32 }
%const___sigset_t = type { [32 x i32] }
%struct_random_data = type { i32*, i32*, i32*, i32, i32, i32, i32* }
%struct_drand48_data = type { [3 x i16], [3 x i16], i16, i16, i64 }
%div_t = type { i32, i32 }
%ldiv_t = type { i32, i32 }
%lldiv_t = type { i64, i64 }
%imaxdiv_t = type { i64, i64 }
%struct___locale_struct = type { [13 x i8*], i16*, i32*, i32*, [13 x i8*] }
%tm = type { i32, i32, i32, i32, i32, i32, i32, i32, i32 }
%stat = type { i32, i32, i32, i32, i32, i32, i32, i32, i32, i32 }
%POINT = type { i32, i32 }
%SIZE = type { i32, i32 }
%LOGFONT = type { i32, i32, i32, i32, i32, i8, i8, i8, i8, i8, i8, i8, i8, i8* }
%FILETIME = type { i32, i32 }
%RECT = type { i32, i32, i32, i32 }
%SMALL_RECT = type { i16, i16, i16, i16 }
%CONTEXT = type { i32, i32, i32, i32, i32, i32, i32, i32, i32, i32, i32, i32 }
%WSADATA = type { i32, i32, i8*, i8*, i16, i16, i8* }
%SOCKADDR = type { i16, [14 x i8] }
%WSAPROTOCOL_INFO = type { i32, i32, i32, i32, i32, i32 }
%LARGE_INTEGER = type { i64 }
%MSG = type { i32*, i32, i32, i32, i32, %POINT }
%WNDCLASSEX = type { i32, i32, i32(i32)*, i32, i32, i32*, i32*, i32*, i32*, i8*, i8*, i32* }
%WNDCLASSEX_W = type { i32, i32, i32(i32)*, i32, i32, i32*, i32*, i32*, i32*, i32*, i32*, i32* }
%GUID = type { i32, i16, i16, [8 x i8] }
%MSGBOXPARAMS = type { i32, i32*, i32*, i8*, i8*, i32, i8*, i32*, i32*, i32 }
%MSGBOXPARAMS_W = type { i32, i32*, i32*, i32*, i32*, i32, i32*, i32*, i32*, i32 }
%CRYPT_BIT_BLOB = type { i32, i8*, i32 }
%CRYPT_OBJID_BLOB = type { i32, i8* }
%CRYPT_ALGORITHM_IDENTIFIER = type { i8*, %CRYPT_OBJID_BLOB }
%CERT_PUBLIC_KEY_INFO = type { %CRYPT_ALGORITHM_IDENTIFIER, %CRYPT_BIT_BLOB }
%CRYPT_DECODE_PARA = type { i32, i32*, i32* }
%SCROLLINFO = type { i32, i32, i32, i32, i32, i32, i32 }
%BLENDFUNCTION = type { i8, i8, i8, i8 }
%PAINTSTRUCT = type { i32*, i1, %RECT, i1, i1, [32 x i8] }
%FLASHWINFO = type { i32, i32*, i32, i32, i32 }
%MONITORINFO = type { i32, %RECT, %RECT, i32 }
%SHFILEINFO = type { i32*, i32, i32, [260 x i8], [80 x i8] }
%SHFILEINFO_W = type { i32*, i32, i32, [260 x i16], [80 x i16] }
%SHELLEXECUTEINFO = type { i32, i32, i32*, i8*, i8*, i8*, i8*, i32, i32*, i32*, i8*, i32*, i32, i32*, i32* }
%SHELLEXECUTEINFO_W = type { i32, i32, i32*, i32*, i32*, i32*, i32*, i32, i32*, i32*, i32*, i32*, i32, i32*, i32* }
%SUBCLASSPROC = type { i32*, i32, i32*, i32*, i32*, i32* }
%SYSTEMTIME = type { i16, i16, i16, i16, i16, i16, i16, i16 }
%CRITICAL_SECTION = type { i32, i32*, i32*, i32* }
%INITCOMMONCONTROLSEX = type { i32*, i32* }
%GdiplusStartupInput = type { i32, i32(i32, i8*)*, i1, i1 }
%GdiplusStartupOutput = type { i32(i32*)*, void(i32)* }
%WIN32_FIND_DATA = type { i32, %FILETIME, %FILETIME, %FILETIME, i32, i32, i32, i32, [260 x i8], [14 x i8] }
%WIN32_FIND_DATA_W = type { i32, %FILETIME, %FILETIME, %FILETIME, i32, i32, i32, i32, [260 x i16], [14 x i16] }
%SECURITY_ATTRIBUTES = type { i32, i32*, i1 }
%CHANGEFILTERSTRUCT = type { i32, i32 }
%ALTTABINFO = type { i32, i32, i32, i32, i32, i32, i32, i32, %POINT }
%GUITHREADINFO = type { i32, i32, i32*, i32*, i32*, i32*, i32*, i32*, %RECT }
%TITLEBARINFO = type { i32, %RECT, [6 x i32] }
%WINDOWINFO = type { i32, %RECT, %RECT, i32, i32, i32, i32, i32, i16, i16 }
%WINDOWPLACEMENT = type { i32, i32, i32, %POINT, %POINT, %RECT }
%UPDATELAYEREDWINDOWINFO = type { i32, i32*, %POINT*, %SIZE*, i32*, %POINT*, i32, %BLENDFUNCTION*, i32, %RECT* }
%XFORM = type { float, float, float, float, float, float }
%CHOOSECOLOR = type { i32, i32*, i32*, i32, i32*, i32, i32*, i32*(i32*, i32, i32*, i32*)*, i8* }
%CHOOSECOLOR_W = type { i32, i32*, i32*, i32, i32*, i32, i32*, i32*(i32*, i32, i32*, i32*)*, i32* }
%CHOOSEFONT = type { i32, i32*, i32*, %LOGFONT*, i32, i32, i32, i32*, i32*(i32*, i32, i32*, i32*)*, i8*, i32*, i8*, i16, i32, i32 }
%CHOOSEFONT_W = type { i32, i32*, i32*, %LOGFONT*, i32, i32, i32, i32*, i32*(i32*, i32, i32*, i32*)*, i32*, i32*, i8*, i16, i32, i32 }
%FINDREPLACE = type { i32, i32*, i32*, i32, i8*, i8*, i16, i16, i32*, i32*(i32*, i32, i32*, i32*)*, i8* }
%FINDREPLACE_W = type { i32, i32*, i32*, i32, i32*, i32*, i16, i16, i32*, i32*(i32*, i32, i32*, i32*)*, i32* }
%OPENFILENAME = type { i32, i32*, i32*, i8*, i8*, i32, i32, i8*, i32, i8*, i32, i8*, i8*, i32, i16, i16, i8*, i32*, i32*(i32*, i32, i32*, i32*)*, i8*, i8*, i32, i32 }
%OPENFILENAME_W = type { i32, i32*, i32*, i32*, i32*, i32, i32, i32*, i32, i32*, i32, i32*, i32*, i32, i16, i16, i32*, i32*, i32*(i32*, i32, i32*, i32*)*, i32*, i8*, i32, i32 }
%PAGESETUPDLG = type { i32, i32*, i32*, i32*, i32, %POINT, %RECT, %RECT, i32*, i32*, i32*(i32*, i32, i32*, i32*)*, i32*(i32*, i32, i32*, i32*)*, i8*, i8* }
%PAGESETUPDLG_W = type { i32, i32*, i32*, i32*, i32, %POINT, %RECT, %RECT, i32*, i32*, i32*(i32*, i32, i32*, i32*)*, i32*(i32*, i32, i32*, i32*)*, i32*, i32* }
%PRINTPAGERANGE = type { i32, i32 }
%PRINTDLGEX = type { i32, i32*, i32*, i32*, i32*, i32, i32, i32, i32, i32, %PRINTPAGERANGE*, i32, i32, i32, i32*, i8*, i32*, i32, i32*, i32, i32 }
%PRINTDLG = type { i32, i32*, i32*, i32*, i32*, i32, i16, i16, i16, i16, i16, i32*, i32*, i32*(i32*, i32, i32*, i32*)*, i32*(i32*, i32, i32*, i32*)*, i8*, i8*, i32*, i32* }
%PRINTDLG_W = type { i32, i32*, i32*, i32*, i32*, i32, i16, i16, i16, i16, i16, i32*, i32*, i32*(i32*, i32, i32*, i32*)*, i32*(i32*, i32, i32*, i32*)*, i32*, i32*, i32*, i32* }
%OVERLAPPED = type { i32*, i32*, i8*, i32* }
%DEBUG_EVENT = type { i32, i32, i32, i32* }
%CALDATETIME = type { i32, i32, i32, i32, i32, i32, i32, i32, i32, i32 }
%ACCEL = type { i8, i16, i16 }
%ACCEL_W = type { i16, i16, i16 }
%ICONINFO = type { i1, i32, i32, i32*, i32* }
%ICONINFOEX = type { i32, i1, i32, i32, i32*, i32*, i16, [260 x i8], [260 x i8] }
%ICONINFOEX_W = type { i32, i1, i32, i32, i32*, i32*, i16, [260 x i16], [260 x i16] }
%SID_IDENTIFIER_AUTHORITY = type { [6 x i8] }
%SID = type { i8, i8, %SID_IDENTIFIER_AUTHORITY, [1 x i32] }
%BITMAP = type { i32, i32, i32, i32, i16, i16, i8* }
%LOGBRUSH = type { i32, i32, i32* }
%COORD = type { i16, i16 }
%CONSOLE_CURSOR_INFO = type { i32, i1 }
%CONSOLE_HISTORY_INFO = type { i32, i32, i32, i32 }
%INPUT_RECORD = type { i16, i32 }
%CHAR_INFO = type { i8, i16 }
%CHAR_INFO_W = type { i16, i16 }
%CONSOLE_SCREEN_BUFFER_INFOEX = type { i32, %COORD, %COORD, i16, %SMALL_RECT, %COORD, i16, i1, [16 x i32] }
%ACL = type { i8, i8, i16, i16, i16 }
%SECURITY_DESCRIPTOR = type { i8, i8, i16, %SID*, %SID*, %ACL, %ACL }
%DLGTEMPLATE = type { i32, i32, i16, i16, i16, i16, i16 }
%BITMAPINFOHEADER = type { i32, i32, i32, i16, i16, i32, i32, i32, i32, i32, i32 }
%RGBQUAD = type { i8, i8, i8, i8 }
%BITMAPINFO = type { %BITMAPINFOHEADER, %RGBQUAD }
%PALETTEENTRY = type { i8, i8, i8, i8 }
%LOGPALETTE = type { i32, i32, %PALETTEENTRY }
%GENERIC_MAPPING = type { i32, i32, i32, i32 }
%STARTUPINFO = type { i32, i8*, i8*, i8*, i32, i32, i32, i32, i32, i32, i32, i32, i16, i16, i8*, i32*, i32*, i32* }
%STARTUPINFO_W = type { i32, i32*, i32*, i32*, i32, i32, i32, i32, i32, i32, i32, i32, i16, i16, i32*, i32*, i32*, i32* }
%PROCESS_INFORMATION = type { i32*, i32*, i32, i32 }


; ------------ Functions Declarations ------------
declare i32 @unknown_80485fc () nounwind  ;	 adddress: 80485fc
declare i32 @unknown_804865c () nounwind  ;	 adddress: 804865c
declare i32 @unknown_804882c () nounwind  ;	 adddress: 804882c
declare void @__ZNSt13basic_filebufIcSt11char_traitsIcEE4openERKSsSt13_Ios_Openmode () nounwind  ;	 adddress: 8049406
declare i32 @unknown_80559c4 () nounwind  ;	 adddress: 80559c4


; ------------ Global Variables and Constants Declarations ------------
@glob_var_8057512 = constant [20 x i8] c"/var/run/.lightscan\00"				 ; address: 0x8057512
@glob_var_8057526 = constant [19 x i8] c"/var/run/lightscan\00"				 ; address: 0x8057526
@glob_var_8057539 = constant [16 x i8] c"/var/run/mipsel\00"				 ; address: 0x8057539
@glob_var_8057549 = constant [14 x i8] c"/var/run/mips\00"				 ; address: 0x8057549
@glob_var_8057557 = constant [12 x i8] c"/var/run/sh\00"				 ; address: 0x8057557
@glob_var_8057563 = constant [13 x i8] c"/var/run/arm\00"				 ; address: 0x8057563
@glob_var_8057570 = constant [13 x i8] c"/var/run/ppc\00"				 ; address: 0x8057570
@glob_var_805757d = constant [11 x i8] c"/var/run/m\00"				 ; address: 0x805757d
@glob_var_8057588 = constant [12 x i8] c"/var/run/mi\00"				 ; address: 0x8057588
@glob_var_8057594 = constant [11 x i8] c"/var/run/s\00"				 ; address: 0x8057594
@glob_var_805759f = constant [11 x i8] c"/var/run/a\00"				 ; address: 0x805759f
@glob_var_80575aa = constant [11 x i8] c"/var/run/p\00"				 ; address: 0x80575aa
@glob_var_80575b5 = constant [13 x i8] c"/var/run/msx\00"				 ; address: 0x80575b5
@glob_var_80575c2 = constant [12 x i8] c"/var/run/mx\00"				 ; address: 0x80575c2
@glob_var_80575ce = constant [12 x i8] c"/var/run/sx\00"				 ; address: 0x80575ce
@glob_var_80575da = constant [12 x i8] c"/var/run/ax\00"				 ; address: 0x80575da
@glob_var_80575e6 = constant [12 x i8] c"/var/run/px\00"				 ; address: 0x80575e6
@glob_var_80575f2 = constant [12 x i8] c"/var/run/32\00"				 ; address: 0x80575f2
@glob_var_80575fe = constant [13 x i8] c"/var/run/sel\00"				 ; address: 0x80575fe
@glob_var_805760b = constant [13 x i8] c"/var/run/pid\00"				 ; address: 0x805760b
@glob_var_8057618 = constant [13 x i8] c"/var/run/gcc\00"				 ; address: 0x8057618
@glob_var_8057625 = constant [13 x i8] c"/var/run/dev\00"				 ; address: 0x8057625
@glob_var_8057632 = constant [13 x i8] c"/var/run/psx\00"				 ; address: 0x8057632
@glob_var_805763f = constant [13 x i8] c"/var/run/mpl\00"				 ; address: 0x805763f
@glob_var_805764c = constant [13 x i8] c"/var/run/mps\00"				 ; address: 0x805764c
@glob_var_8057659 = constant [13 x i8] c"/var/run/sph\00"				 ; address: 0x8057659
@glob_var_8057666 = constant [14 x i8] c"/var/run/arml\00"				 ; address: 0x8057666
@glob_var_8057674 = constant [16 x i8] c"/var/run/mips.l\00"				 ; address: 0x8057674
@glob_var_8057684 = constant [17 x i8] c"/var/run/mipsell\00"				 ; address: 0x8057684
@glob_var_8057695 = constant [14 x i8] c"/var/run/ppcl\00"				 ; address: 0x8057695
@glob_var_80576a3 = constant [13 x i8] c"/var/run/shl\00"				 ; address: 0x80576a3
@glob_var_80576b0 = constant [8 x i8] c"/bin/pp\00"				 ; address: 0x80576b0
@glob_var_80576b8 = constant [8 x i8] c"/bin/mi\00"				 ; address: 0x80576b8
@glob_var_80576c0 = constant [9 x i8] c"/bin/mii\00"				 ; address: 0x80576c0
@glob_var_80576c9 = constant [27 x i8] c"/var/tmp/dreams.install.sh\00"				 ; address: 0x80576c9
@glob_var_80576e4 = constant [17 x i8] c"/var/tmp/ep2.ppc\00"				 ; address: 0x80576e4
@glob_var_80576f5 = constant [14 x i8] c"/usr/bin/wget\00"				 ; address: 0x80576f5
@glob_var_80576f9 = constant [10 x i8] c"/bin/wget\00"				 ; address: 0x80576f9
@glob_var_8057703 = constant [15 x i8] c"/usr/bin/-wget\00"				 ; address: 0x8057703


; ------------ Intrinsic Functions Declarations ------------
declare i8 @llvm.ctpop.i8(i8)


; ------------ Undefined Functions Declarations ------------
declare i32 @__decompiler_undefined_function_0() nounwind
declare i32* @__decompiler_undefined_function_1() nounwind


; ------------ Address of main(): 0xffffffffffffffff

declare void @__decompiler_prevent_var_from_removal_0(i32*)

;-------------------------------------
;	Function: function_8048960		8048960 - 8048b9d
;-------------------------------------
define void @function_8048960() nounwind {

	%local_ret_0 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_1 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_10 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_11 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_12 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_13 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_14 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_15 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_16 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_17 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_18 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_19 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_2 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_20 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_21 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_22 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_23 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_24 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_25 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_26 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_27 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_28 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_29 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_3 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_30 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_31 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_32 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_33 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_34 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_35 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_36 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_37 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_38 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_39 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_4 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_40 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_41 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_42 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_43 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_44 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_45 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_46 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_5 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_6 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_7 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_8 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1
	%local_ret_9 = alloca i32		; original storage :  @gpr0, debug: 0, LTI: 1

	%stack_var_-36 = alloca i32		; offset: -36
	%stack_var_-36_x = call i32 @__decompiler_undefined_function_0()
	store i32 %stack_var_-36_x, i32* %stack_var_-36
	%stack_var_-32 = alloca i32*		; offset: -32
	%stack_var_-32_x = call i32* @__decompiler_undefined_function_1()
	store i32* %stack_var_-32_x, i32** %stack_var_-32
	%stack_var_-28 = alloca i32		; offset: -28

; 	call void @__decompiler_prevent_var_from_removal_0(i32* %stack_var_-28)

	%stack_var_-28_x = call i32 @__decompiler_undefined_function_0()
	store i32 %stack_var_-28_x, i32* %stack_var_-28
	%stack_var_-24 = alloca i32		; offset: -24
	%stack_var_-24_x = call i32 @__decompiler_undefined_function_0()
	store i32 %stack_var_-24_x, i32* %stack_var_-24
	%stack_var_-20 = alloca i32		; offset: -20
	%stack_var_-20_x = call i32 @__decompiler_undefined_function_0()
	store i32 %stack_var_-20_x, i32* %stack_var_-20
	%stack_var_-16 = alloca i32*		; offset: -16
	%stack_var_-16_x = call i32* @__decompiler_undefined_function_1()
	store i32* %stack_var_-16_x, i32** %stack_var_-16
	%stack_var_-12 = alloca i32		; offset: -12
	%stack_var_-12_x = call i32 @__decompiler_undefined_function_0()
	store i32 %stack_var_-12_x, i32* %stack_var_-12
	%stack_var_0 = alloca i32		; offset: 0
	%stack_var_0_x = call i32 @__decompiler_undefined_function_0()
	store i32 %stack_var_0_x, i32* %stack_var_0

	br label %dec_label_pc_8048960	; This is only for LLVM correctness, it needs branch before label
dec_label_pc_8048960:	;100000111110110000001100
	;SUB {4}, {12}  decode__instr_grpxx_5_r32_simm8__instr_sub_5_rmxx_simm8__MODRMxx_mod11_5_reg32__gpr32__simm8__
	%u0_8048960 = add i8 12, 0 ; used signed value. Unsigned value: 12
	%u1_8048960 = sext i8 %u0_8048960 to i32
	%u2_8048960 = load i32, i32*  @gpr4
	%_b_subinst_0_8048960 = add i32 15, 0
	%u0_subinst_0_8048960 = and i32 %u2_8048960, %_b_subinst_0_8048960

	%_d_subinst_0_8048960 = add i32 15, 0
	%u1_subinst_0_8048960 = and i32 %u1_8048960, %_d_subinst_0_8048960

	%u2_subinst_0_8048960 = sub i32 %u0_subinst_0_8048960, %u1_subinst_0_8048960

	%_g_subinst_0_8048960 = add i32 15, 0
	%u3_8048960 = icmp ugt i32 %u2_subinst_0_8048960, %_g_subinst_0_8048960
	%_f_8048960 = add i32 0, 0
	store i1 %u3_8048960, i1*  @af0	; store to i1 register, should we ignore it? But than it causes problems, see #153
	%u4_8048960 = icmp ult i32 %u2_8048960, %u1_8048960
	%_h_8048960 = add i32 0, 0
	store i1 %u4_8048960, i1*  @cf0	; store to i1 register, should we ignore it? But than it causes problems, see #153
	; overflow_sub is a little bit more complicated, so it contains more code
	%sub_ab_0_8048960 = sub i32 %u2_8048960, %u1_8048960
	%xor_ab_0_8048960 = xor i32 %u2_8048960, %u1_8048960
	%xor_aab_0_8048960 = xor i32 %u2_8048960, %sub_ab_0_8048960
	%and_aab_0_8048960 = and i32 %xor_ab_0_8048960, %xor_aab_0_8048960
	%u5_8048960 = icmp slt i32 %and_aab_0_8048960, 0

	%_j_8048960 = add i32 0, 0
	store i1 %u5_8048960, i1*  @of0	; store to i1 register, should we ignore it? But than it causes problems, see #153
	%u6_8048960 = sub i32 %u2_8048960, %u1_8048960

	%_b_subinst_1_8048960 = add i32 0, 0
	%u0_subinst_1_8048960 = icmp eq i32 %u6_8048960, %_b_subinst_1_8048960
	%_d_subinst_1_8048960 = add i32 0, 0
	store i1 %u0_subinst_1_8048960, i1*  @zf0	; store to i1 register, should we ignore it? But than it causes problems, see #153
	%_e_subinst_1_8048960 = add i32 0, 0
	%u1_subinst_1_8048960 = icmp slt i32 %u6_8048960, %_e_subinst_1_8048960
	%_g_subinst_1_8048960 = add i32 0, 0
	store i1 %u1_subinst_1_8048960, i1*  @sf0	; store to i1 register, should we ignore it? But than it causes problems, see #153
	%u2_subinst_1_8048960 = trunc i32 %u6_8048960 to i8
	%parity_odd_bit_cnt_1_8048960 = call i8 @llvm.ctpop.i8( i8 %u2_subinst_1_8048960 ) nounwind
	%parity_odd_mod_1_8048960 = urem i8 %parity_odd_bit_cnt_1_8048960, 2
	%u3_subinst_1_8048960 = icmp eq i8 1, %parity_odd_mod_1_8048960

	%_j_subinst_1_8048960 = add i32 0, 0
	store i1 %u3_subinst_1_8048960, i1*  @pf0	; store to i1 register, should we ignore it? But than it causes problems, see #153
	; store of stack pointer to offset -12 into register  @gpr4


	;8048963	1011101000000001000000000000000000000000	ba 01 00 00 00
	;MOV {2}, {1}  decode__instr_grpxx_op0_r32_uimm32__instr_mov_op0_rxx_uimmxx__gpr32__uimm32__
	%u0_8048963 = add i32 1, 0 ; used signed value. Unsigned value: 1
	store i32 %u0_8048963, i32*  @gpr2

	;8048968	1011100011101001011100110000010100001000	b8 e9 73 05 08
	;MOV {0}, {134575081}  decode__instr_grpxx_op0_r32_uimm32__instr_mov_op0_rxx_uimmxx__gpr32__uimm32__
	%u0_8048968 = add i32 134575081, 0 ; used signed value. Unsigned value: 134575081
	store i32 %u0_8048968, i32*  @gpr0

	;804896d	1110100010001010111111001111111111111111	e8 8a fc ff ff
	;CALL {-886}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_804896d = add i32 -886, 0 ; used signed value. Unsigned value: 4294966410
	%u1_804896d = add i32 134515053, 0	; Assign current PC
	%_d_804896d = add i32 5, 0
	%u2_804896d = add i32 %u1_804896d, %_d_804896d

	%_f_804896d = add i32 4, 0
	%u3_804896d = load i32, i32* @gpr4
	%u4_804896d = add i32 %u2_804896d, %u0_804896d

	%_i_804896d = add i32 -4, 0
	%u5_804896d = add i32 %u3_804896d, %_i_804896d

	%conv_804896d_1 = inttoptr i32 %u2_804896d to i32*
	store i32* %conv_804896d_1, i32** %stack_var_-16
	%_k_804896d = add i32 4, 0
	; store of stack pointer to offset -16 into register  @gpr4

	%local_ret_0_804896d = call i32  @unknown_80485fc() nounwind
	store i32 %local_ret_0_804896d, i32* %local_ret_0


	;8048972	1011101000000001000000000000000000000000	ba 01 00 00 00
	;MOV {2}, {1}  decode__instr_grpxx_op0_r32_uimm32__instr_mov_op0_rxx_uimmxx__gpr32__uimm32__
	%u0_8048972 = add i32 1, 0 ; used signed value. Unsigned value: 1
	store i32 %u0_8048972, i32*  @gpr2

	;8048977	1011100000101111011101000000010100001000	b8 2f 74 05 08
	;MOV {0}, {134575151}  decode__instr_grpxx_op0_r32_uimm32__instr_mov_op0_rxx_uimmxx__gpr32__uimm32__
	%u0_8048977 = add i32 134575151, 0 ; used signed value. Unsigned value: 134575151
	store i32 %u0_8048977, i32*  @gpr0

	;804897c	1110100001111011111111001111111111111111	e8 7b fc ff ff
	;CALL {-901}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_804897c = add i32 -901, 0 ; used signed value. Unsigned value: 4294966395
	%u1_804897c = add i32 134515068, 0	; Assign current PC
	%_d_804897c = add i32 5, 0
	%u2_804897c = add i32 %u1_804897c, %_d_804897c

	%_f_804897c = add i32 4, 0
	%u3_804897c = load i32, i32* @gpr4
	%u4_804897c = add i32 %u2_804897c, %u0_804897c

	%_i_804897c = add i32 -4, 0
	%u5_804897c = add i32 %u3_804897c, %_i_804897c

	%conv_804897c_1 = inttoptr i32 %u2_804897c to i32*
	store i32* %conv_804897c_1, i32** %stack_var_-16
	%_k_804897c = add i32 4, 0
	; store of stack pointer to offset -16 into register  @gpr4

	%local_ret_1_804897c = call i32  @unknown_80485fc() nounwind
	store i32 %local_ret_1_804897c, i32* %local_ret_1


	;8048981	1011101000000001000000000000000000000000	ba 01 00 00 00
	;MOV {2}, {1}  decode__instr_grpxx_op0_r32_uimm32__instr_mov_op0_rxx_uimmxx__gpr32__uimm32__
	%u0_8048981 = add i32 1, 0 ; used signed value. Unsigned value: 1
	store i32 %u0_8048981, i32*  @gpr2

	;8048986	1011100001111010011101000000010100001000	b8 7a 74 05 08
	;MOV {0}, {134575226}  decode__instr_grpxx_op0_r32_uimm32__instr_mov_op0_rxx_uimmxx__gpr32__uimm32__
	%u0_8048986 = add i32 134575226, 0 ; used signed value. Unsigned value: 134575226
	store i32 %u0_8048986, i32*  @gpr0

	;804898b	1110100001101100111111001111111111111111	e8 6c fc ff ff
	;CALL {-916}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_804898b = add i32 -916, 0 ; used signed value. Unsigned value: 4294966380
	%u1_804898b = add i32 134515083, 0	; Assign current PC
	%_d_804898b = add i32 5, 0
	%u2_804898b = add i32 %u1_804898b, %_d_804898b

	%_f_804898b = add i32 4, 0
	%u3_804898b = load i32, i32* @gpr4
	%u4_804898b = add i32 %u2_804898b, %u0_804898b

	%_i_804898b = add i32 -4, 0
	%u5_804898b = add i32 %u3_804898b, %_i_804898b

	%conv_804898b_1 = inttoptr i32 %u2_804898b to i32*
	store i32* %conv_804898b_1, i32** %stack_var_-16
	%_k_804898b = add i32 4, 0
	; store of stack pointer to offset -16 into register  @gpr4

	%local_ret_2_804898b = call i32  @unknown_80485fc() nounwind
	store i32 %local_ret_2_804898b, i32* %local_ret_2


	;8048990	0011000111010010	31 d2
	;XOR {2}, {2}  decode__instr_grpxx_R32_r32__instr_xor_rmxx_rxx__MODRMxx_mod11_reg32_REG32__gpr32__gpr32__
	%u0_8048990 = load i32, i32*  @gpr2
	%u1_8048990 = load i32, i32*  @gpr2
	%_d_8048990 = add i32 0, 0
	%_e_8048990 = add i1 0, 0
	store i1 %_e_8048990, i1*  @cf0	; store to i1 register, should we ignore it? But than it causes problems, see #153
	%_f_8048990 = add i32 0, 0
	%_g_8048990 = add i1 0, 0
	store i1 %_g_8048990, i1*  @of0	; store to i1 register, should we ignore it? But than it causes problems, see #153
	%_h_8048990 = add i32 0, 0
	%_i_8048990 = add i1 0, 0
	store i1 %_i_8048990, i1*  @af0	; store to i1 register, should we ignore it? But than it causes problems, see #153
	%u2_8048990 = xor i32 %u1_8048990, %u0_8048990

	%_b_subinst_2_8048990 = add i32 0, 0
	%u0_subinst_2_8048990 = icmp eq i32 %u2_8048990, %_b_subinst_2_8048990
	%_d_subinst_2_8048990 = add i32 0, 0
	store i1 %u0_subinst_2_8048990, i1*  @zf0	; store to i1 register, should we ignore it? But than it causes problems, see #153
	%_e_subinst_2_8048990 = add i32 0, 0
	%u1_subinst_2_8048990 = icmp slt i32 %u2_8048990, %_e_subinst_2_8048990
	%_g_subinst_2_8048990 = add i32 0, 0
	store i1 %u1_subinst_2_8048990, i1*  @sf0	; store to i1 register, should we ignore it? But than it causes problems, see #153
	%u2_subinst_2_8048990 = trunc i32 %u2_8048990 to i8
	%parity_odd_bit_cnt_0_8048990 = call i8 @llvm.ctpop.i8( i8 %u2_subinst_2_8048990 ) nounwind
	%parity_odd_mod_0_8048990 = urem i8 %parity_odd_bit_cnt_0_8048990, 2
	%u3_subinst_2_8048990 = icmp eq i8 1, %parity_odd_mod_0_8048990

	%_j_subinst_2_8048990 = add i32 0, 0
	store i1 %u3_subinst_2_8048990, i1*  @pf0	; store to i1 register, should we ignore it? But than it causes problems, see #153
	store i32 %u2_8048990, i32*  @gpr2

	;8048992	1011100010100110011101000000010100001000	b8 a6 74 05 08
	;MOV {0}, {134575270}  decode__instr_grpxx_op0_r32_uimm32__instr_mov_op0_rxx_uimmxx__gpr32__uimm32__
	%u0_8048992 = add i32 134575270, 0 ; used signed value. Unsigned value: 134575270
	store i32 %u0_8048992, i32*  @gpr0

	;8048997	1110100001100000111111001111111111111111	e8 60 fc ff ff
	;CALL {-928}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_8048997 = add i32 -928, 0 ; used signed value. Unsigned value: 4294966368
	%u1_8048997 = add i32 134515095, 0	; Assign current PC
	%_d_8048997 = add i32 5, 0
	%u2_8048997 = add i32 %u1_8048997, %_d_8048997

	%_f_8048997 = add i32 4, 0
	%u3_8048997 = load i32, i32* @gpr4
	%u4_8048997 = add i32 %u2_8048997, %u0_8048997

	%_i_8048997 = add i32 -4, 0
	%u5_8048997 = add i32 %u3_8048997, %_i_8048997

	%conv_8048997_1 = inttoptr i32 %u2_8048997 to i32*
	store i32* %conv_8048997_1, i32** %stack_var_-16
	%_k_8048997 = add i32 4, 0
	; store of stack pointer to offset -16 into register  @gpr4

	%local_ret_3_8048997 = call i32  @unknown_80485fc() nounwind
	store i32 %local_ret_3_8048997, i32* %local_ret_3


	;804899c	1011100011010010011101000000010100001000	b8 d2 74 05 08
	;MOV {0}, {134575314}  decode__instr_grpxx_op0_r32_uimm32__instr_mov_op0_rxx_uimmxx__gpr32__uimm32__
	%u0_804899c = add i32 134575314, 0 ; used signed value. Unsigned value: 134575314
	store i32 %u0_804899c, i32*  @gpr0

	;80489a1	1110100010000110111111101111111111111111	e8 86 fe ff ff
	;CALL {-378}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_80489a1 = add i32 -378, 0 ; used signed value. Unsigned value: 4294966918
	%u1_80489a1 = add i32 134515105, 0	; Assign current PC
	%_d_80489a1 = add i32 5, 0
	%u2_80489a1 = add i32 %u1_80489a1, %_d_80489a1

	%_f_80489a1 = add i32 4, 0
	%u3_80489a1 = load i32, i32* @gpr4
	%u4_80489a1 = add i32 %u2_80489a1, %u0_80489a1

	%_i_80489a1 = add i32 -4, 0
	%u5_80489a1 = add i32 %u3_80489a1, %_i_80489a1

	%conv_80489a1_1 = inttoptr i32 %u2_80489a1 to i32*
	store i32* %conv_80489a1_1, i32** %stack_var_-16
	%_k_80489a1 = add i32 4, 0
	; store of stack pointer to offset -16 into register  @gpr4

	%local_ret_4_80489a1 = call i32  @unknown_804882c() nounwind
	store i32 %local_ret_4_80489a1, i32* %local_ret_4


	;80489a6	1011100011011010011101000000010100001000	b8 da 74 05 08
	;MOV {0}, {134575322}  decode__instr_grpxx_op0_r32_uimm32__instr_mov_op0_rxx_uimmxx__gpr32__uimm32__
	%u0_80489a6 = add i32 134575322, 0 ; used signed value. Unsigned value: 134575322
	store i32 %u0_80489a6, i32*  @gpr0

	;80489ab	1110100010101100111111001111111111111111	e8 ac fc ff ff
	;CALL {-852}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_80489ab = add i32 -852, 0 ; used signed value. Unsigned value: 4294966444
	%u1_80489ab = add i32 134515115, 0	; Assign current PC
	%_d_80489ab = add i32 5, 0
	%u2_80489ab = add i32 %u1_80489ab, %_d_80489ab

	%_f_80489ab = add i32 4, 0
	%u3_80489ab = load i32, i32* @gpr4
	%u4_80489ab = add i32 %u2_80489ab, %u0_80489ab

	%_i_80489ab = add i32 -4, 0
	%u5_80489ab = add i32 %u3_80489ab, %_i_80489ab

	%conv_80489ab_1 = inttoptr i32 %u2_80489ab to i32*
	store i32* %conv_80489ab_1, i32** %stack_var_-16
	%_k_80489ab = add i32 4, 0
	; store of stack pointer to offset -16 into register  @gpr4

	%local_ret_5_80489ab = call i32  @unknown_804865c() nounwind
	store i32 %local_ret_5_80489ab, i32* %local_ret_5


	;80489b0	1011100011101101011101000000010100001000	b8 ed 74 05 08
	;MOV {0}, {134575341}  decode__instr_grpxx_op0_r32_uimm32__instr_mov_op0_rxx_uimmxx__gpr32__uimm32__
	%u0_80489b0 = add i32 134575341, 0 ; used signed value. Unsigned value: 134575341
	store i32 %u0_80489b0, i32*  @gpr0

	;80489b5	1110100010100010111111001111111111111111	e8 a2 fc ff ff
	;CALL {-862}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_80489b5 = add i32 -862, 0 ; used signed value. Unsigned value: 4294966434
	%u1_80489b5 = add i32 134515125, 0	; Assign current PC
	%_d_80489b5 = add i32 5, 0
	%u2_80489b5 = add i32 %u1_80489b5, %_d_80489b5

	%_f_80489b5 = add i32 4, 0
	%u3_80489b5 = load i32, i32* @gpr4
	%u4_80489b5 = add i32 %u2_80489b5, %u0_80489b5

	%_i_80489b5 = add i32 -4, 0
	%u5_80489b5 = add i32 %u3_80489b5, %_i_80489b5

	%conv_80489b5_1 = inttoptr i32 %u2_80489b5 to i32*
	store i32* %conv_80489b5_1, i32** %stack_var_-16
	%_k_80489b5 = add i32 4, 0
	; store of stack pointer to offset -16 into register  @gpr4

	%local_ret_6_80489b5 = call i32  @unknown_804865c() nounwind
	store i32 %local_ret_6_80489b5, i32* %local_ret_6


	;80489ba	1011100000000000011101010000010100001000	b8 00 75 05 08
	;MOV {0}, {134575360}  decode__instr_grpxx_op0_r32_uimm32__instr_mov_op0_rxx_uimmxx__gpr32__uimm32__
	%u0_80489ba = add i32 134575360, 0 ; used signed value. Unsigned value: 134575360
	store i32 %u0_80489ba, i32*  @gpr0

	;80489bf	1110100010011000111111001111111111111111	e8 98 fc ff ff
	;CALL {-872}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_80489bf = add i32 -872, 0 ; used signed value. Unsigned value: 4294966424
	%u1_80489bf = add i32 134515135, 0	; Assign current PC
	%_d_80489bf = add i32 5, 0
	%u2_80489bf = add i32 %u1_80489bf, %_d_80489bf

	%_f_80489bf = add i32 4, 0
	%u3_80489bf = load i32, i32* @gpr4
	%u4_80489bf = add i32 %u2_80489bf, %u0_80489bf

	%_i_80489bf = add i32 -4, 0
	%u5_80489bf = add i32 %u3_80489bf, %_i_80489bf

	%conv_80489bf_1 = inttoptr i32 %u2_80489bf to i32*
	store i32* %conv_80489bf_1, i32** %stack_var_-16
	%_k_80489bf = add i32 4, 0
	; store of stack pointer to offset -16 into register  @gpr4

	%local_ret_7_80489bf = call i32  @unknown_804865c() nounwind
	store i32 %local_ret_7_80489bf, i32* %local_ret_7


	;80489c4	100000111110110000001100	83 ec 0c
	;SUB {4}, {12}  decode__instr_grpxx_5_r32_simm8__instr_sub_5_rmxx_simm8__MODRMxx_mod11_5_reg32__gpr32__simm8__
	%u0_80489c4 = add i8 12, 0 ; used signed value. Unsigned value: 12
	%u1_80489c4 = sext i8 %u0_80489c4 to i32
	%u2_80489c4 = load i32, i32*  @gpr4
	%_b_subinst_3_80489c4 = add i32 15, 0
	%u0_subinst_3_80489c4 = and i32 %u2_80489c4, %_b_subinst_3_80489c4

	%_d_subinst_3_80489c4 = add i32 15, 0
	%u1_subinst_3_80489c4 = and i32 %u1_80489c4, %_d_subinst_3_80489c4

	%u2_subinst_3_80489c4 = sub i32 %u0_subinst_3_80489c4, %u1_subinst_3_80489c4

	%_g_subinst_3_80489c4 = add i32 15, 0
	%u3_80489c4 = icmp ugt i32 %u2_subinst_3_80489c4, %_g_subinst_3_80489c4
	%_f_80489c4 = add i32 0, 0
	store i1 %u3_80489c4, i1*  @af0	; store to i1 register, should we ignore it? But than it causes problems, see #153
	%u4_80489c4 = icmp ult i32 %u2_80489c4, %u1_80489c4
	%_h_80489c4 = add i32 0, 0
	store i1 %u4_80489c4, i1*  @cf0	; store to i1 register, should we ignore it? But than it causes problems, see #153
	; overflow_sub is a little bit more complicated, so it contains more code
	%sub_ab_0_80489c4 = sub i32 %u2_80489c4, %u1_80489c4
	%xor_ab_0_80489c4 = xor i32 %u2_80489c4, %u1_80489c4
	%xor_aab_0_80489c4 = xor i32 %u2_80489c4, %sub_ab_0_80489c4
	%and_aab_0_80489c4 = and i32 %xor_ab_0_80489c4, %xor_aab_0_80489c4
	%u5_80489c4 = icmp slt i32 %and_aab_0_80489c4, 0

	%_j_80489c4 = add i32 0, 0
	store i1 %u5_80489c4, i1*  @of0	; store to i1 register, should we ignore it? But than it causes problems, see #153
	%u6_80489c4 = sub i32 %u2_80489c4, %u1_80489c4

	%_b_subinst_4_80489c4 = add i32 0, 0
	%u0_subinst_4_80489c4 = icmp eq i32 %u6_80489c4, %_b_subinst_4_80489c4
	%_d_subinst_4_80489c4 = add i32 0, 0
	store i1 %u0_subinst_4_80489c4, i1*  @zf0	; store to i1 register, should we ignore it? But than it causes problems, see #153
	%_e_subinst_4_80489c4 = add i32 0, 0
	%u1_subinst_4_80489c4 = icmp slt i32 %u6_80489c4, %_e_subinst_4_80489c4
	%_g_subinst_4_80489c4 = add i32 0, 0
	store i1 %u1_subinst_4_80489c4, i1*  @sf0	; store to i1 register, should we ignore it? But than it causes problems, see #153
	%u2_subinst_4_80489c4 = trunc i32 %u6_80489c4 to i8
	%parity_odd_bit_cnt_1_80489c4 = call i8 @llvm.ctpop.i8( i8 %u2_subinst_4_80489c4 ) nounwind
	%parity_odd_mod_1_80489c4 = urem i8 %parity_odd_bit_cnt_1_80489c4, 2
	%u3_subinst_4_80489c4 = icmp eq i8 1, %parity_odd_mod_1_80489c4

	%_j_subinst_4_80489c4 = add i32 0, 0
	store i1 %u3_subinst_4_80489c4, i1*  @pf0	; store to i1 register, should we ignore it? But than it causes problems, see #153
	; store of stack pointer to offset -24 into register  @gpr4


	;80489c7	0110100000010010011101010000010100001000	68 12 75 05 08
	;PUSH {134575378}  decode__instr_grpxx_uimm32__instr_push_uimmxx__uimm32__
	%u0_80489c7 = add i32 134575378, 0 ; used signed value. Unsigned value: 134575378
	%_c_80489c7 = add i32 4, 0
	%u1_80489c7 = load i32, i32* @gpr4
	%_e_80489c7 = add i32 -4, 0
	%phitmp_80489c7 = add i32 %u1_80489c7, %_e_80489c7

	%glob_var_8057512_1345151430 = getelementptr inbounds [20 x i8], [20 x i8]* @glob_var_8057512, i64 0, i64 0
	%conv_80489c7_1 = ptrtoint i8* %glob_var_8057512_1345151430 to i32


	store i32 %conv_80489c7_1, i32* %stack_var_-28
; 	store i32 %conv_80489c7_1, i32* %stack_var_-28


	%_g_80489c7 = add i32 4, 0
	; store of stack pointer to offset -28 into register  @gpr4


	;80489cc	1110100011110011110011110000000000000000	e8 f3 cf 00 00
	;CALL {53235}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_80489cc = add i32 53235, 0 ; used signed value. Unsigned value: 53235
	%u1_80489cc = add i32 134515148, 0	; Assign current PC
	%_d_80489cc = add i32 5, 0
	%u2_80489cc = add i32 %u1_80489cc, %_d_80489cc

	%_f_80489cc = add i32 4, 0
	%u3_80489cc = load i32, i32* @gpr4
	%u4_80489cc = add i32 %u2_80489cc, %u0_80489cc

	%_i_80489cc = add i32 -4, 0
	%u5_80489cc = add i32 %u3_80489cc, %_i_80489cc

	%conv_80489cc_1 = inttoptr i32 %u2_80489cc to i32*
	store i32* %conv_80489cc_1, i32** %stack_var_-32
	%_k_80489cc = add i32 4, 0
	; store of stack pointer to offset -32 into register  @gpr4

	%local_ret_8_80489cc = call i32  @unknown_80559c4() nounwind
	store i32 %local_ret_8_80489cc, i32* %local_ret_8


	;80489d1	11000111000001000010010000100110011101010000010100001000	c7 04 24 26 75 05 08
	;MOV DWORD [ {4}  ], {134575398}  decode__instr_grp32_0_m32_uimm32__instr_mov_0_rmxx_uimmxx__MODRM32_0_mem32__SIB_mod00_32_0_base32_index32__base32_sib_mod00__SIB_scaled_index32_none__uimm32__
	%u0_80489d1 = load i32, i32*  @gpr4
	%u1_80489d1 = add i32 134575398, 0 ; used signed value. Unsigned value: 134575398
	%glob_var_8057526_1345151530 = getelementptr inbounds [19 x i8], [19 x i8]* @glob_var_8057526, i64 0, i64 0
	%conv_80489d1_1 = ptrtoint i8* %glob_var_8057526_1345151530 to i32
	store i32 %conv_80489d1_1, i32* %stack_var_-28

	;80489d8	1110100011100111110011110000000000000000	e8 e7 cf 00 00
	;CALL {53223}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_80489d8 = add i32 53223, 0 ; used signed value. Unsigned value: 53223
	%u1_80489d8 = add i32 134515160, 0	; Assign current PC
	%_d_80489d8 = add i32 5, 0
	%u2_80489d8 = add i32 %u1_80489d8, %_d_80489d8

	%_f_80489d8 = add i32 4, 0
	%u3_80489d8 = load i32, i32* @gpr4
	%u4_80489d8 = add i32 %u2_80489d8, %u0_80489d8

	%_i_80489d8 = add i32 -4, 0
	%u5_80489d8 = add i32 %u3_80489d8, %_i_80489d8

	%conv_80489d8_1 = inttoptr i32 %u2_80489d8 to i32*
	store i32* %conv_80489d8_1, i32** %stack_var_-32
	%_k_80489d8 = add i32 4, 0
	; store of stack pointer to offset -32 into register  @gpr4

	%local_ret_9_80489d8 = call i32  @unknown_80559c4() nounwind
	store i32 %local_ret_9_80489d8, i32* %local_ret_9


	;80489dd	11000111000001000010010000111001011101010000010100001000	c7 04 24 39 75 05 08
	;MOV DWORD [ {4}  ], {134575417}  decode__instr_grp32_0_m32_uimm32__instr_mov_0_rmxx_uimmxx__MODRM32_0_mem32__SIB_mod00_32_0_base32_index32__base32_sib_mod00__SIB_scaled_index32_none__uimm32__
	%u0_80489dd = load i32, i32*  @gpr4
	%u1_80489dd = add i32 134575417, 0 ; used signed value. Unsigned value: 134575417
	%glob_var_8057539_1345151650 = getelementptr inbounds [16 x i8], [16 x i8]* @glob_var_8057539, i64 0, i64 0
	%conv_80489dd_1 = ptrtoint i8* %glob_var_8057539_1345151650 to i32
	store i32 %conv_80489dd_1, i32* %stack_var_-28

	;80489e4	1110100011011011110011110000000000000000	e8 db cf 00 00
	;CALL {53211}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_80489e4 = add i32 53211, 0 ; used signed value. Unsigned value: 53211
	%u1_80489e4 = add i32 134515172, 0	; Assign current PC
	%_d_80489e4 = add i32 5, 0
	%u2_80489e4 = add i32 %u1_80489e4, %_d_80489e4

	%_f_80489e4 = add i32 4, 0
	%u3_80489e4 = load i32, i32* @gpr4
	%u4_80489e4 = add i32 %u2_80489e4, %u0_80489e4

	%_i_80489e4 = add i32 -4, 0
	%u5_80489e4 = add i32 %u3_80489e4, %_i_80489e4

	%conv_80489e4_1 = inttoptr i32 %u2_80489e4 to i32*
	store i32* %conv_80489e4_1, i32** %stack_var_-32
	%_k_80489e4 = add i32 4, 0
	; store of stack pointer to offset -32 into register  @gpr4

	%local_ret_10_80489e4 = call i32  @unknown_80559c4() nounwind
	store i32 %local_ret_10_80489e4, i32* %local_ret_10


	;80489e9	11000111000001000010010001001001011101010000010100001000	c7 04 24 49 75 05 08
	;MOV DWORD [ {4}  ], {134575433}  decode__instr_grp32_0_m32_uimm32__instr_mov_0_rmxx_uimmxx__MODRM32_0_mem32__SIB_mod00_32_0_base32_index32__base32_sib_mod00__SIB_scaled_index32_none__uimm32__
	%u0_80489e9 = load i32, i32*  @gpr4
	%u1_80489e9 = add i32 134575433, 0 ; used signed value. Unsigned value: 134575433
	%glob_var_8057549_1345151770 = getelementptr inbounds [14 x i8], [14 x i8]* @glob_var_8057549, i64 0, i64 0
	%conv_80489e9_1 = ptrtoint i8* %glob_var_8057549_1345151770 to i32
	store i32 %conv_80489e9_1, i32* %stack_var_-28

	;80489f0	1110100011001111110011110000000000000000	e8 cf cf 00 00
	;CALL {53199}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_80489f0 = add i32 53199, 0 ; used signed value. Unsigned value: 53199
	%u1_80489f0 = add i32 134515184, 0	; Assign current PC
	%_d_80489f0 = add i32 5, 0
	%u2_80489f0 = add i32 %u1_80489f0, %_d_80489f0

	%_f_80489f0 = add i32 4, 0
	%u3_80489f0 = load i32, i32* @gpr4
	%u4_80489f0 = add i32 %u2_80489f0, %u0_80489f0

	%_i_80489f0 = add i32 -4, 0
	%u5_80489f0 = add i32 %u3_80489f0, %_i_80489f0

	%conv_80489f0_1 = inttoptr i32 %u2_80489f0 to i32*
	store i32* %conv_80489f0_1, i32** %stack_var_-32
	%_k_80489f0 = add i32 4, 0
	; store of stack pointer to offset -32 into register  @gpr4

	%local_ret_11_80489f0 = call i32  @unknown_80559c4() nounwind
	store i32 %local_ret_11_80489f0, i32* %local_ret_11


	;80489f5	11000111000001000010010001010111011101010000010100001000	c7 04 24 57 75 05 08
	;MOV DWORD [ {4}  ], {134575447}  decode__instr_grp32_0_m32_uimm32__instr_mov_0_rmxx_uimmxx__MODRM32_0_mem32__SIB_mod00_32_0_base32_index32__base32_sib_mod00__SIB_scaled_index32_none__uimm32__
	%u0_80489f5 = load i32, i32*  @gpr4
	%u1_80489f5 = add i32 134575447, 0 ; used signed value. Unsigned value: 134575447
	%glob_var_8057557_1345151890 = getelementptr inbounds [12 x i8], [12 x i8]* @glob_var_8057557, i64 0, i64 0
	%conv_80489f5_1 = ptrtoint i8* %glob_var_8057557_1345151890 to i32
	store i32 %conv_80489f5_1, i32* %stack_var_-28

	;80489fc	1110100011000011110011110000000000000000	e8 c3 cf 00 00
	;CALL {53187}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_80489fc = add i32 53187, 0 ; used signed value. Unsigned value: 53187
	%u1_80489fc = add i32 134515196, 0	; Assign current PC
	%_d_80489fc = add i32 5, 0
	%u2_80489fc = add i32 %u1_80489fc, %_d_80489fc

	%_f_80489fc = add i32 4, 0
	%u3_80489fc = load i32, i32* @gpr4
	%u4_80489fc = add i32 %u2_80489fc, %u0_80489fc

	%_i_80489fc = add i32 -4, 0
	%u5_80489fc = add i32 %u3_80489fc, %_i_80489fc

	%conv_80489fc_1 = inttoptr i32 %u2_80489fc to i32*
	store i32* %conv_80489fc_1, i32** %stack_var_-32
	%_k_80489fc = add i32 4, 0
	; store of stack pointer to offset -32 into register  @gpr4

	%local_ret_12_80489fc = call i32  @unknown_80559c4() nounwind
	store i32 %local_ret_12_80489fc, i32* %local_ret_12


	;8048a01	11000111000001000010010001100011011101010000010100001000	c7 04 24 63 75 05 08
	;MOV DWORD [ {4}  ], {134575459}  decode__instr_grp32_0_m32_uimm32__instr_mov_0_rmxx_uimmxx__MODRM32_0_mem32__SIB_mod00_32_0_base32_index32__base32_sib_mod00__SIB_scaled_index32_none__uimm32__
	%u0_8048a01 = load i32, i32*  @gpr4
	%u1_8048a01 = add i32 134575459, 0 ; used signed value. Unsigned value: 134575459
	%glob_var_8057563_1345152010 = getelementptr inbounds [13 x i8], [13 x i8]* @glob_var_8057563, i64 0, i64 0
	%conv_8048a01_1 = ptrtoint i8* %glob_var_8057563_1345152010 to i32
	store i32 %conv_8048a01_1, i32* %stack_var_-28

	;8048a08	1110100010110111110011110000000000000000	e8 b7 cf 00 00
	;CALL {53175}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_8048a08 = add i32 53175, 0 ; used signed value. Unsigned value: 53175
	%u1_8048a08 = add i32 134515208, 0	; Assign current PC
	%_d_8048a08 = add i32 5, 0
	%u2_8048a08 = add i32 %u1_8048a08, %_d_8048a08

	%_f_8048a08 = add i32 4, 0
	%u3_8048a08 = load i32, i32* @gpr4
	%u4_8048a08 = add i32 %u2_8048a08, %u0_8048a08

	%_i_8048a08 = add i32 -4, 0
	%u5_8048a08 = add i32 %u3_8048a08, %_i_8048a08

	%conv_8048a08_1 = inttoptr i32 %u2_8048a08 to i32*
	store i32* %conv_8048a08_1, i32** %stack_var_-32
	%_k_8048a08 = add i32 4, 0
	; store of stack pointer to offset -32 into register  @gpr4

	%local_ret_13_8048a08 = call i32  @unknown_80559c4() nounwind
	store i32 %local_ret_13_8048a08, i32* %local_ret_13


	;8048a0d	11000111000001000010010001110000011101010000010100001000	c7 04 24 70 75 05 08
	;MOV DWORD [ {4}  ], {134575472}  decode__instr_grp32_0_m32_uimm32__instr_mov_0_rmxx_uimmxx__MODRM32_0_mem32__SIB_mod00_32_0_base32_index32__base32_sib_mod00__SIB_scaled_index32_none__uimm32__
	%u0_8048a0d = load i32, i32*  @gpr4
	%u1_8048a0d = add i32 134575472, 0 ; used signed value. Unsigned value: 134575472
	%glob_var_8057570_1345152130 = getelementptr inbounds [13 x i8], [13 x i8]* @glob_var_8057570, i64 0, i64 0
	%conv_8048a0d_1 = ptrtoint i8* %glob_var_8057570_1345152130 to i32
	store i32 %conv_8048a0d_1, i32* %stack_var_-28

	;8048a14	1110100010101011110011110000000000000000	e8 ab cf 00 00
	;CALL {53163}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_8048a14 = add i32 53163, 0 ; used signed value. Unsigned value: 53163
	%u1_8048a14 = add i32 134515220, 0	; Assign current PC
	%_d_8048a14 = add i32 5, 0
	%u2_8048a14 = add i32 %u1_8048a14, %_d_8048a14

	%_f_8048a14 = add i32 4, 0
	%u3_8048a14 = load i32, i32* @gpr4
	%u4_8048a14 = add i32 %u2_8048a14, %u0_8048a14

	%_i_8048a14 = add i32 -4, 0
	%u5_8048a14 = add i32 %u3_8048a14, %_i_8048a14

	%conv_8048a14_1 = inttoptr i32 %u2_8048a14 to i32*
	store i32* %conv_8048a14_1, i32** %stack_var_-32
	%_k_8048a14 = add i32 4, 0
	; store of stack pointer to offset -32 into register  @gpr4

	%local_ret_14_8048a14 = call i32  @unknown_80559c4() nounwind
	store i32 %local_ret_14_8048a14, i32* %local_ret_14


	;8048a19	11000111000001000010010001111101011101010000010100001000	c7 04 24 7d 75 05 08
	;MOV DWORD [ {4}  ], {134575485}  decode__instr_grp32_0_m32_uimm32__instr_mov_0_rmxx_uimmxx__MODRM32_0_mem32__SIB_mod00_32_0_base32_index32__base32_sib_mod00__SIB_scaled_index32_none__uimm32__
	%u0_8048a19 = load i32, i32*  @gpr4
	%u1_8048a19 = add i32 134575485, 0 ; used signed value. Unsigned value: 134575485
	%glob_var_805757d_1345152250 = getelementptr inbounds [11 x i8], [11 x i8]* @glob_var_805757d, i64 0, i64 0
	%conv_8048a19_1 = ptrtoint i8* %glob_var_805757d_1345152250 to i32
	store i32 %conv_8048a19_1, i32* %stack_var_-28

	;8048a20	1110100010011111110011110000000000000000	e8 9f cf 00 00
	;CALL {53151}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_8048a20 = add i32 53151, 0 ; used signed value. Unsigned value: 53151
	%u1_8048a20 = add i32 134515232, 0	; Assign current PC
	%_d_8048a20 = add i32 5, 0
	%u2_8048a20 = add i32 %u1_8048a20, %_d_8048a20

	%_f_8048a20 = add i32 4, 0
	%u3_8048a20 = load i32, i32* @gpr4
	%u4_8048a20 = add i32 %u2_8048a20, %u0_8048a20

	%_i_8048a20 = add i32 -4, 0
	%u5_8048a20 = add i32 %u3_8048a20, %_i_8048a20

	%conv_8048a20_1 = inttoptr i32 %u2_8048a20 to i32*
	store i32* %conv_8048a20_1, i32** %stack_var_-32
	%_k_8048a20 = add i32 4, 0
	; store of stack pointer to offset -32 into register  @gpr4

	%local_ret_15_8048a20 = call i32  @unknown_80559c4() nounwind
	store i32 %local_ret_15_8048a20, i32* %local_ret_15


	;8048a25	11000111000001000010010010001000011101010000010100001000	c7 04 24 88 75 05 08
	;MOV DWORD [ {4}  ], {134575496}  decode__instr_grp32_0_m32_uimm32__instr_mov_0_rmxx_uimmxx__MODRM32_0_mem32__SIB_mod00_32_0_base32_index32__base32_sib_mod00__SIB_scaled_index32_none__uimm32__
	%u0_8048a25 = load i32, i32*  @gpr4
	%u1_8048a25 = add i32 134575496, 0 ; used signed value. Unsigned value: 134575496
	%glob_var_8057588_1345152370 = getelementptr inbounds [12 x i8], [12 x i8]* @glob_var_8057588, i64 0, i64 0
	%conv_8048a25_1 = ptrtoint i8* %glob_var_8057588_1345152370 to i32
	store i32 %conv_8048a25_1, i32* %stack_var_-28

	;8048a2c	1110100010010011110011110000000000000000	e8 93 cf 00 00
	;CALL {53139}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_8048a2c = add i32 53139, 0 ; used signed value. Unsigned value: 53139
	%u1_8048a2c = add i32 134515244, 0	; Assign current PC
	%_d_8048a2c = add i32 5, 0
	%u2_8048a2c = add i32 %u1_8048a2c, %_d_8048a2c

	%_f_8048a2c = add i32 4, 0
	%u3_8048a2c = load i32, i32* @gpr4
	%u4_8048a2c = add i32 %u2_8048a2c, %u0_8048a2c

	%_i_8048a2c = add i32 -4, 0
	%u5_8048a2c = add i32 %u3_8048a2c, %_i_8048a2c

	%conv_8048a2c_1 = inttoptr i32 %u2_8048a2c to i32*
	store i32* %conv_8048a2c_1, i32** %stack_var_-32
	%_k_8048a2c = add i32 4, 0
	; store of stack pointer to offset -32 into register  @gpr4

	%local_ret_16_8048a2c = call i32  @unknown_80559c4() nounwind
	store i32 %local_ret_16_8048a2c, i32* %local_ret_16


	;8048a31	11000111000001000010010010010100011101010000010100001000	c7 04 24 94 75 05 08
	;MOV DWORD [ {4}  ], {134575508}  decode__instr_grp32_0_m32_uimm32__instr_mov_0_rmxx_uimmxx__MODRM32_0_mem32__SIB_mod00_32_0_base32_index32__base32_sib_mod00__SIB_scaled_index32_none__uimm32__
	%u0_8048a31 = load i32, i32*  @gpr4
	%u1_8048a31 = add i32 134575508, 0 ; used signed value. Unsigned value: 134575508
	%glob_var_8057594_1345152490 = getelementptr inbounds [11 x i8], [11 x i8]* @glob_var_8057594, i64 0, i64 0
	%conv_8048a31_1 = ptrtoint i8* %glob_var_8057594_1345152490 to i32
	store i32 %conv_8048a31_1, i32* %stack_var_-28

	;8048a38	1110100010000111110011110000000000000000	e8 87 cf 00 00
	;CALL {53127}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_8048a38 = add i32 53127, 0 ; used signed value. Unsigned value: 53127
	%u1_8048a38 = add i32 134515256, 0	; Assign current PC
	%_d_8048a38 = add i32 5, 0
	%u2_8048a38 = add i32 %u1_8048a38, %_d_8048a38

	%_f_8048a38 = add i32 4, 0
	%u3_8048a38 = load i32, i32* @gpr4
	%u4_8048a38 = add i32 %u2_8048a38, %u0_8048a38

	%_i_8048a38 = add i32 -4, 0
	%u5_8048a38 = add i32 %u3_8048a38, %_i_8048a38

	%conv_8048a38_1 = inttoptr i32 %u2_8048a38 to i32*
	store i32* %conv_8048a38_1, i32** %stack_var_-32
	%_k_8048a38 = add i32 4, 0
	; store of stack pointer to offset -32 into register  @gpr4

	%local_ret_17_8048a38 = call i32  @unknown_80559c4() nounwind
	store i32 %local_ret_17_8048a38, i32* %local_ret_17


	;8048a3d	11000111000001000010010010011111011101010000010100001000	c7 04 24 9f 75 05 08
	;MOV DWORD [ {4}  ], {134575519}  decode__instr_grp32_0_m32_uimm32__instr_mov_0_rmxx_uimmxx__MODRM32_0_mem32__SIB_mod00_32_0_base32_index32__base32_sib_mod00__SIB_scaled_index32_none__uimm32__
	%u0_8048a3d = load i32, i32*  @gpr4
	%u1_8048a3d = add i32 134575519, 0 ; used signed value. Unsigned value: 134575519
	%glob_var_805759f_1345152610 = getelementptr inbounds [11 x i8], [11 x i8]* @glob_var_805759f, i64 0, i64 0
	%conv_8048a3d_1 = ptrtoint i8* %glob_var_805759f_1345152610 to i32
	store i32 %conv_8048a3d_1, i32* %stack_var_-28

	;8048a44	1110100001111011110011110000000000000000	e8 7b cf 00 00
	;CALL {53115}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_8048a44 = add i32 53115, 0 ; used signed value. Unsigned value: 53115
	%u1_8048a44 = add i32 134515268, 0	; Assign current PC
	%_d_8048a44 = add i32 5, 0
	%u2_8048a44 = add i32 %u1_8048a44, %_d_8048a44

	%_f_8048a44 = add i32 4, 0
	%u3_8048a44 = load i32, i32* @gpr4
	%u4_8048a44 = add i32 %u2_8048a44, %u0_8048a44

	%_i_8048a44 = add i32 -4, 0
	%u5_8048a44 = add i32 %u3_8048a44, %_i_8048a44

	%conv_8048a44_1 = inttoptr i32 %u2_8048a44 to i32*
	store i32* %conv_8048a44_1, i32** %stack_var_-32
	%_k_8048a44 = add i32 4, 0
	; store of stack pointer to offset -32 into register  @gpr4

	%local_ret_18_8048a44 = call i32  @unknown_80559c4() nounwind
	store i32 %local_ret_18_8048a44, i32* %local_ret_18


	;8048a49	11000111000001000010010010101010011101010000010100001000	c7 04 24 aa 75 05 08
	;MOV DWORD [ {4}  ], {134575530}  decode__instr_grp32_0_m32_uimm32__instr_mov_0_rmxx_uimmxx__MODRM32_0_mem32__SIB_mod00_32_0_base32_index32__base32_sib_mod00__SIB_scaled_index32_none__uimm32__
	%u0_8048a49 = load i32, i32*  @gpr4
	%u1_8048a49 = add i32 134575530, 0 ; used signed value. Unsigned value: 134575530
	%glob_var_80575aa_1345152730 = getelementptr inbounds [11 x i8], [11 x i8]* @glob_var_80575aa, i64 0, i64 0
	%conv_8048a49_1 = ptrtoint i8* %glob_var_80575aa_1345152730 to i32
	store i32 %conv_8048a49_1, i32* %stack_var_-28

	;8048a50	1110100001101111110011110000000000000000	e8 6f cf 00 00
	;CALL {53103}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_8048a50 = add i32 53103, 0 ; used signed value. Unsigned value: 53103
	%u1_8048a50 = add i32 134515280, 0	; Assign current PC
	%_d_8048a50 = add i32 5, 0
	%u2_8048a50 = add i32 %u1_8048a50, %_d_8048a50

	%_f_8048a50 = add i32 4, 0
	%u3_8048a50 = load i32, i32* @gpr4
	%u4_8048a50 = add i32 %u2_8048a50, %u0_8048a50

	%_i_8048a50 = add i32 -4, 0
	%u5_8048a50 = add i32 %u3_8048a50, %_i_8048a50

	%conv_8048a50_1 = inttoptr i32 %u2_8048a50 to i32*
	store i32* %conv_8048a50_1, i32** %stack_var_-32
	%_k_8048a50 = add i32 4, 0
	; store of stack pointer to offset -32 into register  @gpr4

	%local_ret_19_8048a50 = call i32  @unknown_80559c4() nounwind
	store i32 %local_ret_19_8048a50, i32* %local_ret_19


	;8048a55	11000111000001000010010010110101011101010000010100001000	c7 04 24 b5 75 05 08
	;MOV DWORD [ {4}  ], {134575541}  decode__instr_grp32_0_m32_uimm32__instr_mov_0_rmxx_uimmxx__MODRM32_0_mem32__SIB_mod00_32_0_base32_index32__base32_sib_mod00__SIB_scaled_index32_none__uimm32__
	%u0_8048a55 = load i32, i32*  @gpr4
	%u1_8048a55 = add i32 134575541, 0 ; used signed value. Unsigned value: 134575541
	%glob_var_80575b5_1345152850 = getelementptr inbounds [13 x i8], [13 x i8]* @glob_var_80575b5, i64 0, i64 0
	%conv_8048a55_1 = ptrtoint i8* %glob_var_80575b5_1345152850 to i32
	store i32 %conv_8048a55_1, i32* %stack_var_-28

	;8048a5c	1110100001100011110011110000000000000000	e8 63 cf 00 00
	;CALL {53091}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_8048a5c = add i32 53091, 0 ; used signed value. Unsigned value: 53091
	%u1_8048a5c = add i32 134515292, 0	; Assign current PC
	%_d_8048a5c = add i32 5, 0
	%u2_8048a5c = add i32 %u1_8048a5c, %_d_8048a5c

	%_f_8048a5c = add i32 4, 0
	%u3_8048a5c = load i32, i32* @gpr4
	%u4_8048a5c = add i32 %u2_8048a5c, %u0_8048a5c

	%_i_8048a5c = add i32 -4, 0
	%u5_8048a5c = add i32 %u3_8048a5c, %_i_8048a5c

	%conv_8048a5c_1 = inttoptr i32 %u2_8048a5c to i32*
	store i32* %conv_8048a5c_1, i32** %stack_var_-32
	%_k_8048a5c = add i32 4, 0
	; store of stack pointer to offset -32 into register  @gpr4

	%local_ret_20_8048a5c = call i32  @unknown_80559c4() nounwind
	store i32 %local_ret_20_8048a5c, i32* %local_ret_20


	;8048a61	11000111000001000010010011000010011101010000010100001000	c7 04 24 c2 75 05 08
	;MOV DWORD [ {4}  ], {134575554}  decode__instr_grp32_0_m32_uimm32__instr_mov_0_rmxx_uimmxx__MODRM32_0_mem32__SIB_mod00_32_0_base32_index32__base32_sib_mod00__SIB_scaled_index32_none__uimm32__
	%u0_8048a61 = load i32, i32*  @gpr4
	%u1_8048a61 = add i32 134575554, 0 ; used signed value. Unsigned value: 134575554
	%glob_var_80575c2_1345152970 = getelementptr inbounds [12 x i8], [12 x i8]* @glob_var_80575c2, i64 0, i64 0
	%conv_8048a61_1 = ptrtoint i8* %glob_var_80575c2_1345152970 to i32
	store i32 %conv_8048a61_1, i32* %stack_var_-28

	;8048a68	1110100001010111110011110000000000000000	e8 57 cf 00 00
	;CALL {53079}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_8048a68 = add i32 53079, 0 ; used signed value. Unsigned value: 53079
	%u1_8048a68 = add i32 134515304, 0	; Assign current PC
	%_d_8048a68 = add i32 5, 0
	%u2_8048a68 = add i32 %u1_8048a68, %_d_8048a68

	%_f_8048a68 = add i32 4, 0
	%u3_8048a68 = load i32, i32* @gpr4
	%u4_8048a68 = add i32 %u2_8048a68, %u0_8048a68

	%_i_8048a68 = add i32 -4, 0
	%u5_8048a68 = add i32 %u3_8048a68, %_i_8048a68

	%conv_8048a68_1 = inttoptr i32 %u2_8048a68 to i32*
	store i32* %conv_8048a68_1, i32** %stack_var_-32
	%_k_8048a68 = add i32 4, 0
	; store of stack pointer to offset -32 into register  @gpr4

	%local_ret_21_8048a68 = call i32  @unknown_80559c4() nounwind
	store i32 %local_ret_21_8048a68, i32* %local_ret_21


	;8048a6d	11000111000001000010010011001110011101010000010100001000	c7 04 24 ce 75 05 08
	;MOV DWORD [ {4}  ], {134575566}  decode__instr_grp32_0_m32_uimm32__instr_mov_0_rmxx_uimmxx__MODRM32_0_mem32__SIB_mod00_32_0_base32_index32__base32_sib_mod00__SIB_scaled_index32_none__uimm32__
	%u0_8048a6d = load i32, i32*  @gpr4
	%u1_8048a6d = add i32 134575566, 0 ; used signed value. Unsigned value: 134575566
	%glob_var_80575ce_1345153090 = getelementptr inbounds [12 x i8], [12 x i8]* @glob_var_80575ce, i64 0, i64 0
	%conv_8048a6d_1 = ptrtoint i8* %glob_var_80575ce_1345153090 to i32
	store i32 %conv_8048a6d_1, i32* %stack_var_-28

	;8048a74	1110100001001011110011110000000000000000	e8 4b cf 00 00
	;CALL {53067}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_8048a74 = add i32 53067, 0 ; used signed value. Unsigned value: 53067
	%u1_8048a74 = add i32 134515316, 0	; Assign current PC
	%_d_8048a74 = add i32 5, 0
	%u2_8048a74 = add i32 %u1_8048a74, %_d_8048a74

	%_f_8048a74 = add i32 4, 0
	%u3_8048a74 = load i32, i32* @gpr4
	%u4_8048a74 = add i32 %u2_8048a74, %u0_8048a74

	%_i_8048a74 = add i32 -4, 0
	%u5_8048a74 = add i32 %u3_8048a74, %_i_8048a74

	%conv_8048a74_1 = inttoptr i32 %u2_8048a74 to i32*
	store i32* %conv_8048a74_1, i32** %stack_var_-32
	%_k_8048a74 = add i32 4, 0
	; store of stack pointer to offset -32 into register  @gpr4

	%local_ret_22_8048a74 = call i32  @unknown_80559c4() nounwind
	store i32 %local_ret_22_8048a74, i32* %local_ret_22


	;8048a79	11000111000001000010010011011010011101010000010100001000	c7 04 24 da 75 05 08
	;MOV DWORD [ {4}  ], {134575578}  decode__instr_grp32_0_m32_uimm32__instr_mov_0_rmxx_uimmxx__MODRM32_0_mem32__SIB_mod00_32_0_base32_index32__base32_sib_mod00__SIB_scaled_index32_none__uimm32__
	%u0_8048a79 = load i32, i32*  @gpr4
	%u1_8048a79 = add i32 134575578, 0 ; used signed value. Unsigned value: 134575578
	%glob_var_80575da_1345153210 = getelementptr inbounds [12 x i8], [12 x i8]* @glob_var_80575da, i64 0, i64 0
	%conv_8048a79_1 = ptrtoint i8* %glob_var_80575da_1345153210 to i32
	store i32 %conv_8048a79_1, i32* %stack_var_-28

	;8048a80	1110100000111111110011110000000000000000	e8 3f cf 00 00
	;CALL {53055}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_8048a80 = add i32 53055, 0 ; used signed value. Unsigned value: 53055
	%u1_8048a80 = add i32 134515328, 0	; Assign current PC
	%_d_8048a80 = add i32 5, 0
	%u2_8048a80 = add i32 %u1_8048a80, %_d_8048a80

	%_f_8048a80 = add i32 4, 0
	%u3_8048a80 = load i32, i32* @gpr4
	%u4_8048a80 = add i32 %u2_8048a80, %u0_8048a80

	%_i_8048a80 = add i32 -4, 0
	%u5_8048a80 = add i32 %u3_8048a80, %_i_8048a80

	%conv_8048a80_1 = inttoptr i32 %u2_8048a80 to i32*
	store i32* %conv_8048a80_1, i32** %stack_var_-32
	%_k_8048a80 = add i32 4, 0
	; store of stack pointer to offset -32 into register  @gpr4

	%local_ret_23_8048a80 = call i32  @unknown_80559c4() nounwind
	store i32 %local_ret_23_8048a80, i32* %local_ret_23


	;8048a85	11000111000001000010010011100110011101010000010100001000	c7 04 24 e6 75 05 08
	;MOV DWORD [ {4}  ], {134575590}  decode__instr_grp32_0_m32_uimm32__instr_mov_0_rmxx_uimmxx__MODRM32_0_mem32__SIB_mod00_32_0_base32_index32__base32_sib_mod00__SIB_scaled_index32_none__uimm32__
	%u0_8048a85 = load i32, i32*  @gpr4
	%u1_8048a85 = add i32 134575590, 0 ; used signed value. Unsigned value: 134575590
	%glob_var_80575e6_1345153330 = getelementptr inbounds [12 x i8], [12 x i8]* @glob_var_80575e6, i64 0, i64 0
	%conv_8048a85_1 = ptrtoint i8* %glob_var_80575e6_1345153330 to i32
	store i32 %conv_8048a85_1, i32* %stack_var_-28

	;8048a8c	1110100000110011110011110000000000000000	e8 33 cf 00 00
	;CALL {53043}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_8048a8c = add i32 53043, 0 ; used signed value. Unsigned value: 53043
	%u1_8048a8c = add i32 134515340, 0	; Assign current PC
	%_d_8048a8c = add i32 5, 0
	%u2_8048a8c = add i32 %u1_8048a8c, %_d_8048a8c

	%_f_8048a8c = add i32 4, 0
	%u3_8048a8c = load i32, i32* @gpr4
	%u4_8048a8c = add i32 %u2_8048a8c, %u0_8048a8c

	%_i_8048a8c = add i32 -4, 0
	%u5_8048a8c = add i32 %u3_8048a8c, %_i_8048a8c

	%conv_8048a8c_1 = inttoptr i32 %u2_8048a8c to i32*
	store i32* %conv_8048a8c_1, i32** %stack_var_-32
	%_k_8048a8c = add i32 4, 0
	; store of stack pointer to offset -32 into register  @gpr4

	%local_ret_24_8048a8c = call i32  @unknown_80559c4() nounwind
	store i32 %local_ret_24_8048a8c, i32* %local_ret_24


	;8048a91	11000111000001000010010011110010011101010000010100001000	c7 04 24 f2 75 05 08
	;MOV DWORD [ {4}  ], {134575602}  decode__instr_grp32_0_m32_uimm32__instr_mov_0_rmxx_uimmxx__MODRM32_0_mem32__SIB_mod00_32_0_base32_index32__base32_sib_mod00__SIB_scaled_index32_none__uimm32__
	%u0_8048a91 = load i32, i32*  @gpr4
	%u1_8048a91 = add i32 134575602, 0 ; used signed value. Unsigned value: 134575602
	%glob_var_80575f2_1345153450 = getelementptr inbounds [12 x i8], [12 x i8]* @glob_var_80575f2, i64 0, i64 0
	%conv_8048a91_1 = ptrtoint i8* %glob_var_80575f2_1345153450 to i32
	store i32 %conv_8048a91_1, i32* %stack_var_-28

	;8048a98	1110100000100111110011110000000000000000	e8 27 cf 00 00
	;CALL {53031}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_8048a98 = add i32 53031, 0 ; used signed value. Unsigned value: 53031
	%u1_8048a98 = add i32 134515352, 0	; Assign current PC
	%_d_8048a98 = add i32 5, 0
	%u2_8048a98 = add i32 %u1_8048a98, %_d_8048a98

	%_f_8048a98 = add i32 4, 0
	%u3_8048a98 = load i32, i32* @gpr4
	%u4_8048a98 = add i32 %u2_8048a98, %u0_8048a98

	%_i_8048a98 = add i32 -4, 0
	%u5_8048a98 = add i32 %u3_8048a98, %_i_8048a98

	%conv_8048a98_1 = inttoptr i32 %u2_8048a98 to i32*
	store i32* %conv_8048a98_1, i32** %stack_var_-32
	%_k_8048a98 = add i32 4, 0
	; store of stack pointer to offset -32 into register  @gpr4

	%local_ret_25_8048a98 = call i32  @unknown_80559c4() nounwind
	store i32 %local_ret_25_8048a98, i32* %local_ret_25


	;8048a9d	11000111000001000010010011111110011101010000010100001000	c7 04 24 fe 75 05 08
	;MOV DWORD [ {4}  ], {134575614}  decode__instr_grp32_0_m32_uimm32__instr_mov_0_rmxx_uimmxx__MODRM32_0_mem32__SIB_mod00_32_0_base32_index32__base32_sib_mod00__SIB_scaled_index32_none__uimm32__
	%u0_8048a9d = load i32, i32*  @gpr4
	%u1_8048a9d = add i32 134575614, 0 ; used signed value. Unsigned value: 134575614
	%glob_var_80575fe_1345153570 = getelementptr inbounds [13 x i8], [13 x i8]* @glob_var_80575fe, i64 0, i64 0
	%conv_8048a9d_1 = ptrtoint i8* %glob_var_80575fe_1345153570 to i32
	store i32 %conv_8048a9d_1, i32* %stack_var_-28

	;8048aa4	1110100000011011110011110000000000000000	e8 1b cf 00 00
	;CALL {53019}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_8048aa4 = add i32 53019, 0 ; used signed value. Unsigned value: 53019
	%u1_8048aa4 = add i32 134515364, 0	; Assign current PC
	%_d_8048aa4 = add i32 5, 0
	%u2_8048aa4 = add i32 %u1_8048aa4, %_d_8048aa4

	%_f_8048aa4 = add i32 4, 0
	%u3_8048aa4 = load i32, i32* @gpr4
	%u4_8048aa4 = add i32 %u2_8048aa4, %u0_8048aa4

	%_i_8048aa4 = add i32 -4, 0
	%u5_8048aa4 = add i32 %u3_8048aa4, %_i_8048aa4

	%conv_8048aa4_1 = inttoptr i32 %u2_8048aa4 to i32*
	store i32* %conv_8048aa4_1, i32** %stack_var_-32
	%_k_8048aa4 = add i32 4, 0
	; store of stack pointer to offset -32 into register  @gpr4

	%local_ret_26_8048aa4 = call i32  @unknown_80559c4() nounwind
	store i32 %local_ret_26_8048aa4, i32* %local_ret_26


	;8048aa9	11000111000001000010010000001011011101100000010100001000	c7 04 24 0b 76 05 08
	;MOV DWORD [ {4}  ], {134575627}  decode__instr_grp32_0_m32_uimm32__instr_mov_0_rmxx_uimmxx__MODRM32_0_mem32__SIB_mod00_32_0_base32_index32__base32_sib_mod00__SIB_scaled_index32_none__uimm32__
	%u0_8048aa9 = load i32, i32*  @gpr4
	%u1_8048aa9 = add i32 134575627, 0 ; used signed value. Unsigned value: 134575627
	%glob_var_805760b_1345153690 = getelementptr inbounds [13 x i8], [13 x i8]* @glob_var_805760b, i64 0, i64 0
	%conv_8048aa9_1 = ptrtoint i8* %glob_var_805760b_1345153690 to i32
	store i32 %conv_8048aa9_1, i32* %stack_var_-28

	;8048ab0	1110100000001111110011110000000000000000	e8 0f cf 00 00
	;CALL {53007}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_8048ab0 = add i32 53007, 0 ; used signed value. Unsigned value: 53007
	%u1_8048ab0 = add i32 134515376, 0	; Assign current PC
	%_d_8048ab0 = add i32 5, 0
	%u2_8048ab0 = add i32 %u1_8048ab0, %_d_8048ab0

	%_f_8048ab0 = add i32 4, 0
	%u3_8048ab0 = load i32, i32* @gpr4
	%u4_8048ab0 = add i32 %u2_8048ab0, %u0_8048ab0

	%_i_8048ab0 = add i32 -4, 0
	%u5_8048ab0 = add i32 %u3_8048ab0, %_i_8048ab0

	%conv_8048ab0_1 = inttoptr i32 %u2_8048ab0 to i32*
	store i32* %conv_8048ab0_1, i32** %stack_var_-32
	%_k_8048ab0 = add i32 4, 0
	; store of stack pointer to offset -32 into register  @gpr4

	%local_ret_27_8048ab0 = call i32  @unknown_80559c4() nounwind
	store i32 %local_ret_27_8048ab0, i32* %local_ret_27


	;8048ab5	11000111000001000010010000011000011101100000010100001000	c7 04 24 18 76 05 08
	;MOV DWORD [ {4}  ], {134575640}  decode__instr_grp32_0_m32_uimm32__instr_mov_0_rmxx_uimmxx__MODRM32_0_mem32__SIB_mod00_32_0_base32_index32__base32_sib_mod00__SIB_scaled_index32_none__uimm32__
	%u0_8048ab5 = load i32, i32*  @gpr4
	%u1_8048ab5 = add i32 134575640, 0 ; used signed value. Unsigned value: 134575640
	%glob_var_8057618_1345153810 = getelementptr inbounds [13 x i8], [13 x i8]* @glob_var_8057618, i64 0, i64 0
	%conv_8048ab5_1 = ptrtoint i8* %glob_var_8057618_1345153810 to i32
	store i32 %conv_8048ab5_1, i32* %stack_var_-28

	;8048abc	1110100000000011110011110000000000000000	e8 03 cf 00 00
	;CALL {52995}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_8048abc = add i32 52995, 0 ; used signed value. Unsigned value: 52995
	%u1_8048abc = add i32 134515388, 0	; Assign current PC
	%_d_8048abc = add i32 5, 0
	%u2_8048abc = add i32 %u1_8048abc, %_d_8048abc

	%_f_8048abc = add i32 4, 0
	%u3_8048abc = load i32, i32* @gpr4
	%u4_8048abc = add i32 %u2_8048abc, %u0_8048abc

	%_i_8048abc = add i32 -4, 0
	%u5_8048abc = add i32 %u3_8048abc, %_i_8048abc

	%conv_8048abc_1 = inttoptr i32 %u2_8048abc to i32*
	store i32* %conv_8048abc_1, i32** %stack_var_-32
	%_k_8048abc = add i32 4, 0
	; store of stack pointer to offset -32 into register  @gpr4

	%local_ret_28_8048abc = call i32  @unknown_80559c4() nounwind
	store i32 %local_ret_28_8048abc, i32* %local_ret_28


	;8048ac1	11000111000001000010010000100101011101100000010100001000	c7 04 24 25 76 05 08
	;MOV DWORD [ {4}  ], {134575653}  decode__instr_grp32_0_m32_uimm32__instr_mov_0_rmxx_uimmxx__MODRM32_0_mem32__SIB_mod00_32_0_base32_index32__base32_sib_mod00__SIB_scaled_index32_none__uimm32__
	%u0_8048ac1 = load i32, i32*  @gpr4
	%u1_8048ac1 = add i32 134575653, 0 ; used signed value. Unsigned value: 134575653
	%glob_var_8057625_1345153930 = getelementptr inbounds [13 x i8], [13 x i8]* @glob_var_8057625, i64 0, i64 0
	%conv_8048ac1_1 = ptrtoint i8* %glob_var_8057625_1345153930 to i32
	store i32 %conv_8048ac1_1, i32* %stack_var_-28

	;8048ac8	1110100011110111110011100000000000000000	e8 f7 ce 00 00
	;CALL {52983}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_8048ac8 = add i32 52983, 0 ; used signed value. Unsigned value: 52983
	%u1_8048ac8 = add i32 134515400, 0	; Assign current PC
	%_d_8048ac8 = add i32 5, 0
	%u2_8048ac8 = add i32 %u1_8048ac8, %_d_8048ac8

	%_f_8048ac8 = add i32 4, 0
	%u3_8048ac8 = load i32, i32* @gpr4
	%u4_8048ac8 = add i32 %u2_8048ac8, %u0_8048ac8

	%_i_8048ac8 = add i32 -4, 0
	%u5_8048ac8 = add i32 %u3_8048ac8, %_i_8048ac8

	%conv_8048ac8_1 = inttoptr i32 %u2_8048ac8 to i32*
	store i32* %conv_8048ac8_1, i32** %stack_var_-32
	%_k_8048ac8 = add i32 4, 0
	; store of stack pointer to offset -32 into register  @gpr4

	%local_ret_29_8048ac8 = call i32  @unknown_80559c4() nounwind
	store i32 %local_ret_29_8048ac8, i32* %local_ret_29


	;8048acd	11000111000001000010010000110010011101100000010100001000	c7 04 24 32 76 05 08
	;MOV DWORD [ {4}  ], {134575666}  decode__instr_grp32_0_m32_uimm32__instr_mov_0_rmxx_uimmxx__MODRM32_0_mem32__SIB_mod00_32_0_base32_index32__base32_sib_mod00__SIB_scaled_index32_none__uimm32__
	%u0_8048acd = load i32, i32*  @gpr4
	%u1_8048acd = add i32 134575666, 0 ; used signed value. Unsigned value: 134575666
	%glob_var_8057632_1345154050 = getelementptr inbounds [13 x i8], [13 x i8]* @glob_var_8057632, i64 0, i64 0
	%conv_8048acd_1 = ptrtoint i8* %glob_var_8057632_1345154050 to i32
	store i32 %conv_8048acd_1, i32* %stack_var_-28

	;8048ad4	1110100011101011110011100000000000000000	e8 eb ce 00 00
	;CALL {52971}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_8048ad4 = add i32 52971, 0 ; used signed value. Unsigned value: 52971
	%u1_8048ad4 = add i32 134515412, 0	; Assign current PC
	%_d_8048ad4 = add i32 5, 0
	%u2_8048ad4 = add i32 %u1_8048ad4, %_d_8048ad4

	%_f_8048ad4 = add i32 4, 0
	%u3_8048ad4 = load i32, i32* @gpr4
	%u4_8048ad4 = add i32 %u2_8048ad4, %u0_8048ad4

	%_i_8048ad4 = add i32 -4, 0
	%u5_8048ad4 = add i32 %u3_8048ad4, %_i_8048ad4

	%conv_8048ad4_1 = inttoptr i32 %u2_8048ad4 to i32*
	store i32* %conv_8048ad4_1, i32** %stack_var_-32
	%_k_8048ad4 = add i32 4, 0
	; store of stack pointer to offset -32 into register  @gpr4

	%local_ret_30_8048ad4 = call i32  @unknown_80559c4() nounwind
	store i32 %local_ret_30_8048ad4, i32* %local_ret_30


	;8048ad9	11000111000001000010010000111111011101100000010100001000	c7 04 24 3f 76 05 08
	;MOV DWORD [ {4}  ], {134575679}  decode__instr_grp32_0_m32_uimm32__instr_mov_0_rmxx_uimmxx__MODRM32_0_mem32__SIB_mod00_32_0_base32_index32__base32_sib_mod00__SIB_scaled_index32_none__uimm32__
	%u0_8048ad9 = load i32, i32*  @gpr4
	%u1_8048ad9 = add i32 134575679, 0 ; used signed value. Unsigned value: 134575679
	%glob_var_805763f_1345154170 = getelementptr inbounds [13 x i8], [13 x i8]* @glob_var_805763f, i64 0, i64 0
	%conv_8048ad9_1 = ptrtoint i8* %glob_var_805763f_1345154170 to i32
	store i32 %conv_8048ad9_1, i32* %stack_var_-28

	;8048ae0	1110100011011111110011100000000000000000	e8 df ce 00 00
	;CALL {52959}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_8048ae0 = add i32 52959, 0 ; used signed value. Unsigned value: 52959
	%u1_8048ae0 = add i32 134515424, 0	; Assign current PC
	%_d_8048ae0 = add i32 5, 0
	%u2_8048ae0 = add i32 %u1_8048ae0, %_d_8048ae0

	%_f_8048ae0 = add i32 4, 0
	%u3_8048ae0 = load i32, i32* @gpr4
	%u4_8048ae0 = add i32 %u2_8048ae0, %u0_8048ae0

	%_i_8048ae0 = add i32 -4, 0
	%u5_8048ae0 = add i32 %u3_8048ae0, %_i_8048ae0

	%conv_8048ae0_1 = inttoptr i32 %u2_8048ae0 to i32*
	store i32* %conv_8048ae0_1, i32** %stack_var_-32
	%_k_8048ae0 = add i32 4, 0
	; store of stack pointer to offset -32 into register  @gpr4

	%local_ret_31_8048ae0 = call i32  @unknown_80559c4() nounwind
	store i32 %local_ret_31_8048ae0, i32* %local_ret_31


	;8048ae5	11000111000001000010010001001100011101100000010100001000	c7 04 24 4c 76 05 08
	;MOV DWORD [ {4}  ], {134575692}  decode__instr_grp32_0_m32_uimm32__instr_mov_0_rmxx_uimmxx__MODRM32_0_mem32__SIB_mod00_32_0_base32_index32__base32_sib_mod00__SIB_scaled_index32_none__uimm32__
	%u0_8048ae5 = load i32, i32*  @gpr4
	%u1_8048ae5 = add i32 134575692, 0 ; used signed value. Unsigned value: 134575692
	%glob_var_805764c_1345154290 = getelementptr inbounds [13 x i8], [13 x i8]* @glob_var_805764c, i64 0, i64 0
	%conv_8048ae5_1 = ptrtoint i8* %glob_var_805764c_1345154290 to i32
	store i32 %conv_8048ae5_1, i32* %stack_var_-28

	;8048aec	1110100011010011110011100000000000000000	e8 d3 ce 00 00
	;CALL {52947}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_8048aec = add i32 52947, 0 ; used signed value. Unsigned value: 52947
	%u1_8048aec = add i32 134515436, 0	; Assign current PC
	%_d_8048aec = add i32 5, 0
	%u2_8048aec = add i32 %u1_8048aec, %_d_8048aec

	%_f_8048aec = add i32 4, 0
	%u3_8048aec = load i32, i32* @gpr4
	%u4_8048aec = add i32 %u2_8048aec, %u0_8048aec

	%_i_8048aec = add i32 -4, 0
	%u5_8048aec = add i32 %u3_8048aec, %_i_8048aec

	%conv_8048aec_1 = inttoptr i32 %u2_8048aec to i32*
	store i32* %conv_8048aec_1, i32** %stack_var_-32
	%_k_8048aec = add i32 4, 0
	; store of stack pointer to offset -32 into register  @gpr4

	%local_ret_32_8048aec = call i32  @unknown_80559c4() nounwind
	store i32 %local_ret_32_8048aec, i32* %local_ret_32


	;8048af1	11000111000001000010010001011001011101100000010100001000	c7 04 24 59 76 05 08
	;MOV DWORD [ {4}  ], {134575705}  decode__instr_grp32_0_m32_uimm32__instr_mov_0_rmxx_uimmxx__MODRM32_0_mem32__SIB_mod00_32_0_base32_index32__base32_sib_mod00__SIB_scaled_index32_none__uimm32__
	%u0_8048af1 = load i32, i32*  @gpr4
	%u1_8048af1 = add i32 134575705, 0 ; used signed value. Unsigned value: 134575705
	%glob_var_8057659_1345154410 = getelementptr inbounds [13 x i8], [13 x i8]* @glob_var_8057659, i64 0, i64 0
	%conv_8048af1_1 = ptrtoint i8* %glob_var_8057659_1345154410 to i32
	store i32 %conv_8048af1_1, i32* %stack_var_-28

	;8048af8	1110100011000111110011100000000000000000	e8 c7 ce 00 00
	;CALL {52935}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_8048af8 = add i32 52935, 0 ; used signed value. Unsigned value: 52935
	%u1_8048af8 = add i32 134515448, 0	; Assign current PC
	%_d_8048af8 = add i32 5, 0
	%u2_8048af8 = add i32 %u1_8048af8, %_d_8048af8

	%_f_8048af8 = add i32 4, 0
	%u3_8048af8 = load i32, i32* @gpr4
	%u4_8048af8 = add i32 %u2_8048af8, %u0_8048af8

	%_i_8048af8 = add i32 -4, 0
	%u5_8048af8 = add i32 %u3_8048af8, %_i_8048af8

	%conv_8048af8_1 = inttoptr i32 %u2_8048af8 to i32*
	store i32* %conv_8048af8_1, i32** %stack_var_-32
	%_k_8048af8 = add i32 4, 0
	; store of stack pointer to offset -32 into register  @gpr4

	%local_ret_33_8048af8 = call i32  @unknown_80559c4() nounwind
	store i32 %local_ret_33_8048af8, i32* %local_ret_33


	;8048afd	11000111000001000010010001100110011101100000010100001000	c7 04 24 66 76 05 08
	;MOV DWORD [ {4}  ], {134575718}  decode__instr_grp32_0_m32_uimm32__instr_mov_0_rmxx_uimmxx__MODRM32_0_mem32__SIB_mod00_32_0_base32_index32__base32_sib_mod00__SIB_scaled_index32_none__uimm32__
	%u0_8048afd = load i32, i32*  @gpr4
	%u1_8048afd = add i32 134575718, 0 ; used signed value. Unsigned value: 134575718
	%glob_var_8057666_1345154530 = getelementptr inbounds [14 x i8], [14 x i8]* @glob_var_8057666, i64 0, i64 0
	%conv_8048afd_1 = ptrtoint i8* %glob_var_8057666_1345154530 to i32
	store i32 %conv_8048afd_1, i32* %stack_var_-28

	;8048b04	1110100010111011110011100000000000000000	e8 bb ce 00 00
	;CALL {52923}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_8048b04 = add i32 52923, 0 ; used signed value. Unsigned value: 52923
	%u1_8048b04 = add i32 134515460, 0	; Assign current PC
	%_d_8048b04 = add i32 5, 0
	%u2_8048b04 = add i32 %u1_8048b04, %_d_8048b04

	%_f_8048b04 = add i32 4, 0
	%u3_8048b04 = load i32, i32* @gpr4
	%u4_8048b04 = add i32 %u2_8048b04, %u0_8048b04

	%_i_8048b04 = add i32 -4, 0
	%u5_8048b04 = add i32 %u3_8048b04, %_i_8048b04

	%conv_8048b04_1 = inttoptr i32 %u2_8048b04 to i32*
	store i32* %conv_8048b04_1, i32** %stack_var_-32
	%_k_8048b04 = add i32 4, 0
	; store of stack pointer to offset -32 into register  @gpr4

	%local_ret_34_8048b04 = call i32  @unknown_80559c4() nounwind
	store i32 %local_ret_34_8048b04, i32* %local_ret_34


	;8048b09	11000111000001000010010001110100011101100000010100001000	c7 04 24 74 76 05 08
	;MOV DWORD [ {4}  ], {134575732}  decode__instr_grp32_0_m32_uimm32__instr_mov_0_rmxx_uimmxx__MODRM32_0_mem32__SIB_mod00_32_0_base32_index32__base32_sib_mod00__SIB_scaled_index32_none__uimm32__
	%u0_8048b09 = load i32, i32*  @gpr4
	%u1_8048b09 = add i32 134575732, 0 ; used signed value. Unsigned value: 134575732
	%glob_var_8057674_1345154650 = getelementptr inbounds [16 x i8], [16 x i8]* @glob_var_8057674, i64 0, i64 0
	%conv_8048b09_1 = ptrtoint i8* %glob_var_8057674_1345154650 to i32
	store i32 %conv_8048b09_1, i32* %stack_var_-28

	;8048b10	1110100010101111110011100000000000000000	e8 af ce 00 00
	;CALL {52911}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_8048b10 = add i32 52911, 0 ; used signed value. Unsigned value: 52911
	%u1_8048b10 = add i32 134515472, 0	; Assign current PC
	%_d_8048b10 = add i32 5, 0
	%u2_8048b10 = add i32 %u1_8048b10, %_d_8048b10

	%_f_8048b10 = add i32 4, 0
	%u3_8048b10 = load i32, i32* @gpr4
	%u4_8048b10 = add i32 %u2_8048b10, %u0_8048b10

	%_i_8048b10 = add i32 -4, 0
	%u5_8048b10 = add i32 %u3_8048b10, %_i_8048b10

	%conv_8048b10_1 = inttoptr i32 %u2_8048b10 to i32*
	store i32* %conv_8048b10_1, i32** %stack_var_-32
	%_k_8048b10 = add i32 4, 0
	; store of stack pointer to offset -32 into register  @gpr4

	%local_ret_35_8048b10 = call i32  @unknown_80559c4() nounwind
	store i32 %local_ret_35_8048b10, i32* %local_ret_35


	;8048b15	11000111000001000010010010000100011101100000010100001000	c7 04 24 84 76 05 08
	;MOV DWORD [ {4}  ], {134575748}  decode__instr_grp32_0_m32_uimm32__instr_mov_0_rmxx_uimmxx__MODRM32_0_mem32__SIB_mod00_32_0_base32_index32__base32_sib_mod00__SIB_scaled_index32_none__uimm32__
	%u0_8048b15 = load i32, i32*  @gpr4
	%u1_8048b15 = add i32 134575748, 0 ; used signed value. Unsigned value: 134575748
	%glob_var_8057684_1345154770 = getelementptr inbounds [17 x i8], [17 x i8]* @glob_var_8057684, i64 0, i64 0
	%conv_8048b15_1 = ptrtoint i8* %glob_var_8057684_1345154770 to i32
	store i32 %conv_8048b15_1, i32* %stack_var_-28

	;8048b1c	1110100010100011110011100000000000000000	e8 a3 ce 00 00
	;CALL {52899}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_8048b1c = add i32 52899, 0 ; used signed value. Unsigned value: 52899
	%u1_8048b1c = add i32 134515484, 0	; Assign current PC
	%_d_8048b1c = add i32 5, 0
	%u2_8048b1c = add i32 %u1_8048b1c, %_d_8048b1c

	%_f_8048b1c = add i32 4, 0
	%u3_8048b1c = load i32, i32* @gpr4
	%u4_8048b1c = add i32 %u2_8048b1c, %u0_8048b1c

	%_i_8048b1c = add i32 -4, 0
	%u5_8048b1c = add i32 %u3_8048b1c, %_i_8048b1c

	%conv_8048b1c_1 = inttoptr i32 %u2_8048b1c to i32*
	store i32* %conv_8048b1c_1, i32** %stack_var_-32
	%_k_8048b1c = add i32 4, 0
	; store of stack pointer to offset -32 into register  @gpr4

	%local_ret_36_8048b1c = call i32  @unknown_80559c4() nounwind
	store i32 %local_ret_36_8048b1c, i32* %local_ret_36


	;8048b21	11000111000001000010010010010101011101100000010100001000	c7 04 24 95 76 05 08
	;MOV DWORD [ {4}  ], {134575765}  decode__instr_grp32_0_m32_uimm32__instr_mov_0_rmxx_uimmxx__MODRM32_0_mem32__SIB_mod00_32_0_base32_index32__base32_sib_mod00__SIB_scaled_index32_none__uimm32__
	%u0_8048b21 = load i32, i32*  @gpr4
	%u1_8048b21 = add i32 134575765, 0 ; used signed value. Unsigned value: 134575765
	%glob_var_8057695_1345154890 = getelementptr inbounds [14 x i8], [14 x i8]* @glob_var_8057695, i64 0, i64 0
	%conv_8048b21_1 = ptrtoint i8* %glob_var_8057695_1345154890 to i32
	store i32 %conv_8048b21_1, i32* %stack_var_-28

	;8048b28	1110100010010111110011100000000000000000	e8 97 ce 00 00
	;CALL {52887}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_8048b28 = add i32 52887, 0 ; used signed value. Unsigned value: 52887
	%u1_8048b28 = add i32 134515496, 0	; Assign current PC
	%_d_8048b28 = add i32 5, 0
	%u2_8048b28 = add i32 %u1_8048b28, %_d_8048b28

	%_f_8048b28 = add i32 4, 0
	%u3_8048b28 = load i32, i32* @gpr4
	%u4_8048b28 = add i32 %u2_8048b28, %u0_8048b28

	%_i_8048b28 = add i32 -4, 0
	%u5_8048b28 = add i32 %u3_8048b28, %_i_8048b28

	%conv_8048b28_1 = inttoptr i32 %u2_8048b28 to i32*
	store i32* %conv_8048b28_1, i32** %stack_var_-32
	%_k_8048b28 = add i32 4, 0
	; store of stack pointer to offset -32 into register  @gpr4

	%local_ret_37_8048b28 = call i32  @unknown_80559c4() nounwind
	store i32 %local_ret_37_8048b28, i32* %local_ret_37


	;8048b2d	11000111000001000010010010100011011101100000010100001000	c7 04 24 a3 76 05 08
	;MOV DWORD [ {4}  ], {134575779}  decode__instr_grp32_0_m32_uimm32__instr_mov_0_rmxx_uimmxx__MODRM32_0_mem32__SIB_mod00_32_0_base32_index32__base32_sib_mod00__SIB_scaled_index32_none__uimm32__
	%u0_8048b2d = load i32, i32*  @gpr4
	%u1_8048b2d = add i32 134575779, 0 ; used signed value. Unsigned value: 134575779
	%glob_var_80576a3_1345155010 = getelementptr inbounds [13 x i8], [13 x i8]* @glob_var_80576a3, i64 0, i64 0
	%conv_8048b2d_1 = ptrtoint i8* %glob_var_80576a3_1345155010 to i32
	store i32 %conv_8048b2d_1, i32* %stack_var_-28

	;8048b34	1110100010001011110011100000000000000000	e8 8b ce 00 00
	;CALL {52875}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_8048b34 = add i32 52875, 0 ; used signed value. Unsigned value: 52875
	%u1_8048b34 = add i32 134515508, 0	; Assign current PC
	%_d_8048b34 = add i32 5, 0
	%u2_8048b34 = add i32 %u1_8048b34, %_d_8048b34

	%_f_8048b34 = add i32 4, 0
	%u3_8048b34 = load i32, i32* @gpr4
	%u4_8048b34 = add i32 %u2_8048b34, %u0_8048b34

	%_i_8048b34 = add i32 -4, 0
	%u5_8048b34 = add i32 %u3_8048b34, %_i_8048b34

	%conv_8048b34_1 = inttoptr i32 %u2_8048b34 to i32*
	store i32* %conv_8048b34_1, i32** %stack_var_-32
	%_k_8048b34 = add i32 4, 0
	; store of stack pointer to offset -32 into register  @gpr4

	%local_ret_38_8048b34 = call i32  @unknown_80559c4() nounwind
	store i32 %local_ret_38_8048b34, i32* %local_ret_38


	;8048b39	11000111000001000010010010110000011101100000010100001000	c7 04 24 b0 76 05 08
	;MOV DWORD [ {4}  ], {134575792}  decode__instr_grp32_0_m32_uimm32__instr_mov_0_rmxx_uimmxx__MODRM32_0_mem32__SIB_mod00_32_0_base32_index32__base32_sib_mod00__SIB_scaled_index32_none__uimm32__
	%u0_8048b39 = load i32, i32*  @gpr4
	%u1_8048b39 = add i32 134575792, 0 ; used signed value. Unsigned value: 134575792
	%glob_var_80576b0_1345155130 = getelementptr inbounds [8 x i8], [8 x i8]* @glob_var_80576b0, i64 0, i64 0
	%conv_8048b39_1 = ptrtoint i8* %glob_var_80576b0_1345155130 to i32
	store i32 %conv_8048b39_1, i32* %stack_var_-28

	;8048b40	1110100001111111110011100000000000000000	e8 7f ce 00 00
	;CALL {52863}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_8048b40 = add i32 52863, 0 ; used signed value. Unsigned value: 52863
	%u1_8048b40 = add i32 134515520, 0	; Assign current PC
	%_d_8048b40 = add i32 5, 0
	%u2_8048b40 = add i32 %u1_8048b40, %_d_8048b40

	%_f_8048b40 = add i32 4, 0
	%u3_8048b40 = load i32, i32* @gpr4
	%u4_8048b40 = add i32 %u2_8048b40, %u0_8048b40

	%_i_8048b40 = add i32 -4, 0
	%u5_8048b40 = add i32 %u3_8048b40, %_i_8048b40

	%conv_8048b40_1 = inttoptr i32 %u2_8048b40 to i32*
	store i32* %conv_8048b40_1, i32** %stack_var_-32
	%_k_8048b40 = add i32 4, 0
	; store of stack pointer to offset -32 into register  @gpr4

	%local_ret_39_8048b40 = call i32  @unknown_80559c4() nounwind
	store i32 %local_ret_39_8048b40, i32* %local_ret_39


	;8048b45	11000111000001000010010010111000011101100000010100001000	c7 04 24 b8 76 05 08
	;MOV DWORD [ {4}  ], {134575800}  decode__instr_grp32_0_m32_uimm32__instr_mov_0_rmxx_uimmxx__MODRM32_0_mem32__SIB_mod00_32_0_base32_index32__base32_sib_mod00__SIB_scaled_index32_none__uimm32__
	%u0_8048b45 = load i32, i32*  @gpr4
	%u1_8048b45 = add i32 134575800, 0 ; used signed value. Unsigned value: 134575800
	%glob_var_80576b8_1345155250 = getelementptr inbounds [8 x i8], [8 x i8]* @glob_var_80576b8, i64 0, i64 0
	%conv_8048b45_1 = ptrtoint i8* %glob_var_80576b8_1345155250 to i32
	store i32 %conv_8048b45_1, i32* %stack_var_-28

	;8048b4c	1110100001110011110011100000000000000000	e8 73 ce 00 00
	;CALL {52851}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_8048b4c = add i32 52851, 0 ; used signed value. Unsigned value: 52851
	%u1_8048b4c = add i32 134515532, 0	; Assign current PC
	%_d_8048b4c = add i32 5, 0
	%u2_8048b4c = add i32 %u1_8048b4c, %_d_8048b4c

	%_f_8048b4c = add i32 4, 0
	%u3_8048b4c = load i32, i32* @gpr4
	%u4_8048b4c = add i32 %u2_8048b4c, %u0_8048b4c

	%_i_8048b4c = add i32 -4, 0
	%u5_8048b4c = add i32 %u3_8048b4c, %_i_8048b4c

	%conv_8048b4c_1 = inttoptr i32 %u2_8048b4c to i32*
	store i32* %conv_8048b4c_1, i32** %stack_var_-32
	%_k_8048b4c = add i32 4, 0
	; store of stack pointer to offset -32 into register  @gpr4

	%local_ret_40_8048b4c = call i32  @unknown_80559c4() nounwind
	store i32 %local_ret_40_8048b4c, i32* %local_ret_40


	;8048b51	11000111000001000010010011000000011101100000010100001000	c7 04 24 c0 76 05 08
	;MOV DWORD [ {4}  ], {134575808}  decode__instr_grp32_0_m32_uimm32__instr_mov_0_rmxx_uimmxx__MODRM32_0_mem32__SIB_mod00_32_0_base32_index32__base32_sib_mod00__SIB_scaled_index32_none__uimm32__
	%u0_8048b51 = load i32, i32*  @gpr4
	%u1_8048b51 = add i32 134575808, 0 ; used signed value. Unsigned value: 134575808
	%glob_var_80576c0_1345155370 = getelementptr inbounds [9 x i8], [9 x i8]* @glob_var_80576c0, i64 0, i64 0
	%conv_8048b51_1 = ptrtoint i8* %glob_var_80576c0_1345155370 to i32
	store i32 %conv_8048b51_1, i32* %stack_var_-28

	;8048b58	1110100001100111110011100000000000000000	e8 67 ce 00 00
	;CALL {52839}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_8048b58 = add i32 52839, 0 ; used signed value. Unsigned value: 52839
	%u1_8048b58 = add i32 134515544, 0	; Assign current PC
	%_d_8048b58 = add i32 5, 0
	%u2_8048b58 = add i32 %u1_8048b58, %_d_8048b58

	%_f_8048b58 = add i32 4, 0
	%u3_8048b58 = load i32, i32* @gpr4
	%u4_8048b58 = add i32 %u2_8048b58, %u0_8048b58

	%_i_8048b58 = add i32 -4, 0
	%u5_8048b58 = add i32 %u3_8048b58, %_i_8048b58

	%conv_8048b58_1 = inttoptr i32 %u2_8048b58 to i32*
	store i32* %conv_8048b58_1, i32** %stack_var_-32
	%_k_8048b58 = add i32 4, 0
	; store of stack pointer to offset -32 into register  @gpr4

	%local_ret_41_8048b58 = call i32  @unknown_80559c4() nounwind
	store i32 %local_ret_41_8048b58, i32* %local_ret_41


	;8048b5d	11000111000001000010010011001001011101100000010100001000	c7 04 24 c9 76 05 08
	;MOV DWORD [ {4}  ], {134575817}  decode__instr_grp32_0_m32_uimm32__instr_mov_0_rmxx_uimmxx__MODRM32_0_mem32__SIB_mod00_32_0_base32_index32__base32_sib_mod00__SIB_scaled_index32_none__uimm32__
	%u0_8048b5d = load i32, i32*  @gpr4
	%u1_8048b5d = add i32 134575817, 0 ; used signed value. Unsigned value: 134575817
	%glob_var_80576c9_1345155490 = getelementptr inbounds [27 x i8], [27 x i8]* @glob_var_80576c9, i64 0, i64 0
	%conv_8048b5d_1 = ptrtoint i8* %glob_var_80576c9_1345155490 to i32
	store i32 %conv_8048b5d_1, i32* %stack_var_-28

	;8048b64	1110100001011011110011100000000000000000	e8 5b ce 00 00
	;CALL {52827}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_8048b64 = add i32 52827, 0 ; used signed value. Unsigned value: 52827
	%u1_8048b64 = add i32 134515556, 0	; Assign current PC
	%_d_8048b64 = add i32 5, 0
	%u2_8048b64 = add i32 %u1_8048b64, %_d_8048b64

	%_f_8048b64 = add i32 4, 0
	%u3_8048b64 = load i32, i32* @gpr4
	%u4_8048b64 = add i32 %u2_8048b64, %u0_8048b64

	%_i_8048b64 = add i32 -4, 0
	%u5_8048b64 = add i32 %u3_8048b64, %_i_8048b64

	%conv_8048b64_1 = inttoptr i32 %u2_8048b64 to i32*
	store i32* %conv_8048b64_1, i32** %stack_var_-32
	%_k_8048b64 = add i32 4, 0
	; store of stack pointer to offset -32 into register  @gpr4

	%local_ret_42_8048b64 = call i32  @unknown_80559c4() nounwind
	store i32 %local_ret_42_8048b64, i32* %local_ret_42


	;8048b69	11000111000001000010010011100100011101100000010100001000	c7 04 24 e4 76 05 08
	;MOV DWORD [ {4}  ], {134575844}  decode__instr_grp32_0_m32_uimm32__instr_mov_0_rmxx_uimmxx__MODRM32_0_mem32__SIB_mod00_32_0_base32_index32__base32_sib_mod00__SIB_scaled_index32_none__uimm32__
	%u0_8048b69 = load i32, i32*  @gpr4
	%u1_8048b69 = add i32 134575844, 0 ; used signed value. Unsigned value: 134575844
	%glob_var_80576e4_1345155610 = getelementptr inbounds [17 x i8], [17 x i8]* @glob_var_80576e4, i64 0, i64 0
	%conv_8048b69_1 = ptrtoint i8* %glob_var_80576e4_1345155610 to i32
	store i32 %conv_8048b69_1, i32* %stack_var_-28

	;8048b70	1110100001001111110011100000000000000000	e8 4f ce 00 00
	;CALL {52815}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_8048b70 = add i32 52815, 0 ; used signed value. Unsigned value: 52815
	%u1_8048b70 = add i32 134515568, 0	; Assign current PC
	%_d_8048b70 = add i32 5, 0
	%u2_8048b70 = add i32 %u1_8048b70, %_d_8048b70

	%_f_8048b70 = add i32 4, 0
	%u3_8048b70 = load i32, i32* @gpr4
	%u4_8048b70 = add i32 %u2_8048b70, %u0_8048b70

	%_i_8048b70 = add i32 -4, 0
	%u5_8048b70 = add i32 %u3_8048b70, %_i_8048b70

	%conv_8048b70_1 = inttoptr i32 %u2_8048b70 to i32*
	store i32* %conv_8048b70_1, i32** %stack_var_-32
	%_k_8048b70 = add i32 4, 0
	; store of stack pointer to offset -32 into register  @gpr4

	%local_ret_43_8048b70 = call i32  @unknown_80559c4() nounwind
	store i32 %local_ret_43_8048b70, i32* %local_ret_43


	;8048b75	11000111000001000010010011111001011101100000010100001000	c7 04 24 f9 76 05 08
	;MOV DWORD [ {4}  ], {134575865}  decode__instr_grp32_0_m32_uimm32__instr_mov_0_rmxx_uimmxx__MODRM32_0_mem32__SIB_mod00_32_0_base32_index32__base32_sib_mod00__SIB_scaled_index32_none__uimm32__
	%u0_8048b75 = load i32, i32*  @gpr4
	%u1_8048b75 = add i32 134575865, 0 ; used signed value. Unsigned value: 134575865
	%glob_var_80576f9_1345155730 = getelementptr inbounds [10 x i8], [10 x i8]* @glob_var_80576f9, i64 0, i64 0
	%conv_8048b75_1 = ptrtoint i8* %glob_var_80576f9_1345155730 to i32
	store i32 %conv_8048b75_1, i32* %stack_var_-28

	;8048b7c	1110100001000011110011100000000000000000	e8 43 ce 00 00
	;CALL {52803}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_8048b7c = add i32 52803, 0 ; used signed value. Unsigned value: 52803
	%u1_8048b7c = add i32 134515580, 0	; Assign current PC
	%_d_8048b7c = add i32 5, 0
	%u2_8048b7c = add i32 %u1_8048b7c, %_d_8048b7c

	%_f_8048b7c = add i32 4, 0
	%u3_8048b7c = load i32, i32* @gpr4
	%u4_8048b7c = add i32 %u2_8048b7c, %u0_8048b7c

	%_i_8048b7c = add i32 -4, 0
	%u5_8048b7c = add i32 %u3_8048b7c, %_i_8048b7c

	%conv_8048b7c_1 = inttoptr i32 %u2_8048b7c to i32*
	store i32* %conv_8048b7c_1, i32** %stack_var_-32
	%_k_8048b7c = add i32 4, 0
	; store of stack pointer to offset -32 into register  @gpr4

	%local_ret_44_8048b7c = call i32  @unknown_80559c4() nounwind
	store i32 %local_ret_44_8048b7c, i32* %local_ret_44


	;8048b81	11000111000001000010010011110101011101100000010100001000	c7 04 24 f5 76 05 08
	;MOV DWORD [ {4}  ], {134575861}  decode__instr_grp32_0_m32_uimm32__instr_mov_0_rmxx_uimmxx__MODRM32_0_mem32__SIB_mod00_32_0_base32_index32__base32_sib_mod00__SIB_scaled_index32_none__uimm32__
	%u0_8048b81 = load i32, i32*  @gpr4
	%u1_8048b81 = add i32 134575861, 0 ; used signed value. Unsigned value: 134575861
	%glob_var_80576f5_1345155850 = getelementptr inbounds [14 x i8], [14 x i8]* @glob_var_80576f5, i64 0, i64 0
	%conv_8048b81_1 = ptrtoint i8* %glob_var_80576f5_1345155850 to i32
	store i32 %conv_8048b81_1, i32* %stack_var_-28

	;8048b88	1110100000110111110011100000000000000000	e8 37 ce 00 00
	;CALL {52791}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_8048b88 = add i32 52791, 0 ; used signed value. Unsigned value: 52791
	%u1_8048b88 = add i32 134515592, 0	; Assign current PC
	%_d_8048b88 = add i32 5, 0
	%u2_8048b88 = add i32 %u1_8048b88, %_d_8048b88

	%_f_8048b88 = add i32 4, 0
	%u3_8048b88 = load i32, i32* @gpr4
	%u4_8048b88 = add i32 %u2_8048b88, %u0_8048b88

	%_i_8048b88 = add i32 -4, 0
	%u5_8048b88 = add i32 %u3_8048b88, %_i_8048b88

	%conv_8048b88_1 = inttoptr i32 %u2_8048b88 to i32*
	store i32* %conv_8048b88_1, i32** %stack_var_-32
	%_k_8048b88 = add i32 4, 0
	; store of stack pointer to offset -32 into register  @gpr4

	%local_ret_45_8048b88 = call i32  @unknown_80559c4() nounwind
	store i32 %local_ret_45_8048b88, i32* %local_ret_45


	;8048b8d	11000111000001000010010000000011011101110000010100001000	c7 04 24 03 77 05 08
	;MOV DWORD [ {4}  ], {134575875}  decode__instr_grp32_0_m32_uimm32__instr_mov_0_rmxx_uimmxx__MODRM32_0_mem32__SIB_mod00_32_0_base32_index32__base32_sib_mod00__SIB_scaled_index32_none__uimm32__
	%u0_8048b8d = load i32, i32*  @gpr4
	%u1_8048b8d = add i32 134575875, 0 ; used signed value. Unsigned value: 134575875
	%glob_var_8057703_1345155970 = getelementptr inbounds [15 x i8], [15 x i8]* @glob_var_8057703, i64 0, i64 0
	%conv_8048b8d_1 = ptrtoint i8* %glob_var_8057703_1345155970 to i32
	store i32 %conv_8048b8d_1, i32* %stack_var_-28

	;8048b94	1110100000101011110011100000000000000000	e8 2b ce 00 00
	;CALL {52779}  decode__instr_grpxx_op1_rel32__instr_call_relxx__op1_rel32__
	%u0_8048b94 = add i32 52779, 0 ; used signed value. Unsigned value: 52779
	%u1_8048b94 = add i32 134515604, 0	; Assign current PC
	%_d_8048b94 = add i32 5, 0
	%u2_8048b94 = add i32 %u1_8048b94, %_d_8048b94

	%_f_8048b94 = add i32 4, 0
	%u3_8048b94 = load i32, i32* @gpr4
	%u4_8048b94 = add i32 %u2_8048b94, %u0_8048b94

	%_i_8048b94 = add i32 -4, 0
	%u5_8048b94 = add i32 %u3_8048b94, %_i_8048b94

	%conv_8048b94_1 = inttoptr i32 %u2_8048b94 to i32*
	store i32* %conv_8048b94_1, i32** %stack_var_-32
	%_k_8048b94 = add i32 4, 0
	; store of stack pointer to offset -32 into register  @gpr4

	%local_ret_46_8048b94 = call i32  @unknown_80559c4() nounwind
	store i32 %local_ret_46_8048b94, i32* %local_ret_46


	;8048b99	100000111100010000011100	83 c4 1c
	;ADD {4}, {28}  decode__instr_grpxx_0_r32_simm8__instr_add_0_rmxx_simm8__MODRMxx_mod11_0_reg32__gpr32__simm8__
	%u0_8048b99 = add i8 28, 0 ; used signed value. Unsigned value: 28
	%u1_8048b99 = sext i8 %u0_8048b99 to i32
	%u2_8048b99 = load i32, i32*  @gpr4
	%_b_subinst_5_8048b99 = add i32 15, 0
	%u0_subinst_5_8048b99 = and i32 %u2_8048b99, %_b_subinst_5_8048b99

	%_d_subinst_5_8048b99 = add i32 15, 0
	%u1_subinst_5_8048b99 = and i32 %u1_8048b99, %_d_subinst_5_8048b99

	%u2_subinst_5_8048b99 = add i32 %u1_subinst_5_8048b99, %u0_subinst_5_8048b99

	%_g_subinst_5_8048b99 = add i32 15, 0
	%u3_8048b99 = icmp ugt i32 %u2_subinst_5_8048b99, %_g_subinst_5_8048b99
	%_f_8048b99 = add i32 0, 0
	store i1 %u3_8048b99, i1*  @af0	; store to i1 register, should we ignore it? But than it causes problems, see #153
	; carry_add
	%cadd_ab_0_8048b99 = add i32 %u2_8048b99, %u1_8048b99
	%u4_8048b99 = icmp ult i32 %cadd_ab_0_8048b99, %u2_8048b99

	%_h_8048b99 = add i32 0, 0
	store i1 %u4_8048b99, i1*  @cf0	; store to i1 register, should we ignore it? But than it causes problems, see #153
	; overflow_add is a little bit more complicated, so it contains more code
	%add_ab_1_8048b99 = add i32 %u2_8048b99, %u1_8048b99
	%xor_aab_1_8048b99 = xor i32 %u2_8048b99, %add_ab_1_8048b99
	%xor_bab_1_8048b99 = xor i32 %u1_8048b99, %add_ab_1_8048b99
	%and_aabbab_1_8048b99 = and i32 %xor_aab_1_8048b99, %xor_bab_1_8048b99
	%u5_8048b99 = icmp slt i32 %and_aabbab_1_8048b99, 0

	%_j_8048b99 = add i32 0, 0
	store i1 %u5_8048b99, i1*  @of0	; store to i1 register, should we ignore it? But than it causes problems, see #153
	%u6_8048b99 = add i32 %u2_8048b99, %u1_8048b99

	%_b_subinst_6_8048b99 = add i32 0, 0
	%u0_subinst_6_8048b99 = icmp eq i32 %u6_8048b99, %_b_subinst_6_8048b99
	%_d_subinst_6_8048b99 = add i32 0, 0
	store i1 %u0_subinst_6_8048b99, i1*  @zf0	; store to i1 register, should we ignore it? But than it causes problems, see #153
	%_e_subinst_6_8048b99 = add i32 0, 0
	%u1_subinst_6_8048b99 = icmp slt i32 %u6_8048b99, %_e_subinst_6_8048b99
	%_g_subinst_6_8048b99 = add i32 0, 0
	store i1 %u1_subinst_6_8048b99, i1*  @sf0	; store to i1 register, should we ignore it? But than it causes problems, see #153
	%u2_subinst_6_8048b99 = trunc i32 %u6_8048b99 to i8
	%parity_odd_bit_cnt_2_8048b99 = call i8 @llvm.ctpop.i8( i8 %u2_subinst_6_8048b99 ) nounwind
	%parity_odd_mod_2_8048b99 = urem i8 %parity_odd_bit_cnt_2_8048b99, 2
	%u3_subinst_6_8048b99 = icmp eq i8 1, %parity_odd_mod_2_8048b99

	%_j_subinst_6_8048b99 = add i32 0, 0
	store i1 %u3_subinst_6_8048b99, i1*  @pf0	; store to i1 register, should we ignore it? But than it causes problems, see #153
	; store of stack pointer to offset 0 into register  @gpr4


	;8048b9c	11000011	c3
	;RET  decode__instr_ret_nearxx__
	%_b_8048b9c = add i32 4, 0
	%u0_8048b9c = load i32, i32* @gpr4
	%u1_8048b9c = load i32, i32* %stack_var_0
	%_e_8048b9c = add i32 4, 0
	%u2_8048b9c = add i32 %u0_8048b9c, %_e_8048b9c

	%_g_8048b9c = add i32 4, 0
	; ; we ignore this assignment of stack pointer, because this is the last BB with no follower

	ret void


	;8048b9d	10010000	90
	;NOP  decode__instr_nop_grpxx_op0_r32__instr_nop__	 Comment: "Instruction has no effect. Instruction removed in extractor pass 'Semantics printing'."
	; Artificially added return to ensure that functions ends with return
	ret void


}

; ------------ Functions info ------------
; void function_8048960()        addr: 8048960


; Entry point from input file: 8056b1c

; Info: Total code size: 696 bytes
; Info: Decoder 0:
;	Instruction length:   8
;		Groups:   4
;		Instructions in groups:    55
;	Instruction length:  16
;		Groups:  15
;		Instructions in groups:   703
;	Instruction length:  24
;		Groups:  62
;		Instructions in groups:  3691
;	Instruction length:  32
;		Groups:  81
;		Instructions in groups:  5091
;	Instruction length:  40
;		Groups:  71
;		Instructions in groups:  2072
;	Instruction length:  48
;		Groups:  86
;		Instructions in groups:  1271
;	Instruction length:  56
;		Groups:  67
;		Instructions in groups:  2787
;	Instruction length:  64
;		Groups:  42
;		Instructions in groups:  2508
;	Instruction length:  72
;		Groups:  39
;		Instructions in groups:   536
;	Instruction length:  80
;		Groups:  36
;		Instructions in groups:   188
;	Instruction length:  88
;		Groups:  12
;		Instructions in groups:    88
;	Instructions in decoder: 18990

;	Decoded instructions:        152
;	Undecoded instructions:        0
