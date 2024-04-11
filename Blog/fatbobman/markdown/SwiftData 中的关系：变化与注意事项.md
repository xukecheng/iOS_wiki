在之前的两篇文章 [ 掌握 Core Data 中的关系：基础 ](/zh/posts/mastering-relationships-in-core-
data-fundamentals/) 和 [ 掌握 Core Data 中的关系：实战 ](/zh/posts/mastering-
relationships-in-core-data-practical/) 中，我们详细探讨了 Core Data
中关系的概念和技巧。虽然这些知识在很大程度上同样适用于 Core Data 的继任者 SwiftData，但 SwiftData
在关系处理上也引入了一些显著的变化。本文将重点介绍 SwiftData 在关系方面发生的变化，以及由此带来的潜在挑战和值得注意的细节。

## 从“由里至表”到“由表及里”的变革

在 SwiftData 的众多创新中，最引人注目的莫过于允许开发者通过纯代码直接声明数据模型。在 Core Data 中，开发者需要先在 Xcode
的数据模型编辑器里创建数据模型（对应 NSManagedObjectModel），然后才是编写或自动生成 NSManagedObject 子类代码。

这一过程本质上是从模型（“里”）到类型代码（“表”）的转换。开发者能在一定程度上调整类型代码，例如将 `Optional` 改为 `Non-
Optional` 或将 `NSSet` 改为 `Set` ，从而优化开发体验，只要这些修改不影响 Core Data 在代码与模型之间的映射。

SwiftData 的纯代码声明方式彻底改变了这一流程。在 SwiftData 中，类型代码和数据模型的声明是同步进行的，或者更准确地说，SwiftData
会根据开发者声明的类型代码自动生成相应的数据模型。声明方式由传统的“由里至表”转变为了“由表及里”。

这种变化在大多数情况下都是正面的，但对于某些具体应用场景，开发者需要调整他们之前的开发习惯和技巧。例如，在之前的文章 [ 《掌握 Core Data
中的关系：实战》 ](/zh/posts/mastering-relationships-in-core-data-practical/)
中提到的将数据模型声明为 `Optional` 的关系对应的代码修改为 `Non-Optional` 的技巧，在 SwiftData
中将不再适用。模型将严格遵循类型代码的声明创建：

    @Model
    final class Item {
        var timestamp: Date = Date.now
        var tag: Tag?
        init(timestamp: Date) {
            self.timestamp = timestamp
        }
    }

    @Model class Tag {
        var name: String
        var items: [Item] = []
        init(name: String) {
            self.name = name
        }
    }

在这段代码中， `var tag: Tag?` 表明 `tag` 关系是可选的。如果我们去掉 `?` ，那么在对应的数据模型中， `tag`
关系将变为非可选。同样， `var items: [Item] = []` 指出 `items` 关系是非可选的。

## 关系可以设置默认值的误区

在 Core Data 中，与其他类型的属性不同，开发者无法为关系设置默认值。这一限制在 SwiftData 中同样适用。然而，SwiftData
当前的声明方式可能会误导开发者认为可以为关系设置默认值。以以下代码为例：

    @Model
    final class Item {
        var timestamp: Date = .now
        var tag: Tag = Tag(name: "hello")
        init(timestamp: Date) {
            self.timestamp = timestamp
        }
    }

    @Model class Tag {
        var name: String
        var items: [Item] = []
        init(name: String) {
            self.name = name
        }
    }

乍一看， `var tag: Tag = Tag(name: "hello")` 和 `var items: [Item] = []`
似乎都在为关系设置默认值。但实际上并非如此。

首先，尽管 `var tag: Tag = Tag(name: "hello")`
这段代码可以编译通过，但它会在运行时产生错误，错误提示为：“Failed to find any currently loaded container
for Tag”。至于 `var items: [Item] = []` ，虽然不会报错，但这并不代表它在为 `items` 设置了有效的默认值。

在之前的文章 [ 《揭秘 SwiftData 的数据建模原理》 ](/zh/posts/unveiling-the-data-modeling-
principles-of-swiftdata/) 中，我们详细探讨了 SwiftData
是如何根据声明的代码创建数据模型的。无论是通过字面量赋值，还是通过构造方法赋值，这些操作都只是在创建了托管对象实例之后进行的。也就是说，在创建托管对象的过程中，并不会生成“预期”的默认值（关系对象）。

