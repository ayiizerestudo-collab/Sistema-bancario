# Sistema Bancário em Python — POO

Este projeto apresenta um sistema bancário simples, desenvolvido em Python com Programação Orientada a Objetos (POO), seguindo um modelo de classes UML para facilitar o entendimento e futuras expansões.

## 📦 Estrutura de Classes

```python
from abc import ABC, abstractmethod
from datetime import datetime

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class Conta:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0
        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append((datetime.now(), f"Depósito: +R${valor:.2f}"))
            return True
        return False

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.extrato.append((datetime.now(), f"Saque: -R${valor:.2f}"))
            return True
        return False

    def mostrar_extrato(self):
        print(f"Extrato da Conta {self.numero} - Cliente: {self.cliente.nome}")
        for data, operacao in self.extrato:
            print(f"{data.strftime('%d/%m/%Y %H:%M:%S')} - {operacao}")
        print(f"Saldo atual: R${self.saldo:.2f}")

class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []
        self.contas = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def criar_conta(self, cliente):
        numero = len(self.contas) + 1
        conta = Conta(numero, cliente)
        cliente.adicionar_conta(conta)
        self.contas.append(conta)
        return conta
```

## 🚀 Exemplo de uso

```python
banco = Banco("Banco Copilot")

rafael = Cliente("Rafael", "123.456.789-00")
banco.adicionar_cliente(rafael)

conta_rafael = banco.criar_conta(rafael)
conta_rafael.depositar(500)
conta_rafael.sacar(150)
conta_rafael.mostrar_extrato()
```

## ✨ Principais Conceitos Envolvidos

- Encapsulamento
- Relacionamento entre classes (Banco, Cliente, Conta)
- Métodos de instância
- Uso de listas para compor objetos

---

Sinta-se à vontade para expandir esse projeto — adicione operações, tipos de conta, autenticação, etc.!