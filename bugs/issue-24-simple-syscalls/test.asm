; compile by:
; nasm -f elf test.asm && ld -m elf_i386 test.o -o test

BITS 32
global _start

section .text
_start:
	mov eax, 5 ; sys_open
	mov ebx, fileName
	mov ecx, 66 ; creation flags: O_RDWR | O_CREAT
	mov edx, 292 ; file mode: S_IRUSR | S_IRGRP | S_IROTH
	int 0x80 ; syscall, eax now contains file descriptor

	mov ebx, eax
	mov eax, 4 ; sys_write
	mov ecx, payload
	mov edx, payloadSize
	int 0x80

	mov eax, 1
	int 0x80
fileName:
    	db  "/tmp/myfile",0
payload:
	db "malicious payload here", 0ah, 0
payloadSize: equ $-payload
