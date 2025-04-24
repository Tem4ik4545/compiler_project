section .data
newline db 10, 0
format db "%d", 10, 0
format_str db "%s", 10, 0
True dq 1
False dq 0
x dq 0
y dq 0
t0 dq 0
t1 dq 0
t2 dq 0
t3 dq 0
t4 dq 0
i dq 0
t5 dq 0
t6 dq 0
j dq 0
t7 dq 0
t8 dq 0
v dq 0
t9 dq 0
t10 dq 0
t11 dq 0
a dq 0
b dq 0
str_0 db "Hello, MyLang!", 0

section .text
extern printf
extern getchar
global _start
func_add:
push rbp
mov rbp, rsp
mov qword [rel a], rdi
mov qword [rel b], rsi
_start:
mov rdi, 1
mov rsi, 2
call func_add
mov rsi, rax
mov rdi, format
xor rax, rax
call printf
mov rdi, format_str
lea rsi, [rel str_0]
xor rax, rax
call printf
mov rsi, 42
mov rdi, format
xor rax, rax
call printf
mov rax, 5
mov qword [rel x], rax
mov rax, 10
mov qword [rel y], rax
mov rax, qword [rel x]
add rax, qword [rel y]
mov qword [rel t0], rax
mov rsi, qword [rel t0]
mov rdi, format
xor rax, rax
call printf
mov rax, qword [rel x]
cmp rax, 0
sete al
movzx rax, al
mov qword [rel t1], rax
mov rax, qword [rel t1]
cmp rax, 0
sete al
movzx rax, al
mov qword [rel t2], rax
mov rax, qword [rel y]
cmp rax, 0
sete al
movzx rbx, al
mov rax, qword [rel t2]
cmp rax, 0
sete al
movzx rax, al
and rax, rbx
mov qword [rel t3], rax
mov rax, qword [rel x]
cmp rax, qword [rel t3]
setl al
movzx rax, al
mov qword [rel t4], rax
mov rax, qword [rel t4]
cmp rax, 0
je else_0
mov rsi, 1
mov rdi, format
xor rax, rax
call printf
jmp endif_1
else_0:
mov rsi, 0
mov rdi, format
xor rax, rax
call printf
endif_1:
mov rax, 0
mov qword [rel i], rax
while_start_2:
mov rax, qword [rel i]
cmp rax, 3
setl al
movzx rax, al
mov qword [rel t5], rax
mov rax, qword [rel t5]
cmp rax, 0
je while_end_3
mov rsi, 0
mov rdi, format
xor rax, rax
call printf
mov rax, qword [rel i]
add rax, 1
mov qword [rel t6], rax
mov rax, qword [rel t6]
mov qword [rel i], rax
jmp while_start_2
while_end_3:
mov rax, 0
mov qword [rel j], rax
for_start_4:
mov rax, qword [rel j]
cmp rax, 3
setl al
movzx rax, al
mov qword [rel t7], rax
mov rax, qword [rel t7]
cmp rax, 0
je for_end_5
mov rsi, 0
mov rdi, format
xor rax, rax
call printf
mov rax, qword [rel j]
add rax, 1
mov qword [rel t8], rax
mov rax, qword [rel t8]
mov qword [rel j], rax
jmp for_start_4
for_end_5:
try_6:
mov rsi, 123
mov rdi, format
xor rax, rax
call printf
jmp end_try_8
catch_7:
mov rsi, 999
mov rdi, format
xor rax, rax
call printf
end_try_8:
mov rax, 2
mov qword [rel v], rax
mov rax, qword [rel v]
cmp rax, 1
sete al
movzx rax, al
mov qword [rel t9], rax
mov rax, qword [rel t9]
cmp rax, 0
jne case_0_10
mov rax, qword [rel v]
cmp rax, 2
sete al
movzx rax, al
mov qword [rel t10], rax
mov rax, qword [rel t10]
cmp rax, 0
jne case_1_11
jmp default_case_12
case_0_10:
mov rsi, 11
mov rdi, format
xor rax, rax
call printf
jmp end_match_9
case_1_11:
mov rsi, 22
mov rdi, format
xor rax, rax
call printf
jmp end_match_9
default_case_12:
mov rsi, 33
mov rdi, format
xor rax, rax
call printf
end_match_9:
mov rax, qword [rel a]
add rax, qword [rel b]
mov qword [rel t11], rax
mov rax, qword [rel t11]
pop rbp
ret
call getchar
mov rax, 60
xor rdi, rdi
syscall