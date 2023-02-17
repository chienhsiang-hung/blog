---
title: "5 Basic Design Patterns You Need to Know (1/2): Singleton, Factory, Observer"
date: 2023-02-15T06:10:00+08:00
lastmod: 2023-02-15T06:15:00+08:00
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: "Singleton pattern: This pattern ensures that only one instance of a class is created and provides a global point of access to that instance."
featuredimage: featured-image.png
tags: ["Design Patterns", "Design Pattern In Python", "Factory Pattern", "Singleton Pattern", "Observer Pattern"]
categories: ["SWE Interview 101"]
toc:
  enable: true
---
## Brief
1.  **Singleton pattern**: This pattern ensures that only one instance of a class is created and provides a global point of access to that instance.
    
2.  **Factory pattern**: This pattern provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.
    
3.  **Observer pattern**: This pattern defines a one-to-many dependency between objects, so that when one object changes state, all its dependents are notified and updated automatically.
    
4.  **Decorator pattern**: This pattern allows behavior to be added to an individual object, either statically or dynamically, without affecting the behavior of other objects from the same class.
    
5.  **Adapter pattern**: This pattern allows the interface of an existing class to be used as another interface, without modifying the source code of the existing class.

## Introduction
### Singleton

The Singleton pattern is a **creational** design pattern that **restricts the instantiation of a class to a single object**. This is accomplished by ensuring that ***the class has only one instance and providing a global point of access to that instance***.

To create a Singleton class, we usually define a static method in the class, which is responsible for **creating the instance of the Singleton class** if it doesn't already exist, and returning it. Here's an example implementation in Python:

```python
class Singleton:
    __instance = None
    
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
```

In this example, we define a `__new__` method that checks whether an instance of the class already exists. If it does not, the `__new__` method creates a new instance of the class using the `super().__new__` method, and assigns it to the class variable `__instance`. If an instance already exists, the `__new__` method simply returns the existing instance.

Using the Singleton pattern can be useful in situations **where we need to ensure that only one instance of a class is created**, such as when we want to **control access to a shared resource** or maintain a global state. However, it's important to be aware of the potential drawbacks of the Singleton pattern, such as **making it harder to test the code and making the code more tightly coupled**.
{{< youtube WV2Ed1QTst8 >}}

### Factory
The Factory pattern is a **creational** design pattern that provides an interface for creating objects in a superclass, but **allows subclasses to alter the type of objects that will be created**.

To create a Factory class, we first define a superclass (or interface) that declares the methods for creating objects. We then define a concrete implementation of the superclass for each type of object that we want to create. Finally, we define a Factory class that takes in a parameter and **returns an object of the appropriate type based on that parameter**.

Here's an example implementation of the Factory pattern in Python:

```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            return None
```

In this example, we define an `Animal` superclass with a `speak` method, which is then **implemented by the `Dog` and `Cat` subclasses**. We then define an `AnimalFactory` class with a `create_animal` method that takes in a `animal_type` parameter and returns an object of the appropriate type based on that parameter.

Using the Factory pattern can be useful in situations where we want to abstract away the details of object creation and provide a flexible way to create objects. It can also be helpful in situations where we want to decouple the code that uses the objects from the code that creates them.

### Observer (Publisher)
The Observer pattern is a behavioral design pattern that defines a one-to-many dependency between objects, so that when one object changes state, all its dependents are notified and updated automatically.

To create an Observer pattern, we first define a Subject class that maintains a list of its dependents (also known as observers), and provides methods for adding, removing, and notifying observers. We then define one or more Observer classes that implement an update method, which is called by the Subject when its state changes.

Here's an example implementation of the Observer pattern in Python:

It also notifies the other objects also that’s why we generally call it Publisher[^Publisher]. All the objects that want to track changes in the publisher’s state are called subscribers.

![Observer (Publisher)](featured-image.png "Observer (Publisher)")

<script src="https://gist.github.com/chienhsiang-hung/a74123e075386afd8e58247439773f3a.js"></script>

In this example, we define a `Subject` superclass with `attach`, `detach`, and `notify` methods for managing its list of observers. We also define an `Observer` superclass with an `update` method that is called by the `Subject` when its state changes.

We then define a `ConcreteSubject` class that extends the `Subject` and maintains a private `_state` variable. When the `ConcreteSubject`'s state changes using the `set_state` method, it notifies all its observers by calling their `update` methods.

Finally, we define a `ConcreteObserver` class that extends the `Observer` and prints a message when its `update` method is called.

Using the Observer pattern can be useful in situations where we want to maintain loose coupling between objects and decouple the code that changes the state of an object from the code that reacts to the change. It can also be helpful in situations where we want to provide a flexible way to add and remove observers without changing the code of the subject class.

## Use Cases
Singleton:

-   **Configuration objects that need to be shared across an application**
-   Database connection objects that need to be reused
-   **Logging objects that need to be accessed from different parts of the application**
-   Objects that need to maintain a single point of control, such as a **global counter** or sequence generator

Factory:

-   **Object creation that requires complex initialization or multiple steps**
-   Object creation that needs to be decoupled from the calling code
-   Creating objects based on runtime parameters or configuration settings
-   Creating objects that are difficult to instantiate directly, such as objects with circular dependencies or objects that require access to a particular resource

Observer:

-   **Implementing publish-subscribe systems, where one object sends messages and other objects receive them**
-   Implementing event-based systems, where multiple objects need to respond to changes in state
-   Implementing user interface components that need to update in response to changes in data
-   **Implementing notification systems that send updates to multiple listeners or subscribers**


[^Publisher]: [Observer method - Python Design Patterns - GeeksforGeeks](https://www.geeksforgeeks.org/observer-method-python-design-patterns/)