"""AP Computer Science A units and topics, aligned to the College Board CED.

Unit names and exam weighting ranges match the official Course and Exam
Description (Java-based). Topic names follow the CED's topic list where
known. Weights across all units sum to roughly 100%.
"""

UNITS = [
    {
        "name": "Primitive Types",
        "description": "Introduces variables, primitive data types, expressions, and how Java evaluates and casts numeric values.",
        "ap_weight_min": 2.5,
        "ap_weight_max": 7.5,
        "display_order": 1,
        "topics": [
            {
                "name": "Variables and Data Types",
                "description": "Declares and initializes variables using primitive types such as int and double.",
                "skill_tags": ["variables", "primitive-types"],
                "display_order": 1,
            },
            {
                "name": "Expressions and Assignment Statements",
                "description": "Evaluates arithmetic expressions and assigns resulting values to variables.",
                "skill_tags": ["expressions", "assignment"],
                "display_order": 2,
            },
            {
                "name": "Compound Assignment Operators",
                "description": "Uses shorthand operators such as +=, -=, and *= to update variable values.",
                "skill_tags": ["operators", "assignment"],
                "display_order": 3,
            },
            {
                "name": "Casting and Ranges of Variables",
                "description": "Converts between int and double using casting and reasons about precision loss and overflow.",
                "skill_tags": ["casting", "type-conversion"],
                "display_order": 4,
            },
        ],
    },
    {
        "name": "Using Objects",
        "description": "Covers object creation, calling methods on objects, and using the String and other library classes.",
        "ap_weight_min": 5.0,
        "ap_weight_max": 10.0,
        "display_order": 2,
        "topics": [
            {
                "name": "Objects: Instances of Classes",
                "description": "Creates objects using constructors and understands reference vs. primitive variables.",
                "skill_tags": ["objects", "constructors"],
                "display_order": 1,
            },
            {
                "name": "Calling a Void Method",
                "description": "Invokes methods that perform an action but do not return a value.",
                "skill_tags": ["methods", "void-methods"],
                "display_order": 2,
            },
            {
                "name": "Calling a Method That Returns a Value",
                "description": "Invokes methods that return a value and uses that value in an expression.",
                "skill_tags": ["methods", "return-values"],
                "display_order": 3,
            },
            {
                "name": "String Class",
                "description": "Uses String methods such as length, substring, indexOf, and equals to manipulate text.",
                "skill_tags": ["strings", "library-classes"],
                "display_order": 4,
            },
            {
                "name": "Wrapper Classes and Autoboxing",
                "description": "Relates primitive types to their corresponding wrapper classes such as Integer and Double.",
                "skill_tags": ["wrapper-classes", "autoboxing"],
                "display_order": 5,
            },
        ],
    },
    {
        "name": "Boolean Expressions and if Statements",
        "description": "Uses boolean expressions and conditional statements to control program flow.",
        "ap_weight_min": 15.0,
        "ap_weight_max": 17.5,
        "display_order": 3,
        "topics": [
            {
                "name": "Boolean Expressions",
                "description": "Evaluates relational and logical operators to produce true or false values.",
                "skill_tags": ["boolean-logic", "operators"],
                "display_order": 1,
            },
            {
                "name": "if Statements and Control Flow",
                "description": "Uses if statements to conditionally execute blocks of code.",
                "skill_tags": ["conditionals", "control-flow"],
                "display_order": 2,
            },
            {
                "name": "if-else Statements",
                "description": "Uses if-else and nested if statements to select among alternative execution paths.",
                "skill_tags": ["conditionals", "control-flow"],
                "display_order": 3,
            },
            {
                "name": "Compound Boolean Expressions",
                "description": "Combines boolean expressions using &&, ||, and ! and applies De Morgan's laws.",
                "skill_tags": ["boolean-logic", "compound-expressions"],
                "display_order": 4,
            },
            {
                "name": "Equivalent Boolean Expressions",
                "description": "Determines when two boolean expressions are logically equivalent.",
                "skill_tags": ["boolean-logic", "equivalence"],
                "display_order": 5,
            },
        ],
    },
    {
        "name": "Iteration",
        "description": "Uses while and for loops to repeat statements and reasons about loop behavior and nested iteration.",
        "ap_weight_min": 17.5,
        "ap_weight_max": 22.5,
        "display_order": 4,
        "topics": [
            {
                "name": "while Loops",
                "description": "Repeats a block of statements while a boolean condition remains true.",
                "skill_tags": ["loops", "while-loop"],
                "display_order": 1,
            },
            {
                "name": "for Loops",
                "description": "Uses for loops with initialization, condition, and update expressions to iterate a known number of times.",
                "skill_tags": ["loops", "for-loop"],
                "display_order": 2,
            },
            {
                "name": "Developing Algorithms Using Strings",
                "description": "Writes iterative algorithms that process characters of a String.",
                "skill_tags": ["loops", "strings"],
                "display_order": 3,
            },
            {
                "name": "Nested Iteration",
                "description": "Uses loops within loops to process two-dimensional patterns or data.",
                "skill_tags": ["loops", "nested-loops"],
                "display_order": 4,
            },
        ],
    },
    {
        "name": "Writing Classes",
        "description": "Designs classes with instance variables, constructors, methods, and encapsulation, including static features.",
        "ap_weight_min": 5.0,
        "ap_weight_max": 10.0,
        "display_order": 5,
        "topics": [
            {
                "name": "Anatomy of a Class",
                "description": "Defines a class with instance variables, constructors, and methods.",
                "skill_tags": ["classes", "class-design"],
                "display_order": 1,
            },
            {
                "name": "Constructors",
                "description": "Writes constructors that initialize instance variables when an object is created.",
                "skill_tags": ["classes", "constructors"],
                "display_order": 2,
            },
            {
                "name": "Documentation with Comments",
                "description": "Uses comments and Javadoc-style documentation to describe class and method behavior.",
                "skill_tags": ["documentation", "style"],
                "display_order": 3,
            },
            {
                "name": "Accessor and Mutator Methods",
                "description": "Writes getter and setter methods to access and modify private instance variables.",
                "skill_tags": ["encapsulation", "accessors-mutators"],
                "display_order": 4,
            },
            {
                "name": "Static Variables and Methods",
                "description": "Distinguishes static (class-level) members from instance members.",
                "skill_tags": ["classes", "static-members"],
                "display_order": 5,
            },
            {
                "name": "Scope and Access",
                "description": "Reasons about variable scope and the effect of public and private access modifiers.",
                "skill_tags": ["scope", "access-modifiers"],
                "display_order": 6,
            },
        ],
    },
    {
        "name": "Array",
        "description": "Creates and traverses one-dimensional arrays to store and process collections of primitive or object data.",
        "ap_weight_min": 7.5,
        "ap_weight_max": 10.0,
        "display_order": 6,
        "topics": [
            {
                "name": "Array Creation and Access",
                "description": "Declares, instantiates, and accesses elements of a one-dimensional array by index.",
                "skill_tags": ["arrays", "indexing"],
                "display_order": 1,
            },
            {
                "name": "Traversing Arrays",
                "description": "Uses for and enhanced for loops to traverse and process all elements of an array.",
                "skill_tags": ["arrays", "loops"],
                "display_order": 2,
            },
            {
                "name": "Enhanced for Loop for Arrays",
                "description": "Uses the enhanced for loop syntax to iterate over array elements without an explicit index.",
                "skill_tags": ["arrays", "for-each"],
                "display_order": 3,
            },
        ],
    },
    {
        "name": "ArrayList",
        "description": "Uses the ArrayList class to store, traverse, and modify collections of objects that can grow and shrink.",
        "ap_weight_min": 2.5,
        "ap_weight_max": 7.5,
        "display_order": 7,
        "topics": [
            {
                "name": "Introduction to ArrayList",
                "description": "Creates an ArrayList and adds, accesses, and sets elements.",
                "skill_tags": ["arraylist", "collections"],
                "display_order": 1,
            },
            {
                "name": "ArrayList Methods",
                "description": "Uses methods such as add, remove, get, and size to manipulate an ArrayList.",
                "skill_tags": ["arraylist", "methods"],
                "display_order": 2,
            },
            {
                "name": "Traversing an ArrayList",
                "description": "Iterates over an ArrayList using loops, including safe removal during traversal.",
                "skill_tags": ["arraylist", "loops"],
                "display_order": 3,
            },
        ],
    },
    {
        "name": "2D Array",
        "description": "Creates and traverses two-dimensional arrays using nested iteration, including row-major and column-major traversal.",
        "ap_weight_min": 7.5,
        "ap_weight_max": 10.0,
        "display_order": 8,
        "topics": [
            {
                "name": "2D Array Creation and Access",
                "description": "Declares, instantiates, and accesses elements of a two-dimensional array using row and column indices.",
                "skill_tags": ["2d-arrays", "indexing"],
                "display_order": 1,
            },
            {
                "name": "Traversing 2D Arrays",
                "description": "Uses nested loops to traverse a 2D array in row-major or column-major order.",
                "skill_tags": ["2d-arrays", "nested-loops"],
                "display_order": 2,
            },
            {
                "name": "2D Array Algorithms",
                "description": "Applies nested iteration to compute row, column, or diagonal sums and other common 2D array algorithms.",
                "skill_tags": ["2d-arrays", "algorithms"],
                "display_order": 3,
            },
        ],
    },
    {
        "name": "Inheritance",
        "description": "Builds class hierarchies using inheritance, method overriding, polymorphism, and the Object superclass.",
        "ap_weight_min": 5.0,
        "ap_weight_max": 10.0,
        "display_order": 9,
        "topics": [
            {
                "name": "Creating Superclasses and Subclasses",
                "description": "Defines subclasses that extend a superclass to inherit fields and methods.",
                "skill_tags": ["inheritance", "class-hierarchy"],
                "display_order": 1,
            },
            {
                "name": "Writing Constructors for Subclasses",
                "description": "Uses super() to call a superclass constructor from within a subclass constructor.",
                "skill_tags": ["inheritance", "constructors"],
                "display_order": 2,
            },
            {
                "name": "Overriding Methods",
                "description": "Overrides superclass methods in a subclass to change or extend behavior.",
                "skill_tags": ["inheritance", "polymorphism"],
                "display_order": 3,
            },
            {
                "name": "super Keyword and Polymorphism",
                "description": "Uses the super keyword to call overridden superclass methods and reasons about polymorphic behavior.",
                "skill_tags": ["inheritance", "polymorphism"],
                "display_order": 4,
            },
            {
                "name": "The Object Superclass",
                "description": "Understands that all classes inherit from Object and may override equals and toString.",
                "skill_tags": ["inheritance", "object-class"],
                "display_order": 5,
            },
        ],
    },
    {
        "name": "Recursion",
        "description": "Writes and analyzes recursive methods, including base cases and recursive calls on arrays and simple algorithms.",
        "ap_weight_min": 5.0,
        "ap_weight_max": 7.5,
        "display_order": 10,
        "topics": [
            {
                "name": "Recursive Method Structure",
                "description": "Defines a recursive method with a base case and a recursive case that makes progress toward it.",
                "skill_tags": ["recursion", "base-case"],
                "display_order": 1,
            },
            {
                "name": "Tracing Recursive Calls",
                "description": "Traces the call stack of a recursive method to determine intermediate and final return values.",
                "skill_tags": ["recursion", "tracing"],
                "display_order": 2,
            },
            {
                "name": "Recursive Searching and Sorting",
                "description": "Applies recursion to classic algorithms such as binary search and merge sort.",
                "skill_tags": ["recursion", "algorithms"],
                "display_order": 3,
            },
        ],
    },
]
