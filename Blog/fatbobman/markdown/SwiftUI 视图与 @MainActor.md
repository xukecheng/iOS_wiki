越来越多的开发者开始尝试开启并发严格检查选项，为 Swift 6 的到来做准备。在收到的警告和错误中，有一部分是与 SwiftUI
的视图有关，其中很多都是由于开发者没有正确的理解和使用 `@MainActor` 造成的。本文将聊聊 `@MainActor` 的含义，以及在
SwiftUI 的视图中应用 `@MainActor` 的技巧和注意事项。

## 我的 PasteButton 不好用了

不久前，在我的 [ Discord ](https://discord.com/servers/zhou-zi-de-swiftji-shi-
ben-967978112509935657) 社区中，一位朋友反映在启用并发严格检查选项后，编译器对 `PasteButton` 给出了下面的错误：

    Call to main actor-isolated initializer 'init(payloadType:onPast:)' in a synchronous nonisolated context

![pasteButton-MainActor-
error-2024-03-13](https://cdn.fatbobman.com/pasteButton-MainActor-
error-2024-03-13.png)

查看 `PasteButton` 的声明后，我询问他是否将该视图代码放在 `body` 之外。得到肯定答复后，我让他为声明 `PasteButton` 的变量添加 `@MainActor` ，问题就解决了。

    @MainActor public struct PasteButton : View {
        @MainActor public init(supportedContentTypes: [UTType], payloadAction: @escaping ([NSItemProvider]) -> Void)

        @MainActor public init<T>(payloadType: T.Type, onPaste: @escaping ([T]) -> Void) where T : Transferable
        public typealias Body = some View
    }

那么，之前的问题出在哪里？为什么添加@MainActor 就能解决？

## 什么是 @MainActor

在 Swift 的并发模型中， `actor` 提供一种安全且易于理解的方式来编写并发代码。 `actor`
类似于类（class），但它专门用来解决并发环境下的数据竞争和同步问题。

    actor Counter {
        private var value = 0

        func increment() {
            value += 1
        }

        func getValue() async -> Int {
            return value
        }
    }

    let counter = Counter()
    Task {
      await counter.increment()
    }

`actor` 的魔法在于通过串行化访问来避免数据竞争，为并发操作提供了一条清晰、安全的路径。然而，这种隔离是局部的，仅限于特定的 `actor`
实例。Swift 进一步引入了 `GlobalActor` 概念，以在更广泛的范围内实现隔离。

`GlobalActor` 允许我们标记跨不同模块的文件中的代码，确保这些操作在相同的串行队列中执行，从而维持操作的原子性和一致性。

    @globalActor actor MyActor: GlobalActor {
        static let shared = MyActor()
    }

    @MyActor
    struct A {
      var name:String = "fat"
    }

    class B {
      var age:Int = 10
    }

    @MyActor
    func printInfo() {
      let a = A()
      let b = B()
      print(a.name,b.age)
    }

`@MainActor` 是 Swift 定义的一个特殊的 `GlobalActor` 。其职责是确保所有标记为 `@MainActor`
的代码都在同一串行队列中执行，并且这一切发生在主线程上。

    @globalActor actor MainActor : GlobalActor {
        static let shared: MainActor
    }

`@MainActor` 这一简洁而强大的特性，为我们曾经依赖 `DispatchQueue.main.async`
来处理的操作提供了一个类型安全且整合了 Swift 并发模型的方法。这不仅简化了代码，降低了出错率，还通过编译器的保护，确保了所有标记 `@MainActor` 的操作安全地在主线程上执行。

## View 协议与 @MainActor

在 SwiftUI
的世界里，视图（View）扮演着将应用程序状态以声明式方式展现在屏幕上的角色。这自然让人们假设，构成视图的所有代码都将在主线程中执行，毕竟，视图直接关联着用户界面的展现。

然而，探究 View 协议将揭示了一个细节：仅有 `body` 属性被显式地标记为 `@MainActor` 。这个发现意味着遵循 View
协议的类型，并不保证其整体运行在主线程上。除了 `body` 之外，编译器不会自动确保其他属性或方法在主线程中执行。

    public protocol View {
        associatedtype Body : View
        @ViewBuilder @MainActor var body: Self.Body { get }
    }

