在本文中，我们将对 `@FetchRequest` 、 `@SectionedFetchRequest` 、 `@Query` 、 `@Namespace` 和 `@Bindable` 等属性包装器进行探讨。这些属性包装器涵盖了在视图中对 Core Data 和 SwiftData
数据进行检索以及在视图中创建命名空间等功能。

> 本文旨在提供对这些属性包装器的主要功能和使用注意事项的概述，而非详尽的使用指南。

- [ @State、@Binding、@StateObject、@ObservedObject、@EnvironmentObject、@Environment ](/zh/posts/exploring-key-property-wrappers-in-swiftui/)
- [ @AppStorage、@SceneStorage、@FocusState、@GestureState、@ScaledMetric ](/zh/posts/exploring-swiftui-property-wrappers-2/)
- [ @UIApplicationDelegateAdaptor, @AccessibilityFocusState, @FocusedObject, @FocusedValue, @FocusedBinding ](/zh/posts/exploring-swiftui-property-wrappers-4/)

## 1\. @FetchRequest

在 SwiftUI 中， `@FetchRequest` 用于在视图中检索 Core Data
的实体数据。它可以简化从持久化存储中检索数据的过程，并在数据发生变化时自动更新视图。

### 1.1 基本用法

    @FetchRequest(
        sortDescriptors: [NSSortDescriptor(keyPath: \Item.timestamp, ascending: true)],
        predicate: nil,
        animation: .default)
    private var items: FetchedResults<Item>

    List {
        ForEach(items) { item in
            if let timestamp = item.timestamp {
                NavigationLink {
                    Text("Item at \(timestamp, format: .dateTime)")
                } label: {
                    Text(timestamp, format: .dateTime)
                }
            }
        }
    }

### 1.2 主要功能

- `@FetchRequest` 使得从 Core Data 中检索数据变得简单直接。开发者可以定义实体类型、排序描述符和谓词来过滤结果。
- 在 Core Data 中的数据发生任何变动时， `@FetchRequest` 能够自动更新其检索结果，确保视图与数据间的实时同步。
- 与 SwiftUI 的声明式编程模型紧密结合， `@FetchRequest` 提供了一种更为自然和流畅的方式，用于将数据驱动的界面融入应用中。

### 1.3 注意事项与使用技巧

