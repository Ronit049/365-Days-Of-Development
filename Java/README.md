# ☕ Java Programming

Java is a statically typed, object-oriented language used in backend systems, enterprise software, Android development, and many coding interviews.

## First program

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, Java!");
    }
}
```

Save as `Main.java`, then run:

```bash
javac Main.java
java Main
```

## Variables and types

```java
int age = 20;
long population = 8_000_000_000L;
double score = 92.5;
char grade = 'A';
boolean learning = true;
String name = "Ronit";
```

## Conditions and loops

```java
if (age >= 18) {
    System.out.println("Adult");
} else {
    System.out.println("Minor");
}

for (int i = 0; i < 5; i++) {
    System.out.println(i);
}
```

## Methods

```java
static int add(int a, int b) {
    return a + b;
}
```

Java passes arguments by value. For object references, the reference value is copied.

## Classes and objects

```java
class Student {
    private final String name;

    Student(String name) {
        this.name = name;
    }

    void introduce() {
        System.out.println("I am " + name);
    }
}

public class Main {
    public static void main(String[] args) {
        Student student = new Student("Ronit");
        student.introduce();
    }
}
```

## Collections

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        List<Integer> numbers = new ArrayList<>(List.of(4, 2, 8));
        Collections.sort(numbers);

        Map<String, Integer> frequency = new HashMap<>();
        frequency.put("apple", frequency.getOrDefault("apple", 0) + 1);

        Set<Integer> unique = new HashSet<>(numbers);
        Queue<Integer> queue = new ArrayDeque<>();
        queue.offer(10);
    }
}
```

Learn `ArrayList`, `LinkedList`, `HashMap`, `HashSet`, `TreeMap`, `PriorityQueue`, `ArrayDeque`, and the `Collections` utility class.

## Exceptions

```java
try {
    int result = 10 / 0;
} catch (ArithmeticException exception) {
    System.out.println("Cannot divide by zero.");
}
```

## Core topics checklist

- [ ] Primitive and reference types
- [ ] Strings and arrays
- [ ] Methods and constructors
- [ ] Encapsulation, inheritance, polymorphism, abstraction
- [ ] Interfaces and abstract classes
- [ ] Exception handling
- [ ] Generics
- [ ] Collections Framework
- [ ] Streams and lambdas
- [ ] File I/O
- [ ] Unit testing basics

## Practice exercises

1. Create a Student class with marks and grade calculation.
2. Count word frequencies using a HashMap.
3. Sort a list of custom objects.
4. Build a simple library management program.
5. Implement a queue using two stacks.

## Official resource

[Dev.java Learn](https://dev.java/learn/)
