在之前的文章 [ 掌握 Core Data 中的关系：基础 ](/zh/posts/mastering-relationships-in-core-
data-fundamentals/) 中，我们已经对 Core Data 中的关系基本概念和使用原则进行了探讨。本文将在此基础上进一步，分享关于处理
Core Data 关系的一些实用经验和技巧。目的是为了帮助开发者更有效地利用 Core Data 框架的关系功能，提高开发的灵活性和效率。

> 本文旨在为已具备一定 Core Data 关系知识和实践经验的读者提供进阶理解和应用的视角，并非旨在提供一个全面的教程。

## 可选值

在 Xcode 的模型编辑器中定义实体属性时，开发者应区分编辑器中的 `Optional` 选项和 Swift 语言中的 `Optional`
类型，两者并非一回事。在 Core Data 中， `Optional` 选项意味着相应的 SQLite 字段可以接受 NULL 值。而 Swift
中的 `Optional` 类型则是一种语言层面的特性，表示变量可能为 `nil` 。在 Core Data 模型中，这两种 `Optional` 的使用取决于具体场景和开发者的需求，并不需要严格对应。

在 Core Data 中，如果模型端的某个属性被标记为 `Optional` ，则在相应的 Swift 代码中，这个属性可以被定义为 `Non-
Optional` 。这种做法提供了更多的灵活性，允许开发者根据实际应用场景来决定是否在代码中使用 Swift 的 `Optional` 类型。