## 在构造方法中创建关系数据

在过去几个月中，我接触了许多使用 SwiftData 框架编写代码的开发者。其中，特别是那些没有 Core Data
开发经验的开发者，他们常常采用类似于以下的实现方式：

    @Model
    final class Item {
        var timestamp: Date
        var tag: Tag?
        init(timestamp: Date, name: String) {
            self.timestamp = timestamp
            tag = Tag(name: name)
        }
    }

    @Model class Tag {
        var name: String
        var item: Item?
        init(name: String) {
            self.name = name
        }
    }

从这种普遍的实践方式可以看出，SwiftData 在改变数据模型定义模式上取得了显著的成功。由于 `@Model`
宏要求必须定义构造方法，开发者往往会按照标准的 Swift
类型定义的模式，在一个实体的构造方法中直接生成另一个实体的数据。这种方法不仅简洁、直观，而且在构造方法中创建的实体数据也无需额外地插入到 `ModelContext` 中：

    let newItem = Item(timestamp: Date(),name: "hello")
    modelContext.insert(newItem)

这一实践反映了 SwiftData 对传统数据模型定义方式的重大简化和改进。它使得关系数据的创建更符合 Swift
语言的本质风格，同时也降低了开发者的学习曲线，尤其是对于那些初次接触数据持久化框架的开发者而言。

> 在构造方法中创建的关系数据同样不属于默认值。

## SwiftData 中的逆向关系设置及其困惑

在之前的文章 [ 《掌握 Core Data 中的关系：基础》 ](/zh/posts/mastering-relationships-in-core-
data-fundamentals/) 中，我们讨论了逆向关系的重要性。在 Core Data 中，开发者需要在 Xcode
的模型编辑器中显式地为双向关系设置逆向关系，并且若未设置，Xcode 会发出警告。而在 SwiftData
中，逆向关系的设置规则并不那么明确。在某些情况下，即使开发者未使用 `@Relationship(inverse:)` 设置逆向关系，SwiftData
也可能自动为模型添加。

通过我的实验，我发现 SwiftData 对逆向关系的处理规则如下：

- **One-to-One（一对一）** ：当两端都是 `Optional` 时，SwiftData 会自动添加逆向关系。例如：

  @Model
  final class Item {
  var timestamp: Date
  var tag: Tag? // Optional
  init(timestamp: Date) {
  self.timestamp = timestamp
  }
  }

  @Model class Tag {
  var name:String
  var item: Item？// Optional
  init(name: String) {
  self.name = name
  }
  }

- **One-to-One（一对一）** ：若一端不为 `Optional` ，则需要开发者明确设置逆向关系（在任一侧设置即可）。例如：

  @Model
  final class Item {
  var timestamp: Date
  @Relationship(inverse:\Tag.item)
  var tag: Tag?
  init(timestamp: Date, name: String) {
  self.timestamp = timestamp
  }
  }

  @Model class Tag {
  var name: String
  var item: Item
  init(name: String,item:Item) {
  self.name = name
  self.item = item
  }
  }

- **One-to-Many（一对多）** ：两端都是 `Optional` 时 SwiftData 会自动设置逆向关系；一端不为 `Optional` 时，需要开发者明确设置逆向关系
- **Many-to-Many（多对多）** ：两端都为或任意一段为 `Optional` 时，SwiftData 会自动设置；若两端均为 `Non-Optional` ，则需要开发者明确设置。

总的来说，除了 `Many-to-Many` 情况外，在 `One-to-One` 和 `One-to-Many` 关系中，只要任意一端不为 `Optional` ，就需要显式设置逆向关系。

虽然这些规则不算过于复杂，但为了避免潜在的问题，建议开发者在声明模型时始终明确设置逆关系。

## 丢失的 Core Data with CloudKit 兼容性自动检查

当我们需要在应用中为 Core Data 开启云存储功能（即 Core Data with CloudKit）时，在创建数据模型阶段，就必须根据 Core
Data with CloudKit 的要求对模型进行一些特定的调整。例如，必须设置逆向关系、不能使用 `Deny` 删除规则等。

在 Core Data 的环境下，即使没有为项目启用 iCloudKit 功能，只要在 Xcode 的 Configuration 中勾选 `Used
with CloudKit` 选项，Xcode 就会自动检查当前数据模型是否符合 Core Data with CloudKit
的标准，并相应地给出提示。

