section .data
newline    db 10, 0
format     db "%d", 10, 0
format_float db "%.6f", 10, 0
format_str db "%s", 10, 0
div_zero_err db "Error: division by zero", 10, 0
True dq 1
False dq 0
x dq 0
y dq 0
t0 dq 0
z dq 0
t1 dq 0
t2 dq 0
t3 dq 0
t4 dq 0
t5 dq 0
i dq 0
t6 dq 0
t7 dq 0
j dq 0
t8 dq 0
t9 dq 0
v dq 0
t10 dq 0
t11 dq 0
a dq 0
b dq 0
t12 dq 0
t13 dq 0
res dq 0
t14 dq 0
t15 dq 0
t16 dq 0
total dq 0
align 4
c dd 0.0
d dq 0
e dq 0
align 4
f dd 0.0
g dq 0
t17 dq 0
t18 dq 0
t19 dq 0
t20 dq 0
t21 dq 0
t22 dq 0
t23 dq 0
r dq 0
t24 dq 0
t25 dq 0
t26 dq 0
t27 dq 0
t28 dq 0
t29 dq 0
t30 dq 0
t31 dq 0
t32 dq 0
t33 dq 0
t34 dq 0
t35 dq 0
k dq 0
l dq 0
t36 dq 0
t37 dq 0
t38 dq 0
t39 dq 0
t40 dq 0
align 4
m dd 0.0
align 4
t41 dd 0.0
align 4
t42 dd 0.0
str_0 db "Hello, MyLang!", 0
str_1 db "yes", 0
align 4
float_0 dd 3.1415926
align 4
float_1 dd 2.0
align 4
float_2 dd 0.0
section .text
default rel
extern printf
extern ExitProcess
global main
func_add:
    push rbp
    mov rbp, rsp
    mov rax, [rel a]
    add rax, [rel b]
    mov [rel t12], rax
    mov rax, [rel t12]
    mov rsp, rbp
    pop rbp
    ret
func_mul:
    push rbp
    mov rbp, rsp
    mov rax, [rel a]
    imul rax, [rel b]
    mov [rel t14], rax
    mov rax, [rel t14]
    mov rsp, rbp
    pop rbp
    ret
func_total7:
    push rbp
    mov rbp, rsp
    mov rax, [rel a]
    add rax, [rel b]
    mov [rel t17], rax
    mov rax, [rel t17]
    add rax, [rel c]
    mov [rel t18], rax
    mov rax, [rel t18]
    add rax, [rel d]
    mov [rel t19], rax
    mov rax, [rel t19]
    add rax, [rel e]
    mov [rel t20], rax
    mov rax, [rel t20]
    add rax, [rel f]
    mov [rel t21], rax
    mov rax, [rel t21]
    add rax, [rel g]
    mov [rel t22], rax
    mov rax, [rel t22]
    mov rsp, rbp
    pop rbp
    ret
main:
    sub rsp, 32
    sub rsp, 32
    lea rdx, [rel str_0]
    mov rcx, format_str
    xor rax, rax
    call printf
    add rsp, 32
    sub rsp, 32
    mov rdx, 42
    mov rcx, format
    xor rax, rax
    call printf
    add rsp, 32
    mov rax, 5
    mov [rel x], rax
    mov rax, 10
    mov [rel y], rax
    mov rax, [rel x]
    add rax, [rel y]
    mov [rel t0], rax
    mov rax, [rel t0]
    mov [rel z], rax
    sub rsp, 32
    mov rdx, [rel z]
    mov rcx, format
    xor rax, rax
    call printf
    add rsp, 32
    mov rax, [rel x]
    cmp rax, [rel y]
    setl al
    movzx rax, al
    mov [rel t1], rax
    mov rax, [rel x]
    cmp rax, 0
    sete al
    movzx rax, al
    mov [rel t2], rax
    mov rax, [rel t2]
    cmp rax, 0
    sete al
    movzx rax, al
    mov [rel t3], rax
    mov rax, [rel t1]
    cmp rax, 0
    je skip_0
    mov rax, [rel t3]
    cmp rax, 0
    setne al
    jmp end_1
skip_0:
    mov al, 0
end_1:
    movzx rax, al
    mov [rel t4], rax
    mov rax, [rel t4]
    cmp rax, 0
    sete al
    movzx rax, al
    mov [rel t5], rax
    mov rax, [rel t5]
    test rax, rax
    jne else_0
    sub rsp, 32
    mov rdx, 1
    mov rcx, format
    xor rax, rax
    call printf
    add rsp, 32
    jmp endif_1
else_0:
    sub rsp, 32
    mov rdx, 0
    mov rcx, format
    xor rax, rax
    call printf
    add rsp, 32
endif_1:
    mov rax, 0
    mov [rel i], rax
