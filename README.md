---

# **Sistema de Gerenciamento de Usuários e Relatórios**

Este projeto implementa um sistema modular e flexível de gerenciamento de usuários, notificações e geração de relatórios, utilizando os padrões de projeto **Observer** e **Decorator**.

---

## **Objetivo do Projeto**
Demonstrar a aplicação prática de dois padrões de design (Observer e Decorator) em um sistema funcional. O sistema:
1. Permite o registro de usuários e notifica diferentes serviços sobre novos registros.
2. Gera relatórios personalizáveis com formatações dinâmicas.

---

## **Funcionalidades**
1. **Registro de Usuários**:
   - Adiciona novos usuários ao sistema.
   - Notifica serviços cadastrados, como envio de e-mails e registros em logs.

2. **Notificações**:
   - Utiliza o padrão **Observer** para enviar notificações a múltiplos observadores sempre que um evento ocorre.

3. **Geração de Relatórios**:
   - Usa o padrão **Decorator** para personalizar relatórios, adicionando cabeçalhos, rodapés e outros elementos dinamicamente.

---

## **Estrutura do Projeto**
O projeto é composto pelos seguintes módulos:

### **1. Registro de Usuários (Observer)**
- **`UserRegistry`**: Classe principal que registra usuários e notifica observadores.
- **Observadores**:
  - **`EmailNotifier`**: Envia notificações por e-mail.
  - **`LogNotifier`**: Registra logs no sistema.

### **2. Relatórios (Decorator)**
- **`SimpleReport`**: Classe base para relatórios simples.
- **Decoradores**:
  - **`HeaderDecorator`**: Adiciona um cabeçalho ao relatório.
  - **`FooterDecorator`**: Adiciona um rodapé ao relatório.

---

## **Como Executar o Projeto**
### **Pré-requisitos**
- Python 3.8 ou superior instalado no sistema.

### **Passos**
1. Clone o repositório:
   ```bash
   git clone https://github.com/Waxier17/observer_decorator.git
   cd observer_decorator
   ```
2. Execute o arquivo principal:
   ```bash
   python main.py
   ```

3. **Saída esperada**:
   - Notificações ao registrar novos usuários.
   - Exibição de um relatório formatado.

---

## **Exemplo de Saída**
Após adicionar dois usuários e gerar um relatório, o sistema produzirá uma saída como esta:

### **Notificações**:
```
Email enviado: Novo usuário registrado: Alice
Log registrado: Novo usuário registrado: Alice
Email enviado: Novo usuário registrado: Bob
Log registrado: Novo usuário registrado: Bob
```

### **Relatório Final**:
```
Cabeçalho: Relatório de Usuários
Relatório básico
Rodapé: Fim do Relatório
```

---

## **Tecnologias Utilizadas**
- **Linguagem**: Python
- **Paradigma**: Programação Orientada a Objetos (POO)
- **Padrões de Projeto**: Observer e Decorator

---

## **Autores**
- Guilherme Andersen Correa
---

## **O que Aprendemos**
1. **Observer**: Como implementar um sistema de notificações flexível e escalável.
2. **Decorator**: Como adicionar funcionalidades a relatórios de maneira modular.

---