然而，在 SwiftData 中，开发者首先需要为项目启用 CloudKit 功能并指定 CloudKit 容器。只有在运行应用后，如果模型不符合 Core
Data with CloudKit 的规范，才会收到模型错误的通知。

因此，对于那些已经启用或计划未来启用 Core Data with CloudKit 功能的开发者来说，应尽早在项目中设置相应的 CloudKit
选项。这样做可以避免因为模型不规范而导致未来需要进行大规模的代码更新。

> 关于 Core Data with CloudKit 对模型的具体要求，可参阅文章 [ 《Core Data with
> CloudKit：同步本地数据库到 iCloud 私有数据库》 ](/zh/posts/coredatawithcloudkit-2/) 。

## Array 创新还是陷阱

### 使用 Array 表示无序对多关系，字面意义存疑

SwiftData 在处理多对多关系时的一大变革是要求开发者直接使用数组（Array）来声明关系。与 Core Data 不同的是， `@Model`
宏不会为对多数据操作创建独立的方法，而是允许开发者直接对数组进行操作：

    @Model
    final class Item {
        var timestamp: Date
        var tags: [Tag] = []
        init(timestamp: Date, name: String) {
            self.timestamp = timestamp
        }
    }

    item.tags.append(tag)

对于这种变化，许多开发者的反馈是积极的。他们认为这大大提升了代码的字面清晰度，使模型声明和数据操作更加符合 Swift 语言的特性。

开发团队可能认为统一使用 Array 声明有序或无序的对多关系会降低 SwiftData 的学习门槛，因此没有采用 Set
来声明无序的多对关系。我个人对使用 Array 表示无序的对多关系持有保留意见，因为 Array
使代码失去了对数据元素唯一性和无特定顺序性的直观表达。因此，对开发者（尤其是初学者）来说，必须明确无序对多关系返回的顺序是不保证的（即使使用了
Array）。开发者应考虑采用在 “实战” 一文中介绍的更可控的对多关系数据获取方式。

### 通过数组操作多对关系数据的效率问题

在 Core Data 中，对于对多关系，Xcode 会自动生成一些专门的操作方法，例如 `addToTags(_ value: Tag)` 和 `removeFromTags(_ value: Tag)`
等。与使用多个特定方法相比，从形式上讲，直接使用熟悉的数组方法来操作多对关系数据似乎是一种进步。然而，在 SwiftData
的首个版本中，这种实现方式在某些场景下可能会导致严重的性能问题。

考虑以下代码示例：

    @Model
    final class Item {
        var timestamp: Int
        @Relationship(deleteRule: .cascade,inverse: \Tag.item)
        var tags:Array<Tag> = []

        init(timestamp: Int) {
            self.timestamp = timestamp
        }
    }

    @Model
    final class Tag {
        var name:String
        var item:Item?

        init(name: String) {
            self.name = name
        }
    }

    // Create One Item and One Hunderd Tags
    measure {
        let item = Item(timestamp: 100)
        context.insert(item)
        for i in 0..<100 {
            let tag = Tag(name: "\(i)")
            item.tags.append(tag)
        }
        try? context.save()
    }

在这个例子中， `Item` 和 `Tag` 之间是一对多关系。我们创建了一个 `Item` 实例和 100 个 `Tag` 实例，并通过
`item.tags.append(tag)` 建立关联。

与之对应的 Core Data 代码在执行相同操作时的平均耗时为 **0.003 秒** ，而上述 SwiftData 的代码平均耗时为 **0.106
秒** 。

虽然可以理解 SwiftData 作为封装层会有一些性能损耗，但超过 30 倍的时间差异仍然令人震惊。更为惊人的是，将循环增加到 1000 和 10000
时，时间差异更为显著：

将循环调整至 1000，700 多倍多时间差:

- 当循环次数为 1000：
  - Core Data: **0.012 秒**
  - SwiftData: **9.080 秒**
- 当循环次数为 10000：
  - Core Data: **0.082 秒**
  - SwiftData: 抱歉，我实在是没有耐心等下去了

这种显著的性能差异表明，尽管 SwiftData 在表面上简化了多对关系的操作，但在处理大量数据时，其效率远不及 Core Data。

### 问题的根源在哪里？

通过探究 SwiftData 与 Core Data 在添加多对关系数据时的差异，我们可以找出潜在的性能问题原因。