while_start_2:
    mov rax, [rel i]
    cmp rax, 3
    setl al
    movzx rax, al
    mov [rel t6], rax
    mov rax, [rel t6]
    test rax, rax
    je  while_end_3
    sub rsp, 32
    mov rdx, [rel i]
    mov rcx, format
    xor rax, rax
    call printf
    add rsp, 32
    mov rax, [rel i]
    add rax, 1
    mov [rel t7], rax
    mov rax, [rel t7]
    mov [rel i], rax
    jmp while_start_2
while_end_3:
    mov rax, 0
    mov [rel j], rax
for_start_4:
    mov rax, [rel j]
    cmp rax, 3
    setl al
    movzx rax, al
    mov [rel t8], rax
    mov rax, [rel t8]
    test rax, rax
    je  for_end_5
    sub rsp, 32
    mov rdx, [rel j]
    mov rcx, format
    xor rax, rax
    call printf
    add rsp, 32
    mov rax, [rel j]
    add rax, 1
    mov [rel t9], rax
    mov rax, [rel t9]
    mov [rel j], rax
    jmp for_start_4
for_end_5:
try_6:
    sub rsp, 32
    mov rdx, 123
    mov rcx, format
    xor rax, rax
    call printf
    add rsp, 32
    jmp end_try_8
catch_7:
    sub rsp, 32
    mov rdx, 999
    mov rcx, format
    xor rax, rax
    call printf
    add rsp, 32
end_try_8:
    mov rax, 2
    mov [rel v], rax
    mov rax, [rel v]
    cmp rax, 1
    sete al
    movzx rax, al
    mov [rel t10], rax
    mov rax, [rel t10]
    test rax, rax
    jne case_0_10
    mov rax, [rel v]
    cmp rax, 2
    sete al
    movzx rax, al
    mov [rel t11], rax
    mov rax, [rel t11]
    test rax, rax
    jne case_1_11
    jmp default_case_12
case_0_10:
    sub rsp, 32
    mov rdx, 11
    mov rcx, format
    xor rax, rax
    call printf
    add rsp, 32
    jmp end_match_9
case_1_11:
    sub rsp, 32
    mov rdx, 22
    mov rcx, format
    xor rax, rax
    call printf
    add rsp, 32
    jmp end_match_9
default_case_12:
    sub rsp, 32
    mov rdx, 33
    mov rcx, format
    xor rax, rax
    call printf
    add rsp, 32
end_match_9:
    mov rcx, 7
    mov rdx, 8
    mov [rel a], rcx
    mov [rel b], rdx
    sub rsp, 32
    call func_add
    add rsp, 32
    mov [rel t13], rax
    mov rax, [rel t13]
    mov [rel res], rax
    sub rsp, 32
    mov rdx, [rel res]
    mov rcx, format
    xor rax, rax
    call printf
    add rsp, 32
    mov rcx, 2
    mov rdx, 3
    mov [rel a], rcx
    mov [rel b], rdx
    sub rsp, 32
    call func_mul
    add rsp, 32
    mov [rel t15], rax
    mov rcx, [rel t15]
    mov rdx, 4
    mov [rel a], rcx
    mov [rel b], rdx
    sub rsp, 32
    call func_add
    add rsp, 32
    mov [rel t16], rax
    mov rax, [rel t16]
    mov [rel total], rax
    sub rsp, 32
    mov rdx, [rel total]
    mov rcx, format
    xor rax, rax
    call printf
    add rsp, 32
    mov rcx, 1
    mov rdx, 2
    mov r8, 3
    mov r9, 4
    mov qword [rsp + 32], 5
    mov qword [rsp + 40], 6
    mov qword [rsp + 48], 7
    mov [rel a], rcx
    mov [rel b], rdx
    mov [rel c], r8
    mov [rel d], r9
    mov rax, qword [rsp + 32]
    mov [rel e], rax
    mov rax, qword [rsp + 40]
    mov [rel f], rax
    mov rax, qword [rsp + 48]
    mov [rel g], rax
    sub rsp, 48
    call func_total7
    add rsp, 48
    mov [rel t23], rax
    mov rax, [rel t23]
    mov [rel r], rax
    sub rsp, 32
    mov rdx, [rel r]
    mov rcx, format
    xor rax, rax
    call printf
    add rsp, 32
    mov rax, 1
    mov [rel a], rax
    mov rax, 0
    mov [rel b], rax
    mov rax, [rel a]
    cmp rax, 1
    sete al
    movzx rax, al
    mov [rel t24], rax
    mov rax, [rel b]
    cmp rax, 1
    sete al
    movzx rax, al
    mov [rel t25], rax
    mov rax, [rel t24]
    cmp rax, 0
    jne skip_2
    mov rax, [rel t25]
    cmp rax, 0
    setne al
    jmp end_3
skip_2:
    mov al, 1
end_3:
    movzx rax, al
    mov [rel t26], rax
    mov rax, [rel t26]
    cmp rax, 0
    sete al
    movzx rax, al
    mov [rel t27], rax
    mov rax, [rel t27]
    test rax, rax
    jne else_13
    sub rsp, 32
    mov rdx, 100
    mov rcx, format
    xor rax, rax
    call printf
    add rsp, 32
    jmp endif_14