这一发现对于理解 SwiftUI 官方组件如 `PasteButton` 的使用尤为关键，因为它与大多数其他组件不同，被明确地标记为 `@MainActor` 。这表示， `PasteButton` 必须在同样被标记为 `@MainActor`
的上下文中使用，否则编译器将报错，指出不允许在非隔离的同步上下文中调用隔离于主线程的初始化器：

    struct PasteButtonDemo:View {
      var body: some View {
        VStack {
          Text("Hello")
          button
        }
      }

      var button:some View {
        PasteButton(payloadType: String.self){ str in // Call to main actor-isolated initializer 'init(payloadType:onPaste:)' in a synchronous nonisolated context
          print(str)
        }
      }
    }

为解决这一问题，简单地将 `button` 变量标记为 `@MainActor` 就可以顺利通过编译，因为这样做确保了 `button`
在一个符合要求的上下文中被初始化和使用：

    @MainActor
    var button:some View {
      PasteButton(payloadType: String.self){ str in
        print(str)
      }
    }

> 大多数 SwiftUI 组件都是值类型并符合 Sendable 协议，它们并未被显式标记为 `@MainActor` ，因此不会遇到 `PasteButton` 所面临的特定问题。

这个改动突显了在 SwiftUI 视图中使用 `@MainActor` 的重要性，同时也提醒开发者注意，不是所有视图相关的代码都默认运行在主线程中。

## 为 View 应用 @MainActor

或许有读者会想，我直接为 `PasteButtonDemo` 视图类型标注 `@MainActor` ，是不是就可以从根本上解决问题？

将整个 `PasteButtonDemo` 视图标注为 `@MainActor` 确实可以解决目前面临的问题。标注了 `@MainActor`
后，Swift 编译器就会假定该视图内的所有属性和方法均在主线程中执行，这样就无需对 `button` 进行单独的标注了。

    @MainActor
    struct PasteButtonDemo:View {
      var body: some View {
        ...
      }

      var button:some View {
        PasteButton(payloadType: String.self){ str in
          ...
        }
      }
    }

这种做法还带来了其他一些好处。比如，在利用 `Observation` 框架构建的可观察对象时，为了确保其状态更新在主线程进行，可以给可观察对象本身标注
`@MainActor` ：

    @MainActor
    @Observable
    class Model {
      var name = "fat"
      var age = 10
    }

然而，如果尝试按照官方文档建议，使用 `@State` 在视图中声明此可观察对象实例，就会遇到编译器警告：这在 Swift 6 中被视为错误。

    struct DemoView: View {
      @State var model = Model() // Main actor-isolated default value in a nonisolated context; this is an error in Swift 6
      var body: some View {
        NameView(model: model)
      }
    }

    struct NameView: View {
      let model: Model
      var body: some View {
        Text(model.name)
      }
    }

这种情况的发生是因为，默认情况下视图的实现并未标注为 `@MainActor` ，因此无法在视图中直接声明标注了 `@MainActor`
的类型。一旦 `DemoView` 被标注为 `@MainActor` ，上述问题便迎刃而解。

为进一步简化操作，我们还可以定义一个使用 `@MainActor` 标注的协议，让任何遵循该协议的视图自动继承主线程的执行环境：

    @MainActor
    protocol MainActorView: View {}

这样，任何实现了 `MainActorView` 协议的视图都保证其全部操作都在主线程上执行：

    struct AsyncDemoView: MainActorView {
      var body: some View {
        Text("abc")
          .task {
            await doSomething()
          }
      }

      func doSomething() async {
        print(Thread.isMainThread) // true
      }
    }

尽管为视图类型标注 `@MainActor`
似乎是个不错的解决方案，但这样会使所有声明在视图中的异步方法都必须在主线程执行，这可能不总是开发者所期望的。例如：

    @MainActor
    struct AsyncDemoView: View {
      var body: some View {
        Text("abc")
          .task {
            await doSomething()
          }
      }

      func doSomething() async {
        print(Thread.isMainThread) // true
      }
    }

