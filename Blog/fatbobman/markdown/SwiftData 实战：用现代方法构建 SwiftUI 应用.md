在之前的文章 [ SwiftData 中的并发编程 ](/zh/posts/concurret-programming-in-swiftdata/)
中，我们深入探讨了 SwiftData
提出的创新并发编程模式，包括它的原理、核心操作及相关的注意事项。这种优雅的编程解决方案赢得了不少赞誉。然而，随着更多开发者在实际的 SwiftUI
应用中尝试使用 SwiftData，他们遇到了一些挑战：尤其在启用 Swift 的严格并发检查后，发现 SwiftData 基于 Actor
的并发模型与传统的应用构建方法很难融合。本文将采用类似教程的方式阐述如何将 SwiftData 与现代编程理念相结合，顺畅地融入 SwiftUI
应用之中，同时提供策略来应对目前开发者面临的挑战。

## 什么是所谓的现代方法？

在探讨现代编程方法时，虽然不同的开发者可能会有不同的见解，但有些核心原则是广泛认同的。在使用 SwiftData 构建 SwiftUI
应用的上下文中，我认为现代编程方法至少应满足以下几个关键标准：

- **模块化** ：通过将数据定义和操作逻辑封装在独立的模块中，我们不仅能增强代码的可读性和可维护性，还能促进功能的重用。模块化是确保项目结构清晰、灵活应对未来变化的基石。
- **全面可测试** ：确保每一个数据操作都通过彻底的单元测试是至关重要的。这种做法保证了代码的可靠性和稳定性，同时也使得持续集成和部署过程更加顺畅。
- **线程安全** ：在并发编程中保持数据的完整性和一致性是极其重要的。有效的线程安全措施不仅防止了数据冲突和竞态条件，而且符合 Swift 的严格并发标准，确保应用的高性能和稳定运行。
- **与架构无关** ：一个强大的数据管理模块应当灵活适应不同的架构设计，无论是 SwiftUI 自身的数据注入机制还是整合其他第三方框架，都应无缝对接，展现出高度的适应性。
- **支持预览** ：SwiftUI 的预览功能是其开发体验中的一大亮点，允许开发者即时看到界面变化。因此，确保数据层支持这一功能，对于加快开发流程和提高效率至关重要。
- **数据展示与操作分离** ：在遵循 SwiftUI 的响应式设计原则的同时，有效地分离数据展示与操作逻辑。通过 `@Query` 直观地展示数据并响应变化，而将创建、更新、删除等操作交由 SwiftData 的新并发模式处理，这样既提升了效率，又充分利用了 SwiftUI 响应式框架的优势。

为了更好地理解本文所讨论的概念，并实际看到这些现代编程方法在实践中的应用，我准备了一个演示项目。你可以通过访问以下 GitHub 仓库来获取完整的项目代码：

