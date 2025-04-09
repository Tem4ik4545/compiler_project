section .data
newline db 10, 0
format db "%d", 10, 0
True dq 1
False dq 0
t0 dq 0
a dq 0
b dq 0

section .text
extern printf
global _start
_start:
func_add:
push rbp
mov rbp, rsp
mov qword [a], rdi
mov qword [b], rsi
mov rax, qword [a]
add rax, qword [b]
mov qword [t0], rax
mov rax, qword [t0]
pop rbp
ret
; Exit syscall
mov rax, 60
xor rdi, rdi
syscall