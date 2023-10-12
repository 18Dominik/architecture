# Demonstrating the SOLID Principles
## Interface Segregation Principle (ISP): Clint should only depend on the interfaces they utilize. For example, if a client wants to send emails, then it should depend on an interface like ‘MessageSender’, not like ‘SmptClient’ that can do more than just sending emails.
## The Interface Segregation Principle (ISP) suggests that clients should not be forced to depend on interfaces they do not use.
## -> Best practices for interfaces: Easy to lean - easy to use, atomic information units, fit the needs of the component (not more, not less)

from abc import ABC, abstractmethod

# Interface for sending emails
class EmailSender(ABC):
    @abstractmethod
    def send_email(self, recipient, subject, message):
        pass

# Concrete implementation for sending emails using SMTP
class SmtpEmailSender(EmailSender):
    def send_email(self, recipient, subject, message):
        print(f"Sending email via SMTP to {recipient} with subject '{subject}' and message: {message}")

# Concrete implementation for sending emails using a REST API
class RestApiEmailSender(EmailSender):
    def send_email(self, recipient, subject, message):
        print(f"Sending email via REST API to {recipient} with subject '{subject}' and message: {message}")

# Client class that uses the EmailSender interface. EmailClient holds an instance of an EmailSender
class EmailClient:
    """
    By following this design, you can easily switch between different email-sending mechanisms by creating new classes that implement the EmailSender interface without changing the EmailClient class. 
    This adheres to the Open-Closed Principle.
    It also ensures that EmailClient follows the Interface Segregation Principle as it depends only on the relevant interface for its specific needs.
    """
    def __init__(self, sender): #sender is a concrete instance of EmailSender (either Smtp or Rest)
        """principle of composition over inheritance. 
        In object-oriented design, composition is a way of building complex functionality by combining smaller, more focused classes (or objects) rather than using inheritance to create a hierarchy.
        """
        self.sender = sender # Composite "EmailClient" HAS A Component "EmailSender"

    def send_email(self, recipient, subject, message):
        self.sender.send_email(recipient, subject, message)

# Usage
smtp_sender = SmtpEmailSender()
rest_api_sender = RestApiEmailSender()

smtp_client = EmailClient(smtp_sender)
rest_api_client = EmailClient(rest_api_sender)

smtp_client.send_email("recipient@example.com", "Hello", "This is an email sent via SMTP.")
rest_api_client.send_email("recipient@example.com", "Hello", "This is an email sent via REST API.")

#Inhertitance vs. Composition:
#Inheritance, creates a tight coupling between classes, making them less flexible and more challenging to extend or modify. 
# Composition, as demonstrated in the code, promotes a more modular and flexible design.





