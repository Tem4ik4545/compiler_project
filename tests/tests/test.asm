section .data
    msg db 'Hello World!', 10, 0   ; \n для сброса буфера

section .text
    extern printf
    extern ExitProcess
    global main

main:
    sub rsp, 40                   ; shadow space + alignment
    mov rcx, msg
    call printf
    add rsp, 40
    xor ecx, ecx
    call ExitProcess