# Architecture
This repo focuses on some architectural principles

## SOLID
SOLID, this acronym was coined by Michael Feathers, it represents the five basic principles of object-oriented programming developed by Robert C. Martin (Uncle Bob) (https://blog.cleancoder.com/).

### Single Responsibility Principle
A class should have only one reason to change.

![image](https://github.com/18Dominik/architecture/assets/35842490/8fd27e22-cd7b-4bf9-ad9c-ac6fd3c81d96)
Source: https://accesto.com/blog/solid-php-solid-principles-in-php/

### Open/Closed Principle
Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.

![image](https://github.com/18Dominik/architecture/assets/35842490/c582ea2e-f034-4bea-b6e3-8f9d23c2895e)
Source: https://accesto.com/blog/solid-php-solid-principles-in-php/

### Liskov Substitution Principle
Subtypes must be substitutable for their base types without altering the correctness of the program.

![image](https://github.com/18Dominik/architecture/assets/35842490/7f0c07a3-8c69-4b07-a6aa-a8313c98b1e3)
Source: https://accesto.com/blog/solid-php-solid-principles-in-php/

### Interface Segregation Principle (ISP)
Clients should not be forced to depend on interfaces they do not use.

![image](https://github.com/18Dominik/architecture/assets/35842490/5ac05c4d-f3a4-40fd-8d57-7cfc1e31cbac)
Source: https://accesto.com/blog/solid-php-solid-principles-in-php/

### Dependency Inversion Principle (DIP)
High-level modules should not depend on low-level modules. Both should depend on abstractions. Furthermore, abstractions should not depend on details. Details should depend on abstractions.
Aims to reduce coupling between high-level and low-level modules/concrete implementation in software systems by inverting the traditional dependency hierarchy
-  High-Level Modules Should Not Depend on Low-Level Modules/concrete implementation. Instead, both should depend on abstractions (Inversion of dependencies)
-  Abstractions (e.g. via interfaces or abstract classes) over Implementations
-  a first-class combination of the Open Closed Principle and the and the Liskov Substitution Principle
-  Dependency Injection is a practical technique for achieving the Dependency Inversion Principle
![image](https://github.com/18Dominik/architecture/assets/35842490/30fb47da-5a07-49eb-8a0d-d905496cfaea)

Source: https://blog.devgenius.io/dependency-injection-and-dependency-inversion-5585dd2b19fd?gi=4cc720d8abef

![image](https://github.com/18Dominik/architecture/assets/35842490/2626f3e5-c035-48a8-aa54-db388e59e2d5)

Source: https://medium.com/@kedren.villena/simplifying-dependency-inversion-principle-dip-59228122649a


Article on the relationship between Dependency Inversion Principle (DIP), Inversion of Control (IoC), and Dependency Injection (DI):
https://martinfowler.com/articles/dipInTheWild.html#YouMeanDependencyInversionRight
- DI is about how one object acquires a dependency. When a dependency is provided externally, then the system is using DI.
- IoC is about who initiates the call. If the container/system/library calls back into code that you provided it, is it IoC.
- DI is about wiring, IoC is about direction, and DIP is about shape

![image](https://github.com/18Dominik/architecture/assets/35842490/364dfb0a-3207-4acb-9da0-e24d176b107e)

Source: https://www.linkedin.com/pulse/dependency-inversion-principledip-mamata-raote-she-her-/

![image](https://github.com/18Dominik/architecture/assets/35842490/2da0b140-5835-4f28-8af1-5286beb3b9bd)

Source: https://www.linkedin.com/pulse/dependency-inversion-principledip-mamata-raote-she-her-/

## Interface Design/Types of Coupling: 
### Composition over Inheritance Principle
![image](https://github.com/18Dominik/architecture/assets/35842490/5bae169e-c286-40fb-9338-3cf3984e40cf)
Source: https://medium.com/@kamilmasyhur/a-principle-of-object-oriented-design-79b9bfefd446
Composition: One ***component** contains another vs. Inheritance: Subclasses inherit the implementation of the superclass

### Use/Delegation
A usage or delegation is a **method or function** call that originates in one component and is handled by another.

### Creation/Factory pattern
factory method allows a class to delegate the creation of objects to subclasses.
- creating objects without having to specify the exact class of these objects.
- Objects returned by a factory method are often referred to as products.
- you can override the factory method in a subclass and change the class of products being created by the method.
- All products must follow the same interface (e.g. 'deliver()')

  ![image](https://github.com/18Dominik/architecture/assets/35842490/6d2e0796-593b-4cb9-aae7-9e878f71e142)
  ![image](https://github.com/18Dominik/architecture/assets/35842490/950cf7f7-c637-4cfc-8620-b1df800cbeff)

  Source: https://refactoring.guru/design-patterns/factory-method
  
### Other types of coupling
- Messages or Events (Asynchronous Communication). Also see 'Promises' for asynchronous programming in JavaScript (Callback function -> Promises -> Async/Await (https://www.w3schools.com/js/js_asynchronous.asp))
- Temporal Coupling: If component A can only perform a task if another component B has completed another task, then A temporarily depends on B, e.g. Authentication in online banking system before performing banking transfers
- Coupling via data types
- Coupling via data (e.g. database between a write and a read component)
- Coupling via hardware (e.g. encryption and storing encryption key)

## Deployment Strategies
https://thenewstack.io/deployment-strategies/
![image](https://github.com/18Dominik/architecture/assets/35842490/65443936-0a5e-4fb4-9b0d-b9c6a569e6a3)

## Architecture Documentation
[arc42](https://www.arc42.de/overview/) offers an easy-to-use template for software architecture documentation.
1. Introduction & Goals: Short description of requirements, Top 3-5 quality requirements of architecture, list of most important stakeholders and their expectations
2. Constraints: Everything that is constraining the design and development
3. Context: Delimiting the context from the system's environment
4. Solution Strategy: Summary of fundamental design decisions
5. Building Blocks Layer: Abstraction of source code as a hierarchy of white boxes and (and black boxes) up to the appropriate detail level
6. Run-Time Layer: Behaviour of building blocks within dynamic scenarios, considering the most important processes/interactions
7. Distribution Layer: Technical Infrastructure including real and virtual processors
8. Crosscutting Concepts: Generic principles that are re-used in different parts (Domain Model, Patterns, Persistence, UI/UX, Logging)
9. Architecture Decisions: Important, critical, risky, or expensive architecture decisions
10. Quality Requirements: Showcasing scenarios with a quality tree according to Chapter 1 (quality requirements)
11. Risks and technical debts: Known risks and technical debts
12. Glossary: Most important domain-specific language, stakeholder-oriented, translations in multi-lingual environments
![image](https://github.com/18Dominik/architecture/assets/35842490/0bcac792-b889-44af-9714-673f34a80f92)


## Books
### Design Patterns: Elements of Reusable Object-Oriented Software
Authors: Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides
https://learning.oreilly.com/library/view/design-patterns-elements/0201633612/