[ 访问演示项目代码 ](https://github.com/fatbobman/SwiftDataConcurrencyDemo)

该项目包含了使用 SwiftData 在 SwiftUI 应用中实现的示例，展示了如何按照文章中介绍的现代编程标准来构建应用。

## 创建数据管理模块

长久以来，将数据管理逻辑抽离出主项目，封装到一个独立的模块中，一直是一个广受推崇的做法。许多开发者在使用 Core Data
的项目中也采纳了这种模式。然而，与 SwiftData 相比，Core Data 在模块化方面给开发者带来了额外的挑战。这主要是由于 Core Data
在构建数据模型时使用图形化的模型编辑器，而数据模型本身则存储为独立的文件，它们会在应用的不同生命周期阶段以不同的文件扩展名被加载。这种对外部模型文件的依赖，在很大程度上减弱了开发者将数据管理代码模块化的意愿。

而
SwiftData，它的纯代码声明方式极大地简化了这一过程，实际上已经没有借口不将数据管理逻辑独立化了。这种方法不仅简化了代码的维护，而且还增加了代码的可移植性和可重用性。

考虑到数据管理模块通常与特定项目高度相关，在展示项目中我在项目的当前目录下创建一个新的 Swift Package，而不是为它建立一个单独的仓库。

首先创建一个名为 `DataProvider` 的包。在其 `Package.swift` 文件中，我们启用了 Swift
的严格并发检查功能，确保并发代码的安全性：

    .target(
      name: "DataProvider",
      swiftSettings: [
        .enableExperimentalFeature("StrictConcurrency"),
      ]
    ),

![image-20240316210229483](https://cdn.fatbobman.com/image-20240316210229483-zipic.png)

在这个独立的模块中，我们将完成数据模型的定义、数据操作逻辑的实现以及相关的测试工作。这样的结构不仅清晰地划分了应用的不同关注点，还使得维护和测试工作变得更加高效。

## 构建数据模型

在 SwiftData 中，构建数据模型的方法与定义 Swift 的基础类型极为相似，仅需通过纯代码即可完成。在我们的演示项目中，我们定义了一个简洁的模型
`Item` ：

    @Model
    public final class Item {
      public var timestamp: Date
      public var createTimestamp: Date

      public init(timestamp: Date) {
        self.timestamp = timestamp
        createTimestamp = .now
      }
    }

需要注意的是，采用 SwiftData
的纯代码建模方式意味着，一旦应用部署后需要修改数据模型或进行数据迁移，我们必须手动管理所有版本的数据模型。因此，尽管目前我们的模型版本只有一个，最好从一开始就规划好数据迁移的策略。

为此，我们首先定义一个用于表示模型版本的枚举，并通过 `CurrentScheme` 类型别名将其标记为当前使用的版本：

    public typealias CurrentScheme = SchemaV1

    public enum SchemaV1: VersionedSchema {
      public static var versionIdentifier: Schema.Version {
        .init(1, 0, 0)
      }

      public static var models: [any PersistentModel.Type] {
        [Item.self]
      }
    }

接下来，我们将 `Item` 类的声明嵌入到 `SchemaV1` 中，并通过类型别名保持名称的连贯性：

    public typealias Item = SchemaV1.Item

    extension SchemaV1 {
      @Model
      public final class Item {
        public var timestamp: Date
        public var createTimestamp: Date

        public init(timestamp: Date) {
          self.timestamp = timestamp
          createTimestamp = .now
        }
      }
    }

在我们的演示项目中，为了简化学习过程，我们没有进一步扩展数据模型。但在实际应用中，开发者可以通过扩展来为数据模型增加预设的谓词、排序规则或
FetchDescriptor 等信息，详见 [ 此示例代码
](https://gist.github.com/fatbobman/6dc873ae18bb28cd1ccc521b3f56cefb) 。

现在，无论是在模块内还是外部，我们都可以使用 `Item` 来引用这个版本的数据模型。若未来模型有变更，我们可以轻松地引入新的 Schema 版本，比如
`SchemaV2` ，并相应地调整类型别名，以适应新的模型结构。

> 要深入了解 SwiftData 数据模型的构建原理，请参阅 [ 揭秘 SwiftData 的数据建模原理 ](/zh/posts/unveiling-
> the-data-modeling-principles-of-swiftdata/) 。此外，若对 SwiftData
> 的数据模型迁移方法感兴趣，可阅读 [ 这篇文章 ](/zh/posts/what-s-new-in-core-data-in-
> wwdc23/#%E9%98%B6%E6%AE%B5%E5%BC%8F%E8%BF%81%E7%A7%BB-staged-migration)
> ，其中介绍了迁移策略和实施步骤。

## SwiftData 同样需要 Stack

在 Core Data 项目中，开发者习惯于构建一个类似于 Stack 的结构，用以集中管理持久化容器的声明和数据操作逻辑。SwiftData
显著简化了这一过程，允许开发者通过直接调用例如 `.modelContainer(for: Item.self)`
的简洁方式来快速构建容器并进行数据注入。那么，在使用 SwiftData 的场景下，是否还需要维护一个类似于 Stack 的结构呢？

尽管接下来我们将采用 `@ModelActor` 宏来封装数据操作逻辑，但构建一个类似于 Stack
的结构依然十分重要。这样的结构不仅为应用的不同部分统一提供容器和 `@ModelActor` 实现，而且在尝试结合 SwiftData 和 Core
Data 双框架模式的项目中尤为关键，因为它可以在同一位置处理两种框架的容器构建。

在我们的演示项目里，我们定义了一个 `DataProvider` 类。这个类在功能上类似于 Core Data 项目中常用的 `CoreDataStack` ：

    public final class DataProvider: Sendable {
      public static let shared = DataProvider()

      public let sharedModelContainer: ModelContainer = {
        let schema = Schema(CurrentScheme.models)
        let modelConfiguration = ModelConfiguration(schema: schema, isStoredInMemoryOnly: false)

        do {
          return try ModelContainer(for: schema, configurations: [modelConfiguration])
        } catch {
          fatalError("Could not create ModelContainer: \(error)")
        }
      }()

      public init() {}
    }

在这里，构建 schema 时直接利用了 `CurrentScheme.models` 提供的类型信息。此外，若数据模型需要迁移，相应的迁移逻辑也将在
`sharedModelContainer` 的初始化闭包中实现。

> 请阅读 [ 掌握 Core Data Stack ](/zh/posts/masteringofcoredatastack/) ，了解更多 Core
> Data Stack 的构建技巧。

## 用 @ModelActor 封装数据操作逻辑

SwiftData 提供了 `@ModelActor` 宏，鼓励开发者利用这一功能来创建一个 Actor 类型，进而在其中封装数据操作逻辑。对于我们的
`Item` 类型，我们定义了创建、更新和删除数据项的相关逻辑：

    @ModelActor
    public actor DataHandler {
      @discardableResult
      public func newItem(date: Date) throws -> PersistentIdentifier {
        let item = Item(timestamp: date)
        modelContext.insert(item)
        try modelContext.save()
        return item.persistentModelID
      }

      public func updateItem(id: PersistentIdentifier, timestamp: Date) throws {
        guard let item = self[id, as: Item.self] else { return }
        item.timestamp = timestamp
        try modelContext.save()
      }

      public func deleteItem(id: PersistentIdentifier) throws {
        guard let item = self[id, as: Item.self] else { return }
        modelContext.delete(item)
        try modelContext.save()
      }
    }

在实现这些功能时，有几点需要特别注意：

- 更新和删除操作仅接受 `PersistentIdentifier` 作为参数。
- 创建新的 Item 实例后，该方法会返回新创建对象的 `PersistentIdentifier` 。虽然在许多实际应用场景中这个返回值可能不常用，但它在进行单元测试时非常有用，提供了一种有效的方式来引用和测试新创建的数据实体。

> 为深入理解 `@ModelActor` 的用法及其在 SwiftData 中的角色，请参考文章 [ SwiftData 中的并发编程
> ](/zh/posts/concurret-programming-in-swiftdata/) 。

## 编写测试

尽管基于测试驱动开发（TDD）的逻辑通常推荐先编写测试再实现功能，但在我们的演示项目中，我们会在完成数据操作逻辑后才构建测试单元。

首先，我们设置一个专用于测试的辅助函数，确保每个测试用例都能使用一个干净的数据库环境：

    enum ContainerForTest {
      static func temp(_ name: String, delete: Bool = true) throws -> ModelContainer {
        let url = URL.temporaryDirectory.appending(component: name)
        if delete, FileManager.default.fileExists(atPath: url.path) {
          try FileManager.default.removeItem(at: url)
        }
        let schema = Schema(CurrentScheme.models)
        let configuration = ModelConfiguration(url: url)
        let container = try! ModelContainer(for: schema, configurations: configuration)
        return container
      }
    }

该辅助函数为每个测试用例创建独立的数据库，数据库名称基于测试函数的名称。默认情况下，它会在每次测试前删除旧的数据文件。

下面是一个测试用例，用于验证创建新的 `Item` 实例的功能：

    final class DataProviderTests: XCTestCase {
      @MainActor
      func testNewItem() async throws {
        // Arrange
        let container = try ContainerForTest.temp(#function)
        let hander = DataHandler(modelContainer: container)

        // ACT
        let date = Date(timeIntervalSince1970: 0)
        try await hander.newItem(date: date)

        // Assert
        let fetchDescriptor = FetchDescriptor<Item>()
        let items = try container.mainContext.fetch(fetchDescriptor)

        XCTAssertNotNil(items.first, "The item should be created and fetched successfully.")
        XCTAssertEqual(items.count, 1, "There should be exactly one item in the store.")

        if let firstItem = items.first {
          XCTAssertEqual(firstItem.timestamp, date, "The item's timestamp should match the initially provided date.")
        } else {
          XCTFail("Expected to find an item but none was found.")
        }
      }
    }

测试流程概述：

- 初始化一个新的、干净的数据库实例。
- 利用 `DataHandler` 添加新的数据项。
- 通过容器的 `mainContext` 从数据库中检索 `Item` 数据。
- 断言检索到的数据是否符合预期。

需要特别注意的是：

- 测试用例用 `@MainActor` 标注，以允许直接使用容器的 `mainContext` 。
- 创建和检索数据在不同的上下文中进行，以确保逻辑的准确性并模拟实际应用中的使用场景。
- 删除测试功能时，可以利用新创建数据项的返回值 `PersistentIdentifier` 来简化流程，避免重复从数据库检索数据。
- 返回的 `PersistentIdentifier` 应在相同的上下文中使用，特别是在它仍然是临时状态的情况下。对于跨上下文的操作，可能需要重新检索数据以获取持久化的标识符。

关于测试效率的顾虑：根据实际经验，即使是创建新数据库文件的测试方法也能在短时间内顺利完成大量测试，开发者无需担心其对测试性能的影响。

## 为注入做好准备

在完成了演示项目中对数据操作的全面测试后，下一步是考虑如何将 `DataHandler`
以安全且符合现代编程模式的方式，让项目中的其他代码轻松访问或进行注入。

为此，在 `DataProvider` 类中，我们定义了以下方法：

    public func dataHandlerCreator() -> @Sendable () async -> DataHandler {
      let container = sharedModelContainer
      return { DataHandler(modelContainer: container) }
    }

此辅助函数提供了一种安全的方法来创建 `DataHandler` 实例，这在启用 Swift 的严格并发检查功能时尤其关键。

在演示项目中，我们使用了将 `DataHandler`
创建函数注入到视图环境的做法。这种思路不仅限于通过环境值注入的方式，也适用于其他各种架构设计。例如，在使用 The Composable
Architecture (TCA) 时，可以采用相似的策略来定义 `DependencyKey` ，以便实现依赖注入的目的。此外，鉴于 `DataProvider` 本身符合 `Sendable`
协议，它也可以直接用作依赖注入的源，在某些场景下这种做法同样有效。这种灵活性允许开发者根据具体的应用架构需求，选择最合适的注入和依赖管理策略。

通过扩展 SwiftUI 的 `EnvironmentValues` ，我们能够将 `DataHandler` 的生成逻辑无缝集成到 SwiftUI
的环境中，从而为视图层提供强大的数据操作功能：

    public struct DataHandlerKey: EnvironmentKey {
      public static let defaultValue: @Sendable () async -> DataHandler? = { nil }
    }

    extension EnvironmentValues {
      public var createDataHandler: @Sendable () async -> DataHandler? {
        get { self[DataHandlerKey.self] }
        set { self[DataHandlerKey.self] = newValue }
      }
    }

至此，我们已经完成了数据管理模块的所有准备工作，现在可以将其集成到项目中，并开始利用这一模块了。

## 始终使用一个实例还是每次创建新的实例

在使用 SwiftData 进行开发时，我建议避免在 `DataProvider` 中持有一个长期共享的 `DataHandler`
实例。相反，在每个业务逻辑场景中独立创建新的实例或许是更好的选择。这种方法有几个优点：

首先，考虑到现代设备的性能已经非常出色，动态创建一个新的 `DataHandler`
实例的开销通常是可以接受的，不会对应用的响应速度或效率产生负面影响。

其次，由于 SwiftData
在某些方面如错误处理和合并策略等配置上的缺失，为每次数据操作创建一个新的独立实例可以简化异常处理的复杂度。这样，每个实例都是自包含的，操作互不干扰，从而降低了出错的风险，并使得代码更加清晰、易于维护。

## 将数据模块集成到项目中

在项目中引入 Package 后，我们可以开始在应用中使用它，为视图提供 `container` 和 `DataHandler` 生成方法。

    import DataProvider
    import SwiftData
    import SwiftUI

    @main
    struct SwiftDataConcurrencyDemoApp: App {
      let dataProvider = DataProvider.shared

      var body: some Scene {
        WindowGroup {
          ContentView()
            .environment(\.createDataHandler, dataProvider.dataHandlerCreator())
        }
        .modelContainer(dataProvider.sharedModelContainer)
      }
    }

此代码段将 `DataProvider` 的实例集成到了 SwiftUI 应用的主入口。我们通过 `.environment` 修饰器注入 `createDataHandler` 方法，使其在 `ContentView` 及其子视图中可用。

在 `ContentView` 中，我们实现了添加新数据项的功能，如下所示：

    struct ContentView: View {
      @Environment(\.modelContext) private var modelContext
      @Environment(\.createDataHandler) private var createDataHandler
      @Query(sort: \Item.createTimestamp, animation: .smooth) private var items: [Item]

      var body: some View {
        NavigationSplitView {
          List {
            ForEach(items) { item in
              ItemView(item: item)
            }
          }
          .toolbar {
            ToolbarItem {
              Button(action: addItem) {
                Label("Add Item", systemImage: "plus")
              }
            }
          }
        } detail: {
          Text("Select an item")
        }
      }

      @MainActor
      private func addItem() {
        let createDataHandler = createDataHandler
        Task.detached {
          if let dataHandler = await createDataHandler() {
            try await dataHandler.newItem(date: .now)
          }
        }
      }
    }

关键点概述：

- 使用 `@Environment(\.createDataHandler)` 将创建 `DataHandler` 的方法引入视图。
- 为了符合 Swift 的严格并发检查，我们需用 `@MainActor` 标注 `addItem` 函数。
- 利用 `Task.detached` 创建一个分离的任务，确保在非主线程上创建 `DataHandler` 实例，并进行数据操作，从而避免阻塞 UI。

通过这种方式，数据管理逻辑与视图逻辑分离，保持了代码的清晰性和可维护性，同时也利于异步数据处理和更新界面。

## 构建独立视图来展示数据

继列表视图之后，我们接下来将构建用于展示 `Item` 数据详细信息的独立视图。在 `ItemView` 中，我们利用 `createDataHandler` 环境变量来创建 `DataHandler` 实例，分别处理数据的删除和更新操作。所有 `DataHandler` 实例的操作都在非主线程上进行，以确保界面的流畅性不受数据处理过程的影响。

    struct ItemView: View {
      @Environment(\.createDataHandler) private var createDataHandler
      let item: Item
      var body: some View {
        VStack {
          Text("\(item.timestamp.timeIntervalSince1970)")
          HStack {
            Button("Update Timestamp") {
              let id = item.id
              let date = Date.now
              let createDataHandler = createDataHandler
              Task.detached {
                if let dataHandler = await createDataHandler() {
                  try? await dataHandler.updateItem(id: id, timestamp: date)
                }
              }
            }
            Button("Delete") {
              let id = item.id
              let createDataHandler = createDataHandler
              Task.detached {
                if let dataHandler = await createDataHandler() {
                  try? await dataHandler.deleteItem(id: id)
                }
              }
            }
          }
        }
        .buttonStyle(.bordered)
      }
    }

现在，我们就可以在模拟器中完整的运行项目并实现数据的添加与删除了。

## 是否还需要数据转换层？

在传统的 Core Data
项目中，通常会创建一个值类型的数据转换层，这一层主要作用是将托管对象（引用类型）转换为更适合视图使用的值类型，这有助于提高数据处理的安全性和简化视图的数据绑定。

在 SwiftData 中，模型本身就是用纯 Swift 类型构建的，加上 SwiftData 的 `PersistentModel` 采用 `Observation`
框架提供的观察机制，这一机制为每个属性提供了观察能力，确保了视图能精准响应数据变化。如果在视图中对这些数据进行转换，会破坏此观察机制，增加不必要的视图更新，因此，建议在视图中直接使用
SwiftData 中定义的数据模型。

然而，这并不意味着在所有场景下都不需要数据转换层。实际上，在创建或更新数据时，使用基于值类型的数据模型可以更加安全和高效，尤其在涉及数据比对和测试时。

虽然在演示项目中我们没有提供转换层的数据类型，但在实际应用的开发过程中，开发者应根据具体需求考虑是否引入这一层。这种设计决策应基于项目的具体需求，考虑到数据安全、开发效率以及是否能够提升整体的代码质量和可维护性。

## 为预览做准备

在 SwiftUI
开发中，预览是一个不可或缺的功能，它可以大大提高开发效率。因此，为预览配置适当的环境是至关重要的。我们通常推荐使用基于内存的数据库用于预览场景，这就要求我们需要对
`DataProvider` 进行适当的调整。

首先，我们在 `DataProvider` 中添加以下代码，以初始化一个非持久化的 `ModelContainer` ，专门用于预览环境：

    public let previewContainer: ModelContainer = {
      let schema = Schema(CurrentScheme.models)
      let modelConfiguration = ModelConfiguration(schema: schema, isStoredInMemoryOnly: true)
      do {
        return try ModelContainer(for: schema, configurations: [modelConfiguration])
      } catch {
        fatalError("Could not create ModelContainer: \(error)")
      }
    }()

接着，我们修改 `dataHandlerCreator` 函数，使其能够根据需求选择使用持久化或非持久化的容器：

    public func dataHandlerCreator(preview: Bool = false) -> @Sendable () async -> DataHandler {
      let container = preview ? previewContainer : sharedModelContainer
      return { DataHandler(modelContainer: container) }
    }

为了在预览中有效利用这些配置，我们通常会创建一个专用的预览包装视图，它不仅准备预览环境，还可以构建演示数据。以下是一个示例，展示了如何为 `ItemView` 构建一个预览容器：

    #if DEBUG
      struct ItemViewPreviewContainer: View {
        @Environment(\.createDataHandler) var createDataHandler
        @Query var items: [Item]
        var body: some View {
          VStack {
            if let item = items.first {
              ItemView(item: item)
            }
          }
          .task {
            if let dataHander = await createDataHandler() {
              let _ = try? await dataHander.newItem(date: .now)
            }
          }
        }
      }
    #endif

    #Preview {
      let dataProvider = DataProvider()
      return ItemViewPreviewContainer()
        .environment(\.createDataHandler, dataProvider.dataHandlerCreator(preview: true))
        .modelContainer(dataProvider.previewContainer)
    }

当配置 `ItemViewPreviewContainer` 的预览环境时，确保使用专门为预览准备的 `container` 和 `DataHandler` 创建函数。这样可以保证预览环境是隔离的，不会影响到实际的应用数据，同时提供了一种快速高效的方式来演示和测试视图。

## 新的问题：数据更新后视图没有刷新

如果你跟随本文构建自己的代码，可能会遇到一个问题：在 `ItemView`
中点击更新数据的按钮时，界面上的数据并没有相应地更新。考虑到我们的单元测试能够正常通过，且数据更新逻辑本身没有问题，那么这个问题是怎么引起的呢？

这实际上是由当前 SwiftData 的一个已知 Bug 导致的，当满足以下两个条件时，会出现数据更新后视图未刷新的情况：

- 数据更新逻辑被封装在 `ModelActor` 中。
- 使用独立的视图来展示和响应数据的变化（例如，当我们将展示代码做如下调整，通过直接使用 `Text` 显示数据时，可以明显看到更新后的区别）：

  List {
  ForEach(items) { item in
  VStack {
  Text("\(item.timestamp.timeIntervalSince1970)")
  ItemView(item: item) // don't change after update
  }
  }
  }

这个问题已有多位使用 `ModelActor`
的开发者向我提出，我当时给出的解决方案并不理想，主要是通过为数据展示视图增加额外的参数来实现更新感知。这种方法局限性较大，且可能会丢失首次更新的变化。本文将探讨其他可能的解决方案。

    struct ItemView: View {
      @Environment(\.createDataHandler) private var createDataHandler
      let item: Item
      let date: Date
      var body: some View {
         ....
      }
    }

    ItemView(item: item, date: item.timestamp)

> 我已经向苹果提交了反馈（ `FB13689240` ），希望问题能够尽早得到修复。

## 解决思路

为了解决数据更新后视图不刷新的问题，我们首先会考虑以下两种方法：

1. 避免使用独立视图来展示和响应数据。
2. 将数据更新逻辑从 `DataHandler` 中剥离，并直接在 `mainContext` 中修改数据。

显然，出于维护现有架构模式和测试流程的考虑，这两种方法都不是我们所希望的。但是，如果在 `mainContext`
中执行数据更新操作可以避免视图不刷新的问题，那么我们是否可以考虑创建一个专门用于数据更新操作的 `DataHandler` 实例，它直接使用 `mainContext` 呢？

> `mainContext` 是由 `ModelContainer` 实例提供的，它被标注了 `@MainActor`
> 只能在主线程中使用。我们在视图中通过 `@Qurey` 检索数据时便是通过这个上下文。

Swift 的宏（Macro）功能为这种思路提供了实现的可能性。通过探索由 `@ModelActor`
宏生成的代码，我们可以洞察其背后的实现机制，并据此进行必要的调整。

观察 `@ModelActor` 宏生成的 `DataHandler` 初始化方法：

    public init(modelContainer: SwiftData.ModelContainer) {
        let modelContext = ModelContext(modelContainer)
        self.modelExecutor = DefaultSerialModelExecutor(modelContext: modelContext)
        self.modelContainer = modelContainer
    }

这个初始化方法通过 `ModelContext(modelContainer)` 创建了一个新的 `ModelContext` 实例，并设定
Actor 的执行环境与此上下文相关联（ 使用相同的线程 ）。因此，我们可以考虑为 `DataHandler`
添加一个新的构造方法，这样就可以在不大幅度调整当前开发模式的前提下，提供一个解决方案。

## 临时解决方案

我们的这个临时方案涉及对 `DataHandler` 类的扩展和对 `DataProvider` 的调整，以确保在主线程上的 `mainContext` 进行数据更新操作。

首先，我们为 `DataHandler` 添加一个新的构造方法：

    @MainActor
    public init(modelContainer: ModelContainer, mainActor _: Bool) {
      let modelContext = modelContainer.mainContext
      modelExecutor = DefaultSerialModelExecutor(modelContext: modelContext)
      self.modelContainer = modelContainer
    }

此构造函数通过 `@MainActor` 标注确保能够将 `modelContainer.mainContext` 与 Actor
的执行器直接绑定。我们引入了一个未使用的参数来避免与现有构造函数签名冲突。

然后，在 `DataProvider` 中添加一个新的辅助方法，用于生成绑定到 `mainContext` 的 `DataHandler`
实例：

    public func dataHandlerWithMainContextCreator(preview: Bool = false) -> @Sendable @MainActor () async -> DataHandler {
      let container = preview ? previewContainer : sharedModelContainer
      return { DataHandler(modelContainer: container, mainActor: true) }
    }

接下来，我们定义一个新的环境键，并扩展 `EnvironmentValues` 以注入新的辅助方法：

    public struct MainActorDataHandlerKey: EnvironmentKey {
      public static let defaultValue: @Sendable @MainActor () async -> DataHandler? = { nil }
    }

    extension EnvironmentValues {
      public var createDataHandlerWithMainContext: @Sendable @MainActor () async -> DataHandler? {
        get { self[MainActorDataHandlerKey.self] }
        set { self[MainActorDataHandlerKey.self] = newValue }
      }
    }

在应用的根视图中，我们注入这个新的环境值：

    WindowGroup {
      ContentView()
        .environment(\.createDataHandler, dataProvider.dataHandlerCreator())
        // new
        .environment(\.createDataHandlerWithMainContext, dataProvider.dataHandlerWithMainContextCreator())
    }

在 `ItemView` 中，我们引入并使用这个新环境值来执行数据更新操作：

    struct ItemView: View {
      @Environment(\.createDataHandler) private var createDataHandler
      @Environment(\.createDataHandlerWithMainContext) private var createDataHandlerWithMainContext
      let item: Item
      var body: some View {
        VStack {
          Text("\(item.timestamp.timeIntervalSince1970)")
          HStack {
            Button("Update Timestamp") {
              updateItemTimestamp()
            }
    				....
          }
        }
        .buttonStyle(.bordered)
      }

      @MainActor
      private func updateItemTimestamp() {
        let id = item.id
        let date = Date.now
        Task { @MainActor in
          if let dataHandler = await createDataHandlerWithMainContext() {
            try? await dataHandler.updateItem(id: id, timestamp: date)
          }
        }
      }
    }

确保预览环境也注入了相应的环境值：

    #Preview {
      let dataProvider = DataProvider()
      return ItemViewPreviewContainer()
        .environment(\.createDataHandler, dataProvider.dataHandlerCreator(preview: true))
        .environment(\.createDataHandlerWithMainContext, dataProvider.dataHandlerWithMainContextCreator(preview: true))
        .modelContainer(dataProvider.previewContainer)
    }

通过这种方式，我们可以保证数据更新操作会在一个绑定到主线程 `mainContext` 的 `DataHandler`
实例中进行，而其他操作仍在非主线程执行。虽然这需要我们为更新操作进行特别的处理，但这是在不改变原有架构的前提下的一个可行的妥协方案。我希望这个问题可以尽快被官方修复。

> **特别提醒** ：自首个版本（iOS 17.0）起，SwiftData
> 几乎在每个版本中都对一些已知问题进行了修复，同时也可能引入了新的问题。因此，当你运行文章中提供的 Demo
> 项目，而项目运行在不同的系统版本或使用不同版本的 Xcode
> 编译时，可能会遇到与预期不一致的结果（比如，点击添加按钮后无法看到新数据，或应用被推到后台时崩溃等）。我们还需等待苹果对这些问题进行进一步的修复。尽管如此，我相信文章中介绍的数据操作逻辑本身是正确的。为了确保在当前项目中以稳定、可靠的方式使用本文介绍的方法，请通过
> `createDataHandlerWithMainContext` 创建所有的 `DataHandler` （即使用主上下文来构建 `DataHandler` ）。

## 总结

在这篇文章中，我们探讨了如何采用新思维来构建使用 SwiftData 的 SwiftUI
应用。当我们开始使用新框架时，特别是那些在旧有框架基础上发展起来的框架，我们不能仅仅将旧有的经验和习惯直接移植过来。我们需要深入思考如何利用新框架的优势，同时融入最新的编程理念，以打造更加高效、现代化的应用。

框架的每次更新不仅是一项挑战，也是一个机遇。它要求开发者离开舒适区，重新审视和学习新工具的潜力和最佳实践。通过这样做，我们不仅能够提升个人技能，还能够为用户提供更好的产品。SwiftData
作为一个现代化的数据管理框架，给予了开发者更大的灵活性和更强大的功能，使得数据处理更加直观和高效。

随着 Swift 和 SwiftUI 的不断进化，结合像 SwiftData
这样的框架，开发者被赋予了创造出更加安全、更加响应式、更加丰富和更具互动性应用的能力。因此，紧跟最新的开发趋势，并学会利用这些新工具的强大功能，将是每一个致力于提升自身技能和产品质量的开发者的必经之路。