若不进行 `@MainActor` 标注，我们便能更灵活地根据需要对属性和方法进行逐一标注：

    struct AsyncDemoView: View {
      var body: some View {
        Text("abc")
          .task {
            await doSomething()
          }
      }

      func doSomething() async {
        print(Thread.isMainThread) // false
      }
    }

因此，是否为视图类型标注 `@MainActor` 取决于实际的应用场景。

## @StateObject 的新用途

随着 Observation 框架成为新标准， `@StateObject` 的传统用途似乎变得不那么显著。然而，它仍然拥有一项特殊功能，让其仍可以在
Observation 时代发挥作用。正如我们之前讨论的，一个被 `@MainActor` 标注的 `@Observable`
可观察对象不能直接通过 `@State` 声明——除非整个视图也被标注为 `@MainActor` 。但是，有了 `@StateObject`
，我们就能巧妙地绕过这一限制。

考虑下面的示例，我们可以无需将整个视图标注为 `@MainActor` ，就能在视图中安全地引入被 `@MainActor` 标注的可观察对象：

    @MainActor
    @Observable
    class Model: ObservableObject {
      var name = "fat"
      var age = 10
    }

    struct StateObjectDemo:View {
      @StateObject var model = Model()
      var body: some View {
        VStack {
          NameView(model: model)
          AgeView(model: model)
          Button("update age"){
            model.age = Int.random(in: 0..<100)
          }
        }
      }
    }

这一实践的可行性源自于 `@StateObject` 的独特加载机制。在视图被实际加载之时， `@StateObject`
才会在主线程上调用其构造方法中的闭包。此外， `@StateObject` 的 `wrappedValue` 被标注为 `@MainActor`
，这保证了它能正确地初始化和使用被 `@MainActor` 标注的符合 `ObservableObject` 协议的类型。

    @frozen @propertyWrapper public struct StateObject<ObjectType>: SwiftUI.DynamicProperty where ObjectType: Combine.ObservableObject {
        @usableFromInline
        @frozen internal enum Storage {
            case initially(() -> ObjectType)
            case object(SwiftUI.ObservedObject<ObjectType>)
        }

        @usableFromInline
        internal var storage: SwiftUI.StateObject<ObjectType>.Storage
        @inlinable public init(wrappedValue thunk: @autoclosure @escaping () -> ObjectType) {
            storage = .initially(thunk)
        }

        @_Concurrency.MainActor(unsafe) public var wrappedValue: ObjectType {
            get
        }

        @_Concurrency.MainActor(unsafe) public var projectedValue: SwiftUI.ObservedObject<ObjectType>.Wrapper {
            get
        }

        public static func _makeProperty<V>(in buffer: inout SwiftUI._DynamicPropertyBuffer, container: SwiftUI._GraphValue<V>, fieldOffset: Swift.Int, inputs: inout SwiftUI._GraphInputs)
    }

这种方法的主要优势在于它既确保了可观察对象的生命周期安全，又完整地保留了其基于 Observation
框架的观察逻辑。这样，我们便能在不必将整个视图强制标注为 `@MainActor` 的情况下，灵活地使用被 `@MainActor`
标记的可观察类型。这为我们提供了一条既维护了视图灵活性，又不损害数据安全和响应逻辑的路径。在苹果官方提供更明确的在主线程上运行 `@State`
或调整视图声明的解决方案之前，这种做法是一个实用且有效的临时策略。

## 总结

在开启并发严格检查之后，许多开发者在面对一系列的警告和错误时可能会感到困惑和不知所措。其中一些人可能会采取根据提示逐个修改代码的方式来消除这些错误。然而，引入新的并发模型到项目中的根本目的远不止于“欺骗”编译器。实际上，开发者应当深入理解
Swift
的并发模型，并在更宏观的层面上重新审视自己的代码，以发现更优质、更安全的解决策略，而不是仅仅头痛医头、脚痛医脚。这种方法不仅能够提高代码的质量和可维护性，也能够帮助开发者在
Swift 的并发编程世界中更加自信和得心应手。
