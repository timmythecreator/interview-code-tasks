// ======================== Question 1: Virtual methods in constructors ========================
// TASK:
// What will be printed in the log by the following code?
public class A
{
    public A()
    {
        Console.WriteLine("A");
        mthd();
    }

    public virtual void mthd()
    {
        Console.WriteLine("Method A");
    }
}

public class B : A
{
    public B()
    {
        Console.WriteLine("B");
        mthd();
    }

    public override void mthd()
    {
        Console.WriteLine("Method B");
    }
}

public class Program
{
    public static void Main()
    {
        A obj = new B();
        obj.mthd();
    }
}

// OUTPUT:
// A
// Method B
// B
// Method B
// Method B

// EXPLANATION:
// • new B() first runs A() (base ctor runs before derived) → "A". More: https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/base
// • A() calls virtual mthd(), which resolves to B.mthd() → "Method B".
// • Then B() runs, prints "B", calls mthd() again → "Method B".
// • Finally, obj.mthd() uses virtual dispatch to B.mthd() → "Method B".