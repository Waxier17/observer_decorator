from abc import ABC, abstractmethod

# Padrão Observer
class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        pass

class Subject(ABC):
    def __init__(self):
        self._observers = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self, message: str):
        for observer in self._observers:
            observer.update(message)

class UserRegistry(Subject):
    def __init__(self):
        super().__init__()
        self._users = []

    def add_user(self, user: str):
        self._users.append(user)
        self.notify(f"Novo usuário registrado: {user}")

    def list_users(self):
        return self._users

class EmailNotifier(Observer):
    def update(self, message: str):
        print(f"Email enviado: {message}")

class LogNotifier(Observer):
    def update(self, message: str):
        print(f"Log registrado: {message}")

# Padrão Decorator
class Report(ABC):
    @abstractmethod
    def display(self) -> str:
        pass

class SimpleReport(Report):
    def display(self) -> str:
        return "Relatório básico"

class ReportDecorator(Report):
    def __init__(self, report: Report):
        self._report = report

    def display(self) -> str:
        return self._report.display()

class HeaderDecorator(ReportDecorator):
    def display(self) -> str:
        return f"Cabeçalho: Relatório de Usuários\n{self._report.display()}"

class FooterDecorator(ReportDecorator):
    def display(self) -> str:
        return f"{self._report.display()}\nRodapé: Fim do Relatório"

# Testando o sistema
if __name__ == "__main__":
    # Configurando o sistema de notificações
    registry = UserRegistry()
    email_notifier = EmailNotifier()
    log_notifier = LogNotifier()

    registry.attach(email_notifier)
    registry.attach(log_notifier)

    # Registrando usuários
    registry.add_user("Alice")
    registry.add_user("Bob")

    # Gerando relatórios formatados
    basic_report = SimpleReport()
    report_with_header = HeaderDecorator(basic_report)
    full_report = FooterDecorator(report_with_header)

    print("\nRelatório Final:\n")
    print(full_report.display())
