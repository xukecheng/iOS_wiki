这是我在 Let’s VisionOS 2024
上的演讲内容。为了便于阅读，我对原始内容进行了简化，并调整为更加书面化的表达。本次分享的核心是传达这样一个中心思想：尽管这些新框架是为了解决现有框架中的问题而设计的，但我们不应被过往的经验和惯例所限制。需要用开放的心态和全新的视角去学习和使用这些新工具。将采用新框架的过程视为将项目向更安全、更现代化方向重构的绝佳机会。

> 可在 [ 此处 ](https://cdn.fatbobman.com/new-framework-new-mindset.pdf) 获得
> Keynotes 的 PDF 版本。

## 正文

大家好，我是徐杨，有一些朋友可能会更熟悉我其他的名字，“肘子”或是 “Fat”。很高兴能在这里与大家一起探讨应用开发相关的内容。首先，我要感谢
SwiftGG 和 XR 基地举办了 Let’s VisionOS 这个活动，搭建了这个交流平台。

今天，我将聚焦于”新思维”这一概念，并介绍两个去年推出的新框架 Observation 和
SwiftData。我不会过多涉及它们的具体用法和实现细节，只会重点阐述构建这两个新框架的背景和意义，如何以开放的心态学习和使用这些工具，以及如何将这种”新思维”融入我们未来的开发实践中。

## Observation

### 构建 Observation 的目的

让我们先来谈谈 Observation 框架。正如其名称所暗示的，这个框架旨在提供观察功能。它究竟旨在解决什么问题呢？

Observation 的核心目标是为 SwiftUI 引入一个全新的观察机制，以此来提升 SwiftUI 应用的性能。

为什么会有这样一个目标？这需要我们从 SwiftUI 当前的观察机制讲起。

### SwiftUI 当前的观察机制

作为一个响应式框架，SwiftUI 的视图需要随着状态的变化而更新。这就要求它依赖于某种机制来追踪这些状态变化。

在引入 Observation 框架之前，SwiftUI 实际上已经有了两套不同的观察机制。

首先是针对值类型状态的观察机制。例如，对于视图内的简单状态，我们一般使用 `@State`
进行声明，而这些状态大多是值类型。对于此类状态，SwiftUI 能够自行进行观察。

然而，对于那些有更广泛影响，甚至是全局性的状态，开发者通常会把它们放在一个引用类型的容器中。对于这些引用类型的状态，SwiftUI
不能独立进行观察，而需要借助 Combine 框架提供的“发布者-订阅者”模式来实现观察。实际上，这种观察模式在当前的 SwiftUI 中存在一些问题。

### 导致大量视图无效更新的原因

来看看这个问题的根源在哪里。

    final class MyObservableObject: ObservableObject {
        @Published var name: String
        @Published var age: Int
        // 更多属性...
    }

    extension MyObservableObject {
      var objectWillChange: Self.ObjectWillChangePublisher // 内部发布者实例，视图将订阅这个发布者
    }

当我们使用 Combine 框架，并声明一个类型为 `ObservableObject` 的可观察对象时，首先需要的是符合 `ObservableObject` 协议。这个协议会在类中创建一个发布者实例。每当有属性被 `@Published` 修饰符标记的变量发生改变时， `@Published` 会触发类中的这个发布者，向所有订阅者发送通知。然而，因为这些通知不包含改变的具体信息，订阅者无法得知是哪个 `@Published` 标记的属性发生了变化。

> 深入了解 `@Published` 的工作原理，可以参考文章 [ 为自定义属性包装类型添加@Published 的能力
> ](/zh/posts/adding-published-ability-to-custom-property-wrapper-types/) 。

在 SwiftUI
中，与可观察对象相关联的视图就是这些订阅者。即使是可观察对象中极小的一部分状态发生变化，也会导致所有相关联的视图进行更新，进而造成了大量的无效视图更新，严重影响了应用的性能。

通过一个具体的例子，我们可以更清晰地看到这个问题：

这里有一个具有两个属性的可观察对象：

    final class Store: ObservableObject {
      @Published var name = "肥肥"
      @Published var age = 5
    }

在两个不同的子视图中，我们分别引用了这个对象，并且每个视图只使用了其中一个属性：

    struct NameView: View {
      @ObservedObject var store: Store
      var body: some View {
        let _ = print("NameView Update")
        Text(store.name)
      }
    }

    struct AgeView: View {
      @ObservedObject var store: Store
      var body: some View {
        let _ = print("AgeView Update")
        Text(store.age, format: .number)
      }
    }

由于 NameView 视图与 `store` 实例建立了联系（即响应该实例发出的通知），因此，即便是 `age`
属性发生变化时，它也会被更新。这就揭示了当前观察机制的不足之处。

### 改善无效更新的手段

随着我们对 SwiftUI 运作机制的深入理解，开发者们已经逐步掌握了一些技巧来改善上述问题。

> 想要深入理解这些技巧，建议阅读 [ 避免 SwiftUI 视图的重复计算
> ](/zh/posts/avoid_repeated_calculations_of_swiftui_views/) 以获取更多细节。

这些常见的改善手段包括：

- **按需引入状态**

一种有效的方法是，不将整个状态容器引入视图，而是仅传递视图实际所需的状态。这样做虽然能减少不必要的视图更新，但会增加开发的工作量，并且此方法只适用于不需要在视图中调用状态容器方法的纯展示场景。

    struct NameView{
      let name: String
      var body: some View{
        let _ = print("NameView Update")
        Text(name)
      }
    }

经过调整后的 NameView，不会因为 `age` 状态的变化而更新。

- **利用等值协议（Equatable）**

另一种方法是使视图遵循 `Equatable` 协议，并自定义比较逻辑以避免不相关的属性更新导致的重绘。不过，这种方法对于基于类的容器来说不适用。

    @State var student = Student(name: "fat", age: 88)

    struct StudentNameView: View, Equatable {
        let student: Student
        var body: some View {
            let _ = Self._printChanges()
            Text(student.name)
        }

        static func == (lhs: Self, rhs: Self) -> Bool {
            lhs.student.name == rhs.student.name
        }
    }

- **拆分状态容器**

将较大的状态容器拆分为若干个更小的状态容器也是一个解决方案。这种方式能够缩小更新的范围，但同时牺牲了状态管理的便捷性。

    class Store: ObservableObject {
      @Published var a: String
      @Published var b: String
    }

    class SubStore1: ObservableObject {
      @Published var a: String
    }

    class SubStore2: ObservableObject {
      @Published var b: String
    }

- **状态的逐级比对**

一些第三方框架通过在状态变化时进行逐级比对，以排除未发生变化的部分，从而优化性能。但这种比对本身也是一种性能消耗。当状态层级较深时，比对所需的资源会更多，性能提升的效果也会减弱。此外，这种方法还会增加学习成本。

虽然上述方法在特定场景下有其用处，但它们并未从根本上解决由观察机制引起的性能问题，仅仅是治标不治本。因此，SwiftUI
迫切需要一种新的观察机制，专门针对引用类型的状态。我们希望这种新的框架不仅能解决当前面临的无效更新问题，还能为开发者提供更加灵活和强大的状态管理能力。

正是基于这个考虑，苹果公司推出了 Observation 框架。

### Observation 的观察方式

那么，Observation 框架是如何创建可观察对象并构建观察操作的呢？

Observation 框架为开发者提供了两个主要工具： `@Observable` 宏和 `withObservationTracking`
函数。

> 宏在 Swift 5.9 中引入，旨在减轻开发者的负担，避免手动编写重复的代码，从而提高开发效率。

`@Observable` 首先在引用类型声明中引入一个“观察协调器”—— `ObservationRegistrar`
实例。这个协调器负责维护可观察属性与观察者之间的联系。这有点类似于 `ObservableObject`
协议为类添加发布者的过程，但原理和工作机制完全不同。

接着， `@Observable` 会把存储属性转化为计算属性，确保它们的存储操作完全由观察协调器管理，这样可以整合观察逻辑，这在某种程度上类似于 `@Published` 属性包装器的工作方式。

在声明完可观察对象后，我们需要使用全局函数 `withObservationTracking`
来构建观察。这个函数要求开发者提供两个闭包：所有需要被观察的属性都必须在 `apply`
闭包中出现并被读取其值。当被观察的属性即将发生变化时，框架会调用 `onChange` 闭包，完成“观察-回调”的完整流程。

通过这种方式， `Observation` 提供了对属性的细粒度观察能力，解决了仅能观察整个实例而导致的精度不足问题，这是其解决 Combine
观察机制中存在问题的根本方案。

### Observation 的特点

Observation 框架所提供的观察机制展现了几个独特的特点：

- **局部观察性** ：仅对 `apply` 闭包中实际读取其值的可观察对象属性进行观察，确保观察的精确性和高效性。
- **变化前通知** ：在属性值实际变化之前（即 `willSet` 阶段）调用 `onChange` 闭包，允许开发者在变化发生前做出响应。
- **一次性观察** ：每次观察都是一次性的，一旦 `onChange` 闭包被触发，相应的观察操作就会结束。
- **多属性、多实例监控** ：在一次观察过程中，可以同时监控多个可观察实例的多个属性。任何一个被观察的属性的变化都会触发 `onChange` 闭包，并结束这次观察。

这种观察逻辑虽然看起来有些独特，但实际上是为了满足 SwiftUI 的特定需求而精心设计的。它形成了一个完美的闭环：从“创建观察”（将视图的 `body` 放入 `apply` ），到“状态变化”，再到“视图更新”（调用 `onChange`
闭包），最后“重新创建观察”（重复之前的步骤），这一系列操作紧密相连，适应了 SwiftUI 的渲染和更新机制。

在实际的 SwiftUI 开发过程中，开发者通常不需要直接使用 `withObservationTracking` 来手动构建观察，因为 SwiftUI
已经在其视图评估逻辑中集成了观察操作。

下一步，我们将之前基于 Combine 的示例修改成使用 Observation 的方式，来具体展示引入新框架后能带来哪些改变。

### 从 Combine 到 Observation

要将基于 Combine 的可观察对象迁移到 Observation 框架，我们需要进行几项关键的调整：移除 `ObservableObject`
协议声明，移除所有的 `@Published` 属性包装器，并在类声明前添加 `@Observable` 宏。通过这样做， `@Observable` 宏将会引入我们之前讨论过的功能，进一步简化可观察类型的声明过程。

    @Observable
    class Store {
      var name: String
      var age: Int

      func updateName() {}
    }

在视图中引用这个新的可观察对象时，我们会用 `@State` 来替换原本的 `@StateObject` ，并通过 `let`
关键字直接在子视图中引入这个实例。经过这样的调整，我们发现，尽管在视图中直接使用了可观察对象，但得益于 Observation 所提供的更精确的观察能力，
`NameView` 视图不会因 `age` 属性的变化而更新。

这一变化示例展示了，如果您的应用当前因观察精度不足而遭受大量无效视图更新和性能下降的问题，仅需将其转换为 Observation
方式，便可迅速看到明显的改善。

> 想要深入了解 Observation 框架的具体使用方法和更多细节，推荐阅读 [ 深度解读 Observation——SwiftUI 性能提升的新途径
> ](/zh/posts/mastering-observation/) 。

### Observation 带来的 “新思维”

Observation 框架不应仅被视作一个提升性能的工具。随着 SwiftUI
获得这样先进的观察能力，它实质上彻底转变了我们对应用状态的构思和设计方式。这种转变不仅仅关乎于修改几行代码，而是需要我们拥抱一种全新的思维模式——一种使应用更加灵活、可靠、可扩展且效率更高的思维方式。

让我们探索一下，除了性能提升，Observation 框架还开启了哪些新的可能性：

- **灵活的构筑形式**

Observation 为我们提供了一种全新的构建和组织应用状态的方式。现在，我们可以将一个可观察对象嵌套在另一个对象中，实现以前难以构建的状态关系。在
Combine 框架下，尝试实现这种嵌套会面临很大的挑战，因为 `@Published` 属性不支持观察引用类型内部的变化。

    @Observable
    class A {
       var b = 1
    }

    @Observable
    class B {
       var b = 1
       var a = A() // 将一个可观察对象作为另一个可观察对象的属性
    }

- **精准的观察构建逻辑**

通过
Observation，我们的视图更新变得更加精准和高效。它不仅精确到属性级别，而且还精确到对属性的具体操作方式。只有当视图实际读取可观察对象的属性（即触发其
getter 方法）时，才会建立观察关系。如果只是赋值或调用可观察对象中的方法，而不触发属性的读取，就不会与视图建立观察联系。在基于 Combine
的实现中，只要将可观察对象引入到视图中（比如使用 `@EnvironmentObject` ），即使 body
中没有使用任何属性或方法，视图仍然需要响应可观察对象实例的变化。Observation
的这种精准观察能力大大减轻了开发者的负担，让我们能以更放松的心态设计状态。

    struct A: View {
      let store: Store
      var body: some View {
        Text(store.name) // 读取属性，创建关联
      }
    }

    struct B: View {
      let store: Store
      var body: some View {
        Button("Update"){
          store.name = "hello" // 未触发getter方法，不会建立观察关系
        }
      }
    }

通过这种“新思维”，我们能够更加自信和富有创造力地设计和构建 SwiftUI
应用的状态。这不仅是技术层面的改变，而是对开发思维的一次全面革新。我们应当拥抱这些新的可能性，充分利用 Observation
带来的优势，为我们的应用带来根本性的改变和提升。

### 前向兼容性（Back-porting）

最后，让我们讨论 Observation 框架的另一个关键优点：前向兼容性。

虽然 Observation 框架的特性非常吸引人，但可能有人担心它仅支持最新的系统版本，这会让很多用户无法使用。

这里有个好消息：尽管 Observation 主要是为 SwiftUI 设计的，苹果仍选择以开源的方式发布它，这意味着它不仅限于 SwiftUI 或
Apple 的生态系统。实际上，Observation 的目标不仅仅是提高 SwiftUI 的应用性能，它还旨在为 Swift
语言在各个平台上提供对引用类型属性级别的观察能力。

得益于其开源属性，开发者可以根据自己的需求对框架进行修改或封装，创建兼容旧版本系统的第三方库，从而使所有 SwiftUI 的应用都能受益于
Observation 带来的创新。

例如，利用像 [ ObservationBP ](https://github.com/onevcat/ObservationBP) 和 [
Perception ](https://github.com/pointfreeco/swift-perception)
这样的第三方库，无论我们的项目处于哪个开发阶段，或依赖于什么版本的 SwiftUI，我们都可以立即享受到 Observation 带来的革新。

因此，虽然 Observation 是一个新框架，但它的设计理念和开源性质确保了它能为更广泛的项目带来好处。当然，有人可能会问 Observation
是否可以用于其他场景，比如 UIKit 或视图之外的领域？理论上是可行的，但目前可能不太方便。Observation 主要还是专注于服务
SwiftUI，因此，我们目前最好还是将其视为 SwiftUI 的一部分。但未来，随着社区的不断努力，Observation
的应用场景肯定会不断扩大。因此，我们没有理由不立即学习和使用这个框架，用新思维来提升应用的品质。

---

至此，我们就结束了关于 Observation 的介绍。接下来，我们将探讨本次主题的另一个框架——SwiftData。

---

## SwiftData

SwiftData 是苹果在去年推出的一个数据管理框架，它被视为 Core Data 的继任者。它结合了 Core Data 的成熟持久化技术和 Swift
的现代并发特性，可以快速的为你的应用增加持久化功能。

为了更好的了解 SwiftData 带来的变化，我首先对 Core Data 进行一个简单的介绍。

### Core Data 简介

- **历史悠久** ：Core Data 是一个资深框架。它最早出现在 2005 年的 MacOS Tiger 版本中，到现在已经 19 年了。它的历史可以一直追溯到乔布斯创建的 NeXTSTEP 开发的 Enterprise Objects Framework（ EOF ）框架。

- **企业级出身，追求稳定与安全** ：EOF 是为企业级应用而设计的，曾在金融机构小范围流行过，因此特别注重安全性和可靠性。

- **分层架构，强大的扩展性** ：同样，作为面向企业的产品，EOF 采用了分层的架构设计，使其具备了很强的扩展能力。稳定性、安全性以及扩展性都被 Core Data 所传承下来了。最近几年苹果为 Core Data 引入的一些新特性，比如持久化历史跟踪和云同步，都是基于其强大的扩展性而实现的。

- **对象图管理框架** ：在 Core Data 中所有的数据都以对象形式存在，并由 Core Data 对这些对象的生命周期、状态，以及它们之间的关系进行管理。因此我们常说 Core Data 是一个对象图管理框架。

对象图通常比较复杂，这样就需要能够更好的管理和表述的工具。开发者平常主要是通过 Xcode 中的模型编辑器为 Core Data
构建数据模型，这种可视化的构建手段对处理复杂的对象关系十分有效。编辑器还能自动为我们生成数据模型对应的代码，

- **简化的数据持久化操作** ：Core Data 的使用者无需掌握数据库方面的知识就能进行数据持久化的操作，而且 Core Data 本身支持多种数据保存形式，并允许开发者构建其他类型的数据存储方式。

作为苹果生态系统中的一个重要基础框架，Core Data 被广泛应用于许多苹果官方应用及其他基础框架中。

### Core Data 在苹果生态中的优势

相较于其他的数据管理框架，在苹果生态中， Core Data 还具备其他一些优势：

- **系统内置框架、低资源占用** ：由作为系统内置的框架，Core Data 让应用体积更紧凑，运行时占用的资源更少。这种高效性特别适用于内存限制严格的环境，如小组件或浏览器扩展。我想这一点对于不少开发过小组件的朋友体会应该比较深。因为很多其他的数据管理框架在这些场景中，都会因为资源的限制而无法使用。
- **无缝的 CloudKit 集成** ：2019 年起，苹果加强了 Core Data 与 CloudKit 的整合，使开发者能够利用一站式解决方案，轻松实现数据的云存储、共享以及跨设备同步。这项集成不仅简化了开发流程，还为应用带来了苹果生态的核心优势：免费的云服务。有不少开发者是被这个特性所吸引从而选择 Core Data 的。

这些优势共同造就了 Core Data 在苹果生态系统中的独特地位。

### Core Data 当前等面临的问题

虽然我们已经探讨了 Core Data 的历史、优势和特性，但仍有一个疑问：既然 Core Data 如此强大，为什么还需要引入新的框架
SwiftData？

事实上，尽管 Core Data
有许多显著的优点，但这些优点主要反映了它过去的设计目的、当时的硬件标准和开发工具。随着时间的推移，这些条件已经发生了变化，Core Data
在适应现代开发需求方面显示出了局限性。

- **目标用户的转变** ：Core Data 最初设计时主要面向企业级应用，对这一领域的功能需求进行了精心的配备。然而，随着焦点转移到桌面和移动应用，尤其是移动领域，Core Data 的复杂性对于广大移动应用开发者而言变得过于繁琐。当代开发者渴望的是更简单、直观且高效的数据管理解决方案。
- **开发工具的进步** ：目前，Swift 已经成为主流开发语言。尽管我们可以在 Swift 项目中利用 Core Data，但由于 Core Data 是基于 Objective-C 构建的，这在使用时可能造成一定的不便和隔阂。这种技术差异阻碍了开发者充分利用 Swift 的许多先进特性，特别是那些与类型安全和编译时检查相关的功能，这些都是 Swift 语言的核心优势。
- **开发框架的更新** ：SwiftUI 的推出改变了 UI 开发的方式，但 Core Data 与 SwiftUI 之间缺乏天然的协同性，开发者往往需要额外构建一个适配层以方便在视图中展示数据。此外，Core Data 仍旧使用基于 Combine 的观察机制，与新推出的 Observation 框架相比显得过时。

这些问题让许多开发者感受到 Core Data
的入门成本比较高，并且在开发和调试过程中也要付出更多的精力。正因如此，苹果一直在努力研发一个既符合当前也顺应未来发展趋势的数据管理框架。最终推出了“SwiftData”。

> 事实上，近几年每当 WWDC 临近时，使用 Core Data 开发者总会期待有新框架的问世，大家很早就将其称作
> SwiftData。没想到苹果最终真的采纳了这一名称。

### SwiftData 的传承与变革

作为承载众多期望的框架，SwiftData 究竟能否担当重任？它是否解决了 Core Data 所面临的现实问题？

- **继承了 Core Data 的稳定性** ：SwiftData 是在 Core Data 的基础架构之上构建，保留了其作为数据管理框架核心部分的稳定性。因此，虽然 SwiftData 是一个全新的框架，它在数据存储和读取的稳定性方面已经是经过验证的。
- **兼容 Core Data 的数据库** ：SwiftData 与 Core Data 构建的数据库完全兼容。因此应用迁移到 SwiftData 时只需进行代码层面的调整，无需修改现有数据。
- **充分利用了 Swift 语言的特性，甚至促进了语言的发展** ：命名为 SwiftData，意味着它与 Swift 语言紧密结合。它不仅充分利用了 Swift 的语言特性，而且得益于苹果和 Swift 社区的支持，引入了专为其量身打造的新功能，让开发者可以享受到安全的并发模式、强类型、编译时检查等先进的语言特性。
- **将复杂功能简单化、隐藏不必要的细节** ：SwiftData 故意省略了 Core Data 中那些复杂、难以理解或很少使用的功能，简化了其分层结构，显著降低了学习门槛。
- **与 Observation 框架深度集成、对 SwiftUI 更加友好** ：通过改进数据模型构建方式和采用基于 Observation 框架的观察机制，SwiftData 提高了在 SwiftUI 中的数据使用便捷性，并优化了应用性能。

总之，SwiftData 保留了 Core Data 的核心优势，同时引入了易学性、易用性，并与 SwiftUI 实现了更紧密的集成，彻底拥抱 Swift
语言的设计理念和最新特性，重新定义了符合 SwiftUI 时代的数据管理框架。

---

作为一个全新的数据管理框架，SwiftData 引入了许多创新功能，值得深入探讨。考虑到时间限制，我将简要介绍其中两个特别突出的特性。

---

### 基于纯代码的数据建模方式

SwiftData 对 Core Data
长期沿用的基于可视化的数据建模方式进行了根本性的转变，采纳了纯代码的建模方法。尽管苹果生态中的其他数据管理框架大多已经使用纯代码方式，但 Core Data
因其强大的处理复杂对象图的能力而一直保持着基于可视化的模型构建方法。然而，随着应用场景的变化，复杂的对象关系管理已不再当前的主要需求了，这样就促使
SwiftData 采用了更加主流和灵活的纯代码建模方式。

其实，在两年前，苹果应该已经意识到这一点，它已经将基于对象图的编辑模式从 Xcode 中移除了。

![qEmjG](https://cdn.fatbobman.com/qEmjG.png)

尽管 SwiftData
在采用基于纯代码方式构建数据模型的领域属于后来者，但它无疑提供了最出色的实现。开发者可以以一种轻松、直观且精确的方式使用代码来定义数据模型。借助于
Swift 语言的宏功能和一系列新颖的语言特性，开发者现在能够以类似于定义原生 Swift
类型的方式来构建他们的数据模型。这种方法不仅大幅降低了学习的难度，而且显著提升了模型代码的可读性，使得数据结构的定义既清晰又直观。

    @Model
    public final class ImageData {
      @Attribute(.externalStorage)
      public var data: Data?

      @Relationship(deleteRule: .nullify)
      public var asset: ImageAsset?

      public init(data: Data? = nil， asset: ImageAsset? = nil) {
        self.data = data
        self.asset = asset
      }
    }

> 阅读 [ 揭秘 SwiftData 的数据建模原理 ](/zh/posts/unveiling-the-data-modeling-
> principles-of-swiftdata/) ，了解更多建模细节。

SwiftData 采用纯代码建模不仅仅是形式上的变化，它还意味着开发者可以用全新的方式来构思和组织他们的数据模型：

- **促进开发者将数据逻辑封装成独立的模块** ：纯代码的方式更适合模块化开发，开发者可以轻松将数据模型和逻辑封装成独立的模块，提高代码的可维护性和可重用性。

我们知道，在 Core Data 中创建数据模型后，Xcode 首先会生成一个 `xcdatamodeld` 的文件，然后会将编译后的 `momd`
文件打包到应用中，我们在构建容器时再用这个文件来转换成数据模型。由于这些资源文件的存在，很多开发者并不喜欢将模型和数据处理逻辑代码分离到一个独立的模块中。而
SwiftData 则没有这方面的负担，所有的数据模型都是基于代码的，因此会促进开发者用模块的方式对数据操作进行更好的抽象和封装。

- **方便开发者进行单元测试** ：与 Core Data 相比，SwiftData 的纯代码模型更容易进行单元测试，开发者可以编写更多的测试用例来确保代码的质量和稳定性。

比如，为 Core Data 构建单元测试也需要一些技巧，尤其是如何使用一个数据模型文件来为不同的测试单元创建数据容器。SwiftData
则简单的多，开发者可以尽情的编写更多的测试单元。这是我目前正在进行的一个项目，可以看到，只需几秒就可以完成近 100 个有关 SwiftData 的测试。

- **更适合在视图中直接使用** ：SwiftData 使得数据模型与 SwiftUI 视图的兼容性更加紧密，开发者可以直接在视图中使用模型，无需额外的适配层。并且 SwiftData 中的对象目前也已经采用了基于 Observation 的观察方式，从而提高了应用的性能。

- **扩展数据管理框架的应用场景** ：SwiftData 极大简化了数据建模的方式，使其能够在众多场景中取代 UserDefaults 和文件操作，成为一个更安全、简洁、高效的持久化解决方案，同时支持云同步功能。这一进步大大拓宽了数据管理框架的应用范围。

通过这些改变，SwiftData 不仅简化了数据模型的声明过程，还推动了整个项目向着更加现代化和安全的方向发展。SwiftData 正在为 SwiftUI
时代的应用开发定义全新的数据管理范式。

### 基于 Actor 的并发操作

除了建模方式之外，SwiftData 在处理并发操作方面也带来了显著的创新。

在过去，虽然 Core Data 的稳定性在多数情况下表现良好，但许多开发者可能对其并发操作的稳定性持有不同看法。因为在 Core Data
中安全地实现并发操作往往依赖于开发者的经验和耐心，且缺乏系统层面的充分支持。

自 Swift 5.5 版本起，Swift 正式进入了结构化并发的新时代。目前，越来越多的开发者启用了严格的并发检查，以迎接 Swift 6
的到来。SwiftData 创新地将数据操作逻辑封装在 Actor 中，让开发者能够从编译器获得并发安全性检查的支持，从而编写出高效、安全且简洁的并发代码。

这是一个 SwiftData 中实现并发编程的示例，其中数据操作逻辑被封装在一个用 `@ModelActor` 宏标记的 Actor
中。无论在哪个线程调用 `DataHandler` 的方法，所有操作都会在一个特定的串行队列中安全执行，将开发者从手动处理 `perform`
代码的沉重负担中解脱出来。

    @ModelActor
    actor DataHandler {
        func updateItem(identifier: PersistentIdentifier， timestamp: Date) throws {
            guard let item = self[identifier， as: Item.self] else {
                throw MyError.objectNotExist
            }
            item.timestamp = timestamp
            try modelContext.save()
        }

        func newItem(timestamp: Date) throws -> Item {
            let item = Item(timestamp: timestamp)
            modelContext.insert(item)
            try modelContext.save()
            return item
        }
    }

> 更多有关 SwiftData 的并发内容，请阅读 [ SwiftData 中的并发编程 ](/zh/posts/concurret-
> programming-in-swiftdata/) 。

这个变革背后包含了巨大的努力和创新，因为在 SwiftData 问世之前，Swift 尚未提供自定义执行者（Executor）的能力来允许 Actor
在指定线程中运行。随着 Swift 5.9 的发布，社区最终实现了这一功能，为 SwiftData 提供了构建新并发编程范式的基础。

并发逻辑的这一转变不仅是技术上的改进，它还鼓励开发者将数据逻辑代码从 SwiftUI
视图中分离，转移到独立的模块中，这符合现代编程的趋势并提高了代码的整洁性和可维护性。

基于 Actor 的封装方式同时也改变了数据操作逻辑在视图或其他状态管理模块中的集成方式，推动了一种更安全、更可靠的数据注入模式。

    extension DataProvider {
      public func dataHandlerCreator(configuration: DataStoreConfiguration? = nil) -> @Sendable () async -> DataHandler {
        let configuration = configuration != nil ? configuration! : self.configuration
        let container = persistentContainer
        return { DataHandler(configuration: configuration， modelContainer: container) }
      }
    }

    struct DataHandlerKey: EnvironmentKey {
      static let defaultValue: @Sendable () async -> DataHandler? = { nil }
    }

    extension EnvironmentValues {
      var createDataHandler: @Sendable () async -> DataHandler? {
        get { self[DataHandlerKey.self] }
        set { self[DataHandlerKey.self] = newValue }
      }
    }

综上所述，SwiftData 的每一项创新都深思熟虑，旨在促进开发者以全新的视角重审业务逻辑和项目架构，实现更加现代化和高效的开发实践。

### SwiftData 实战：用现代方法构建 SwiftUI 应用

作为 Core Data 的现代继承者，SwiftData
不仅仅是对旧概念的重塑，它实质上代表了数据管理理念的全面革新。因此，当开发者考虑将其集成到自己的项目中时，可能会遇到一些挑战和疑问。为了帮助解决这些问题，我在本次活动十几天前撰写了一篇名为
[ SwiftData 实战：用现代方法构建 SwiftUI 应用 ](/zh/posts/practical-swiftdata-building-
swiftui-applications-with-modern-approaches/) 的文章。这篇文章较全面地介绍了如何将 SwiftData
与现代编程理念相结合，并顺畅地融入到 SwiftUI 应用开发中。

## 最后

今天，我们共同探索了苹果在去年推出的两个创新框架。虽然它们分别针对不同的技术领域，但存在着显著的共通之处：

- 它们诞生于对旧有框架的现代化需求
- 紧密结合了 Swift 语言的先进特性
- 具备了塑造现代应用开发逻辑的潜力

本次分享的核心主题是“新框架、新思维”。我们应该打破传统思维的局限，用全新的视角去掌握和应用这些新兴的
API。重要的是要认识到，苹果推出这些新技术的目的不仅仅是为了提高表面的功能性和效率，更是为了满足未来发展的深层次需求，预示着对未来开发逻辑和设计架构的重大影响。

很荣幸能与各位在此交流分享，希望今天的内容能给大家之后的学习和开发带来一点启发。再次感谢主办方的精心组织，也预祝 Let’s VisionOS
活动未来更上一层楼，成为开发社区中的一大亮点。
