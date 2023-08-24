print("Este es un ejemplo de c—digo para un proyecto con GIT")

x = 15
y = 5

print(f"Resultado de {x} + {y} = {x+y}")

print(f"Resultado de {x} - {y} = {x-y}")
print(f"Resultado de {x} / {y} = {x/y}")


def factorial(n):
    fac = 1
    for i in range(n,1,-1):
        fac *= i
    return fac

print(factorial(5))