- 在使用 `@FetchRequest` 前，确保当前视图环境中已注入了托管对象上下文。
- 下面的示例展示了如何在构造器中根据特定参数设置过滤和排序条件：

  @FetchRequest
  private var items: FetchedResults<Item>
  init(startDate:Date,endDate:Date) {
  let predicate = NSPredicate(format: "timestamp >= %@ AND timestamp <= %@", startDate as CVarArg,endDate as CVarArg)
  \_items = FetchRequest(
  entity: Item.entity(),
  sortDescriptors: [.init(key: #keyPath(Item.timestamp), ascending: true)],
  predicate: predicate
  )
  }

- 从 iOS 15 起，开发者可在视图中动态调整 `@FetchRequest` 的过滤和排序条件。但需注意，在 `.onAppear` 和 `.task` 中，此方法不适用。它通常用于根据用户操作动态更新视图。

  Button("abc") {
  $items.nsPredicate.wrappedValue = .init(value: false)
  $items.sortDescriptors.wrappedValue = [.init(\Item.timestamp, order: .reverse)]
  }

- 若要进行更复杂的配置，推荐使用 NSFetchRequest 实例创建 `@FetchRequest` ：

  extension Item {
  static let noFaultRequest: NSFetchRequest = {
  let request = NSFetchRequest<Item>(entityName: "Item")
  request.predicate = nil
  request.sortDescriptors = [.init(keyPath: \Item.timestamp, ascending: true)]
  request.returnsObjectsAsFaults = false
  return request
  }()
  }

  @FetchRequest(fetchRequest: Item.noFaultRequest)
  private var items: FetchedResults<Item>

- `@FetchRequest` 中的 `animation` 参数决定了数据变化时界面更新的动画效果。 `.none` 和 `nil` 均表示无动画。
- 使用 List 展示数据时，List 会忽略 `@FetchRequest` 设置的动画效果，而使用组件默认动画。
- 开发者可以用 `withAnimation` 函数覆盖 `@FetchRequest` 中设定的动画效果，如下所示：

  withAnimation(.none) {
  let newItem = Item(context: viewContext)
  newItem.timestamp = Date()

      do {
          try viewContext.save()
      } catch {
      }

  }

- `@FetchRequest` 是 SwiftUI 对 NSFetchedResultsController 的封装，其主要功能和性能与后者基本一致。
- 与 NSFetchedResultsController 相同， `@FetchRequest` 仅支持返回 NSManagedObject 类型的集合，不支持其他 NSFetchRequestResult 类型（如数字、NSManagedObjectID、字典）。
- `@FetchRequest` 的生命周期与视图的存续期紧密相关。它在视图加载到视图树时开始检索数据，并在视图移除时停止。
- 相比在 ViewModel 中获取 Core Data 实体数据， `@FetchRequest` 更紧密地与视图的生命周期绑定，几乎无首次加载延迟。
- 在首次获取数据后， `@FetchRequest` （NSFetchedResultsController）会根据托管对象上下文的合并信息更新数据集。因此，基于 `fetchLimit` 的设置无法保证在后续数据变化时始终有效。
- 关于 `@FetchRequest` 的工作原理，详见 [ SwiftUI 与 Core Data —— 数据获取 ](/zh/posts/modern-core-data-fetcher/) 。
- FetchedResults 是 NSFetchRequestResult 的封装，遵循 RandomAccessCollection 协议，允许通过下标方式访问数据。
- FetchedResults 提供了一个 `publisher` 属性，一旦结果集数据发生变化，该 Publisher 会发送整个数据集。因此，不建议订阅此属性以监控数据集变化，以避免冗余操作。
- 在 SwiftUI 开发中，推荐将展示 `to-Many` 数据的界面单独封装成独立的视图，并通过 `@FetchRequest` 来获取数据。这种做法不仅确保了数据获取顺序的稳定性，还能及时响应数据变化，并使视图更新更加高效。详情请参阅 [ 掌握 Core Data 中的关系：实战 ](/zh/posts/mastering-relationships-in-core-data-practical/) 。

## 2\. @SectionedFetchRequest

在 SwiftUI 中， `@SectionedFetchRequest` 属性包装器提供了一种便捷的方式来处理并展示按照特定标准分组的 Core
Data 查询结果。这使得开发者能够在界面上以分组形式展示复杂的数据结构。

### 2.1 基本用法

以下是一个 `@SectionedFetchRequest` 的基本使用示例：

![image-20240122162612483](https://cdn.fatbobman.com/image-20240122162612483.png)

    @SectionedFetchRequest(
        entity: Item.entity(),
        sectionIdentifier: \Item.categoryID,
        sortDescriptors: [
            .init(keyPath: \Item.categoryID, ascending: true),
            .init(keyPath: \Item.timestamp, ascending: true),
        ]
    )
    var sectionItems: SectionedFetchResults<Int16, Item>

    ForEach(sectionItems) { section in
        Section(header: Text("\(section.id)")) {
            ForEach(section) { item in
                Row(item: item)
            }
        }
    }

这段代码演示了如何根据 `Item` 实体的 `categoryID` 属性创建一个分组的 `SectionedFetchRequest`
，并根据预设的规则进行排序。

`SectionedFetchResults` 是一个包含两个泛型参数的结构体。第一个参数定义了用作分组标识（section
identifier）的属性类型，而第二个参数指定了托管对象的实体类型

### 2.2 主要功能

- `@SectionedFetchRequest` 允许开发者按照特定属性将查询结果分组，从而在 SwiftUI 视图中以分组形式展示。

- 除了支持分组外，其他特征与 `@FetchRequest` 基本一致。

### 2.3 注意事项与使用技巧

- 大部分适用于 `@FetchRequest` 的注意事项和技巧同样适用于 `@SectionedFetchRequest` 。
- 使用 `@SectionedFetchRequest` 时，必须指定一个用于分组的属性，该属性类型应能被清晰地用于分区，如 String 或 Int 类型。
- 为确保分组的准确顺序，构建 `sortDescriptors` 时，应将用于 `sectionIdentifier` 的属性作为第一排序选项：

  sortDescriptors: [
  .init(keyPath: \Item.categoryID, ascending: true),
  .init(keyPath: \Item.timestamp, ascending: true),
  ]

- 对于难以进行精确分组的属性类型，建议为实体创建一个专门的属性以便分类。例如，可以为 `timestamp` 增加一个 Int16 类型的 `year` 属性，以便按年份进行分组。
- 在 SwiftUI 中，嵌套的 `ForEach` 可能会影响惰性容器的性能优化。通过添加 `Section` ，可以避免 `ForEach` 的递归展开，提高性能。具体细节可参考 [ Demystify SwiftUI performance ](https://developer.apple.com/videos/play/wwdc2023/10160/) 。例如，在以下代码中，如果去除 `Section` ，SwiftUI 将一次性为结果集中的每个数据项构建子视图：

  ForEach(sectionItems) { section in
  // Section(header: Text("\(section.id)")) {
  ForEach(section) { item in
  Row(item: item)
  }
  // }
  }

## 3\. @Query

在 SwiftUI 中， `@Query` 用于在视图中检索 SwiftData
的实体数据。它可以简化从持久化存储中检索数据的过程，并在数据发生变化时自动更新视图。

### 3.1 基本用法

    @Query(sort: \Item.timestamp, animation: .default)
    private var items: [Item]

### 3.2 注意事项与使用技巧

- `@Query` 可以被视为 SwiftData 环境中 `@FetchRequest` 的对应版本。然而，与 `@FetchRequest` 不同的是， `@Query` 不支持在视图内动态修改查询的谓词和排序条件。
- `@FetchRequest` 与 `@Query` 之间的对比如下：
  - Core Data 的 NSFetchRequest 对应于 SwiftData 的 [ FetchDescriptor ](https://developer.apple.com/documentation/swiftdata/fetchdescriptor) 。
  - NSSortDescriptor 对应于 [ SortDescriptor ](https://developer.apple.com/documentation/foundation/sortdescriptor) （后者也可用于 `@FetchRequest` ）。
  - NSPredicate 对应于 Foundation 的 [ Predicate ](https://developer.apple.com/documentation/foundation/predicate) 。
  - 参数方面， `@FetchRequest` 的 predicate 对应于 `@Query` 的 filter。
- 在 `@Predicate` 宏中，不可以直接调用外部方法、函数或计算属性。应先在宏外计算好数值，再作为谓词条件在宏中使用：

  // 示例一：错误方式
  @Query
  private var items: [Item]

  init() {
  let predicate = #Predicate<Item>{
  $0.timestamp < Date.now // 无法编译
  }
  \_items = Query(
  filter: predicate,
  sort:\Item.timestamp,
  order: .forward,
  animation: .default
  )
  }

  // 示例一：正确方式
  let now = Date.now
  let predicate = #Predicate<Item>{
  $0.timestamp < now
  }

  // 示例二：错误方式
  init(item: Item) {
  let predicate = #Predicate<Item>{
  $0.timestamp < item.timestamp // 无法编译
  }
  \_items = Query(
  filter: predicate,
  sort:\Item.timestamp,
  order: .forward,
  animation: .default
  )
  }

  // 示例二：正确方式
  init(item: Item) {
  let startDate = item.timestamp
  let predicate = #Predicate<Item>{
  $0.timestamp < startDate
  }
  }

- SwiftData 并未提供类似于 NSFetchedResultsController 的功能，用于在视图外部进行数据检索并根据数据变化自动更新数据集。对于这种需求，可以考虑使用 Persistent History Tracking。更多详情请参考 [ 如何通过 Persistent History Tracking 观察 SwiftData 的数据变化 ](/zh/posts/persistent-history-tracking-in-swiftdata/) 。

> 在上文中介绍的三个属性包装器都是在 SQLite 端执行数据的筛选、排序和分组操作，这种做法在效率和系统资源占用方面都优于在内存中使用 Swift
> 的高阶函数进行相同操作。

## 4\. @Namespace

`@Namespace` 属性包装器用于创建一个唯一标识符，使得我们可以对视图或元素进行有效的分组和区分。

### 4.1 基本用法

    @Namespace private var namespace

### 4.2 主要功能

- 每个 `@Namespace` 属性包装器都将创建一个唯一标识符，该标识符在创建后在其生命周期中保持不变。
- `@Namespace` 通常会结合其他的 `id` 信息共同为视图进行标注。这种方式可以在不改变 `id` 的情况下，为视图增加更多的可识别信息。

### 4.3 注意事项与使用技巧

- 创建了 `@Namespace` 标识符之后，你可以将其传递到其他视图中使用：

  struct ParentView: View {
  @Namespace var namespace
  let id = "1"
  var body: some View {
  VStack {
  Rectangle().frame(width: 200, height: 200)
  .matchedGeometryEffect(id: id, in: namespace)
  SubView3(namespace: namespace, id: id)
  }
  }
  }

  struct SubView: View {
  let namespace: Namespace.ID
  let id: String
  var body: some View {
  Rectangle()
  .matchedGeometryEffect(id: id, in: namespace, properties: .size, isSource: false)
  }
  }

- 虽然开发者在多数情况下会将 `@Namespace` 与 `matchedGeometryEffect` 结合使用，但重要的是要理解 `@Namespace` 本身仅扮演着标识符的角色，并不直接参与几何信息处理或动画过渡的具体实现。
- `@Namespace` 不仅限于与 `matchedGeometryEffect` 搭配使用，还可以用于其他元素或视图修饰器，如 `accessibilityRotorEntry` 、 `AccessibilityRotorEntry` 、 `accessibilityLinkedGroup` 、 `prefersDefaultFocus` 和 `defaultFocus` 。
- 在使用 `@Namespace` 的场景中，通常会出现标注视图和读取视图信息的操作成对出现的模式：

  // 示例一：
  Rectangle().frame(width: 200, height: 200)
  .matchedGeometryEffect(id: id, in: namespace) // 标注视图
  Rectangle()
  .matchedGeometryEffect(id: id, in: namespace, properties: .size, isSource: false) // 读取带有特定 namespace + id 的视图的几何信息

  // 示例二：
  VStack {
  TextField("email", text: $email)
  .prefersDefaultFocus(true, in: namespace) // 标注视图，该视图为 namespace 中默认获得焦点的视图

      SecureField("password", text: $password)

      Button("login") {
        ...
      }

  }
  .focusScope(namespace) // 读取 namespace 命名空间中具备默认焦点的视图信息，并将焦点设置与其上

- 允许为同一视图应用多个不同的 `namespace + id` 组合。例如，在下面的代码中，我们使用了相同的 `id` 但不同的 `namespace` ，为同一个 `TrendView` 添加了标注。这样做为两个不同的可访问性转子（Rotor）提供了独立的标识：

  struct TrendsView: View {
  let trends: [Trend]

      @Namespace private var customRotorNamespace
      @Namespace private var countSpace

      var body: some View {
          VStack {
              ScrollViewReader { scrollView in
                  List {
                      ForEach(trends, id: \.id) { trend in
                          TrendView(trend: trend)
                              .accessibilityRotorEntry(id: trend.id, in: customRotorNamespace) // 标识1
                              .accessibilityRotorEntry(id: trend.id, in: countSpace) // 标识2
                              .id(trend.id)
                      }
                  }
                  .accessibilityRotor("Negative trends") {
                      ForEach(trends, id: \.id) { trend in
                          if !trend.isPositive {
                              AccessibilityRotorEntry(trend.message, trend.id, in: customRotorNamespace) {
                                  scrollView.scrollTo(trend.id)
                              }
                          }
                      }
                  }
                  .accessibilityRotor("Count"){
                      ForEach(trends,id:\.id){ trend in
                          if trend.count % 2 == 0 {
                              AccessibilityRotorEntry("\(trend.count)", trend.id, in: countSpace) {
                                  scrollView.scrollTo(trend.id)
                              }
                          }
                      }
                  }
              }
          }

      }

  }

> 有关 `AccessibilityRotorEntry` 的更多信息，请参阅 [ Accessibility rotors in SwiftUI
> ](https://swiftwithmajid.com/2021/09/14/accessibility-rotors-in-swiftui/) 。

- 当使用 `ForEach` 时，我们通常会使用 `ForEach` 提供的标识符作为 `id` ，并通过结合不同的 `namespace` 为相同的视图或元素提供多种不同的标识。例如上面的代码。

- 在任何给定时间，应该只存在一个唯一的 `namespace + id` 组合。例如，在下面的代码中，如果运行，将会产生一个警告，因为存在多个使用相同 `namespace + id` 组合的视图：

  struct AView:View {
  @Namespace var namespace
  var body: some View {
  VStack {
  Rectangle()
  .matchedGeometryEffect(id: "111", in: namespace)
  Rectangle()
  .matchedGeometryEffect(id: "111", in: namespace)
  }
  }
  }

  // Multiple inserted views in matched geometry group Pair<String, ID>(first: "111", second: SwiftUI.Namespace.ID(id: 88)) have `isSource: true`, results are undefined.

- 当与 `matchedGeometryEffect` 结合使用时，可以让多个视图共享同一个被标注视图的几何信息。在以下代码中，两个下方的 `Rectangle` 将与第一个 `Rectangle` 的位置重叠，因为它们共享了标记为 `namespace + "111"` 的视图的位置信息：

  struct AView:View {
  @Namespace var namespace
  var body: some View {
  VStack {
  Rectangle()
  .matchedGeometryEffect(id: "111", in: namespace)
  Rectangle().fill(.red)
  .matchedGeometryEffect(id: "111", in: namespace,properties: .position, isSource: false)
  Rectangle().fill(.blue)
  .matchedGeometryEffect(id: "111", in: namespace,properties: .position, isSource: false)
  }
  }
  }

- 在模态视图中使用 `matchedGeometryEffect` 时，若无法正确获取几何信息，这通常是由于 SwiftUI 的一个已知问题，而非 `@Namespace` 的问题。一个解决方案是将视图放入导航容器内。这样做可以确保在模态视图（如 sheet 或 fullscreenCover）中正确获取几何信息。

  // 问题示例：无法获取几何信息
  struct NaviTest: View {
  @Namespace var namespace

      @State var show = false
      var body: some View {
          VStack {
              Button("Show") {
                  show.toggle()
              }
              .sheet(isPresented: $show) {
                  VStack {
                      Rectangle()
                          .fill(.cyan)
                          .matchedGeometryEffect(id: "1", in: namespace, properties: .size, isSource: false)
                  }
                  .frame(width: 300, height: 300)
              }
              Rectangle().fill(.orange).frame(width: 100, height: 200).matchedGeometryEffect(id: "1", in: namespace)
          }
      }

  }

  // 解决方案：在导航容器内可以正确获取几何信息
  NavigationStack {
  VStack {
  Button("Show") {
  show.toggle()
  }
  .sheet(isPresented: $show) {
  VStack {
  Rectangle()
  .fill(.cyan)
  .matchedGeometryEffect(id: "1", in: namespace, properties: .size, isSource: false)
  }
  .frame(width: 300, height: 300)
  }
  Rectangle().fill(.orange).frame(width: 100, height: 200).matchedGeometryEffect(id: "1", in: namespace)
  }
  }

> 想了解更多关于 `matchedGeometryEffect` 的细节，请参考 [ MatchedGeometryEffect – Part 1
> (Hero Animations) ](https://swiftui-lab.com/matchedgeometryeffect-part1/) 。

## 5\. @Bindable

`@Bindable` 属性包装器为创建可观察（Observable）对象实例的可变属性绑定（Binding）提供了一种便捷且高效的方式。

### 5.1 基本用法

    @Observable
    class People {
        var name: String
        var age: Int
        init(name: String, age: Int) {
            self.name = name
            self.age = age
        }
    }

    struct PeopleView: View {
        @State var people = People(name: "fat", age: 18)
        var body: some View {
            VStack {
                Text("\(people.name) \(people.age)")
                PeopleName(people: people)
                PeopleAge(people: people)
            }
        }
    }

    struct PeopleName: View {
        @Bindable var people: People // 用法一
        var body: some View {
            TextField("Name", text: $people.name)
        }
    }

    struct PeopleAge: View {
        let people: People
        var body: some View {
            @Bindable var people = people // 用法二
            TextField("Age:", value: $people.age, format: .number)
        }
    }

### 5.2 注意事项与使用技巧

- `@Bindable` 专门用于符合 `Observation.Observable` 协议的类型，适用于那些通过 `@Observable` 宏或 `@Model` 宏声明的类型。
- 目前，在将 `@Bindable` 应用于 SwiftData 的 PersistentModel 实例时需特别小心。特别是当 `autoSave` 功能被激活时，它可能会导致稳定性问题。预计在未来的更新中，这一问题能得到解决和改进。

## 总结

至此，我们已经介绍了 SwiftUI 中的 16 种不同属性包装器。之后还将用一篇文章对剩下的属性包装器的功能进行探讨，敬请期待。
