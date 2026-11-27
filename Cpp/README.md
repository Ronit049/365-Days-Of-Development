# ⚙️ C++ Programming

C++ is a compiled, general-purpose language commonly used for DSA, systems programming, and performance-sensitive applications.

## Compile and run

Save code in `main.cpp`:

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hello, C++!" << '\n';
    return 0;
}
```

Compile with a C++ compiler:

```bash
g++ -std=c++17 -Wall -Wextra -O2 main.cpp -o main
```

Run on Windows:

```powershell
.\main.exe
```

## Variables and types

```cpp
int age = 20;
long long population = 8000000000LL;
double price = 99.5;
char grade = 'A';
bool isReady = true;
string name = "Ronit";
```

For `string`, include `<string>`.

## Conditions and loops

```cpp
if (age >= 18) {
    cout << "Adult\n";
} else {
    cout << "Minor\n";
}

for (int i = 0; i < 5; ++i) {
    cout << i << '\n';
}
```

## Functions and references

```cpp
int add(int a, int b) {
    return a + b;
}

void increment(int& value) {
    ++value;
}
```

A reference parameter can modify the original variable. Use `const` references for large objects that should not be modified:

```cpp
void printName(const string& name) {
    cout << name << '\n';
}
```

## Arrays and vectors

```cpp
#include <vector>
#include <iostream>
using namespace std;

int main() {
    vector<int> values = {4, 2, 8};
    values.push_back(10);

    for (int value : values) {
        cout << value << ' ';
    }
}
```

Prefer `vector` for a resizable sequence in everyday DSA problems.

## STL essentials

```cpp
#include <algorithm>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <unordered_map>
#include <vector>
using namespace std;

int main() {
    vector<int> a = {5, 1, 3};
    sort(a.begin(), a.end());

    unordered_map<string, int> frequency;
    frequency["apple"]++;

    stack<int> st;
    st.push(10);

    queue<int> q;
    q.push(20);

    set<int> uniqueValues = {2, 2, 4};
}
```

Learn these containers and their common operation costs:
- `vector`, `deque`, `list`
- `stack`, `queue`, `priority_queue`
- `set`, `map`, `unordered_set`, `unordered_map`
- `pair`, `tuple`, `string`

## Pointers and memory

```cpp
int value = 42;
int* pointer = &value;

cout << *pointer << '\n'; // dereference
```

A pointer stores an address. A reference is an alias. Understand object lifetime, stack vs. heap, and ownership. Prefer standard containers and smart pointers over manual `new` and `delete` in modern C++.

## OOP example

```cpp
#include <iostream>
#include <string>
using namespace std;

class Student {
private:
    string name;

public:
    explicit Student(string studentName) : name(studentName) {}

    void introduce() const {
        cout << "Hello, I am " << name << '\n';
    }
};

int main() {
    Student student("Ronit");
    student.introduce();
}
```

## DSA practice sequence

1. Arrays and strings
2. Sorting and binary search
3. Hashing
4. Two pointers and sliding window
5. Linked lists, stacks, and queues
6. Trees and heaps
7. Graphs
8. Greedy and dynamic programming

## Practice exercises

- Find minimum and maximum in a vector.
- Count frequencies with an unordered map.
- Remove duplicates from a sorted vector.
- Implement binary search.
- Implement a stack using a vector.
- Traverse a binary tree.
- Solve a shortest-path problem.

## Official resource

[C++ reference](https://en.cppreference.com/)