两者最显著的区别在于创建关系的方法：SwiftData 使用 `item.tags.append(tag)` ，而 Core Data 使用 `item.addToTags(tag)` 。在 Core Data 中，通过使用专门生成的 `item.addToTags`
方法，框架可以直接识别即将被添加的关系对象。相反，SwiftData 采用标准数组操作，这意味着在执行 `append`
操作后，必须比较新的值（追加后的 `item.tags` ）和旧的值（追加前的 `item.tags`
）来确定新增的对象。结果是，随着数组中数据量的增加，性能会出现指数级劣化。

为验证这一假设，我检查了 SwiftData 的接口文件，发现开发团队仅为 Array 类型增加了以下扩展：

    public protocol RelationshipCollection {
      associatedtype PersistentElement : SwiftData.PersistentModel
    }

    extension Swift.Array : SwiftData.RelationshipCollection where Element : SwiftData.PersistentModel {
      public typealias PersistentElement = Element
    }

这段代码仅表明需要使用数组来声明多对关系，并没有为数组操作（如 `append` ）定制特别的处理。

那么，如果从 `One` 端来创建关系，效率是否会有所提高呢？我们可以调整代码测试这一点：

    let context = sharedModelContainer.mainContext
    measure {
        let item = Item(timestamp:.now)
        context.insert(item)
        for i in 0..<1000 {
            let tag = Tag(name: "\(i)")
            tag.item = item
        }
        try? context.save()
        print(item.tags?.count ?? "null")
    }

在进行 1000 次循环后，SwiftData 的平均用时为 **4.350 秒** ，而 Core Data 仅为 **0.011 秒** 。虽然
SwiftData 的用时有所下降，但与 Core Data 相比仍有显著差距。

这表明，即使从“一”端创建关系，SwiftData 似乎仍然会自动处理“多”端的 Array 数据，从而造成性能损耗。

> 我还尝试了创建没有逆向关系的模型版本，发现运行时间几乎没有差异。这说明 SwiftData 在处理多对关系的 Array
> 数据时，并不受是否设置逆向关系的影响。

### 解决方案

面对 SwiftData 中多对关系数据操作的性能问题，一个可能的解决方案是减少对数组的操作次数，从而提高执行效率。

我们可以通过以下代码调整来尝试解决这一问题：

    let context = sharedModelContainer.mainContext
    measure {
        let item = Item(timestamp:.now)
        context.insert(item)
        var tags = [Tag]()
        for i in 0..<1000 {
            let tag = Tag(name: "\(i)")
            tags.append(tag)
        }
        item.tags?.append(contentsOf: tags)
        try? context.save()
        print(item.tags?.count ?? "null")
    }

在这种方法中，我们先将所有创建的 `Tag` 实例保存在一个临时数组中，然后一次性将这些 `Tag` 实例添加到 `item.tags` 中。

实验显示，在进行 1000 次循环操作后，SwiftData 的平均用时降低至 **0.069570 秒** ，相比之前有了显著提升，效率提高了约 130
倍。然而，与 Core Data 在相同操作下的平均用时 **0.012 秒** 相比，SwiftData 仍然存在一定的差距。

这个例子表明，在处理 `One-to-Many` 或 `Many-to-Many`
类型的关系时，应尽量减少对对多关系数组的操作次数，尽可能将多次操作合并为一次性完成。

至于 SwiftData 的性能问题是否能够最终得到解决，还取决于未来 SwiftData 版本是否会在这方面进行专门的优化。

> 你可以在 [ 此处
> ](https://github.com/fatbobman/BlogCodes/tree/main/ToManyPerformance)
> 获取所有的本文所有的测试代码

## 总结

在本文中，我们探讨了 SwiftData 在处理数据关系方面的变化，并分析了其中可能引起的性能问题。虽然 SwiftData 仍然基于 Core Data
的底层结构，但它已经展现出了自己独特的特性和新的使用方式。这些变化意味着，之前针对 Core Data 的一些技巧和实践，在 SwiftData
中可能需要进行适当的调整和重新考量。

SwiftData 为开发者提供了一种更加现代和直观的方式来处理数据关系，但这也伴随着新的挑战和学习需求。开发者需要不断适应 SwiftData
的特点，灵活运用新的策略和技术，以充分利用其提供的便利并改善性能。