> 有关 Core Data 可选值方面更详尽的内容，请阅读 [ Ask Apple 2022 中与 Core Data 有关的问答 (下）
>
> > ](/zh/posts/core-data-of-ask-
> > apple-2022-2/#%E5%AE%9E%E4%BD%93%E5%B1%9E%E6%80%A7%E7%9A%84%E5%8F%AF%E9%80%89%E6%80%A7)
> > 。

举例来说，假设有 `Item` 和 `Tag` 两个实体，它们之间是 `One-to-One` 关系。在使用 Core Data with
CloudKit 时，这些关系在模型编辑器中必须标记为 `Optional`
。但在实际应用中，如果这两个实体的实例之间总是彼此关联，即它们的关系总是有值的，那么在 Swift
代码中，可以将它们调整为非可选类型。这样做的好处是，可以在代码中更方便地访问这些属性，无需频繁解包。

![Item_Model](https://cdn.fatbobman.com/image-20240107103248579.webp)

![Tag_Model](https://cdn.fatbobman.com/image-20240107103307135.webp)

Core Data 默认生成的代码如下：

    extension Item {
        @NSManaged public var timestamp: Date?
        @NSManaged public var tag: Tag?  // Optional
    }

    extension Tag {
        @NSManaged public var name: String?
        @NSManaged public var item: Item? // Optional
    }

但你可以根据实际情况将它们调整为非可选类型：

    extension Item {
        @NSManaged public var timestamp: Date
        @NSManaged public var tag: Tag  // Non-Optional
    }

    extension Tag {
        @NSManaged public var name: String // None-Optional
        @NSManaged public var item: Item // Non-Optional
    }

这样，就可以更加方便的在代码中获取数据了， **这样调整的前提是开发者必须确保在读取属性前已经给属性进行了赋值** ：

    Text(item.tag.name)

## Core Data 集合类型的 Swift 化

在处理 Core Data 的 `to-Many` 关系时，尤其是涉及有序关系时，调整其在 Swift 代码中的表示方式可带来显著的好处。

例如，考虑将 `tag` 改成有序的对多关系 `tags` ：

![Tags_Model](https://cdn.fatbobman.com/image-20240107110234842.webp)

Core Data 自动生成的代码如下：

    extension Item {
        @NSManaged public var timestamp: Date?
        @NSManaged public var tags: NSOrderedSet?
    }

为了提高代码的可读性和易用性，我们可以考虑将 `NSOrderedSet?` 类型转换为 `Array<Tag>`
。这样的调整不仅减少了解包处理的需要，而且使得 `tags` 属性更加符合 Swift 语言的习惯用法，如使用下标和迭代器进行访问。

    extension Item {
        @NSManaged public var timestamp: Date?
        @NSManaged public var tags: Array<Tag>
    }

调整后，我们可以更方便地在 Swift 中操作这些数据，例如（ Array 符合 RandomAccessCollection 协议 ）：

    ForEach(item.tags){ tag in
        Text(tag.name ?? "")
    }

值得注意的是，在处理非有序的 `to-Many` 关系时，将其转换为 `Array`
类型可能并非最佳选择。这主要是因为非有序集合的本质特性以及它们在 Core Data 中的管理方式。在 Core Data 中，非有序关系通常以 `NSSet` 表示，这直观反应了集合的无序性和元素的唯一性。如果转换为 `Array`
类型，这些关键特性可能会在字面上丢失。因此，对于非有序关系，使用 Swift 中的 `Set` 类型通常是更合适的选择。

例如，对于 `Item` 实体的 `tags` 属性，如果它是非有序的可选的 `to-Many` 关系，可以在 Swift 中这样表示：

    extension Item {
        @NSManaged public var timestamp: Date?
        @NSManaged public var tags: Set<Tag>
    }

这种方式既保持了集合的无序性和唯一性，又使得代码更加符合 Swift 的使用习惯，提高了代码的可读性。

## Count

在处理 `to-Many` 关系时，经常需要获取关联对象的数量。虽然直接使用 `.count`
属性是一种常见方法，但开发者还可以考虑使用派生属性（Derived Attribute）来更高效地获取这一计数。

例如，在下图所示的情况中，我们为 `TodoList` 实体创建了一个名为 `count` 的派生属性。这样，开发者可以通过简单地访问 `todolist.count` 来直接获取与 `TodoList` 相关联的 `items`
对象的数量。这种方法使得获取关联对象数量变得直观且高效。

![Derived](https://cdn.fatbobman.com/image-20211025183247335.webp)

相较于直接调用关系的 `.count`
属性，使用派生属性来计算数量通常更加高效。这是因为派生属性采用了不同的统计机制——它们在写入数据时计算并保存计数值，而在读取数据时则直接使用这个预先计算好的值。这种机制特别适用于那些读操作远多于写操作的场景。

然而，派生属性的一个重要限制在于，它们仅能统计已经持久化的数据量。这意味着如果有数据尚未被保存到持久化存储中，即处于暂存状态，这些数据将不会被派生属性的计数所考虑。因此，在使用派生属性时，开发者需要留意这一点，确保他们的数据处理逻辑考虑到了这种统计方式的这一特性。

> 想要更深入了解派生属性的使用方法，建议阅读 [ 《如何在 Core Data 中使用 Derived 和 Transient 属性》
> ](/zh/posts/derivedandtransient/) ，这篇文章详细介绍了派生属性的应用技巧。

## 管理非有序的 to-Many 数据

在许多实际应用场景中， `to-Many` 关系往往是无序的，这一点在使用 Core Data with CloudKit
时尤为明显，因为它不支持有序关系。

当直接通过关系属性获取数据（如下面的示例代码所示），Core Data 并不能保证返回数据的顺序：

    let tags = Array(items.tags)

> Core Data 在底层绝大多数情况下都会使用 SQLite 数据库来存储数据。在数据库中，除非明确指定排序顺序，否则记录的检索顺序是不确定的。

因此，为了保证获取非有序的 `to-Many` 数据时结果的一致性，建议不要直接使用关系属性。相反，应当创建一个包含谓词和排序条件的 `NSFetchRequest` 来执行查询，如下所示：

    func fetchTagsBy(item:Item) -> [Tag] {
        let request = NSFetchRequest<Tag>(entityName: "Tag")
        request.predicate = NSPredicate(format: "item = %@", item)
        request.sortDescriptors = [NSSortDescriptor(keyPath: \Tag.name, ascending: true)]
        return (try? viewContext.fetch(request)) ?? []
    }

在 SwiftUI 开发中，推荐将展示 `to-Many` 数据的界面单独封装成独立的视图，并通过 `@FetchRequest`
来获取数据。这种做法不仅确保了数据获取顺序的稳定性，还能及时响应数据变化，并使视图更新更加高效：

    struct TagsList: View {
        @FetchRequest var tags: FetchedResults<Tag>
        init(item: Item) {
            let request = NSFetchRequest<Tag>(entityName: "Tag")
            request.predicate = NSPredicate(format: "item = %@", item.objectID) // 使用 NSManagedObject 和 NSManagedObjectID ，生成的 SQL 指令都一样
            request.sortDescriptors = [NSSortDescriptor(keyPath: \Tag.name, ascending: true)]
            _tags = FetchRequest(fetchRequest: request)
        }

        var body: some View {
            List(tags) { tag in
                TagDetail(tag: tag)
            }
        }
    }

    struct TagDetail: View {
        @ObservedObject var tag: Tag
        var body: some View {
            Text(tag.name)
        }
    }

## 对多关系与子查询

在上一篇文章中，我们提到关系可以在某些场景下提高查询效率，并丰富查询手段。Core Data 中的子查询（SubQuery）功能正是这一场景的典型示例。

子查询是 Core Data
框架中一种高效的查询技术，它允许开发者在一个已有的查询结果集上执行更为复杂的查询。这在处理复杂的数据模型时尤其有用，特别是当需要根据关联对象的属性来进行过滤时。

子查询的基本格式如下所示：

    SUBQUERY(collection, $x, condition)

- `collection` 是要查询的集合，通常是一个对多关系属性。
- `$x` 是一个变量代表集合中的每个元素（ 可以任意设定名称 ）。
- `condition` 是应用于集合中每个元素的条件。

举个例子，假设我们想要获取所有至少有一个 `Tag` 名称以 “A” 开头的所有的 `Item` 。可以使用以下的 NSPredicate 表达式：

    NSPredicate(format: "SUBQUERY(tags, $tag, $tag.name BEGINSWITH 'A').@count > 0")

使用 Swift 高阶函数在内存中进行同样的操作对应如下的代码：

    let result = items.filter { item in
        item.tags.contains { tag in
            tag.name.hasPrefix("A")
        }
    }

子查询是直接在 SQLite 端执行的，这意味着无论是在性能上还是在内存占用上，都比在内存中进行筛选要高效得多。此外，所有的筛选和排序操作也建议在
SQLite
端进行，即通过使用精心设计的谓词和排序条件来实现。这样的做法不仅提高了数据处理的效率，还有助于减轻应用程序内存的负担，特别是在处理大型数据集时。

## 接下来

在本文中，我们探讨了在实际开发场景中应用 Core Data
关系的一系列技巧。实际上，一旦开发者掌握了关系的基础理论和内部机制，他们就能不断地在实践中总结和发掘出更适合自己项目的方法和经验。

下一篇文章将专注于 Core Data 的后继框架 — SwiftData。我们不仅会探究 SwiftData
在处理数据关系方面的变化，还会审视这些变化的适用性，特别是在其首个版本中如何有效避免关系操作带来的潜在性能问题。