else_13:
endif_14:
    mov rax, [rel a]
    cmp rax, 0
    sete al
    movzx rax, al
    mov [rel t28], rax
    mov rax, [rel t28]
    cmp rax, 0
    sete al
    movzx rax, al
    mov [rel t29], rax
    mov rax, [rel t29]
    cmp rax, 0
    sete al
    movzx rax, al
    mov [rel t30], rax
    mov rax, [rel t30]
    test rax, rax
    jne else_15
    sub rsp, 32
    mov rdx, 200
    mov rcx, format
    xor rax, rax
    call printf
    add rsp, 32
    jmp endif_16
else_15:
endif_16:
    mov rax, [rel x]
    cmp rax, 0
    setg al
    movzx rax, al
    mov [rel t31], rax
    mov rax, [rel y]
    cmp rax, 5
    setne al
    movzx rax, al
    mov [rel t32], rax
    mov rax, [rel t31]
    cmp rax, 0
    je skip_4
    mov rax, [rel t32]
    cmp rax, 0
    setne al
    jmp end_5
skip_4:
    mov al, 0
end_5:
    movzx rax, al
    mov [rel t33], rax
    mov rax, [rel t33]
    cmp rax, 0
    sete al
    movzx rax, al
    mov [rel t34], rax
    mov rax, [rel t34]
    test rax, rax
    jne else_17
    sub rsp, 32
    mov rdx, 300
    mov rcx, format
    xor rax, rax
    call printf
    add rsp, 32
    jmp endif_18
else_17:
endif_18:
    mov rcx, 1
    mov rdx, 2
    mov [rel a], rcx
    mov [rel b], rdx
    sub rsp, 32
    call func_add
    add rsp, 32
    mov [rel t35], rax
    mov rax, [rel True]
    mov [rel k], rax
    mov rax, [rel False]
    mov [rel l], rax
    mov rax, [rel l]
    cmp rax, 0
    sete al
    movzx rax, al
    mov [rel t36], rax
    mov rax, [rel k]
    cmp rax, 0
    je skip_6
    mov rax, [rel t36]
    cmp rax, 0
    setne al
    jmp end_7
skip_6:
    mov al, 0
end_7:
    movzx rax, al
    mov [rel t37], rax
    mov rax, [rel t37]
    cmp rax, 0
    jne skip_8
    mov rax, [rel False]
    cmp rax, 0
    setne al
    jmp end_9
skip_8:
    mov al, 1
end_9:
    movzx rax, al
    mov [rel t38], rax
    mov rax, [rel t38]
    cmp rax, 0
    sete al
    movzx rax, al
    mov [rel t39], rax
    mov rax, [rel t39]
    test rax, rax
    jne else_19
    sub rsp, 32
    mov rdx, 1
    mov rcx, format
    xor rax, rax
    call printf
    add rsp, 32
    jmp endif_20
else_19:
endif_20:
    mov rax, [rel True]
    cmp rax, 0
    sete al
    movzx rax, al
    mov [rel t40], rax
    mov rax, [rel t40]
    test rax, rax
    jne else_21
    sub rsp, 32
    lea rdx, [rel str_1]
    mov rcx, format_str
    xor rax, rax
    call printf
    add rsp, 32
    jmp endif_22
else_21:
endif_22:
    movss xmm0, [rel float_0]
    movss [rel m], xmm0
    movss xmm0, [rel m]
    movss xmm1, [rel float_1]
    movss xmm2, xmm1
    xorps xmm3, xmm3
    ucomiss xmm2, xmm3
    je _float_div_zero
    divss xmm0, xmm1
    movss [rel t41], xmm0
    movss xmm0, [rel t41]
    movss [rel c], xmm0
    sub rsp, 32
    movss xmm0, [rel c]
    cvtss2sd xmm0, xmm0
    movq rdx, xmm0
    mov rcx, format_float
    mov rax, 1
    call printf
    add rsp, 32
    movss xmm0, [rel m]
    movss xmm1, [rel float_2]
    movss xmm2, xmm1
    xorps xmm3, xmm3
    ucomiss xmm2, xmm3
    je _float_div_zero
    divss xmm0, xmm1
    movss [rel t42], xmm0
    movss xmm0, [rel t42]
    movss [rel f], xmm0
    sub rsp, 32
    movss xmm0, [rel f]
    cvtss2sd xmm0, xmm0
    movq rdx, xmm0
    mov rcx, format_float
    mov rax, 1
    call printf
    add rsp, 32
    xor  ecx, ecx
    call ExitProcess
    add  rsp, 32
_float_div_zero:
    sub rsp, 32
    lea rcx, [rel div_zero_err]
    xor rax, rax
    call printf
    call ExitProcess
_int_div_zero:
    sub rsp, 32
    lea rcx, [rel div_zero_err]
    xor rax, rax
    call printf
    call ExitProcess