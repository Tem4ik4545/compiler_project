section .data
newline db 10, 0
format db "%d", 10, 0
format_str db "%s", 10, 0
True dq 1
False dq 0
a dq 0
b dq 0
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
str_0 db "Hello, MyLang!", 10, 0

section .text
default rel
extern printf
extern ExitProcess
global main
func_add:
push rbp
mov rbp, rsp
mov [rel a], rcx
mov [rel b], rdx
main:
sub rsp, 40
sub rsp, 40
lea rdx, [rel str_0]
mov rcx, format_str
xor rax, rax
call printf
add rsp, 40
sub rsp, 40
mov rdx, 42
mov rcx, format
xor rax, rax
call printf
add rsp, 40
mov rax, 5
mov qword [rel x], rax
mov rax, 10
mov qword [rel y], rax
mov rax, [rel x]
add rax, [rel y]
mov qword [rel t0], rax
sub rsp, 40
mov rdx, [rel t0]
mov rcx, format
xor rax, rax
call printf
add rsp, 40
mov rax, [rel x]
cmp rax, 0
sete al
movzx rax, al
mov qword [rel t1], rax
mov rax, [rel t1]
cmp rax, 0
sete al
movzx rax, al
mov qword [rel t2], rax
mov rax, [rel y]
mov qword [rel t3], rax
mov rax, [rel x]
cmp rax, [rel t3]
setl al
movzx rax, al
mov qword [rel t4], rax
mov rax, [rel t4]
cmp rax, 0
je else_0
sub rsp, 40
mov rdx, 1
mov rcx, format
xor rax, rax
call printf
add rsp, 40
jmp endif_1
else_0:
sub rsp, 40
mov rdx, 0
mov rcx, format
xor rax, rax
call printf
add rsp, 40
endif_1:
mov rax, 0
mov qword [rel i], rax
while_start_2:
mov rax, [rel i]
cmp rax, 3
setl al
movzx rax, al
mov qword [rel t5], rax
mov rax, [rel t5]
cmp rax, 0
je while_end_3
sub rsp, 40
mov rdx, 0
mov rcx, format
xor rax, rax
call printf
add rsp, 40
mov rax, [rel i]
add rax, 1
mov qword [rel t6], rax
mov rax, [rel t6]
mov qword [rel i], rax
jmp while_start_2
while_end_3:
mov rax, 0
mov qword [rel j], rax
for_start_4:
mov rax, [rel j]
cmp rax, 3
setl al
movzx rax, al
mov qword [rel t7], rax
mov rax, [rel t7]
cmp rax, 0
je for_end_5
sub rsp, 40
mov rdx, 0
mov rcx, format
xor rax, rax
call printf
add rsp, 40
mov rax, [rel j]
add rax, 1
mov qword [rel t8], rax
mov rax, [rel t8]
mov qword [rel j], rax
jmp for_start_4
for_end_5:
try_6:
sub rsp, 40
mov rdx, 123
mov rcx, format
xor rax, rax
call printf
add rsp, 40
jmp end_try_8
catch_7:
sub rsp, 40
mov rdx, 999
mov rcx, format
xor rax, rax
call printf
add rsp, 40
end_try_8:
mov rax, 2
mov qword [rel v], rax
mov rax, [rel v]
cmp rax, 1
sete al
movzx rax, al
mov qword [rel t9], rax
mov rax, [rel t9]
cmp rax, 0
jne case_0_10
mov rax, [rel v]
cmp rax, 2
sete al
movzx rax, al
mov qword [rel t10], rax
mov rax, [rel t10]
cmp rax, 0
jne case_1_11
jmp default_case_12
case_0_10:
sub rsp, 40
mov rdx, 11
mov rcx, format
xor rax, rax
call printf
add rsp, 40
jmp end_match_9
case_1_11:
sub rsp, 40
mov rdx, 22
mov rcx, format
xor rax, rax
call printf
add rsp, 40
jmp end_match_9
default_case_12:
sub rsp, 40
mov rdx, 33
mov rcx, format
xor rax, rax
call printf
add rsp, 40
end_match_9:
mov rax, [rel a]
add rax, [rel b]
mov qword [rel t11], rax
mov rax, [rel t11]
pop rbp
ret
xor ecx, ecx
call ExitProcess
add rsp, 40